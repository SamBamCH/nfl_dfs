import pandas as pd
import numpy as np
from collections import defaultdict

from data.data_manager import DataManager

# Define the correlation matrix
position_corr = np.array([
    [0.000, 0.056, 0.455, 0.411, -0.044, 0.271, 0.044, 0.147, 0.226, -0.424],  # QB
    [0.056, 0.000, 0.007, 0.036, 0.050, 0.044, -0.099, 0.070, 0.142, -0.201],  # RB
    [0.455, 0.007, 0.000, 0.030, -0.034, 0.147, 0.087, 0.127, -0.147, -0.234],  # WR
    [0.411, 0.036, 0.030, 0.000, -0.124, 0.226, 0.069, 0.128, 0.129, -0.126],  # TE
    [-0.044, 0.050, -0.034, -0.124, 0.000, -0.424, -0.201, -0.235, -0.126, -0.340],  # DST
    [0.271, 0.044, 0.147, 0.226, -0.424, 0.000, 0.056, 0.456, 0.411, -0.044],  # OPPQB
    [0.044, -0.099, 0.087, 0.069, -0.201, 0.056, 0.000, 0.008, 0.036, 0.050],  # OPPRB
    [0.147, 0.070, 0.127, 0.128, -0.235, 0.456, 0.008, 0.000, 0.030, -0.033],  # OPPWR
    [0.226, 0.142, -0.147, 0.129, -0.126, 0.411, 0.036, 0.030, 0.000, -0.124],  # OPPTE
    [-0.424, -0.201, -0.234, -0.126, -0.340, -0.044, 0.050, -0.033, -0.124, 0.000],  # OPPDST
])

### Entry point of the application
def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # Initialize DataManager for the desired site (e.g., 'dk')
    site = "dk"
    data_manager = DataManager(site)

    # Load player data
    try:
        data_manager.load_player_data()
        print("Player data loaded successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Filter out invalid players
    data_manager.players = [
        player for player in data_manager.players
        if player.ownership not in [0, None] and player.id not in [0, None]
    ]

    # Add a tunable parameter for correlation adjustment
    correlation_adjustment = data_manager.config.get("correlation_adjustment", 0.25)

    # Group players by game
    players_by_game = defaultdict(lambda: {"team_a": [], "team_b": []})
    for player in data_manager.players:
        if player.opponent:
            game_key = tuple(sorted([player.team, player.opponent]))
            if player.team == game_key[0]:
                players_by_game[game_key]["team_a"].append(player)
            else:
                players_by_game[game_key]["team_b"].append(player)

    # Initialize list to store DataFrames for each game
    game_projections_dfs = []

    for game, teams in players_by_game.items():
        team_a_players = teams["team_a"]
        team_b_players = teams["team_b"]
        all_game_players = team_a_players + team_b_players

        num_game_players = len(all_game_players)
        game_corr = np.zeros((num_game_players, num_game_players))

        # Map positions to indices in the correlation matrix
        position_to_index = {
            "QB": 0, "RB": 1, "WR": 2, "TE": 3, "DST": 4,
            "OPPQB": 5, "OPPRB": 6, "OPPWR": 7, "OPPTE": 8, "OPPDST": 9,
        }

        # Build the correlation matrix for the current game
        for i, player_i in enumerate(all_game_players):
            for j, player_j in enumerate(all_game_players):
                pos_i = player_i.position[0]  # Assume single position
                pos_j = player_j.position[0]
                team_i = player_i.team
                team_j = player_j.team

                if team_i == team_j:
                    # Same team correlation
                    game_corr[i, j] = position_corr[
                        position_to_index[pos_i], position_to_index[pos_j]
                    ]
                else:
                    # Cross-team correlation
                    game_corr[i, j] = position_corr[
                        position_to_index[f"OPP{pos_i}"], position_to_index[f"OPP{pos_j}"]
                    ]

        # Ensure positive semi-definiteness
        epsilon = 1e-10
        game_corr = (game_corr + game_corr.T) / 2
        np.fill_diagonal(game_corr, 1.0)
        eigvals = np.linalg.eigvalsh(game_corr)
        if np.min(eigvals) < 0:
            game_corr += (-np.min(eigvals) + epsilon) * np.eye(num_game_players)

        # Generate correlated random values
        mean_fpts = [player.fpts for player in all_game_players]
        stddevs = [player.stddev * data_manager.config["randomness_amount"] / 100 for player in all_game_players]
        uncorrelated = np.random.normal(loc=mean_fpts, scale=stddevs, size=num_game_players)
        L = np.linalg.cholesky(game_corr)
        correlated = np.dot(L, uncorrelated)

        # Apply the correlation adjustment
        adjusted_projections = (1 - correlation_adjustment) * uncorrelated + correlation_adjustment * correlated

        # Create a DataFrame for this game's projections
        game_df = pd.DataFrame({
            "Game": [f"{game[0]} vs {game[1]}"] * num_game_players,
            "Player": [player.name for player in all_game_players],
            "Team": [player.team for player in all_game_players],
            "Position": [player.position[0] for player in all_game_players],
            "Projected FPTS": mean_fpts,
            "Random STDDEV": stddevs,
            "Uncorrelated Projections": uncorrelated,
            "Correlated Projections": correlated,
            "Adjusted Projections": adjusted_projections,
        })
        game_projections_dfs.append(game_df)

    # Combine all game DataFrames into one
    all_projections_df = pd.concat(game_projections_dfs, ignore_index=True)

    # Save to CSV
    all_projections_df.to_csv("random_projections_with_adjustment.csv", index=False)
    print("\nRandom projections saved to 'random_projections_with_adjustment.csv'.")

main()

import pandas as pd

def calculate_exposure(lineups, players):
    """
    Calculate player exposure in the given lineups and return a sorted DataFrame.

    :param lineups: List of lineups, where each lineup is a list of (player, position, player.id) tuples.
    :param players: List of all Player objects used in the lineups.
    :return: Pandas DataFrame sorted by exposure percentage, highest to lowest.
    """
    # Initialize a dictionary to track exposures
    exposure_count = {player.id: 0 for player in players}
    total_lineups = len(lineups)

    # Count the occurrences of each player in the lineups
    for lineup in lineups:
        for player, _, _ in lineup:
            exposure_count[player.id] += 1

    # Create a DataFrame with player data
    data = []
    for player in players:
        exposure = (exposure_count[player.id] / total_lineups) * 100
        data.append({
            "Name": player.name,
            "position": player.position,
            "Team": player.team,
            "Opp": player.opp,
            "Salary": player.salary,
            "Exposure (%)": exposure,
            "ownership": player.ownership, 
            "leverage": exposure - player.ownership,
            "FPTS": player.fpts,
            "value": player.fpts / player.salary * 1000,
            "STDDEV": player.stddev,
            "variance score": player.stddev / player.fpts,
            "boom": player.boom, 
            "bust": player.bust
        })

    # Create and sort the DataFrame
    df = pd.DataFrame(data)
    df.sort_values(by="Exposure (%)", ascending=False, inplace=True)
    return df

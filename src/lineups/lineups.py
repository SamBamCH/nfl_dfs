import numpy as np


class Lineups:
    def __init__(self):
        self.lineups = []

    def add_lineup(self, lineup):
        """Add a new lineup to the collection."""
        formatted_lineup = [
            (player, pos, player.id) for player, pos in lineup
        ]
        self.lineups.append(formatted_lineup)

    def sort_lineup(self, lineup, site):
        """Sort a lineup by position based on the site-specific rules."""
        if site == "dk":
            order = ["QB", "RB", "RB", "WR", "WR", "WR", "TE", "FLEX", "DST"]
            sorted_lineup = [None] * 9
        else:
            order = ["PG", "PG", "SG", "SG", "SF", "SF", "PF", "PF", "C"]
            sorted_lineup = [None] * 9

        for player, pos, player_id in lineup:
            order_idx = order.index(pos)
            if sorted_lineup[order_idx] is None:
                sorted_lineup[order_idx] = (player, pos, player_id)
            else:
                # Find the next available slot for this position
                next_idx = order_idx + 1
                while next_idx < len(sorted_lineup) and sorted_lineup[next_idx] is not None:
                    next_idx += 1
                if next_idx < len(sorted_lineup):
                    sorted_lineup[next_idx] = (player, pos, player_id)

        return [slot for slot in sorted_lineup if slot is not None]  # Remove None values


    def export_to_csv(self, file_path, site):
        """Export the lineups to a CSV file."""
        with open(file_path, "w") as f:
            if site == "dk":
                f.write(
                    "QB,RB,RB,WR,WR,WR,TE,FLEX,DST,Salary,Fpts Proj,Own. Prod.,Own. Sum.,Team Stack,Runback,Stack Positions,Runback Positions,Max Non-QB Team Players,Offensive vs Defensive,Ownership Array\n"
                )
            else:
                f.write(
                    "PG,PG,SG,SG,SF,SF,PF,PF,C,Salary,Fpts Proj,Own. Prod.,Own. Sum.,Minutes,StdDev,Max Non-QB Team Players,Offensive vs Defensive,Ownership Array\n"
                )

            for lineup in self.lineups:
                # Sort the lineup according to the site's position order
                sorted_lineup = self.sort_lineup(lineup, site)

                # Calculate aggregate stats
                salary = sum(player.salary for player, _, _ in sorted_lineup)
                fpts_p = sum(player.fpts for player, _, _ in sorted_lineup)
                own_p = np.prod([player.ownership / 100 for player, _, _ in sorted_lineup])
                own_s = sum(player.ownership for player, _, _ in sorted_lineup)

                # Identify QB team and opponent
                qb = next((player for player, pos, _ in sorted_lineup if pos == "QB"), None)
                qb_team = qb.team
                qb_opponent = qb.opponent

                # Calculate stack and runback details
                stack_positions = []
                runback_positions = []
                team_stack_count = 0
                runback_count = 0
                max_non_qb_team_players = 0
                offensive_count = 0
                defensive_count = 0

                # Track non-QB team players and offensive/defensive players
                non_qb_team_players = {}
                ownership_array = []

                for player, pos, _ in sorted_lineup:
                    ownership_array.append(player.ownership)
                    if pos != "DST":
                        offensive_count += 1

                        if player.team != qb_team and player.team != qb_opponent:
                            if player.team not in non_qb_team_players:
                                non_qb_team_players[player.team] = 0
                            non_qb_team_players[player.team] += 1

                        if player.team == qb_team and pos != "QB":
                            team_stack_count += 1
                            stack_positions.append(pos)
                        elif player.team == qb_opponent:
                            runback_count += 1
                            runback_positions.append(pos)
                    else:
                        defensive_count += 1

                if non_qb_team_players:
                    max_non_qb_team_players = max(non_qb_team_players.values())

                # Generate stack strings
                team_stack_str = f"QB +{team_stack_count} | {runback_count}"
                stack_positions_str = f"{'; '.join(stack_positions)},{'; '.join(runback_positions)}"

                # Format ownership array as a line-separated string for Excel readability
                ownership_array_str = "|".join(map(str, ownership_array))

                # Create the lineup string
                lineup_str = ",".join(
                    [f"{player.name} ({player.id})" for player, _, _ in sorted_lineup]
                )
                f.write(
                    f"{lineup_str},{salary},{round(fpts_p, 2)},{own_p},{own_s},{team_stack_str},{runback_count},{stack_positions_str},{max_non_qb_team_players},{offensive_count}/{defensive_count},\"{ownership_array_str}\"\n"
                )




    def __len__(self):
        return len(self.lineups)
    
    



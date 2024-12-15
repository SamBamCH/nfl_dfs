import os
import csv
import re
from data.player import Player
from datetime import datetime
import pytz
import itertools
import json
import os

class DataManager:
    def __init__(self, site):
        self.site = site
        self.config = self.load_config()
        self.players = []
        self.lineups = []
        self.ids_to_gametime = {}
        self.eastern = pytz.timezone("US/Eastern")

    def get_project_root(self):
        """
        Returns the absolute path of the project root.
        """
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


    def _resolve_path(self, relative_path):
        """
        Resolve a relative path to an absolute path based on the project root.
        :param relative_path: The relative path from the config file.
        :return: The absolute path.
        """
        return os.path.join(self.get_project_root(), relative_path)
    
    def populate_ids_to_gametime(self):
        """
        Populate the ids_to_gametime dictionary with timezone-aware datetimes.
        """
        self.ids_to_gametime = {
            player.id: self.eastern.localize(player.gametime)
            for player in self.players
            if hasattr(player, "id") and hasattr(player, "gametime") and player.id and player.gametime
        }
        print(f"Populated ids_to_gametime with {len(self.ids_to_gametime)} entries.")


    def load_player_data(self):
        """
        Load all player data from projections, ownership, and boom-bust files.
        """
        self._load_projections(self._resolve_path(self.config["projection_path"]))
        self._load_player_ids(self._resolve_path(self.config["player_path"]))

    def _load_projections(self, path):
        with open(path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                fpts = float(row["User Proj."])
                if fpts >= self.config["projection_minimum"]:
                    # Add "FLEX" for DraftKings to a new list of positions
                    positions = [row["Pos"]]  # Convert the single position into a list
                    if "DST" not in positions and "QB" not in positions:
                        positions.append("FLEX")  # Append "FLEX" for DraftKings

                    opp = row["Opp"].split()[-1]  # Take the last part of "vs PIT" or "@ DET"

                    player = Player(
                        name=row["Name"].strip(),
                        team=row["Team"],
                        opp=opp,
                        position=positions,
                        salary=int(row["Salary"].replace(",", "")),
                        stddev=float(row["STDV"]),
                        floor=float(row["Floor"]),
                        ceiling=float(row["Ceiling"]),
                        boom=float(row["Boom"]),
                        bust=float(row["Bust"]),
                        optimal=float(row["Optimal"]),
                        own=float(row["Hero Own"]),
                        fpts=fpts,
                    )
                    self.players.append(player)

    def _load_player_ids(self, path):
        with open(path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                for player in self.players:
                    if player.name == row["Name"].strip() and player.team == row["TeamAbbrev"]:
                        player.id = row["ID"]
                        game_info = row["Game Info"]
                        try:
                            # Split Game Info to extract date and time, handle "ET"
                            date_part, time_part, _ = game_info.split()[-3:]
                            player.gametime = datetime.strptime(
                                f"{date_part} {time_part}", "%m/%d/%Y %I:%M%p"
                            )
                        except ValueError as e:
                            raise ValueError(f"Error parsing Game Info '{game_info}' for player {player.name}: {e}")
                        break


    def load_config(self):
        """
        Load the configuration file for the specified site (e.g., 'dk', 'fd').
        :param site: The site for which to load the configuration ('dk' or 'fd').
        :return: The loaded configuration as a dictionary.
        """
        config_path = "C:/Users/samba/nfl_dfs/data/dk/config/config.json"
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        with open(config_path, encoding="utf-8-sig") as file:
            return json.load(file)


    def _load_player_ids(self, path):
        with open(path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                for player in self.players:
                    if player.name == row["Name"].strip() and player.team == row["TeamAbbrev"]:
                        player.id = row["ID"]
                        game_info = row["Game Info"]
                        try:
                            # Split Game Info to extract date and time, handle "ET"
                            date_part, time_part, _ = game_info.split()[-3:]
                            player.gametime = datetime.strptime(
                                f"{date_part} {time_part}", "%m/%d/%Y %I:%M%p"
                            )
                        except ValueError as e:
                            raise ValueError(f"Error parsing Game Info '{game_info}' for player {player.name}: {e}")
                        break


    def load_player_lineups(self, path):
        # Read projections into a dictionary
        with open(path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(self.lower_first(file))
            current_time = self.eastern.localize(
                datetime(2024, 12, 13, 19, 30)  # Year, Month, Day, Hour, Minute
            )   
            # current_time = datetime.datetime(2023, 10, 24, 20, 0) # testing time, such that LAL/DEN is locked
            print(f"Current time (ET): {current_time}")
            print(f"current player ids and gametimes dict: {self.ids_to_gametime}")
            for row in reader:
                if row["entry id"] != "" and self.site == "dk":
                    PG_id = re.search(r"\((\d+)\)", row["pg"]).group(1)
                    SG_id = re.search(r"\((\d+)\)", row["sg"]).group(1)
                    SF_id = re.search(r"\((\d+)\)", row["sf"]).group(1)
                    PF_id = re.search(r"\((\d+)\)", row["pf"]).group(1)
                    C_id = re.search(r"\((\d+)\)", row["c"]).group(1)
                    G_id = re.search(r"\((\d+)\)", row["g"]).group(1)
                    F_id = re.search(r"\((\d+)\)", row["f"]).group(1)
                    UTIL_id = re.search(r"\((\d+)\)", row["util"]).group(1)
                    self.lineups.append(
                        {
                            "entry_id": row["entry id"],
                            "contest_id": row["contest id"],
                            "contest_name": row["contest name"],
                            "PG": row["pg"].replace("-", "#"),
                            "SG": row["sg"].replace("-", "#"),
                            "SF": row["sf"].replace("-", "#"),
                            "PF": row["pf"].replace("-", "#"),
                            "C": row["c"].replace("-", "#"),
                            "G": row["g"].replace("-", "#"),
                            "F": row["f"].replace("-", "#"),
                            "UTIL": row["util"].replace("-", "#"),
                            "PG_is_locked": (
                                current_time > self.ids_to_gametime[PG_id]
                                if PG_id in self.ids_to_gametime
                                else False
                            ),
                            "SG_is_locked": (
                                current_time > self.ids_to_gametime[SG_id]
                                if SG_id in self.ids_to_gametime
                                else False
                            ),
                            "SF_is_locked": (
                                current_time > self.ids_to_gametime[SF_id]
                                if SF_id in self.ids_to_gametime
                                else False
                            ),
                            "PF_is_locked": (
                                current_time > self.ids_to_gametime[PF_id]
                                if PF_id in self.ids_to_gametime
                                else False
                            ),
                            "C_is_locked": (
                                current_time > self.ids_to_gametime[C_id]
                                if C_id in self.ids_to_gametime
                                else False
                            ),
                            "G_is_locked": (
                                current_time > self.ids_to_gametime[G_id]
                                if G_id in self.ids_to_gametime
                                else False
                            ),
                            "F_is_locked": (
                                current_time > self.ids_to_gametime[F_id]
                                if F_id in self.ids_to_gametime
                                else False
                            ),
                            "UTIL_is_locked": current_time
                            > self.ids_to_gametime[UTIL_id],
                        }
                    )
        print(f"Successfully loaded {len(self.lineups)} lineups for late swap.")

    def lower_first(self, iterator):
        return itertools.chain([next(iterator).lower()], iterator)




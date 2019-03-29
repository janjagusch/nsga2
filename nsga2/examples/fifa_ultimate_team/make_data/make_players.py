import pandas as pd

from nsga2.examples.fifa_ultimate_team.player import Player
from nsga2.examples.fifa_ultimate_team.base import Base


def make_players(players_df):
    base_map = {}
    player_map = {}
    base_player_map = []
    for index, row in players_df.iterrows():
        base_id = row["base_id"]
        if base_id in base_map.keys():
            base = base_map[base_id]
        else:
            base = Base._from_pandas(row)
            base_map[base_id] = base
        player_id = row["player_id"]

        if player_id not in player_map.keys():
            player = Player._from_pandas(row)
            player.base = base
            base.players[player_id] = player
            # club = row["club"]
            # league = row["league"]
            # position = row["position"]
            # nationality = row["nationality"]
            # position = row["position"]
            # overall = row["overall"]
            # price = row["price"]
            row_dict = row.to_dict()
            row_dict["player"] = player
            row_dict["base"] = base
            base_player_map.append(
                    row_dict
            )
    base_player_map = pd.DataFrame(base_player_map)
    base_player_map = base_player_map.set_index("player_id", drop=False)
    return base_player_map

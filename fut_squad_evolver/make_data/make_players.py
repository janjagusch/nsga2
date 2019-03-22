import pandas as pd

from fut_squad_evolver.fut_elements.player import Player
from fut_squad_evolver.fut_elements.base import Base


def make_base_player_map(players_df):
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
            club = row["club"]
            league = row["league"]
            position = row["position"]
            nationality = row["nationality"]
            position = row["position"]
            overall = row["overall"]
            price = row["price"]
            base_player_map.append(
                {
                    "player_id": player_id,
                    "base_id": base_id,
                    "club": club,
                    "league": league,
                    "nationality": nationality,
                    "position": position,
                    "overall": overall,
                    "price": price,
                    "player": player,
                    "base": base
                }
            )
    base_player_map = pd.DataFrame(base_player_map)
    base_player_map = base_player_map.set_index("player_id", drop=False)
    return base_player_map

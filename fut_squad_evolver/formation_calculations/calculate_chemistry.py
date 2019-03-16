def calculate_chemistry_position(player_pos, squad_pos):
    """
    Calculates the position chemistry points between a player's preferred
    position and the position he has to play within the squad.
    Args:
        player_pos: player's preferred position
        squad_pos: position player has to play within the squad
    Returns:
        chemistry_position, integer between 0 and 3 (inclusive).
    """
    chemistry_position = 0
    pos_points = [1, 2, 3]
    if player_pos == squad_pos:
        chemistry_position = pos_points[2]
        return chemistry_position
    if squad_pos == "LWB" and player_pos == "LB":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "RWB" and player_pos == "RB":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CM" and player_pos == "CDM":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CM" and player_pos == "CAM":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CDM" and player_pos == "CM":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CAM" and player_pos == "CM":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CAM" and player_pos == "CF":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CF" and player_pos == "ST":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CF" and player_pos == "CAM":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "ST" and player_pos == "CF":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "RF" and player_pos == "RW":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "RW" and player_pos == "RF":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "RW" and player_pos == "RM":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "RM" and player_pos == "RW":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "LF" and player_pos == "LW":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "LW" and player_pos == "LF":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "LW" and player_pos == "LM":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "LM" and player_pos == "LW":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CB" and player_pos == "RB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CB" and player_pos == "CDM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CB" and player_pos == "LB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LWB" and player_pos == "LM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LWB" and player_pos == "RWB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LWB" and player_pos == "LW":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LB" and player_pos == "LM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LB" and player_pos == "RB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LB" and player_pos == "CB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LB" and player_pos == "LWB":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "RWB" and player_pos == "RM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RWB" and player_pos == "RW":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RWB" and player_pos == "LWB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RB" and player_pos == "RM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RB" and player_pos == "LB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RB" and player_pos == "CB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RB" and player_pos == "RWB":
        chemistry_position = pos_points[1]
        return chemistry_position
    if squad_pos == "CM" and player_pos == "LM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CM" and player_pos == "RM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CDM" and player_pos == "CB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CDM" and player_pos == "CAM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CAM" and player_pos == "CDM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CF" and player_pos == "LF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "CF" and player_pos == "RF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "ST" and player_pos == "LF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "ST" and player_pos == "RF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RF" and player_pos == "ST":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RF" and player_pos == "CF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RF" and player_pos == "LF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RF" and player_pos == "RM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RW" and player_pos == "LW":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RW" and player_pos == "RWB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RM" and player_pos == "RF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RM" and player_pos == "RWB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RM" and player_pos == "RB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RM" and player_pos == "LM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "RM" and player_pos == "CM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LF" and player_pos == "ST":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LF" and player_pos == "CF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LF" and player_pos == "RF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LF" and player_pos == "LM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LW" and player_pos == "RW":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LW" and player_pos == "LWB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LM" and player_pos == "LF":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LM" and player_pos == "LB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LM" and player_pos == "LWB":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LM" and player_pos == "CM":
        chemistry_position = pos_points[0]
        return chemistry_position
    if squad_pos == "LM" and player_pos == "RM":
        chemistry_position = pos_points[0]
        return chemistry_position
    return chemistry_position


def calculate_inter_player_chemistry(player_1, player_2):
    inter_player_chemistry = 0
    if player_1["club"] == player_2["club"]:
        inter_player_chemistry += 1
    if player_1["league"] == player_2["league"]:
        inter_player_chemistry += 1
    if player_1["nationality"] == player_2["nationality"]:
        inter_player_chemistry += 1
    return inter_player_chemistry


def calculate_individual_chemistry(chemistry_sum, n_connections):
    individual_chemistry = 0
    ratio = chemistry_sum / n_connections
    if ratio > 1.6:
        individual_chemistry = 3
        return individual_chemistry
    if ratio >= 1:
        individual_chemistry = 2
        return individual_chemistry
    if ratio > 0.32:
        individual_chemistry = 1
        return individual_chemistry
    return individual_chemistry


def calculate_chemistry(link_chemistry, position_chemistry):
    if link_chemistry == 0:
        if position_chemistry == 0:
            return 0
        if position_chemistry == 1:
            return 1
        if position_chemistry == 2:
            return 2
        if position_chemistry == 3:
            return 3
    if link_chemistry == 1:
        if position_chemistry == 0:
            return 1
        if position_chemistry == 1:
            return 3
        if position_chemistry == 2:
            return 5
        if position_chemistry == 3:
            return 6
    if link_chemistry == 2:
        if position_chemistry == 0:
            return 2
        if position_chemistry == 1:
            return 5
        if position_chemistry == 2:
            return 8
        if position_chemistry == 3:
            return 9
    if link_chemistry == 3:
        if position_chemistry == 0:
            return 2
        if position_chemistry == 1:
            return 5
        if position_chemistry == 2:
            return 9
        if position_chemistry == 3:
            return 10
    print(link_chemistry)
    print(position_chemistry)
    raise ValueError


def make_compatible_players(players, min_compatibility):
    compatible_positions = {position: [other_position for other_position in POSITIONS
                                       if calculate_chemistry_position(
                                           position, other_position) >= 2] for position in ALL_POSITIONS}

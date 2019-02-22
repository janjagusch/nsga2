import pickle


all_positions = ["GK", "CB", "LB", "LWB", "RB", "RWB", "CDM",
                 "CM", "CAM", "CF", "ST", "LM", "LW", "LF", "RM", "RW", "RF"]

formation_inter = {
    "3412": {
        "pos": [all_positions[10], all_positions[8], all_positions[10], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[1], all_positions[1], all_positions[1], all_positions[0]]
    },
    "3421": {
        "pos": [all_positions[13], all_positions[10], all_positions[16], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[1], all_positions[1], all_positions[1], all_positions[0]]
    },
    "343": {
        "pos": [all_positions[12], all_positions[10], all_positions[15], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[1], all_positions[1], all_positions[1], all_positions[0]]
    },
    "352": {
        "pos": [all_positions[10], all_positions[8], all_positions[10], all_positions[11], all_positions[6], all_positions[6], all_positions[14], all_positions[1], all_positions[1], all_positions[1], all_positions[0]]
    },
    "41212": {
        "pos": [all_positions[10], all_positions[8], all_positions[10], all_positions[11], all_positions[6], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "412122": {
        "pos": [all_positions[10], all_positions[8], all_positions[10], all_positions[7], all_positions[6], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4141": {
        "pos": [all_positions[10], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[6], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4231": {
        "pos": [all_positions[10], all_positions[8], all_positions[8], all_positions[8], all_positions[6], all_positions[6], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "42312": {
        "pos": [all_positions[10], all_positions[11], all_positions[8], all_positions[14], all_positions[6], all_positions[6], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4222": {
        "pos": [all_positions[10], all_positions[10], all_positions[8], all_positions[8], all_positions[6], all_positions[6], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4312": {
        "pos": [all_positions[10], all_positions[10], all_positions[8], all_positions[7], all_positions[7], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4321": {
        "pos": [all_positions[13], all_positions[10], all_positions[16], all_positions[7], all_positions[7], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "433": {
        "pos": [all_positions[12], all_positions[10], all_positions[15], all_positions[7], all_positions[7], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4332": {
        "pos": [all_positions[12], all_positions[10], all_positions[15], all_positions[7], all_positions[6], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4333": {
        "pos": [all_positions[12], all_positions[10], all_positions[15], all_positions[6], all_positions[7], all_positions[6], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4334": {
        "pos": [all_positions[12], all_positions[10], all_positions[15], all_positions[7], all_positions[8], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4335": {
        "pos": [all_positions[12], all_positions[9], all_positions[15], all_positions[7], all_positions[6], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4411": {
        "pos": [all_positions[10], all_positions[9], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "442": {
        "pos": [all_positions[10], all_positions[10], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4422": {
        "pos": [all_positions[10], all_positions[10], all_positions[11], all_positions[6], all_positions[6], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "451": {
        "pos": [all_positions[10], all_positions[11], all_positions[8], all_positions[7], all_positions[8], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4512": {
        "pos": [all_positions[10], all_positions[11], all_positions[7], all_positions[7], all_positions[7], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "5212": {
        "pos": [all_positions[10], all_positions[8], all_positions[10], all_positions[7], all_positions[7], all_positions[3], all_positions[1], all_positions[1], all_positions[1], all_positions[5], all_positions[0]]
    },
    "5221": {
        "pos": [all_positions[12], all_positions[10], all_positions[15], all_positions[7], all_positions[7], all_positions[3], all_positions[1], all_positions[1], all_positions[1], all_positions[5], all_positions[0]]
    },
    "532": {
        "pos": [all_positions[10], all_positions[10], all_positions[7], all_positions[7], all_positions[7], all_positions[3], all_positions[1], all_positions[1], all_positions[1], all_positions[5], all_positions[0]]
    },
    "541": {
        "pos": [all_positions[10], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[3], all_positions[1], all_positions[1], all_positions[1], all_positions[5], all_positions[0]]
    },
    "44112": {
        "pos": [all_positions[10], all_positions[8], all_positions[11], all_positions[7], all_positions[7], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "424": {
        "pos": [all_positions[10], all_positions[10], all_positions[12], all_positions[15], all_positions[7], all_positions[7], all_positions[2], all_positions[1], all_positions[1], all_positions[4], all_positions[0]]
    },
    "4132": {
        "pos": [all_positions[10], all_positions[10], all_positions[7], all_positions[11], all_positions[6], all_positions[14], all_positions[2], all_positions[1], all_positions[1], all_positions[1], all_positions[0]]
    },
    "3142": {
        "pos": [all_positions[10], all_positions[10], all_positions[11], all_positions[7], all_positions[6], all_positions[7], all_positions[14], all_positions[1], all_positions[1], all_positions[1], all_positions[0]]
    }
}

formation_pos = {
    "3412": {
        "STL": 1,
        "CAM": 2,
        "STR": 3,
        "LM": 4,
        "CDM": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CB": 9,
        "CBR": 10,
        "GK": 11
    },
    "3421": {
        "LF": 1,
        "ST": 2,
        "RF": 3,
        "LM": 4,
        "CML": 5,
        "CMR": 6,
        "RM": 7,
        "CBL": 8,
        "CB": 9,
        "CBR": 10,
        "GK": 11
    },
    "343": {
        "LW": 1,
        "ST": 2,
        "RW": 3,
        "LM": 4,
        "CML": 5,
        "CMR": 6,
        "RM": 7,
        "CBL": 8,
        "CB": 9,
        "CBR": 10,
        "GK": 11
    },
    "352": {
        "STL": 1,
        "CAM": 2,
        "STR": 3,
        "LM": 4,
        "CDML": 5,
        "CDMR": 6,
        "RM": 7,
        "CBL": 8,
        "CB": 9,
        "CBR": 10,
        "GK": 11
    },
    "41212": {
        "STL": 1,
        "CAM": 2,
        "STR": 3,
        "LM": 4,
        "CDM": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "412122": {
        "STL": 1,
        "CAM": 2,
        "STR": 3,
        "CML": 4,
        "CDM": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4141": {
        "ST": 1,
        "LM": 2,
        "CML": 3,
        "CMR": 4,
        "RM": 5,
        "CDM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4231": {
        "ST": 1,
        "CAML": 2,
        "CAM": 3,
        "CAMR": 4,
        "CDML": 5,
        "CDMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "42312": {
        "ST": 1,
        "LM": 2,
        "CAM": 3,
        "RM": 4,
        "CDML": 5,
        "CDMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4222": {
        "STL": 1,
        "STR": 2,
        "CAML": 3,
        "CAMR": 4,
        "CDML": 5,
        "CDMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "LW": 11
    },
    "4312": {
        "STL": 1,
        "STR": 2,
        "CAML": 3,
        "CML": 4,
        "CM": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4321": {
        "LF": 1,
        "ST": 2,
        "RF": 3,
        "CML": 4,
        "CM": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "LW": 11
    },
    "433": {
        "LW": 1,
        "ST": 2,
        "RW": 3,
        "CML": 4,
        "CM": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4332": {
        "LW": 1,
        "ST": 2,
        "RW": 3,
        "CML": 4,
        "CDM": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "LW": 11
    },
    "4333": {
        "LW": 1,
        "ST": 2,
        "RW": 3,
        "CDML": 4,
        "CM": 5,
        "CDMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4334": {
        "LW": 1,
        "ST": 2,
        "RW": 3,
        "CML": 4,
        "CAM": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "LW": 11
    },
    "4335": {
        "LW": 1,
        "CF": 2,
        "RW": 3,
        "CML": 4,
        "CDM": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4411": {
        "ST": 1,
        "CF": 2,
        "LM": 3,
        "CML": 4,
        "CMR": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "LW": 11
    },
    "442": {
        "STL": 1,
        "STR": 2,
        "LM": 3,
        "CML": 4,
        "CMR": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4422": {
        "STL": 1,
        "STR": 2,
        "LM": 3,
        "CDML": 4,
        "CDMR": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "LW": 11
    },
    "451": {
        "ST": 1,
        "LM": 2,
        "CAML": 3,
        "CM": 4,
        "CAMR": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4512": {
        "ST": 1,
        "LM": 2,
        "CML": 3,
        "CM": 4,
        "CMR": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "LW": 11
    },
    "5212": {
        "STL": 1,
        "CAM": 2,
        "STR": 3,
        "CML": 4,
        "CMR": 5,
        "LWB": 6,
        "CBR": 7,
        "CBL": 8,
        "CB": 9,
        "RWB": 10,
        "GK": 11
    },
    "5221": {
        "LW": 1,
        "ST": 2,
        "RW": 3,
        "CML": 4,
        "CMR": 5,
        "LWB": 6,
        "CBR": 7,
        "CBL": 8,
        "CB": 9,
        "RWB": 10,
        "GK": 11
    },
    "532": {
        "STL": 1,
        "STR": 2,
        "CML": 3,
        "CM": 4,
        "CMR": 5,
        "LWB": 6,
        "CBR": 7,
        "CBL": 8,
        "CB": 9,
        "RWB": 10,
        "GK": 11
    },
    "541": {
        "ST": 1,
        "LM": 2,
        "CML": 3,
        "CMR": 4,
        "RM": 5,
        "LWB": 6,
        "CBL": 7,
        "CB": 8,
        "CBR": 9,
        "RWB": 10,
        "GK": 11
    },
    "44112": {
        "ST": 1,
        "CAM": 2,
        "LM": 3,
        "CML": 4,
        "CMR": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "424": {
        "STL": 1,
        "STR": 2,
        "LW": 3,
        "RW": 4,
        "CML": 5,
        "CMR": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11
    },
    "4132": {
        "STL": 1,
        "STR": 2,
        "CM": 3,
        "LM": 4,
        "CDM": 5,
        "RM": 6,
        "LB": 7,
        "CBL": 8,
        "CBR": 9,
        "RB": 10,
        "GK": 11

    },
    "3142": {
        "STL": 1,
        "STR": 2,
        "LM": 3,
        "CML": 4,
        "CDM": 5,
        "CMR": 6,
        "RM": 7,
        "CBL": 8,
        "CB": 9,
        "CBR": 10,
        "GK": 11
    }
}

formation_draw = {
    "3412": {
        "draw": {
            11: ["CB", "CBR", "CBL"],
            10: ["GK", "CB", "LB"],
            9: ["GK", "CBL", "CBR", "CDM", "RM"],
            8: ["GK", "CB", "LM"],
            7: ["RM", "CBR", "STR"],
            6: ["CB", "CDM", "CAM", "LB"],
            5: ["CB", "CAM", "LM", "RM"],
            4: ["CBL", "STL", "CDM"],
            3: ["LB", "STL", "CAM"],
            2: ["CDM", "STL", "STR", "RM"],
            1: ["CAM", "STR", "LM"]
        }
    },
    "3421": {
        "draw": {
            11: ["CBL", "CB", "CBR"],
            10: ["RM", "CB", "GK"],
            9: ["GK", "CMR", "CML", "CBL", "CBR"],
            8: ["GK", "LM", "CB"],
            7: ["RF", "CMR", "CBR"],
            6: ["CB", "CML", "RF", "RM"],
            5: ["CB", "LF", "LM", "CMR"],
            4: ["LF", "CML", "CBL"],
            3: ["RM", "CMR", "ST"],
            2: ["RF", "LF"],
            1: ["ST", "LM", "CML"]
        }
    },
    "343": {
        "draw": {
            11: ["CBR", "CBL", "CB"],
            10: ["GK", "RM", "CB"],
            9: ["CMR", "CBR", "CML", "CBL", "GK"],
            8: ["GK", "LM", "CB"],
            7: ["RW", "CMR", "CBR"],
            6: ["RM", "CB", "CML", "ST"],
            5: ["ST", "CMR", "CB", "LM"],
            4: ["LW", "CBL", "CML"],
            3: ["RM", "ST"],
            2: ["CML", "LW", "RW", "CMR"],
            1: ["LM", "ST"]
        }
    },
    "352": {
        "draw": {
            11: ["CBL", "CB", "CBR"],
            10: ["CDMR", "RM", "CB", "GK"],
            9: ["CDML", "CDMR", "CBL", "CBR", "GK"],
            8: ["LM", "CDML", "CB", "GK"],
            7: ["STR", "CDMR", "CBR"],
            6: ["CAM", "CDML", "RM", "CB", "CBR"],
            5: ["CAM", "LM", "CDMR", "CBL", "CB"],
            4: ["STL", "CDML", "CBL"],
            3: ["STL", "CAM", "RM"],
            2: ["STL", "STR", "CDML", "CDMR"],
            1: ["CAM", "STR", "LM"]
        }
    },
    "41212": {
        "draw": {
            11: ["CBL", "CBR"],
            10: ["RM", "CBR"],
            9: ["GK", "CBL", "RB", "CDM"],
            8: ["LB", "CBR", "GK", "CDM"],
            7: ["CBL", "LM"],
            6: ["CDM", "CAM", "STR", "RB"],
            5: ["CBL", "CAM", "LM", "RM", "CBR"],
            4: ["CAM", "STL", "CDM", "LB"],
            3: ["STL", "CAM", "RM"],
            2: ["LM", "STL", "STR", "CDM", "RM"],
            1: ["STR", "CAM", "LM"]
        }
    },
    "412122": {
        "draw": {
            11: ["CBL", "CBR"],
            10: ["CMR", "CBR"],
            9: ["CDM", "CBL", "RB", "GK"],
            8: ["CDM", "LB", "CBR", "GK"],
            7: ["CML", "CBL"],
            6: ["CAM", "CDM", "STR", "RB"],
            5: ["CMR", "CAM", "CML", "CBL", "CBR"],
            4: ["STL", "CAM", "CDM", "LB"],
            3: ["CAM", "STL", "CMR"],
            2: ["CMR", "STR", "STL", "CML", "CDM"],
            1: ["CAM", "CML", "STR"]
        }
    },
    "4141": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["RM", "CBR"],
            9: ["CMR", "RB", "CBL", "CDM", "GK"],
            8: ["CML", "CDM", "LB", "CBR", "GK"],
            7: ["CBL", "LM"],
            6: ["CBL", "CMR", "CML", "CBR"],
            5: ["CMR", "ST", "RB"],
            4: ["ST", "CML", "RM", "CDM", "CBR"],
            3: ["CMR", "ST", "LM", "CBL", "CDM"],
            2: ["LB", "ST", "CML"],
            1: ["CML", "LM", "CMR", "RM"]
        }
    },
    "4231": {
        "draw": {
            11: ["CBL", "CBR"],
            10: ["CDMR", "CBR"],
            9: ["CBL", "CDMR", "RB", "GK"],
            8: ["CDML", "CBR", "LB", "GK"],
            7: ["CBL", "CDML"],
            6: ["CAMR", "CAM", "CBR", "RB"],
            5: ["CAML", "LB", "CAM", "CBL"],
            4: ["CAM", "ST", "CDMR"],
            3: ["CAML", "CAMR", "CDML", "ST", "CDMR"],
            2: ["CAM", "ST", "CDML"],
            1: ["CAM", "CAML", "CAMR"]
        }
    },
    "42312": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["CDMR", "RM", "CBR"],
            9: ["GK", "CDMR", "CBL", "RB"],
            8: ["GK", "CDML", "LB", "CBR"],
            7: ["CDML", "LM", "CBL"],
            6: ["RB", "RM", "CAM", "CBR"],
            5: ["LB", "CAM", "LM", "CBL"],
            4: ["CAM", "CDMR", "ST", "RB"],
            3: ["ST", "LM", "RM", "CDML", "CDMR"],
            2: ["CAM", "ST", "CDML", "LB"],
            1: ["RM", "CAM", "LM"]
        }
    },
    "4222": {
        "draw": {
            11: ["CBL", "CBR"],
            10: ["CAMR", "CBR"],
            9: ["RB", "CDMR", "CBL", "GK"],
            8: ["CDML", "CBR", "LB", "GK"],
            7: ["CAML", "CBL"],
            6: ["STR", "CDML", "CAMR", "CBR"],
            5: ["CDMR", "STL", "CAML", "CBL"],
            4: ["CDMR", "STR", "RB"],
            3: ["LB", "STL", "CDML"],
            2: ["STL", "CDMR", "CAMR"],
            1: ["CAML", "STR", "CDML"]
        }
    },
    "4312": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["CMR", "CBR"],
            9: ["CMR", "CM", "RB", "CBL", "GK"],
            8: ["CBR", "CML", "CM", "LB", "GK"],
            7: ["CML", "CBL"],
            6: ["CBR", "STR", "CM", "RB"],
            5: ["CMR", "CAML", "CBL", "CML", "CBR"],
            4: ["LB", "STL", "CM", "CBL"],
            3: ["STR", "STL", "CM"],
            2: ["CAML", "CMR", "STL"],
            1: ["CML", "STR", "CAML"]
        }
    },
    "4321": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["CBR", "CMR"],
            9: ["RB", "CMR", "CBL", "GK"],
            8: ["LB", "CML", "CBR", "GK"],
            7: ["CML", "CBL"],
            6: ["CBR", "RF", "CM", "RB"],
            5: ["CML", "LF", "RF", "CMR"],
            4: ["LF", "CBL", "CM", "LB"],
            3: ["CM", "ST", "CMR"],
            2: ["RF", "LF"],
            1: ["CML", "ST", "CM"]
        }
    },
    "433": {
        "draw": {
            11: ["CBL", "CBR"],
            10: ["CMR", "CBR"],
            9: ["GK", "CM", "CBL", "RB"],
            8: ["GK", "LB", "CM", "CBR"],
            7: ["CBL", "CML"],
            6: ["CM", "RW", "RB"],
            5: ["CBL", "CML", "ST", "CMR", "CBR"],
            4: ["CM", "LW", "LB"],
            3: ["CMR", "ST"],
            2: ["RW", "LW", "CM"],
            1: ["ST", "CML"]
        }
    },
    "4332": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["CBR", "CMR"],
            9: ["RB", "CDM", "CBL", "GK"],
            8: ["CDM", "LB", "CBR", "GK"],
            7: ["CML", "CBL"],
            6: ["ST", "RW", "CML", "CDM", "RB"],
            5: ["CMR", "CBL", "CML", "CBR"],
            4: ["LW", "ST", "CMR", "CDM", "LB"],
            3: ["CMR", "ST"],
            2: ["CMR", "LW", "RW", "CML"],
            1: ["CML", "ST"]
        }
    },
    "4333": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["CDMR", "CBR"],
            9: ["RB", "CDMR", "CBL", "GK"],
            8: ["LB", "CDML", "CBR", "GK"],
            7: ["CBL", "CDML"],
            6: ["CBR", "RW", "CM", "RB"],
            5: ["ST", "CDMR", "CDML"],
            4: ["CBL", "LW", "CM", "LB"],
            3: ["CDMR", "ST"],
            2: ["RW", "LW", "CM"],
            1: ["CDML", "ST"]
        }
    },
    "4334": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["CMR", "RW", "CBR"],
            9: ["RB", "CMR", "CBL", "GK"],
            8: ["LB", "CML", "CBR", "GK"],
            7: ["CBL", "LW", "CML"],
            6: ["CAM", "RW", "CBR", "RB"],
            5: ["CMR", "ST", "CML"],
            4: ["LB", "LW", "CAM", "CBL"],
            3: ["ST", "RB", "CMR"],
            2: ["CAM", "LW", "RW"],
            1: ["CML", "ST", "LB"]
        }
    },
    "4335": {
        "draw": {
            11: ["CBL", "CBR"],
            10: ["CBR", "RW", "CMR"],
            9: ["CDM", "RB", "CBL", "GK"],
            8: ["LB", "CDM", "CBR", "GK"],
            7: ["CML", "LW", "CBL"],
            6: ["CDM", "CF", "RW", "RB"],
            5: ["CML", "CBL", "CMR", "CBR"],
            4: ["CF", "LW", "CDM", "LB"],
            3: ["RB", "CF", "CMR"],
            2: ["RW", "LW", "CML", "CMR"],
            1: ["LB", "CF", "CML"]
        }
    },
    "4411": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["RM", "CBR"],
            9: ["GK", "CBL", "CMR", "RB"],
            8: ["GK", "CML", "LB", "CBR"],
            7: ["LM", "CBL"],
            6: ["CMR", "ST", "RB"],
            5: ["RM", "CF", "CBR", "CML"],
            4: ["CF", "CMR", "LM", "CBL"],
            3: ["CML", "ST", "LB"],
            2: ["ST", "CMR", "CML"],
            1: ["LM", "CF", "RM"]
        }
    },
    "442": {
        "draw": {
            11: ["CBL", "CBR"],
            10: ["CBR", "RM"],
            9: ["CMR", "RB", "CBL", "GK"],
            8: ["LB", "CML", "CBR", "GK"],
            7: ["CBL", "LM"],
            6: ["CMR", "STR", "RB"],
            5: ["STR", "RM", "CML", "CBR"],
            4: ["CBL", "STL", "LM", "CMR"],
            3: ["STL", "CML", "LB"],
            2: ["CMR", "STL", "RM"],
            1: ["LM", "STR", "CML"]
        }
    },
    "4422": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["RM", "CBR"],
            9: ["GK", "CBL", "CDMR", "RB"],
            8: ["GK", "CDML", "LB", "CBR"],
            7: ["LM", "CBL"],
            6: ["CDMR", "STR", "RB"],
            5: ["RM", "STR", "CDML", "CBR"],
            4: ["CBL", "STL", "LM", "CDMR"],
            3: ["CDML", "STL", "LB"],
            2: ["STL", "RM", "CDMR"],
            1: ["LM", "STR", "CDML"]
        }
    },
    "451": {
        "draw": {
            1: ["CAML", "CAMR"],
            2: ["LB", "CAML"],
            3: ["CM", "ST", "LM", "CAMR"],
            4: ["CAML", "CBL", "CAMR", "CBR"],
            5: ["RM", "CM", "ST", "CAML"],
            6: ["RB", "CAMR"],
            7: ["CBL", "LM"],
            8: ["CBR", "CM", "GK", "LB"],
            9: ["CM", "CBL", "GK", "RB"],
            10: ["CBR", "RM"],
            11: ["CBL", "CBR"]
        }
    },
    "4512": {
        "draw": {
            11: ["CBR", "CBL"],
            10: ["CBR", "CMR", "RM"],
            9: ["CBL", "RB", "CM", "CMR", "GK"],
            8: ["LB", "CBR", "CML", "CM", "GK"],
            7: ["LM", "CBL", "CML"],
            6: ["CMR", "ST", "RB"],
            5: ["CBR", "CM", "RM", "RB"],
            4: ["CML", "CMR", "ST", "CBL", "CBR"],
            3: ["LB", "LM", "CM", "CBL"],
            2: ["CML", "ST", "LB"],
            1: ["CM", "LM", "RM"]
        }
    },
    "5212": {
        "draw": {
            11: ["CBL", "CBR", "CB"],
            10: ["CBR", "CMR"],
            9: ["CMR", "CML", "CBR", "CBL", "GK"],
            8: ["CB", "LWB", "GK"],
            7: ["CB", "RWB", "GK"],
            6: ["CBL", "CML"],
            5: ["CAM", "STR", "CB", "CML", "RWB"],
            4: ["CAM", "CMR", "STL", "LWB", "CB"],
            3: ["CAM", "STL", "CMR"],
            2: ["STR", "CML", "STL", "CMR"],
            1: ["CML", "CAM", "STR"]
        }
    },
    "5221": {
        "draw": {
            11: ["CBL", "CBR", "CB"],
            10: ["CBR", "RW", "CMR"],
            9: ["CML", "CMR", "CBL", "CBR", "GK"],
            8: ["GK", "LWB", "CB"],
            7: ["GK", "CB", "RWB"],
            6: ["CML", "LW", "CBL"],
            5: ["CML", "CB", "RWB", "ST", "RW"],
            4: ["CMR", "LWB", "CB", "LW", "ST"],
            3: ["ST", "RWB", "CMR"],
            2: ["RW", "CML", "LW", "CMR"],
            1: ["LWB", "ST", "CML"]
        }
    },
    "532": {
        "draw": {
            11: ["CBL", "CBR", "CB"],
            10: ["CBR", "CMR"],
            9: ["CBR", "CBL", "CM", "GK"],
            8: ["CML", "CB", "LWB", "GK"],
            7: ["CB", "CMR", "RWB", "GK"],
            6: ["CBL", "CML"],
            5: ["CM", "CBR", "STR", "RWB"],
            4: ["CMR", "CB", "STL", "STR", "CML"],
            3: ["LWB", "CBL", "STL", "CM"],
            2: ["CM", "STL", "CMR"],
            1: ["STR", "CM", "CML"]
        }
    },
    "541": {
        "draw": {
            11: [7, 8, 9],
            10: [4, 5, 9],
            9: [8, 10, 11],
            8: [3, 4, 7, 9, 11],
            7: [6, 8, 11],
            6: [2, 7, 3],
            5: [1, 4, 10],
            4: [1, 3, 5, 8, 10],
            3: [1, 2, 4, 8, 6],
            2: [1, 3, 6],
            1: [2, 3, 4, 5]
        }
    },
    "44112": {
        "draw": {
            11: [8, 9],
            10: [6, 9],
            9: [5, 8, 10, 11],
            8: [4, 7, 9, 11],
            7: [3, 8],
            6: [1, 5, 10],
            5: [2, 4, 6, 9],
            4: [2, 3, 5, 8],
            3: [1, 4, 7],
            2: [1, 4, 5],
            1: [2, 3, 6]
        }
    },
    "424": {
        "draw": {
            11: [8, 9],
            10: [4, 6, 9],
            9: [6, 8, 10, 11],
            8: [5, 7, 9, 11],
            7: [3, 5, 8],
            6: [2, 4, 5, 10],
            5: [1, 3, 6, 7],
            4: [2, 6, 10],
            3: [1, 5, 7],
            2: [1, 4, 6],
            1: [2, 3, 5]
        }
    },
    "4132": {
        "draw": {
            11: [8, 9],
            10: [6, 9],
            9: [5, 8, 10, 11],
            8: [5, 7, 9, 11],
            7: [4, 8],
            6: [2, 3, 5, 10],
            5: [3, 4, 6, 8, 9],
            4: [1, 3, 5, 7],
            3: [1, 2, 4, 6],
            2: [1, 3, 6],
            1: [2, 3, 4]
        }
    },
    "3142": {
        "draw": {
            11: [8, 9, 10],
            10: [5, 7, 9, 11],
            9: [5, 8, 10, 11],
            8: [3, 5, 9, 11],
            7: [2, 6, 10],
            6: [2, 5, 7],
            5: [4, 6, 8, 9, 10],
            4: [1, 3, 5],
            3: [1, 4, 8],
            2: [1, 6, 7],
            1: [2, 3, 4]
        }
    }
}

# for key, value in make_formations.formation_pos[formation].items():
#     print("{}: {}".format(
#         key, make_formations.formation_inter_pos[formation]["pos"][value - 1]))


def make_formation(formation_id):
    inter = formation_inter[formation_id]["pos"]
    pos = formation_pos[formation_id]
    draw = formation_draw[formation_id]["draw"]
    formation = {}
    formation["pos"] = {}
    formation["draw"] = {}
    for key, value in pos.items():
        formation["pos"][key] = inter[value - 1]
    for key, value in draw.items():
        for sub_key, sub_value in pos.items():
            if key == sub_value:
                break
        if isinstance(value[0], int):
            new_values = []
            for val in value:
                for nk, nv in pos.items():
                    if nv == val:
                        new_values.append(nk)
        else:
            new_values = value
        formation["draw"][sub_key] = new_values
    return formation


formations = {}
for formation_id in formation_pos.keys():
    formations[formation_id] = make_formation(formation_id)
with open("data/processed/formations.p", "wb") as file_pointer:
    pickle.dump(formations, file_pointer)

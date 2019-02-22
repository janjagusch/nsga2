function regchem() {
    for (var i = 1; i < 12; i++) {
        pcdisplaymain2 = $("#cardlid" + i).hasClass("added");
        if (window.squad_action != "edit") {
            if (pcdisplaymain2 == true) {
                var position = $("#cardlid" + i).attr("data-formpos");
                var player_pos = $("#cardlid" + i).children(".ui-draggable").find(".pcdisplay-pos").html();
                var position_html = $("#cardlid" + i).children(".ui-draggable").find(".pcdisplay-pos");
                if ((position == "GK" && player_pos == "GK") == true) {
                    position_html.html(position)
                }
                if ((position == "CB" && player_pos == "CB") == true) {
                    position_html.html(position)
                }
                if ((position == "ST" && player_pos == "CM") == true) {
                    position_html.html(position)
                }
                if ((position == "ST" && player_pos == "CDM") == true) {
                    position_html.html(position)
                }
                if ((position == "ST" && player_pos == "CAM") == true) {
                    position_html.html(position)
                }
                if ((position == "ST" && player_pos == "CF") == true) {
                    position_html.html(position)
                }
                if ((position == "ST" && player_pos == "ST") == true) {
                    position_html.html(position)
                }
                if ((position == "CF" && player_pos == "CM") == true) {
                    position_html.html(position)
                }
                if ((position == "CF" && player_pos == "CDM") == true) {
                    position_html.html(position)
                }
                if ((position == "CF" && player_pos == "CAM") == true) {
                    position_html.html(position)
                }
                if ((position == "CF" && player_pos == "CF") == true) {
                    position_html.html(position)
                }
                if ((position == "CF" && player_pos == "ST") == true) {
                    position_html.html(position)
                }
                if ((position == "CM" && player_pos == "CM") == true) {
                    position_html.html(position)
                }
                if ((position == "CM" && player_pos == "CDM") == true) {
                    position_html.html(position)
                }
                if ((position == "CM" && player_pos == "CAM") == true) {
                    position_html.html(position)
                }
                if ((position == "CM" && player_pos == "CF") == true) {
                    position_html.html(position)
                }
                if ((position == "CM" && player_pos == "ST") == true) {
                    position_html.html(position)
                }
                if ((position == "CAM" && player_pos == "CM") == true) {
                    position_html.html(position)
                }
                if ((position == "CAM" && player_pos == "CDM") == true) {
                    position_html.html(position)
                }
                if ((position == "CAM" && player_pos == "CAM") == true) {
                    position_html.html(position)
                }
                if ((position == "CAM" && player_pos == "CF") == true) {
                    position_html.html(position)
                }
                if ((position == "CAM" && player_pos == "ST") == true) {
                    position_html.html(position)
                }
                if ((position == "CDM" && player_pos == "CM") == true) {
                    position_html.html(position)
                }
                if ((position == "CDM" && player_pos == "CDM") == true) {
                    position_html.html(position)
                }
                if ((position == "CDM" && player_pos == "CAM") == true) {
                    position_html.html(position)
                }
                if ((position == "CDM" && player_pos == "CF") == true) {
                    position_html.html(position)
                }
                if ((position == "CDM" && player_pos == "ST") == true) {
                    position_html.html(position)
                }
                if ((position == "LW" && player_pos == "LM") == true) {
                    position_html.html(position)
                }
                if ((position == "LW" && player_pos == "LF") == true) {
                    position_html.html(position)
                }
                if ((position == "LW" && player_pos == "LW") == true) {
                    position_html.html(position)
                }
                if ((position == "LM" && player_pos == "LM") == true) {
                    position_html.html(position)
                }
                if ((position == "LM" && player_pos == "LF") == true) {
                    position_html.html(position)
                }
                if ((position == "LM" && player_pos == "LW") == true) {
                    position_html.html(position)
                }
                if ((position == "LF" && player_pos == "LM") == true) {
                    position_html.html(position)
                }
                if ((position == "LF" && player_pos == "LF") == true) {
                    position_html.html(position)
                }
                if ((position == "LF" && player_pos == "LW") == true) {
                    position_html.html(position)
                }
                if ((position == "RW" && player_pos == "RM") == true) {
                    position_html.html(position)
                }
                if ((position == "RW" && player_pos == "RF") == true) {
                    position_html.html(position)
                }
                if ((position == "RW" && player_pos == "RW") == true) {
                    position_html.html(position)
                }
                if ((position == "RM" && player_pos == "RM") == true) {
                    position_html.html(position)
                }
                if ((position == "RM" && player_pos == "RF") == true) {
                    position_html.html(position)
                }
                if ((position == "RM" && player_pos == "RW") == true) {
                    position_html.html(position)
                }
                if ((position == "RF" && player_pos == "RM") == true) {
                    position_html.html(position)
                }
                if ((position == "RF" && player_pos == "RF") == true) {
                    position_html.html(position)
                }
                if ((position == "RF" && player_pos == "RW") == true) {
                    position_html.html(position)
                }
                if ((position == "LWB" && player_pos == "LB") == true) {
                    position_html.html(position)
                }
                if ((position == "LB" && player_pos == "LWB") == true) {
                    position_html.html(position)
                }
                if ((position == "RWB" && player_pos == "RB") == true) {
                    position_html.html(position)
                }
                if ((position == "RB" && player_pos == "RWB") == true) {
                    position_html.html(position)
                }
            }
        }
    }
    ChemistrySquad()
}
var chem3_positions = {
    ST: '("ST", "CF", "CAM", "CM", "CDM")',
    CF: '("ST", "CF", "CAM", "CM", "CDM")',
    CAM: '("ST", "CF", "CAM", "CM", "CDM")',
    CM: '("ST", "CF", "CAM", "CM", "CDM")',
    CDM: '("ST", "CF", "CAM", "CM", "CDM")',
    LF: '("LF", "LW", "LM")',
    LW: '("LF", "LW", "LM")',
    LM: '("LF", "LW", "LM")',
    RF: '("RF", "RW", "RM")',
    RW: '("RF", "RW", "RM")',
    RM: '("RF", "RW", "RM")',
    LB: '("LB", "LWB")',
    LWB: '("LB", "LWB")',
    RB: '("RB", "RWB")',
    RWB: '("RB", "RWB")',
    CB: '("CB")',
    GK: '("GK")'
};
var switch_pos = {
    GK: {
        change: allpositions[0]
    },
    RB: {
        change: [allpositions[4], allpositions[5]]
    },
    RWB: {
        change: [allpositions[4], allpositions[5]]
    },
    LB: {
        change: [allpositions[2], allpositions[3]]
    },
    LWB: {
        change: [allpositions[2], allpositions[3]]
    },
    CB: {
        change: allpositions[1]
    },
    RW: {
        change: [allpositions[14], allpositions[15], allpositions[16]]
    },
    RF: {
        change: [allpositions[14], allpositions[15], allpositions[16]]
    },
    RM: {
        change: [allpositions[14], allpositions[15], allpositions[16]]
    },
    LW: {
        change: [allpositions[11], allpositions[12], allpositions[13]]
    },
    LF: {
        change: [allpositions[11], allpositions[12], allpositions[13]]
    },
    LM: {
        change: [allpositions[11], allpositions[12], allpositions[13]]
    },
    CDM: {
        change: [allpositions[6], allpositions[7], allpositions[8], allpositions[9], allpositions[10]]
    },
    CM: {
        change: [allpositions[6], allpositions[7], allpositions[8], allpositions[9], allpositions[10]]
    },
    CAM: {
        change: [allpositions[6], allpositions[7], allpositions[8], allpositions[9], allpositions[10]]
    },
    CF: {
        change: [allpositions[6], allpositions[7], allpositions[8], allpositions[9], allpositions[10]]
    },
    ST: {
        change: [allpositions[6], allpositions[7], allpositions[8], allpositions[9], allpositions[10]]
    }
};
var chem0_positions = {
    ST: '("LF", "LW", "LM", "RF", "RW", "RM")',
    CF: '("LF", "LW", "LM", "RF", "RW", "RM")',
    CAM: '("LF", "LW", "LM", "RF", "RW", "RM", "CB")',
    CM: '("LF", "LW", "LM", "RF", "RW", "RM", "CB")',
    CDM: '("LF", "LW", "LM", "RF", "RW", "RM", "CB")',
    LF: '("ST", "CF", "CAM", "CM", "CDM", "RF", "RW", "RM")',
    LW: '("RW", "RF", "RM", "LWB", "LB")',
    LM: '("ST", "CF", "CAM", "CM", "CDM", "LB", "LWB", "RM", "RW", "RF")',
    RF: '("ST", "CF", "CAM", "CM", "CDM", "LF", "LW", "LM")',
    RW: '("LW", "LF", "LM", "RWB", "RB")',
    RM: '("ST", "CF", "CAM", "CM", "CDM", "RB", "LM", "LW", "LF", "RWB")',
    LB: '("LF", "LW", "LM", "CB", "RB", "RWB")',
    LWB: '("LF", "LW", "LM", "RWB", "RB")',
    RB: '("RF", "RW", "RM", "CB", "LB", "LWB")',
    RWB: '("RF", "RW", "RM", "LWB", "LB")',
    CB: '("RB", "LB", "ST", "CF", "CAM", "CM", "CDM")',
    GK: '("")'
};
var allpositions = ["GK", "CB", "LB", "LWB", "RB", "RWB", "CDM", "CM", "CAM", "CF", "ST", "LM", "LW", "LF", "RM", "RW", "RF"];
var formation_pos = {
    3412: {
        pos: [allpositions[10], allpositions[8], allpositions[10], allpositions[11], allpositions[7], allpositions[7], allpositions[14], allpositions[1], allpositions[1], allpositions[1], allpositions[0]]
    },
    3421: {
        pos: [allpositions[13], allpositions[10], allpositions[16], allpositions[11], allpositions[7], allpositions[7], allpositions[14], allpositions[1], allpositions[1], allpositions[1], allpositions[0]]
    },
    343: {
        pos: [allpositions[12], allpositions[10], allpositions[15], allpositions[11], allpositions[7], allpositions[7], allpositions[14], allpositions[1], allpositions[1], allpositions[1], allpositions[0]]
    },
    352: {
        pos: [allpositions[10], allpositions[8], allpositions[10], allpositions[11], allpositions[6], allpositions[6], allpositions[14], allpositions[1], allpositions[1], allpositions[1], allpositions[0]]
    },
    41212: {
        pos: [allpositions[10], allpositions[8], allpositions[10], allpositions[11], allpositions[6], allpositions[14], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "41212-2": {
        pos: [allpositions[10], allpositions[8], allpositions[10], allpositions[7], allpositions[6], allpositions[7], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    4141: {
        pos: [allpositions[10], allpositions[11], allpositions[7], allpositions[7], allpositions[14], allpositions[6], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    4231: {
        pos: [allpositions[10], allpositions[8], allpositions[8], allpositions[8], allpositions[6], allpositions[6], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "4231-2": {
        pos: [allpositions[10], allpositions[11], allpositions[8], allpositions[14], allpositions[6], allpositions[6], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    4222: {
        pos: [allpositions[10], allpositions[10], allpositions[8], allpositions[8], allpositions[6], allpositions[6], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    4312: {
        pos: [allpositions[10], allpositions[10], allpositions[8], allpositions[7], allpositions[7], allpositions[7], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    4321: {
        pos: [allpositions[13], allpositions[10], allpositions[16], allpositions[7], allpositions[7], allpositions[7], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    433: {
        pos: [allpositions[12], allpositions[10], allpositions[15], allpositions[7], allpositions[7], allpositions[7], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "433-2": {
        pos: [allpositions[12], allpositions[10], allpositions[15], allpositions[7], allpositions[6], allpositions[7], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "433-3": {
        pos: [allpositions[12], allpositions[10], allpositions[15], allpositions[6], allpositions[7], allpositions[6], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "433-4": {
        pos: [allpositions[12], allpositions[10], allpositions[15], allpositions[7], allpositions[8], allpositions[7], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "433-5": {
        pos: [allpositions[12], allpositions[9], allpositions[15], allpositions[7], allpositions[6], allpositions[7], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    4411: {
        pos: [allpositions[10], allpositions[9], allpositions[11], allpositions[7], allpositions[7], allpositions[14], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    442: {
        pos: [allpositions[10], allpositions[10], allpositions[11], allpositions[7], allpositions[7], allpositions[14], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "442-2": {
        pos: [allpositions[10], allpositions[10], allpositions[11], allpositions[6], allpositions[6], allpositions[14], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    451: {
        pos: [allpositions[10], allpositions[11], allpositions[8], allpositions[7], allpositions[8], allpositions[14], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    "451-2": {
        pos: [allpositions[10], allpositions[11], allpositions[7], allpositions[7], allpositions[7], allpositions[14], allpositions[2], allpositions[1], allpositions[1], allpositions[4], allpositions[0]]
    },
    5212: {
        pos: [allpositions[10], allpositions[8], allpositions[10], allpositions[7], allpositions[7], allpositions[3], allpositions[1], allpositions[1], allpositions[1], allpositions[5], allpositions[0]]
    },
    5221: {
        pos: [allpositions[12], allpositions[10], allpositions[15], allpositions[7], allpositions[7], allpositions[3], allpositions[1], allpositions[1], allpositions[1], allpositions[5], allpositions[0]]
    },
    532: {
        pos: [allpositions[10], allpositions[10], allpositions[7], allpositions[7], allpositions[7], allpositions[3], allpositions[1], allpositions[1], allpositions[1], allpositions[5], allpositions[0]]
    },
    541: {
        pos: ["ST", "LM", "CM", "CM", "RM", "LWB", "CB", "CB", "CB", "RWB", "GK"]
    },
    "4411-2": {
        pos: ["ST", "CAM", "LM", "CM", "CM", "RM", "LB", "CB", "CB", "RB", "GK"]
    },
    424: {
        pos: ["ST", "ST", "LW", "RW", "CM", "CM", "LB", "CB", "CB", "RB", "GK"]
    },
    4132: {
        pos: ["ST", "ST", "CM", "LM", "CDM", "RM", "LB", "CB", "CB", "RB", "GK"]
    },
    3142: {
        pos: ["ST", "ST", "LM", "CM", "CDM", "CM", "RM", "CB", "CB", "CB", "GK"]
    }
};
var loc3412 = {
    STL: 1,
    CAM: 2,
    STR: 3,
    LM: 4,
    CDM: 5,
    RM: 6,
    LB: 7,
    CBL: 8,
    CB: 9,
    CBR: 10,
    GK: 11
};
var loc3421 = {
    LF: 1,
    ST: 2,
    RF: 3,
    LM: 4,
    CML: 5,
    CMR: 6,
    RM: 7,
    CBL: 8,
    CB: 9,
    CBR: 10,
    GK: 11
};
var loc343 = {
    LW: 1,
    ST: 2,
    RW: 3,
    LM: 4,
    CML: 5,
    CMR: 6,
    RM: 7,
    CBL: 8,
    CB: 9,
    CBR: 10,
    GK: 11
};
var loc352 = {
    STL: 1,
    CAM: 2,
    STR: 3,
    LM: 4,
    CDML: 5,
    CDMR: 6,
    RM: 7,
    CBL: 8,
    CB: 9,
    CBR: 10,
    GK: 11
};
var loc41212 = {
    STL: 1,
    CAM: 2,
    STR: 3,
    LM: 4,
    CDM: 5,
    RM: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc412122 = {
    STL: 1,
    CAM: 2,
    STR: 3,
    CML: 4,
    CDM: 5,
    CMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4141 = {
    ST: 1,
    LM: 2,
    CML: 3,
    CMR: 4,
    RM: 5,
    CDM: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4231 = {
    ST: 1,
    CAML: 2,
    CAM: 3,
    CAMR: 4,
    CDML: 5,
    CDMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc42312 = {
    ST: 1,
    LM: 2,
    CAM: 3,
    RM: 4,
    CDML: 5,
    CDMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4222 = {
    STL: 1,
    STR: 2,
    CAML: 3,
    CAMR: 4,
    CDML: 5,
    CDMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4312 = {
    STL: 1,
    STR: 2,
    CAML: 3,
    CML: 4,
    CM: 5,
    CMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4321 = {
    LF: 1,
    ST: 2,
    RF: 3,
    CML: 4,
    CM: 5,
    CMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc433 = {
    LW: 1,
    ST: 2,
    RW: 3,
    CML: 4,
    CM: 5,
    CMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4332 = {
    LW: 1,
    ST: 2,
    RW: 3,
    CML: 4,
    CDM: 5,
    CMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4333 = {
    LW: 1,
    ST: 2,
    RW: 3,
    CDML: 4,
    CM: 5,
    CDMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4334 = {
    LW: 1,
    ST: 2,
    RW: 3,
    CML: 4,
    CAM: 5,
    CMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4335 = {
    LW: 1,
    CF: 2,
    RW: 3,
    CML: 4,
    CDM: 5,
    CMR: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4411 = {
    ST: 1,
    CF: 2,
    LM: 3,
    CML: 4,
    CMR: 5,
    RM: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc442 = {
    STL: 1,
    STR: 2,
    LM: 3,
    CML: 4,
    CMR: 5,
    RM: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4422 = {
    STL: 1,
    STR: 2,
    LM: 3,
    CDML: 4,
    CDMR: 5,
    RM: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc451 = {
    ST: 1,
    LM: 2,
    CAML: 3,
    CM: 4,
    CAMR: 5,
    RM: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc4512 = {
    ST: 1,
    LM: 2,
    CML: 3,
    CM: 4,
    CMR: 5,
    RM: 6,
    LB: 7,
    CBL: 8,
    CBR: 9,
    RB: 10,
    GK: 11
};
var loc5212 = {
    STL: 1,
    CAM: 2,
    STR: 3,
    CML: 4,
    CMR: 5,
    LWB: 6,
    CBR: 7,
    CBL: 8,
    CB: 9,
    RWB: 10,
    GK: 11
};
var loc5221 = {
    LW: 1,
    ST: 2,
    RW: 3,
    CML: 4,
    CMR: 5,
    LWB: 6,
    CBR: 7,
    CBL: 8,
    CB: 9,
    RWB: 10,
    GK: 11
};
var loc532 = {
    STL: 1,
    STR: 2,
    CML: 3,
    CM: 4,
    CMR: 5,
    LWB: 6,
    CBR: 7,
    CBL: 8,
    CB: 9,
    RWB: 10,
    GK: 11
};

var formation_draw = {
    3412: {
        draw: {
            11: [loc3412["CB"], loc3412["CBR"], loc3412["CBL"]],
            10: [loc3412["GK"], loc3412["CB"], loc3412["LB"]],
            9: [loc3412["GK"], loc3412["CBL"], loc3412["CBR"], loc3412["CDM"], loc3412["RM"]],
            8: [loc3412["GK"], loc3412["CB"], loc3412["LM"]],
            7: [loc3412["RM"], loc3412["CBR"], loc3412["STR"]],
            6: [loc3412["CB"], loc3412["CDM"], loc3412["CAM"], loc3412["LB"]],
            5: [loc3412["CB"], loc3412["CAM"], loc3412["LM"], loc3412["RM"]],
            4: [loc3412["CBL"], loc3412["STL"], loc3412["CDM"]],
            3: [loc3412["LB"], loc3412["STL"], loc3412["CAM"]],
            2: [loc3412["CDM"], loc3412["STL"], loc3412["STR"], loc3412["RM"]],
            1: [loc3412["CAM"], loc3412["STR"], loc3412["LM"]]
        }
    },
    3421: {
        draw: {
            11: [loc3421["CBL"], loc3421["CB"], loc3421["CBR"]],
            10: [loc3421["RM"], loc3421["CB"], loc3421["GK"]],
            9: [loc3421["GK"], loc3421["CMR"], loc3421["CML"], loc3421["CBL"], loc3421["CBR"]],
            8: [loc3421["GK"], loc3421["LM"], loc3421["CB"]],
            7: [loc3421["RF"], loc3421["CMR"], loc3421["CBR"]],
            6: [loc3421["CB"], loc3421["CML"], loc3421["RF"], loc3421["RM"]],
            5: [loc3421["CB"], loc3421["LF"], loc3421["LM"], loc3421["CMR"]],
            4: [loc3421["LF"], loc3421["CML"], loc3421["CBL"]],
            3: [loc3421["RM"], loc3421["CMR"], loc3421["ST"]],
            2: [loc3421["RF"], loc3421["LF"]],
            1: [loc3421["ST"], loc3421["LM"], loc3421["CML"]]
        }
    },
    343: {
        draw: {
            11: [loc343["CBR"], loc343["CBL"], loc343["CB"]],
            10: [loc343["GK"], loc343["RM"], loc343["CB"]],
            9: [loc343["CMR"], loc343["CBR"], loc343["CML"], loc343["CBL"], loc343["GK"]],
            8: [loc343["GK"], loc343["LM"], loc343["CB"]],
            7: [loc343["RW"], loc343["CMR"], loc343["CBR"]],
            6: [loc343["RM"], loc343["CB"], loc343["CML"], loc343["ST"]],
            5: [loc343["ST"], loc343["CMR"], loc343["CB"], loc343["LM"]],
            4: [loc343["LW"], loc343["CBL"], loc343["CML"]],
            3: [loc343["RM"], loc343["ST"]],
            2: [loc343["CML"], loc343["LW"], loc343["RW"], loc343["CMR"]],
            1: [loc343["LM"], loc343["ST"]]
        }
    },
    352: {
        draw: {
            11: [loc352["CBL"], loc352["CB"], loc352["CBR"]],
            10: [loc352["CDMR"], loc352["RM"], loc352["CB"], loc352["GK"]],
            9: [loc352["CDML"], loc352["CDMR"], loc352["CBL"], loc352["CBR"], loc352["GK"]],
            8: [loc352["LM"], loc352["CDML"], loc352["CB"], loc352["GK"]],
            7: [loc352["STR"], loc352["CDMR"], loc352["CBR"]],
            6: [loc352["CAM"], loc352["CDML"], loc352["RM"], loc352["CB"], loc352["CBR"]],
            5: [loc352["CAM"], loc352["LM"], loc352["CDMR"], loc352["CBL"], loc352["CB"]],
            4: [loc352["STL"], loc352["CDML"], loc352["CBL"]],
            3: [loc352["STL"], loc352["CAM"], loc352["RM"]],
            2: [loc352["STL"], loc352["STR"], loc352["CDML"], loc352["CDMR"]],
            1: [loc352["CAM"], loc352["STR"], loc352["LM"]]
        }
    },
    41212: {
        draw: {
            11: [loc41212["CBL"], loc41212["CBR"]],
            10: [loc41212["RM"], loc41212["CBR"]],
            9: [loc41212["GK"], loc41212["CBL"], loc41212["RB"], loc41212["CDM"]],
            8: [loc41212["LB"], loc41212["CBR"], loc41212["GK"], loc41212["CDM"]],
            7: [loc41212["CBL"], loc41212["LM"]],
            6: [loc41212["CDM"], loc41212["CAM"], loc41212["STR"], loc41212["RB"]],
            5: [loc41212["CBL"], loc41212["CAM"], loc41212["LM"], loc41212["RM"], loc41212["CBR"]],
            4: [loc41212["CAM"], loc41212["STL"], loc41212["CDM"], loc41212["LB"]],
            3: [loc41212["STL"], loc41212["CAM"], loc41212["RM"]],
            2: [loc41212["LM"], loc41212["STL"], loc41212["STR"], loc41212["CDM"], loc41212["RM"]],
            1: [loc41212["STR"], loc41212["CAM"], loc41212["LM"]]
        }
    },
    "41212-2": {
        draw: {
            11: [loc412122["CBL"], loc412122["CBR"]],
            10: [loc412122["CMR"], loc412122["CBR"]],
            9: [loc412122["CDM"], loc412122["CBL"], loc412122["RB"], loc412122["GK"]],
            8: [loc412122["CDM"], loc412122["LB"], loc412122["CBR"], loc412122["GK"]],
            7: [loc412122["CML"], loc412122["CBL"]],
            6: [loc412122["CAM"], loc412122["CDM"], loc412122["STR"], loc412122["RB"]],
            5: [loc412122["CMR"], loc412122["CAM"], loc412122["CML"], loc412122["CBL"], loc412122["CBR"]],
            4: [loc412122["STL"], loc412122["CAM"], loc412122["CDM"], loc412122["LB"]],
            3: [loc412122["CAM"], loc412122["STL"], loc412122["CMR"]],
            2: [loc412122["CMR"], loc412122["STR"], loc412122["STL"], loc412122["CML"], loc412122["CDM"]],
            1: [loc412122["CAM"], loc412122["CML"], loc412122["STR"]]
        }
    },
    4141: {
        draw: {
            11: [loc4141["CBR"], loc4141["CBL"]],
            10: [loc4141["RM"], loc4141["CBR"]],
            9: [loc4141["CMR"], loc4141["RB"], loc4141["CBL"], loc4141["CDM"], loc4141["GK"]],
            8: [loc4141["CML"], loc4141["CDM"], loc4141["LB"], loc4141["CBR"], loc4141["GK"]],
            7: [loc4141["CBL"], loc4141["LM"]],
            6: [loc4141["CBL"], loc4141["CMR"], loc4141["CML"], loc4141["CBR"]],
            5: [loc4141["CMR"], loc4141["ST"], loc4141["RB"]],
            4: [loc4141["ST"], loc4141["CML"], loc4141["RM"], loc4141["CDM"], loc4141["CBR"]],
            3: [loc4141["CMR"], loc4141["ST"], loc4141["LM"], loc4141["CBL"], loc4141["CDM"]],
            2: [loc4141["LB"], loc4141["ST"], loc4141["CML"]],
            1: [loc4141["CML"], loc4141["LM"], loc4141["CMR"], loc4141["RM"]]
        }
    },
    4231: {
        draw: {
            11: [loc4231["CBL"], loc4231["CBR"]],
            10: [loc4231["CDMR"], loc4231["CBR"]],
            9: [loc4231["CBL"], loc4231["CDMR"], loc4231["RB"], loc4231["GK"]],
            8: [loc4231["CDML"], loc4231["CBR"], loc4231["LB"], loc4231["GK"]],
            7: [loc4231["CBL"], loc4231["CDML"]],
            6: [loc4231["CAMR"], loc4231["CAM"], loc4231["CBR"], loc4231["RB"]],
            5: [loc4231["CAML"], loc4231["LB"], loc4231["CAM"], loc4231["CBL"]],
            4: [loc4231["CAM"], loc4231["ST"], loc4231["CDMR"]],
            3: [loc4231["CAML"], loc4231["CAMR"], loc4231["CDML"], loc4231["ST"], loc4231["CDMR"]],
            2: [loc4231["CAM"], loc4231["ST"], loc4231["CDML"]],
            1: [loc4231["CAM"], loc4231["CAML"], loc4231["CAMR"]]
        }
    },
    "4231-2": {
        draw: {
            11: [loc42312["CBR"], loc42312["CBL"]],
            10: [loc42312["CDMR"], loc42312["RM"], loc42312["CBR"]],
            9: [loc42312["GK"], loc42312["CDMR"], loc42312["CBL"], loc42312["RB"]],
            8: [loc42312["GK"], loc42312["CDML"], loc42312["LB"], loc42312["CBR"]],
            7: [loc42312["CDML"], loc42312["LM"], loc42312["CBL"]],
            6: [loc42312["RB"], loc42312["RM"], loc42312["CAM"], loc42312["CBR"]],
            5: [loc42312["LB"], loc42312["CAM"], loc42312["LM"], loc42312["CBL"]],
            4: [loc42312["CAM"], loc42312["CDMR"], loc42312["ST"], loc42312["RB"]],
            3: [loc42312["ST"], loc42312["LM"], loc42312["RM"], loc42312["CDML"], loc42312["CDMR"]],
            2: [loc42312["CAM"], loc42312["ST"], loc42312["CDML"], loc42312["LB"]],
            1: [loc42312["RM"], loc42312["CAM"], loc42312["LM"]]
        }
    },
    4222: {
        draw: {
            11: [loc4222["CBL"], loc4222["CBR"]],
            10: [loc4222["CAMR"], loc4222["CBR"]],
            9: [loc4222["RB"], loc4222["CDMR"], loc4222["CBL"], loc4222["GK"]],
            8: [loc4222["CDML"], loc4222["CBR"], loc4222["LB"], loc4222["GK"]],
            7: [loc4222["CAML"], loc4222["CBL"]],
            6: [loc4222["STR"], loc4222["CDML"], loc4222["CAMR"], loc4222["CBR"]],
            5: [loc4222["CDMR"], loc4222["STL"], loc4222["CAML"], loc4222["CBL"]],
            4: [loc4222["CDMR"], loc4222["STR"], loc4222["RB"]],
            3: [loc4222["LB"], loc4222["STL"], loc4222["CDML"]],
            2: [loc4222["STL"], loc4222["CDMR"], loc4222["CAMR"]],
            1: [loc4222["CAML"], loc4222["STR"], loc4222["CDML"]]
        }
    },
    4312: {
        draw: {
            11: [loc4312["CBR"], loc4312["CBL"]],
            10: [loc4312["CMR"], loc4312["CBR"]],
            9: [loc4312["CMR"], loc4312["CM"], loc4312["RB"], loc4312["CBL"], loc4312["GK"]],
            8: [loc4312["CBR"], loc4312["CML"], loc4312["CM"], loc4312["LB"], loc4312["GK"]],
            7: [loc4312["CML"], loc4312["CBL"]],
            6: [loc4312["CBR"], loc4312["STR"], loc4312["CM"], loc4312["RB"]],
            5: [loc4312["CMR"], loc4312["CAML"], loc4312["CBL"], loc4312["CML"], loc4312["CBR"]],
            4: [loc4312["LB"], loc4312["STL"], loc4312["CM"], loc4312["CBL"]],
            3: [loc4312["STR"], loc4312["STL"], loc4312["CM"]],
            2: [loc4312["CAML"], loc4312["CMR"], loc4312["STL"]],
            1: [loc4312["CML"], loc4312["STR"], loc4312["CAML"]]
        }
    },
    4321: {
        draw: {
            11: [loc4321["CBR"], loc4321["CBL"]],
            10: [loc4321["CBR"], loc4321["CMR"]],
            9: [loc4321["RB"], loc4321["CMR"], loc4321["CBL"], loc4321["GK"]],
            8: [loc4321["LB"], loc4321["CML"], loc4321["CBR"], loc4321["GK"]],
            7: [loc4321["CML"], loc4321["CBL"]],
            6: [loc4321["CBR"], loc4321["RF"], loc4321["CM"], loc4321["RB"]],
            5: [loc4321["CML"], loc4321["LF"], loc4321["RF"], loc4321["CMR"]],
            4: [loc4321["LF"], loc4321["CBL"], loc4321["CM"], loc4321["LB"]],
            3: [loc4321["CM"], loc4321["ST"], loc4321["CMR"]],
            2: [loc4321["RF"], loc4321["LF"]],
            1: [loc4321["CML"], loc4321["ST"], loc4321["CM"]]
        }
    },
    433: {
        draw: {
            11: [loc433["CBL"], loc433["CBR"]],
            10: [loc433["CMR"], loc433["CBR"]],
            9: [loc433["GK"], loc433["CM"], loc433["CBL"], loc433["RB"]],
            8: [loc433["GK"], loc433["LB"], loc433["CM"], loc433["CBR"]],
            7: [loc433["CBL"], loc433["CML"]],
            6: [loc433["CM"], loc433["RW"], loc433["RB"]],
            5: [loc433["CBL"], loc433["CML"], loc433["ST"], loc433["CMR"], loc433["CBR"]],
            4: [loc433["CM"], loc433["LW"], loc433["LB"]],
            3: [loc433["CMR"], loc433["ST"]],
            2: [loc433["RW"], loc433["LW"], loc433["CM"]],
            1: [loc433["ST"], loc433["CML"]]
        }
    },
    "433-2": {
        draw: {
            11: [loc4332["CBR"], loc4332["CBL"]],
            10: [loc4332["CBR"], loc4332["CMR"]],
            9: [loc4332["RB"], loc4332["CDM"], loc4332["CBL"], loc4332["GK"]],
            8: [loc4332["CDM"], loc4332["LB"], loc4332["CBR"], loc4332["GK"]],
            7: [loc4332["CML"], loc4332["CBL"]],
            6: [loc4332["ST"], loc4332["RW"], loc4332["CML"], loc4332["CDM"], loc4332["RB"]],
            5: [loc4332["CMR"], loc4332["CBL"], loc4332["CML"], loc4332["CBR"]],
            4: [loc4332["LW"], loc4332["ST"], loc4332["CMR"], loc4332["CDM"], loc4332["LB"]],
            3: [loc4332["CMR"], loc4332["ST"]],
            2: [loc4332["CMR"], loc4332["LW"], loc4332["RW"], loc4332["CML"]],
            1: [loc4332["CML"], loc4332["ST"]]
        }
    },
    "433-3": {
        draw: {
            11: [loc4333["CBR"], loc4333["CBL"]],
            10: [loc4333["CDMR"], loc4333["CBR"]],
            9: [loc4333["RB"], loc4333["CDMR"], loc4333["CBL"], loc4333["GK"]],
            8: [loc4333["LB"], loc4333["CDML"], loc4333["CBR"], loc4333["GK"]],
            7: [loc4333["CBL"], loc4333["CDML"]],
            6: [loc4333["CBR"], loc4333["RW"], loc4333["CM"], loc4333["RB"]],
            5: [loc4333["ST"], loc4333["CDMR"], loc4333["CDML"]],
            4: [loc4333["CBL"], loc4333["LW"], loc4333["CM"], loc4333["LB"]],
            3: [loc4333["CDMR"], loc4333["ST"]],
            2: [loc4333["RW"], loc4333["LW"], loc4333["CM"]],
            1: [loc4333["CDML"], loc4333["ST"]]
        }
    },
    "433-4": {
        draw: {
            11: [loc4334["CBR"], loc4334["CBL"]],
            10: [loc4334["CMR"], loc4334["RW"], loc4334["CBR"]],
            9: [loc4334["RB"], loc4334["CMR"], loc4334["CBL"], loc4334["GK"]],
            8: [loc4334["LB"], loc4334["CML"], loc4334["CBR"], loc4334["GK"]],
            7: [loc4334["CBL"], loc4334["LW"], loc4334["CML"]],
            6: [loc4334["CAM"], loc4334["RW"], loc4334["CBR"], loc4334["RB"]],
            5: [loc4334["CMR"], loc4334["ST"], loc4334["CML"]],
            4: [loc4334["LB"], loc4334["LW"], loc4334["CAM"], loc4334["CBL"]],
            3: [loc4334["ST"], loc4334["RB"], loc4334["CMR"]],
            2: [loc4334["CAM"], loc4334["LW"], loc4334["RW"]],
            1: [loc4334["CML"], loc4334["ST"], loc4334["LB"]]
        }
    },
    "433-5": {
        draw: {
            11: [loc4335["CBL"], loc4335["CBR"]],
            10: [loc4335["CBR"], loc4335["RW"], loc4335["CMR"]],
            9: [loc4335["CDM"], loc4335["RB"], loc4335["CBL"], loc4335["GK"]],
            8: [loc4335["LB"], loc4335["CDM"], loc4335["CBR"], loc4335["GK"]],
            7: [loc4335["CML"], loc4335["LW"], loc4335["CBL"]],
            6: [loc4335["CDM"], loc4335["CF"], loc4335["RW"], loc4335["RB"]],
            5: [loc4335["CML"], loc4335["CBL"], loc4335["CMR"], loc4335["CBR"]],
            4: [loc4335["CF"], loc4335["LW"], loc4335["CDM"], loc4335["LB"]],
            3: [loc4335["RB"], loc4335["CF"], loc4335["CMR"]],
            2: [loc4335["RW"], loc4335["LW"], loc4335["CML"], loc4335["CMR"]],
            1: [loc4335["LB"], loc4335["CF"], loc4335["CML"]]
        }
    },
    4411: {
        draw: {
            11: [loc4411["CBR"], loc4411["CBL"]],
            10: [loc4411["RM"], loc4411["CBR"]],
            9: [loc4411["GK"], loc4411["CBL"], loc4411["CMR"], loc4411["RB"]],
            8: [loc4411["GK"], loc4411["CML"], loc4411["LB"], loc4411["CBR"]],
            7: [loc4411["LM"], loc4411["CBL"]],
            6: [loc4411["CMR"], loc4411["ST"], loc4411["RB"]],
            5: [loc4411["RM"], loc4411["CF"], loc4411["CBR"], loc4411["CML"]],
            4: [loc4411["CF"], loc4411["CMR"], loc4411["LM"], loc4411["CBL"]],
            3: [loc4411["CML"], loc4411["ST"], loc4411["LB"]],
            2: [loc4411["ST"], loc4411["CMR"], loc4411["CML"]],
            1: [loc4411["LM"], loc4411["CF"], loc4411["RM"]]
        }
    },
    442: {
        draw: {
            11: [loc442["CBL"], loc442["CBR"]],
            10: [loc442["CBR"], loc442["RM"]],
            9: [loc442["CMR"], loc442["RB"], loc442["CBL"], loc442["GK"]],
            8: [loc442["LB"], loc442["CML"], loc442["CBR"], loc442["GK"]],
            7: [loc442["CBL"], loc442["LM"]],
            6: [loc442["CMR"], loc442["STR"], loc442["RB"]],
            5: [loc442["STR"], loc442["RM"], loc442["CML"], loc442["CBR"]],
            4: [loc442["CBL"], loc442["STL"], loc442["LM"], loc442["CMR"]],
            3: [loc442["STL"], loc442["CML"], loc442["LB"]],
            2: [loc442["CMR"], loc442["STL"], loc442["RM"]],
            1: [loc442["LM"], loc442["STR"], loc442["CML"]]
        }
    },
    "442-2": {
        draw: {
            11: [loc4422["CBR"], loc4422["CBL"]],
            10: [loc4422["RM"], loc4422["CBR"]],
            9: [loc4422["GK"], loc4422["CBL"], loc4422["CDMR"], loc4422["RB"]],
            8: [loc4422["GK"], loc4422["CDML"], loc4422["LB"], loc4422["CBR"]],
            7: [loc4422["LM"], loc4422["CBL"]],
            6: [loc4422["CDMR"], loc4422["STR"], loc4422["RB"]],
            5: [loc4422["RM"], loc4422["STR"], loc4422["CDML"], loc4422["CBR"]],
            4: [loc4422["CBL"], loc4422["STL"], loc4422["LM"], loc4422["CDMR"]],
            3: [loc4422["CDML"], loc4422["STL"], loc4422["LB"]],
            2: [loc4422["STL"], loc4422["RM"], loc4422["CDMR"]],
            1: [loc4422["LM"], loc4422["STR"], loc4422["CDML"]]
        }
    },
    451: {
        draw: {
            1: [loc451["CAML"], loc451["CAMR"]],
            2: [loc451["LB"], loc451["CAML"]],
            3: [loc451["CM"], loc451["ST"], loc451["LM"], loc451["CAMR"]],
            4: [loc451["CAML"], loc451["CBL"], loc451["CAMR"], loc451["CBR"]],
            5: [loc451["RM"], loc451["CM"], loc451["ST"], loc451["CAML"]],
            6: [loc451["RB"], loc451["CAMR"]],
            7: [loc451["CBL"], loc451["LM"]],
            8: [loc451["CBR"], loc451["CM"], loc451["GK"], loc451["LB"]],
            9: [loc451["CM"], loc451["CBL"], loc451["GK"], loc451["RB"]],
            10: [loc451["CBR"], loc451["RM"]],
            11: [loc451["CBL"], loc451["CBR"]]
        }
    },
    "451-2": {
        draw: {
            11: [loc4512["CBR"], loc4512["CBL"]],
            10: [loc4512["CBR"], loc4512["CMR"], loc4512["RM"]],
            9: [loc4512["CBL"], loc4512["RB"], loc4512["CM"], loc4512["CMR"], loc4512["GK"]],
            8: [loc4512["LB"], loc4512["CBR"], loc4512["CML"], loc4512["CM"], loc4512["GK"]],
            7: [loc4512["LM"], loc4512["CBL"], loc4512["CML"]],
            6: [loc4512["CMR"], loc4512["ST"], loc4512["RB"]],
            5: [loc4512["CBR"], loc4512["CM"], loc4512["RM"], loc4512["RB"]],
            4: [loc4512["CML"], loc4512["CMR"], loc4512["ST"], loc4512["CBL"], loc4512["CBR"]],
            3: [loc4512["LB"], loc4512["LM"], loc4512["CM"], loc4512["CBL"]],
            2: [loc4512["CML"], loc4512["ST"], loc4512["LB"]],
            1: [loc4512["CM"], loc4512["LM"], loc4512["RM"]]
        }
    },
    5212: {
        draw: {
            11: [loc5212["CBL"], loc5212["CBR"], loc5212["CB"]],
            10: [loc5212["CBR"], loc5212["CMR"]],
            9: [loc5212["CMR"], loc5212["CML"], loc5212["CBR"], loc5212["CBL"], loc5212["GK"]],
            8: [loc5212["CB"], loc5212["LWB"], loc5212["GK"]],
            7: [loc5212["CB"], loc5212["RWB"], loc5212["GK"]],
            6: [loc5212["CBL"], loc5212["CML"]],
            5: [loc5212["CAM"], loc5212["STR"], loc5212["CB"], loc5212["CML"], loc5212["RWB"]],
            4: [loc5212["CAM"], loc5212["CMR"], loc5212["STL"], loc5212["LWB"], loc5212["CB"]],
            3: [loc5212["CAM"], loc5212["STL"], loc5212["CMR"]],
            2: [loc5212["STR"], loc5212["CML"], loc5212["STL"], loc5212["CMR"]],
            1: [loc5212["CML"], loc5212["CAM"], loc5212["STR"]]
        }
    },
    5221: {
        draw: {
            11: [loc5221["CBL"], loc5221["CBR"], loc5221["CB"]],
            10: [loc5221["CBR"], loc5221["RW"], loc5221["CMR"]],
            9: [loc5221["CML"], loc5221["CMR"], loc5221["CBL"], loc5221["CBR"], loc5221["GK"]],
            8: [loc5221["GK"], loc5221["LWB"], loc5221["CB"]],
            7: [loc5221["GK"], loc5221["CB"], loc5221["RWB"]],
            6: [loc5221["CML"], loc5221["LW"], loc5221["CBL"]],
            5: [loc5221["CML"], loc5221["CB"], loc5221["RWB"], loc5221["ST"], loc5221["RW"]],
            4: [loc5221["CMR"], loc5221["LWB"], loc5221["CB"], loc5221["LW"], loc5221["ST"]],
            3: [loc5221["ST"], loc5221["RWB"], loc5221["CMR"]],
            2: [loc5221["RW"], loc5221["CML"], loc5221["LW"], loc5221["CMR"]],
            1: [loc5221["LWB"], loc5221["ST"], loc5221["CML"]]
        }
    },
    532: {
        draw: {
            11: [loc5221["CBL"], loc5221["CBR"], loc5221["CB"]],
            10: [loc532["CBR"], loc532["CMR"]],
            9: [loc532["CBR"], loc532["CBL"], loc532["CM"], loc532["GK"]],
            8: [loc532["CML"], loc532["CB"], loc532["LWB"], loc532["GK"]],
            7: [loc532["CB"], loc532["CMR"], loc532["RWB"], loc532["GK"]],
            6: [loc532["CBL"], loc532["CML"]],
            5: [loc532["CM"], loc532["CBR"], loc532["STR"], loc532["RWB"]],
            4: [loc532["CMR"], loc532["CB"], loc532["STL"], loc532["STR"], loc532["CML"]],
            3: [loc532["LWB"], loc532["CBL"], loc532["STL"], loc532["CM"]],
            2: [loc532["CM"], loc532["STL"], loc532["CMR"]],
            1: [loc532["STR"], loc532["CM"], loc532["CML"]]
        }
    },
    541: {
        draw: {
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
    "4411-2": {
        draw: {
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
    424: {
        draw: {
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
    4132: {
        draw: {
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
    3142: {
        draw: {
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
};



function AvgDes(avg) {
    switch (true) {
    case avg < 50:
        return "avg-red";
        break;
    case avg < 70 && avg >= 50:
        return "avg-orange";
        break;
    case avg < 80 && avg >= 70:
        return "avg-orange2";
        break;
    case avg < 90 && avg >= 80:
        return "avg-green1";
        break;
    case avg >= 90:
        return "avg-green2";
        break;
    default:
        return "avg-red"
    }
}
function AvgDesMain(avg) {
    switch (true) {
    case avg < 50:
        return "red_fut_stat";
        break;
    case avg < 70 && avg >= 50:
        return "orange_fut_stat";
        break;
    case avg < 80 && avg >= 70:
        return "yellow_fut_stat";
        break;
    case avg < 90 && avg >= 80:
        return "green_fut_stat";
        break;
    case avg >= 90:
        return "dark_green_fut_stat";
        break;
    default:
        return "red_fut_stat"
    }
}
function unique(list) {
    var result = [];
    $.each(list, function(i, e) {
        if ($.inArray(e, result) == -1)
            result.push(e)
    });
    return result
}
function StarsCalc() {
    if (pageTypeExtra == "sbc") {
        var ratingcalc = ChalRatingCalc()
    } else {
        var ratingcalc = SquadRatingCalc()
    }
    $(".squad-rating-value").html(ratingcalc);
    var ratingst = 0;
    var ratingstcl = ".rating-stars";
    var star05 = "<i style='margin-left: 5px;' class='fa fa-star-half-empty stars fa-lg'> </i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star1 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star15 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star-half-empty stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star2 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star-half-empty stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star25 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star-half-empty stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star3 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star35 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star-half-empty stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star4 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star-o stars fa-lg'></i>";
    var star45 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star-half-empty stars fa-lg'></i>";
    var star5 = "<i style='margin-left: 5px;' class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i><i class='fa fa-star stars fa-lg'></i>";
    switch (true) {
    case ratingcalc <= 56:
        ratingst = "0.5";
        $(ratingstcl).html(star05);
        break;
    case ratingcalc >= 57 && ratingcalc <= 59:
        ratingst = "1";
        $(ratingstcl).html(star1);
        break;
    case ratingcalc >= 60 && ratingcalc <= 61:
        ratingst = "1.5";
        $(ratingstcl).html(star15);
        break;
    case ratingcalc >= 62 && ratingcalc <= 63:
        ratingst = "2";
        $(ratingstcl).html(star2);
        break;
    case ratingcalc >= 64 && ratingcalc <= 65:
        ratingst = "2.5";
        $(ratingstcl).html(star25);
        break;
    case ratingcalc >= 66 && ratingcalc <= 69:
        ratingst = "3";
        $(ratingstcl).html(star3);
        break;
    case ratingcalc >= 70 && ratingcalc <= 73:
        ratingst = "3.5";
        $(ratingstcl).html(star35);
        break;
    case ratingcalc >= 74 && ratingcalc <= 76:
        ratingst = "4";
        $(ratingstcl).html(star4);
        break;
    case ratingcalc >= 77 && ratingcalc <= 79:
        ratingst = "4.5";
        $(ratingstcl).html(star45);
        break;
    case ratingcalc >= 80:
        ratingst = "5";
        $(ratingstcl).html(star5);
        break
    }
}
function SquadRatingCalc() {
    var sum = 0;
    var avg = 0;
    var final_rating = 0;
    var bench_count = 0;
    window.players_count = 0;
    $(".pCardHolder.added", "#field").map(function() {
        player_card_id = parseInt($(this).parent().attr("data-cardid"));
        player_rating = parseInt($(this).find(".pcdisplay-rat").html());
        if (typeof player_rating != "undefined" && player_card_id < 19) {
            sum += player_rating;
            if (player_card_id > 11) {
                bench_count++
            }
        }
    });
    avg = sum / (11 + bench_count);
    $(".pCardHolder.added", "#field").map(function() {
        var player_card_id = parseInt($(this).parent().attr("data-cardid"));
        var player_rating = parseInt($(this).find(".pcdisplay-rat").html());
        if (typeof player_rating != "undefined" && player_card_id < 19) {
            if (player_rating > avg) {
                if (player_card_id < 12) {
                    sum = sum + player_rating - avg
                }
                if (player_card_id > 11 && player_card_id < 19) {
                    sum = sum + (player_rating - avg) / 2
                }
            }
        }
        $("#" + $(this).attr("id") + " .addnewc").css("height", 0);
        window.players_count++
    });
    final_rating = Math.floor(Math.round(sum) / (11 + bench_count));
    if (final_rating > 100) {
        final_rating = 100
    }
    return final_rating
}
function SortArrayByKeys(inputarray) {
    var arraykeys = [];
    for (var k in inputarray) {
        arraykeys.push(k)
    }
    arraykeys.sort();
    var outputarray = [];
    for (var i = 0; i < arraykeys.length; i++) {
        outputarray[arraykeys[i]] = inputarray[arraykeys[i]]
    }
    return $.extend({}, outputarray)
}
function posmodf(player_pos, position) {
    var pageTypeExtra = $("#page-info").data("page-type");
    if (pageTypeExtra === "sbc" || pageTypeExtra === "draft") {
        return player_pos
    }
    switch (true) {
    case (position == "GK" && player_pos == "GK") == true:
        return position;
        break;
    case (position == "CB" && player_pos == "CB") == true:
        return position;
        break;
    case (position == "CM" && player_pos == "ST") == true:
        return position;
        break;
    case (position == "CDM" && player_pos == "ST") == true:
        return position;
        break;
    case (position == "CAM" && player_pos == "ST") == true:
        return position;
        break;
    case (position == "CF" && player_pos == "ST") == true:
        return position;
        break;
    case (position == "ST" && player_pos == "ST") == true:
        return position;
        break;
    case (position == "CM" && player_pos == "CF") == true:
        return position;
        break;
    case (position == "CDM" && player_pos == "CF") == true:
        return position;
        break;
    case (position == "CAM" && player_pos == "CF") == true:
        return position;
        break;
    case (position == "CF" && player_pos == "CF") == true:
        return position;
        break;
    case (position == "ST" && player_pos == "CF") == true:
        return position;
        break;
    case (position == "CM" && player_pos == "CM") == true:
        return position;
        break;
    case (position == "CDM" && player_pos == "CM") == true:
        return position;
        break;
    case (position == "CAM" && player_pos == "CM") == true:
        return position;
        break;
    case (position == "CF" && player_pos == "CM") == true:
        return position;
        break;
    case (position == "ST" && player_pos == "CM") == true:
        return position;
        break;
    case (position == "CM" && player_pos == "CAM") == true:
        return position;
        break;
    case (position == "CDM" && player_pos == "CAM") == true:
        return position;
        break;
    case (position == "CAM" && player_pos == "CAM") == true:
        return position;
        break;
    case (position == "CF" && player_pos == "CAM") == true:
        return position;
        break;
    case (position == "ST" && player_pos == "CAM") == true:
        return position;
        break;
    case (position == "CM" && player_pos == "CDM") == true:
        return position;
        break;
    case (position == "CDM" && player_pos == "CDM") == true:
        return position;
        break;
    case (position == "CAM" && player_pos == "CDM") == true:
        return position;
        break;
    case (position == "CF" && player_pos == "CDM") == true:
        return position;
        break;
    case (position == "ST" && player_pos == "CDM") == true:
        return position;
        break;
    case (position == "LM" && player_pos == "LW") == true:
        return position;
        break;
    case (position == "LF" && player_pos == "LW") == true:
        return position;
        break;
    case (position == "LW" && player_pos == "LW") == true:
        return position;
        break;
    case (position == "LM" && player_pos == "LM") == true:
        return position;
        break;
    case (position == "LF" && player_pos == "LM") == true:
        return position;
        break;
    case (position == "LW" && player_pos == "LM") == true:
        return position;
        break;
    case (position == "LM" && player_pos == "LF") == true:
        return position;
        break;
    case (position == "LF" && player_pos == "LF") == true:
        return position;
        break;
    case (position == "LW" && player_pos == "LF") == true:
        return position;
        break;
    case (position == "LM" && player_pos == "LW") == true:
        return position;
        break;
    case (position == "LF" && player_pos == "LW") == true:
        return position;
        break;
    case (position == "LW" && player_pos == "LW") == true:
        return position;
        break;
    case (position == "RM" && player_pos == "RW") == true:
        return position;
        break;
    case (position == "RF" && player_pos == "RW") == true:
        return position;
        break;
    case (position == "RW" && player_pos == "RW") == true:
        return position;
        break;
    case (position == "RM" && player_pos == "RM") == true:
        return position;
        break;
    case (position == "RF" && player_pos == "RM") == true:
        return position;
        break;
    case (position == "RW" && player_pos == "RM") == true:
        return position;
        break;
    case (position == "RM" && player_pos == "RF") == true:
        return position;
        break;
    case (position == "RF" && player_pos == "RF") == true:
        return position;
        break;
    case (position == "RW" && player_pos == "RF") == true:
        return position;
        break;
    case (position == "LWB" && player_pos == "LB") == true:
        return position;
        break;
    case (position == "LB" && player_pos == "LWB") == true:
        return position;
        break;
    case (position == "RWB" && player_pos == "RB") == true:
        return position;
        break;
    case (position == "RB" && player_pos == "RWB") == true:
        return position;
        break;
    default:
        return player_pos
    }
}
function LoyaltyCheck(playerCard, player) {
    var chemistry_loyalty = 0;
    if (typeof playerCard != "undefined") {
        if (playerCard.attr("data-loyalty") == "True") {
            chemistry_loyalty = 1
        }
        if (playerCard.attr("data-loyalty") == "true") {
            chemistry_loyalty = 1
        }
        if (playerCard.attr("data-loyalty") == "True") {
            chemistry_loyalty = 1
        }
    }
    return chemistry_loyalty
}
function LineColor(cln_chemistry) {
    var strokeStyle = "";
    switch (true) {
    case cln_chemistry >= 9:
        strokeStyle = "rgba(114,255,0, 1)";
        break;
    case cln_chemistry >= 3 && cln_chemistry < 9:
        strokeStyle = "rgba(114,250,0, 1)";
        break;
    case cln_chemistry >= 2 && cln_chemistry < 3:
        strokeStyle = "rgba(137, 216, 40, 1)";
        break;
    case cln_chemistry >= 1 && cln_chemistry < 2:
        strokeStyle = "rgba(231, 169, 49, 1)";
        break;
    default:
        strokeStyle = "#ff1738";
        break
    }
    return strokeStyle
}
function ManagerEditCheck(playerCard, player) {
    var chemistry_manedit = 0;
    if (typeof playerCard != "undefined") {
        if ($(player).hasClass("added") && playerCard.attr("data-manager") == "1") {
            chemistry_manedit = 1
        }
    }
    return chemistry_manedit
}
function PlayerInd(sum, linesnum) {
    var chemistry_lines = 0;
    var divide = sum / linesnum;
    switch (true) {
    case divide > 1.6 == true:
        chemistry_lines = 7;
        break;
    case divide >= 1 == true:
        chemistry_lines = 6;
        break;
    case divide > .32 == true:
        chemistry_lines = 3;
        break;
    default:
        chemistry_lines = 0
    }
    return chemistry_lines
}
function positionChemistryPoints(player_pos, squad_pos_des) {
    var chemistry_position = 0;
    var pos_points = [1, 2, 3, -4];
    switch (true) {
    case player_pos == squad_pos_des:
        chemistry_position = pos_points[2];
        break;
    case (squad_pos_des == "LWB" && player_pos == "LB") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "RWB" && player_pos == "RB") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CM" && player_pos == "CDM") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CM" && player_pos == "CAM") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CDM" && player_pos == "CM") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CAM" && player_pos == "CM") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CAM" && player_pos == "CF") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CF" && player_pos == "ST") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CF" && player_pos == "CAM") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "ST" && player_pos == "CF") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "RF" && player_pos == "RW") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "RW" && player_pos == "RF") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "RW" && player_pos == "RM") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "RM" && player_pos == "RW") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "LF" && player_pos == "LW") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "LW" && player_pos == "LF") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "LW" && player_pos == "LM") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "LM" && player_pos == "LW") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CB" && player_pos == "RB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CB" && player_pos == "CDM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CB" && player_pos == "LB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LWB" && player_pos == "LM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LWB" && player_pos == "RWB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LWB" && player_pos == "LW") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LB" && player_pos == "LM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LB" && player_pos == "RB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LB" && player_pos == "CB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LB" && player_pos == "LWB") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "RWB" && player_pos == "RM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RWB" && player_pos == "RW") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RWB" && player_pos == "LWB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RB" && player_pos == "RM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RB" && player_pos == "LB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RB" && player_pos == "CB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RB" && player_pos == "RWB") == true:
        chemistry_position = pos_points[1];
        break;
    case (squad_pos_des == "CM" && player_pos == "LM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CM" && player_pos == "RM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CDM" && player_pos == "CB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CDM" && player_pos == "CAM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CAM" && player_pos == "CDM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CF" && player_pos == "LF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "CF" && player_pos == "RF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "ST" && player_pos == "LF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "ST" && player_pos == "RF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RF" && player_pos == "ST") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RF" && player_pos == "CF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RF" && player_pos == "LF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RF" && player_pos == "RM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RW" && player_pos == "LW") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RW" && player_pos == "RWB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RM" && player_pos == "RF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RM" && player_pos == "RWB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RM" && player_pos == "RB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RM" && player_pos == "LM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "RM" && player_pos == "CM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LF" && player_pos == "ST") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LF" && player_pos == "CF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LF" && player_pos == "RF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LF" && player_pos == "LM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LW" && player_pos == "RW") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LW" && player_pos == "LWB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LM" && player_pos == "LF") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LM" && player_pos == "LB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LM" && player_pos == "LWB") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LM" && player_pos == "CM") == true:
        chemistry_position = pos_points[0];
        break;
    case (squad_pos_des == "LM" && player_pos == "RM") == true:
        chemistry_position = pos_points[0];
        break;
    default:
        chemistry_position = pos_points[3]
    }
    return chemistry_position
}
function checkCLNConnections(playerCard, s_structure, cardId, drawPlayerLines) {
    var addedNodes = 0;
    $.each(formation_draw[s_structure]["draw"][cardId], function(index, key) {
        var ins = new Object;
        var gets = ["data-player-club", "data-player-league", "data-player-nation"];
        var card_rel = $("#cardlid" + key).find(".pCardHolder > .pCard");
        var card_rel = card_rel.length === 0 ? $("#cardlid" + key).find(".pCard").find(".dummy-pcdisplay") : card_rel;
        switch (true) {
        case $("#cardlid" + key).find(".pCardHolder").hasClass("added") || $("#cardlid" + key).hasClass("dummy"):
            addedNodes = addedNodes + 1;
            switch (true) {
            case typeof playerCard.attr(gets[0]) !== "undefined" && playerCard.attr(gets[0]) !== "undefined" && playerCard.attr(gets[0]) == card_rel.attr(gets[0]):
                var clubPoint = 1;
                break;
            default:
                clubPoint = 0
            }
            switch (true) {
            case typeof playerCard.attr(gets[1]) !== "undefined" && playerCard.attr(gets[1]) !== "undefined" && playerCard.attr(gets[1]) == card_rel.attr(gets[1]):
                var leaguePoint = 1;
                break;
            case typeof playerCard.attr(gets[1]) !== "undefined" && playerCard.attr(gets[1]) !== "undefined" && (playerCard.attr(gets[1]) == 2118 || card_rel.attr(gets[1]) == 2118):
                leaguePoint = 1;
                break;
            default:
                leaguePoint = 0
            }
            switch (true) {
            case typeof playerCard.attr(gets[2]) !== "undefined" && playerCard.attr(gets[2]) !== "undefined" && playerCard.attr(gets[2]) == card_rel.attr(gets[2]):
                var nationPoint = 1;
                break;
            default:
                nationPoint = 0
            }
            if (drawPlayerLines.hasOwnProperty(cardId)) {
                drawPlayerLines[cardId][key] = [clubPoint, leaguePoint, nationPoint]
            } else {
                drawPlayerLines[cardId] = Array();
                drawPlayerLines[cardId][key] = [clubPoint, leaguePoint, nationPoint]
            }
            break
        }
    });
    var res = new Object;
    res["linefil"] = _.filter(drawPlayerLines[cardId], function() {
        return true
    });
    return res
}
function drawLines(canvas) {
    var kontext = canvas.getContext("2d");
    kontext.clearRect(0, 0, canvas.width, canvas.height);
    var linesArr = [];
    jQuery.each(playerLinesData, function(key, val) {
        var splitKey = key.split("-");
        var line_type_1 = splitKey[0] + "-" + splitKey[1];
        var line_type_2 = splitKey[1] + "-" + splitKey[0];
        if (!_.contains(linesArr, line_type_1) && !_.contains(linesArr, line_type_2)) {
            mainCardLeft = val.mainCardLeft;
            mainCardTop = val.mainCardTop;
            subCardLeft = val.subCardLeft;
            subCardTop = val.subCardTop;
            kontext.beginPath();
            kontext.moveTo(mainCardLeft, mainCardTop);
            kontext.lineTo(subCardLeft, subCardTop);
            kontext.lineWidth = 4;
            kontext.strokeStyle = val.strokeStyle;
            kontext.stroke();
            kontext.closePath();
            linesArr.push(key)
        }
    })
}
function calcLine(canvas, drawPlayerLines, s_structure, kontext, chem_arr, cardId) {
    var sum = 0;
    var chem_obj = {};
    $.each(formation_draw[s_structure]["draw"][cardId], function(index, key) {
        var mainCard = $("#cardlid" + cardId);
        var mainCardLeft = mainCard.position().left;
        var mainCardTop = mainCard.position().top;
        var subCard = $("#cardlid" + key);
        var subCardLeft = subCard.position().left;
        var subCardTop = subCard.position().top;
        mainCardLeft = Math.round(mainCardLeft + 80);
        mainCardTop = Math.round(mainCardTop + 146);
        subCardLeft = Math.round(subCardLeft + 80);
        subCardTop = Math.round(subCardTop + 146);
        playerLinesData[cardId + "-" + key] = {
            mainCardLeft: mainCardLeft,
            mainCardTop: mainCardTop,
            subCardLeft: subCardLeft,
            subCardTop: subCardTop
        };
        switch (true) {
        case drawPlayerLines.hasOwnProperty(cardId) && drawPlayerLines[cardId].hasOwnProperty(key):
            switch (true) {
            case drawPlayerLines[cardId][key][1] != 0:
                chem_obj.tmp_chemistry_league = 1;
                break;
            default:
                chem_obj.tmp_chemistry_league = 0
            }
            switch (true) {
            case drawPlayerLines[cardId][key][2] != 0:
                chem_obj.tmp_chemistry_nation = 1;
                break;
            default:
                chem_obj.tmp_chemistry_nation = 0
            }
            switch (true) {
            case drawPlayerLines[cardId][key][0] != 0:
                chem_obj.tmp_chemistry_club = 1;
                break;
            default:
                chem_obj.tmp_chemistry_club = 0
            }
            var cln_chemistry = _.sum(drawPlayerLines[cardId][key]);
            sum = sum + chem_obj.tmp_chemistry_club + chem_obj.tmp_chemistry_league + chem_obj.tmp_chemistry_nation;
            playerLinesData[cardId + "-" + key]["strokeStyle"] = LineColor(cln_chemistry);
            break;
        default:
            playerLinesData[cardId + "-" + key]["strokeStyle"] = "#ff1738"
        }
        chem_obj.tmp_sum = sum
    });
    chem_arr[cardId] = chem_arr.hasOwnProperty(cardId) ? chem_arr[cardId] : {};
    chem_arr[cardId]["chemistry_nation"] = chem_obj.hasOwnProperty("tmp_chemistry_nation") ? chem_obj.tmp_chemistry_nation : 0;
    chem_arr[cardId]["chemistry_federation"] = chem_obj.hasOwnProperty("tmp_chemistry_federation") ? chem_obj.tmp_chemistry_federation : 0;
    chem_arr[cardId]["sum"] = chem_obj.hasOwnProperty("tmp_sum") ? chem_obj.tmp_sum : 0
}
function PosBulbDis() {
    for (var i = 1; i < 12; i++) {
        pcdisplaymain = $("#cardlid" + i).hasClass("added");
        if (pcdisplaymain == true) {
            bulbpos = $("#cardlid" + i + "> .addnewc > .position-circ");
            bulbpos.addClass("hide")
        }
    }
}
function PosBulbActive() {
    for (var i = 1; i < 12; i++) {
        pcdisplaymain = $("#cardlid" + i).hasClass("added");
        if (pcdisplaymain == true) {
            bulbpos = $("#cardlid" + i + "> .addnewc > .position-circ");
            bulbpos.removeClass("hide");
            posCircCheck()
        }
    }
}
function rareOrNot(type) {
    if (type == 1) {
        type = "rare"
    } else {
        type = "non-rare"
    }
    return type
}
function charLimit(limitField, limitNum) {
    if (limitField.value.length > limitNum) {
        limitField.value = limitField.value.substring(0, limitNum)
    }
}
var body = document.body, timer;
window.addEventListener("scroll", function() {
    clearTimeout(timer);
    if (!body.classList.contains("disable-hover")) {
        body.classList.add("disable-hover")
    }
    timer = setTimeout(function() {
        body.classList.remove("disable-hover")
    }, 500)
}, false);
function get_squad_player_baseids() {
    var baseIds = "";
    $("#area").find(".added").map(function(index) {
        var baseId = $(this).find(".pcdisplay").attr("data-base-id");
        if (typeof baseId != "undefined") {
            baseId = parseInt(baseId);
            baseIds = baseIds + baseId + ","
        }
    });
    return baseIds
}
function showDetail(id) {
    $("#" + id).find(".pcdisplay-ovr1").hide();
    $("#" + id).find(".pcdisplay-ovr2").hide();
    $("#" + id).find(".pcdisplay-ovr3").hide();
    $("#" + id).find(".pcdisplay-ovr4").hide();
    $("#" + id).find(".pcdisplay-ovr5").hide();
    $("#" + id).find(".pcdisplay-ovr6").hide();
    $("#" + id).find(".pcdisplay-over").hide();
    $("#" + id).find(".pcdisplay-wr").hide();
    $("#" + id).find(".pcdisplay-nation-name").show();
    $("#" + id).find(".pcdisplay-club-name").show();
    $("#" + id).find(".pcdisplay-league-name").show();
    $("#" + id).find(".pcdisplay-foot").show()
}
function lastWeekGraph(resourceId) {
    doAjaxRequestGraphPrice(resourceId)
}
var attemptsGraphAjax;
function doAjaxRequestGraphPrice(resourceId) {
    attemptsGraphAjax = 0;
    doAjaxRequestLoopGraph(resourceId)
}
function doAjaxRequestLoopGraph(resourceId) {
    attemptsGraphAjax += 1;
    if (attemptsGraphAjax > 3) {
        console.log("Something went wrong, please try to refresh the page.");
        return
    }
    var dataString = "resourceid=" + resourceId + "&builder_type=" + builderType;
    var url = "/" + window.year + "/getWeeklyPlayerGraph";
    jQuery.ajax({
        url: url,
        type: "POST",
        data: dataString,
        cache: false,
        dataType: "json",
        success: function(data) {
            if (!graphData.hasOwnProperty(resourceId)) {
                graphData[resourceId] = {}
            }
            $.each(data.players, function(key, value) {
                graphData[resourceId][key] = value
            });
            if (data.errorcode === 200) {
                calculateGraphPrices()
            }
        },
        error: function(error) {
            doAjaxRequestLoopGraph()
        }
    })
}
var graphTotalPrices = {};
function calculateGraphPrices() {
    graphTotalPrices = {};
    if (window.graphEdit === 0 && (window.squad_action === "edit" || window.squad_action === "copy" || window.squad_action === "squad")) {
        graphData = $("#edit-graph-data").html();
        graphData = JSON.parse(graphData);
        window.graphEdit++
    }
    $.each(graphData, function(key, value) {
        $.each(value, function(key2, value2) {
            if (!graphTotalPrices.hasOwnProperty(key2)) {
                graphTotalPrices[key2] = {};
                graphTotalPrices[key2]["ps"] = 0;
                graphTotalPrices[key2]["xone"] = 0;
                graphTotalPrices[key2]["pc"] = 0
            }
            var psAvgGraphPrice = typeof value2.ps_avg !== "undefined" && value2.ps_avg > 0 ? value2.ps_avg : 0;
            var xboxAvgGraphPrice = typeof value2.xbox_avg !== "undefined" && value2.xbox_avg > 0 ? value2.xbox_avg : 0;
            var pcAvgGraphPrice = typeof value2.pc_avg !== "undefined" && value2.pc_avg > 0 ? value2.pc_avg : 0;
            graphTotalPrices[key2]["ps"] += psAvgGraphPrice;
            graphTotalPrices[key2]["xone"] += xboxAvgGraphPrice;
            graphTotalPrices[key2]["pc"] += pcAvgGraphPrice
        })
    });
    drawSquadGraph()
}
function drawSquadGraph() {
    if (!checkCookie("xbox")) {
        setCookie("xbox", true)
    }
    if (!checkCookie("ps")) {
        setCookie("ps", true)
    }
    if (!checkCookie("pc")) {
        setCookie("pc", true)
    }
    var psGraphPrices = [];
    var xboxGraphPrices = [];
    var pcGraphPrices = [];
    var graphDates = [];
    $.each(graphTotalPrices, function(key, value) {
        psGraphPrices.push(value.ps);
        xboxGraphPrices.push(value.xone);
        pcGraphPrices.push(value.pc);
        graphDates.push(moment(key).format("DD-MM"))
    });
    psGraphPrices.reverse();
    xboxGraphPrices.reverse();
    pcGraphPrices.reverse();
    graphDates.reverse();
    Highcharts.setOptions({
        lang: {
            thousandsSep: ","
        }
    });
    $("#squad-graph").highcharts({
        title: {
            text: "Last 7 days squad graph"
        },
        credits: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        subtitle: {
            text: ""
        },
        yAxis: {
            title: {
                text: ""
            }
        },
        legend: {},
        xAxis: {
            categories: graphDates
        },
        plotOptions: {
            series: {
                events: {
                    legendItemClick: function(event) {
                        var selected = this.index;
                        var flag = this.visible ? false : true;
                        var name = this.name.toLowerCase();
                        if (name == "ps4") {
                            name = "ps"
                        }
                        if (name == "xone") {
                            name = "xbox"
                        }
                        setCookie(name, flag);
                        return true
                    }
                }
            },
            spline: {
                marker: {
                    enabled: true
                }
            }
        },
        series: [{
            name: "PS4",
            data: psGraphPrices,
            color: "#3b97d3",
            visible: getCookie("ps") === "true"
        }, {
            name: "XONE",
            data: xboxGraphPrices,
            color: "#77b922",
            visible: getCookie("xbox") === "true"
        }, {
            name: "PC",
            data: pcGraphPrices,
            color: "#f05922",
            visible: getCookie("pc") === "true"
        }]
    })
}
function isEmpty(obj) {
    for (var key in obj) {
        if (obj.hasOwnProperty(key))
            return false
    }
    return true
}
function SquadAvg() {
    var playernum = 0
      , playernum_def = 0
      , playernum_mid = 0
      , playernum_att = 0
      , pace_sum = 0
      , sho_sum = 0
      , pas_sum = 0
      , dri_sum = 0
      , def_sum = 0
      , phy_sum = 0
      , pace_sum_def = 0
      , sho_sum_def = 0
      , pas_sum_def = 0
      , dri_sum_def = 0
      , def_sum_def = 0
      , phy_sum_def = 0
      , hi_sum_def = 0
      , pace_sum_mid = 0
      , sho_sum_mid = 0
      , pas_sum_mid = 0
      , dri_sum_mid = 0
      , def_sum_mid = 0
      , phy_sum_mid = 0
      , hi_sum_mid = 0
      , pace_sum_att = 0
      , sho_sum_att = 0
      , pas_sum_att = 0
      , dri_sum_att = 0
      , def_sum_att = 0
      , phy_sum_att = 0
      , hi_sum_att = 0
      , pace_sum_all = 0
      , sho_sum_all = 0
      , pas_sum_all = 0
      , dri_sum_all = 0
      , def_sum_all = 0
      , phy_sum_all = 0
      , hi_sum_all = 0;
    var delavgdes = "avg-red avg-orange avg-orange2 avg-green1 avg-green2";
    $("#first_11 .form-index .pCardHolder").each(function(i, obj) {
        if ($(this).hasClass("dummy") || $(this).hasClass("locked")) {
            return
        }
        pl_pace = Number($(this).find(".pcdisplay").attr("data-pace"));
        pl_sho = Number($(this).find(".pcdisplay").attr("data-shooting"));
        pl_pas = Number($(this).find(".pcdisplay").attr("data-passing"));
        pl_dri = Number($(this).find(".pcdisplay").attr("data-dribbling"));
        pl_def = Number($(this).find(".pcdisplay").attr("data-defending"));
        pl_phy = Number($(this).find(".pcdisplay").attr("data-physicality"));
        pl_hi = $(this).find(".pcdisplay").data("height");
        pl_hi = pl_hi.substring(0, 3);
        pl_hi = Number(pl_hi);
        var player_pos = $(this).find(".pcdisplay").children(".pcdisplay-pos").html();
        def_pos = ["CB", "RB", "LB", "LWB", "RWB"];
        mid_pos = ["CDM", "CM", "CAM", "RM", "LM"];
        att_pos = ["CF", "ST", "LW", "LF", "RW", "RF"];
        if (_.contains(def_pos, player_pos)) {
            playernum_def++;
            pace_sum_def = Math.round(pace_sum_def * (playernum_def - 1) / playernum_def + pl_pace / playernum_def);
            sho_sum_def = Math.round(sho_sum_def * (playernum_def - 1) / playernum_def + pl_sho / playernum_def);
            pas_sum_def = Math.round(pas_sum_def * (playernum_def - 1) / playernum_def + pl_pas / playernum_def);
            dri_sum_def = Math.round(dri_sum_def * (playernum_def - 1) / playernum_def + pl_dri / playernum_def);
            def_sum_def = Math.round(def_sum_def * (playernum_def - 1) / playernum_def + pl_def / playernum_def);
            phy_sum_def = Math.round(phy_sum_def * (playernum_def - 1) / playernum_def + pl_phy / playernum_def);
            hi_sum_def = Math.round(hi_sum_def * (playernum_def - 1) / playernum_def + pl_hi / playernum_def);
            $("#def-pac").removeClass(delavgdes).html(pace_sum_def).addClass(AvgDesMain(pace_sum_def));
            $("#def-sho").removeClass(delavgdes).html(sho_sum_def).addClass(AvgDesMain(sho_sum_def));
            $("#def-pas").removeClass(delavgdes).html(pas_sum_def).addClass(AvgDesMain(pas_sum_def));
            $("#def-dri").removeClass(delavgdes).html(dri_sum_def).addClass(AvgDesMain(dri_sum_def));
            $("#def-def").removeClass(delavgdes).html(def_sum_def).addClass(AvgDesMain(def_sum_def));
            $("#def-phy").removeClass(delavgdes).html(phy_sum_def).addClass(AvgDesMain(phy_sum_def));
            $("#def-height").html(hi_sum_def + "cm")
        }
        if (_.contains(mid_pos, player_pos)) {
            playernum_mid++;
            pace_sum_mid = Math.round(pace_sum_mid * (playernum_mid - 1) / playernum_mid + pl_pace / playernum_mid);
            sho_sum_mid = Math.round(sho_sum_mid * (playernum_mid - 1) / playernum_mid + pl_sho / playernum_mid);
            pas_sum_mid = Math.round(pas_sum_mid * (playernum_mid - 1) / playernum_mid + pl_pas / playernum_mid);
            dri_sum_mid = Math.round(dri_sum_mid * (playernum_mid - 1) / playernum_mid + pl_dri / playernum_mid);
            def_sum_mid = Math.round(def_sum_mid * (playernum_mid - 1) / playernum_mid + pl_def / playernum_mid);
            phy_sum_mid = Math.round(phy_sum_mid * (playernum_mid - 1) / playernum_mid + pl_phy / playernum_mid);
            hi_sum_mid = Math.round(hi_sum_mid * (playernum_mid - 1) / playernum_mid + pl_hi / playernum_mid);
            $("#mid-pac").removeClass(delavgdes).html(pace_sum_mid).addClass(AvgDesMain(pace_sum_mid));
            $("#mid-sho").removeClass(delavgdes).html(sho_sum_mid).addClass(AvgDesMain(sho_sum_mid));
            $("#mid-pas").removeClass(delavgdes).html(pas_sum_mid).addClass(AvgDesMain(pas_sum_mid));
            $("#mid-dri").removeClass(delavgdes).html(dri_sum_mid).addClass(AvgDesMain(dri_sum_mid));
            $("#mid-def").removeClass(delavgdes).html(def_sum_mid).addClass(AvgDesMain(def_sum_mid));
            $("#mid-phy").removeClass(delavgdes).html(phy_sum_mid).addClass(AvgDesMain(phy_sum_mid));
            $("#mid-height").html(hi_sum_mid + "cm")
        }
        if (_.contains(att_pos, player_pos)) {
            playernum_att++;
            pace_sum_att = Math.round(pace_sum_att * (playernum_att - 1) / playernum_att + pl_pace / playernum_att);
            sho_sum_att = Math.round(sho_sum_att * (playernum_att - 1) / playernum_att + pl_sho / playernum_att);
            pas_sum_att = Math.round(pas_sum_att * (playernum_att - 1) / playernum_att + pl_pas / playernum_att);
            dri_sum_att = Math.round(dri_sum_att * (playernum_att - 1) / playernum_att + pl_dri / playernum_att);
            def_sum_att = Math.round(def_sum_att * (playernum_att - 1) / playernum_att + pl_def / playernum_att);
            phy_sum_att = Math.round(phy_sum_att * (playernum_att - 1) / playernum_att + pl_phy / playernum_att);
            hi_sum_att = Math.round(hi_sum_att * (playernum_att - 1) / playernum_att + pl_hi / playernum_att);
            $("#att-pac").removeClass(delavgdes).html(pace_sum_att).addClass(AvgDesMain(pace_sum_att));
            $("#att-sho").removeClass(delavgdes).html(sho_sum_att).addClass(AvgDesMain(sho_sum_att));
            $("#att-pas").removeClass(delavgdes).html(pas_sum_att).addClass(AvgDesMain(pas_sum_att));
            $("#att-dri").removeClass(delavgdes).html(dri_sum_att).addClass(AvgDesMain(dri_sum_att));
            $("#att-def").removeClass(delavgdes).html(def_sum_att).addClass(AvgDesMain(def_sum_att));
            $("#att-phy").removeClass(delavgdes).html(phy_sum_att).addClass(AvgDesMain(phy_sum_att));
            $("#att-height").html(hi_sum_att + "cm")
        }
        playernum++;
        pace_sum_all = Math.round(pace_sum_all * (playernum - 1) / playernum + pl_pace / playernum);
        sho_sum_all = Math.round(sho_sum_all * (playernum - 1) / playernum + pl_sho / playernum);
        pas_sum_all = Math.round(pas_sum_all * (playernum - 1) / playernum + pl_pas / playernum);
        dri_sum_all = Math.round(dri_sum_all * (playernum - 1) / playernum + pl_dri / playernum);
        def_sum_all = Math.round(def_sum_all * (playernum - 1) / playernum + pl_def / playernum);
        phy_sum_all = Math.round(phy_sum_all * (playernum - 1) / playernum + pl_phy / playernum);
        hi_sum_all = Math.round(hi_sum_all * (playernum - 1) / playernum + pl_hi / playernum);
        $("#all-pac").removeClass(delavgdes).html(pace_sum_all).addClass(AvgDesMain(pace_sum_all));
        $("#all-sho").removeClass(delavgdes).html(sho_sum_all).addClass(AvgDesMain(sho_sum_all));
        $("#all-pas").removeClass(delavgdes).html(pas_sum_all).addClass(AvgDesMain(pas_sum_all));
        $("#all-dri").removeClass(delavgdes).html(dri_sum_all).addClass(AvgDesMain(dri_sum_all));
        $("#all-def").removeClass(delavgdes).html(def_sum_all).addClass(AvgDesMain(def_sum_all));
        $("#all-phy").removeClass(delavgdes).html(phy_sum_all).addClass(AvgDesMain(phy_sum_all));
        $("#all-height").html(hi_sum_all + "cm");
        $("#att-pac-main").removeClass(delavgdes).html(pace_sum_all).addClass(AvgDesMain(pace_sum_all));
        $("#att-sho-main").removeClass(delavgdes).html(sho_sum_all).addClass(AvgDesMain(sho_sum_all));
        $("#att-pas-main").removeClass(delavgdes).html(pas_sum_all).addClass(AvgDesMain(pas_sum_all));
        $("#att-dri-main").removeClass(delavgdes).html(dri_sum_all).addClass(AvgDesMain(dri_sum_all));
        $("#att-def-main").removeClass(delavgdes).html(def_sum_all).addClass(AvgDesMain(def_sum_all));
        $("#att-phy-main").removeClass(delavgdes).html(phy_sum_all).addClass(AvgDesMain(phy_sum_all))
    });
    if (playernum_def == 0) {
        pace_sum_def = 0;
        sho_sum_def = 0;
        pas_sum_def = 0;
        dri_sum_def = 0;
        def_sum_def = 0;
        phy_sum_def = 0;
        hi_sum_def = 0;
        $("#def-pac").removeClass(delavgdes).html(pace_sum_def).addClass(AvgDesMain(pace_sum_def));
        $("#def-sho").removeClass(delavgdes).html(sho_sum_def).addClass(AvgDesMain(sho_sum_def));
        $("#def-pas").removeClass(delavgdes).html(pas_sum_def).addClass(AvgDesMain(pas_sum_def));
        $("#def-dri").removeClass(delavgdes).html(dri_sum_def).addClass(AvgDesMain(dri_sum_def));
        $("#def-def").removeClass(delavgdes).html(def_sum_def).addClass(AvgDesMain(def_sum_def));
        $("#def-phy").removeClass(delavgdes).html(phy_sum_def).addClass(AvgDesMain(phy_sum_def));
        $("#def-height").html('<i class="fa fa-arrows-v"></i> Height: ' + hi_sum_def + "cm")
    }
    if (playernum_mid == 0) {
        pace_sum_mid = 0;
        sho_sum_mid = 0;
        pas_sum_mid = 0;
        dri_sum_mid = 0;
        def_sum_mid = 0;
        phy_sum_mid = 0;
        hi_sum_mid = 0;
        $("#mid-pac").removeClass(delavgdes).html(pace_sum_mid).addClass(AvgDesMain(pace_sum_mid));
        $("#mid-sho").removeClass(delavgdes).html(sho_sum_mid).addClass(AvgDesMain(sho_sum_mid));
        $("#mid-pas").removeClass(delavgdes).html(pas_sum_mid).addClass(AvgDesMain(pas_sum_mid));
        $("#mid-dri").removeClass(delavgdes).html(dri_sum_mid).addClass(AvgDesMain(dri_sum_mid));
        $("#mid-def").removeClass(delavgdes).html(def_sum_mid).addClass(AvgDesMain(def_sum_mid));
        $("#mid-phy").removeClass(delavgdes).html(phy_sum_mid).addClass(AvgDesMain(phy_sum_mid));
        $("#mid-height").html('<i class="fa fa-arrows-v"></i> Height: ' + hi_sum_mid + "cm")
    }
    if (playernum_att == 0) {
        pace_sum_att = 0;
        sho_sum_att = 0;
        pas_sum_att = 0;
        dri_sum_att = 0;
        def_sum_att = 0;
        phy_sum_att = 0;
        hi_sum_att = 0;
        $("#att-pac").removeClass(delavgdes).html(pace_sum_att).addClass(AvgDesMain(pace_sum_att));
        $("#att-sho").removeClass(delavgdes).html(sho_sum_att).addClass(AvgDesMain(sho_sum_att));
        $("#att-pas").removeClass(delavgdes).html(pas_sum_att).addClass(AvgDesMain(pas_sum_att));
        $("#att-dri").removeClass(delavgdes).html(dri_sum_att).addClass(AvgDesMain(dri_sum_att));
        $("#att-def").removeClass(delavgdes).html(def_sum_att).addClass(AvgDesMain(def_sum_att));
        $("#att-phy").removeClass(delavgdes).html(phy_sum_att).addClass(AvgDesMain(phy_sum_att));
        $("#att-height").html('<i class="fa fa-arrows-v"></i> Height: ' + hi_sum_att + "cm")
    }
    if (playernum == 0) {
        pace_sum_all = 0;
        sho_sum_all = 0;
        pas_sum_all = 0;
        dri_sum_all = 0;
        def_sum_all = 0;
        phy_sum_all = 0;
        hi_sum_all = 0;
        $("#all-pac").removeClass(delavgdes).html(pace_sum_att).addClass(AvgDesMain(pace_sum_att));
        $("#all-sho").removeClass(delavgdes).html(sho_sum_all).addClass(AvgDesMain(sho_sum_all));
        $("#all-pas").removeClass(delavgdes).html(pas_sum_all).addClass(AvgDesMain(pas_sum_all));
        $("#all-dri").removeClass(delavgdes).html(dri_sum_all).addClass(AvgDesMain(dri_sum_all));
        $("#all-def").removeClass(delavgdes).html(def_sum_all).addClass(AvgDesMain(def_sum_all));
        $("#all-phy").removeClass(delavgdes).html(phy_sum_all).addClass(AvgDesMain(phy_sum_all));
        $("#all-height").html('<i class="fa fa-arrows-v"></i> Height: ' + hi_sum_all + "cm")
    }
}
function getBaseIds() {
    $("#area").find(".card").map(function(index) {})
}
function get_squad_player_ids_with_data() {
    var players = {};
    $.each(squadObj, function(index, value) {
        if (index != "formation" && index != "TotalChemistry") {
            var pId = value.id;
            if (typeof pId != "undefined" && pId) {
                players[pId] = {};
                players[pId]["id"] = value.id;
                players[pId]["untradeable"] = value.unt
            }
        }
    });
    return JSON.stringify(players)
}
function kFormatter(num) {
    if (num > 999) {
        var newNum = (num / 1e3).toFixed(1);
        newNum = Math.floor(newNum) + "k"
    } else {
        newNum = num
    }
    return newNum
}
function nFormatter(num, digits) {
    var si = [{
        value: 1,
        symbol: ""
    }, {
        value: 1e3,
        symbol: "k"
    }, {
        value: 1e6,
        symbol: "M"
    }, {
        value: 1e9,
        symbol: "G"
    }, {
        value: 1e12,
        symbol: "T"
    }, {
        value: 1e15,
        symbol: "P"
    }, {
        value: 1e18,
        symbol: "E"
    }];
    var rx = /\.0+$|(\.[0-9]*[1-9])0+$/;
    var i;
    for (i = si.length - 1; i > 0; i--) {
        if (num >= si[i].value) {
            break
        }
    }
    return (num / si[i].value).toFixed(digits).replace(rx, "$1") + si[i].symbol
}
function refreshPricesList(type) {
    var user_platform = getCookie("platform");
    if (type == "builder" || type == 0 || type == null) {
        var getPlayersData = get_squad_player_ids_with_data();
        if (getPlayersData.length < 4) {
            return false
        }
        var objData = 1
    } else {
        getPlayersData = get_squad_player_ids();
        objData = 0
    }
    $("#prices-loader").show();
    $("#refresh-prices").hide();
    $("#PriceListRefresh").hide();
    $("#PriceListRefreshCount").html('<span style="color:white; display: none;"></span>');
    $("#PriceListRefreshCount").html(3);
    var interval = setInterval(function() {
        var timeCounter = $("#PriceListRefreshCount").html();
        var updateTime = eval(timeCounter) - eval(1);
        $("#PriceListRefreshCount").html(updateTime);
        if (updateTime == 0) {
            $("#PriceList").removeClass("fa-angle-down").addClass("fa-angle-up");
            $("#PriceListRefreshCount").html("");
            $("#PriceListRefresh").show("fast");
            $("#PriceList").show("fast");
            $("#prices-loader").hide();
            $("#refresh-prices").show();
            clearInterval(interval)
        }
    }, 500);
    jQuery.ajax({
        type: "POST",
        url: "/" + window.year + "/getPricesById",
        cache: false,
        data: {
            players_ids: getPlayersData,
            objData: objData,
            builder_type: builderType
        },
        success: function(data) {
            if (!isEmpty(data)) {
                var players = data["players"];
                $("#squad-prices").attr("data-ps4", data["total_prices"].ps);
                $("#squad-prices").attr("data-xbox", data["total_prices"].xbox);
                $("#squad-prices").attr("data-pc", data["total_prices"].pc);
                if (user_platform == "ps4") {
                    total_price = data["total_prices"].ps
                }
                if (user_platform == "xone") {
                    total_price = data["total_prices"].xbox
                }
                if (user_platform == "pc") {
                    total_price = data["total_prices"].pc
                }
                var total_price = parseInt(total_price.replace(/,/g, ""), 10);
                $("#total-price").fadeOut().fadeIn().html(nFormatter(total_price));
                $("#prices-list-content").html("");
                $.each(players, function(key, value) {
                    if (user_platform == "ps4") {
                        player_price = rouNum(value.ps_price)
                    }
                    if (user_platform == "xone") {
                        player_price = rouNum(value.xbox_price)
                    }
                    if (user_platform == "pc") {
                        player_price = rouNum(value.pc_price)
                    }
                    $(".pCard[data-player-id='" + key + "']").find(".pcdisplay-price").html(player_price);
                    if (!isEmpty(data)) {
                        var total_psPrice = data["total_prices"].ps;
                        var total_xboxPrice = data["total_prices"].xbox;
                        var total_pcPrice = data["total_prices"].pc;
                        var players = data["players"];
                        $("#squad-price-ps3").find("span").text(total_psPrice);
                        $("#squad-price-xbl").find("span").text(total_xboxPrice);
                        $("#squad-price-pc").find("span").text(total_pcPrice);
                        var showPsPrice = window.platform_cookie === "ps4" ? "ps4_color" : "hide";
                        var showXonePrice = window.platform_cookie === "xone" ? "xb1_color" : "hide";
                        var showPcPrice = window.platform_cookie === "pc" ? "pc_color" : "hide";
                        $("#prices-list-content").html("");
                        $.each(players, function(key, value) {
                            var price_row = '<div class="player-price-row-js" id="player_price_' + key + '" style="opacity: 0;"><div class="player_price"><img class="squad_right_lists_price_area_img" src="' + value.image + '"><span class="player_price_name">' + value.name + '</span></div><div class="player_price player_price_num float-right"><span class="' + showPsPrice + '">' + rouNum(value.ps_price) + '</span> <span class="' + showXonePrice + '"> ' + rouNum(value.xbox_price) + '</span> <span class="' + showPcPrice + '"> ' + rouNum(value.pc_price) + '</span> <span><img src="' + window.cdn_url + '/design/img/coins_bin.png" class="coins-icon-list"></span> </div></div><div class="clearfix"></div>';
                            $("#prices-list-content").append(price_row);
                            $("#player_price_" + key).css("opacity", "1")
                        })
                    }
                })
            }
        },
        error: function(error) {
            $("#prices-loader").hide();
            $("#refresh-prices").show()
        }
    })
}
rouNum = function(number) {
    if (number != "undefined") {
        return number.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,")
    } else {
        return 0
    }
}
;
function untradableImgType(rare, rare_type) {
    if (rare === 0) {
        var img = "normal_non_rare_won"
    }
    if (rare === 1 && rare_type < 2) {
        img = "normal_rare_won"
    }
    if (rare_type > 1) {
        img = "special_won"
    }
    return img
}
function untOverlay(rare_type) {
    switch (rare_type) {
    case 47:
        return "normal_non_rare_won";
    case 0:
    case 40:
    case 1:
    case 7:
    case 8:
    case 9:
    case 10:
    case 17:
    case 41:
    case 48:
    case 49:
    case 52:
    case 53:
    case 54:
    case 55:
    case 56:
    case 57:
    case 58:
    case 59:
    case 60:
    case 61:
    case 62:
    case 78:
        return "normal_rare_won";
    default:
        return "special_won"
    }
}
function checkChampsCard(rating, rare_type) {
    allowed_rt = [3, 4, 11];
    if (jQuery.inArray(rare_type, allowed_rt) != -1 && rating > 74) {
        return true
    } else {
        return false
    }
}

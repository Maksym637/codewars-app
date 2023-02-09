from utils.features import read_file
from utils.constants import FILE_PATH_1, FILE_PATH_2, FILE_PATH_3


data_task_1 = [
    ("London", read_file(FILE_PATH_1), 51.199999999999996, 57.428333333333335),
    ("Beijing", read_file(FILE_PATH_1), 52.416666666666664, 4808.37138888889),
    ("Paris", read_file(FILE_PATH_2), 188.89166666666665, 9510.662430555556),
    ("Lima", read_file(FILE_PATH_2), 10.774999999999999, 30.39854166666667),
    ("Lviv", read_file(FILE_PATH_1), float(-1), float(-1)),
    ("Lviv", read_file(FILE_PATH_2), float(-1), float(-1)),
    ("Lviv", read_file(FILE_PATH_3), float(-1), float(-1)),
    ("Kyiv", read_file(FILE_PATH_3), float(-1), float(-1))
]

data_task_2 = [
    (
        ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], 
        ["A", "B"], 
        "(A : 200) - (B : 1140)"
    ),
    (
        ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], 
        ["A", "B", "C", "D"],
        "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"
    ),
    (
        ["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],
        ["A", "B", "C", "W"],
        "(A : 0) - (B : 114) - (C : 70) - (W : 0)"
    ),
    (
        ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 60"],
        ["B", "R", "D", "X"],
        "(B : 364) - (R : 225) - (D : 60) - (X : 0)"
    ),
    (
        [],
        ["B", "R", "D", "X"],
        ""
    ),
    (
        ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 60"],
        [],
        ""
    ),
    (
        ["RTKL 120", "YULA 300", "ASJN 235"],
        ["A", "B", "C", "D", "E", "F"],
        "(A : 235) - (B : 0) - (C : 0) - (D : 0) - (E : 0) - (F : 0)"
    ),
    (
        ["ZKTM 310", "CBART 20", "QZFG 239"],
        ["A", "B"],
        "(A : 0) - (B : 0)"
    )
]

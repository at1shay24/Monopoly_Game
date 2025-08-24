from property import Property
class Board:
    def __init__(self):
        self.spaces = [None] * 40
        self.spaces[0] = "Go"
        self.spaces[10] = "Jail"
        self.spaces[20] = "Free Parking"
        self.spaces[30] = "Go To Jail"

    def place_property(self, index, property_obj):
        if 0 <= index < len(self.spaces):
            self.spaces[index] = property_obj

    def get_space(self, index):
        return self.spaces[index]
# Dark Purple
med_ave = Property("Mediterranean Avenue", 60, 2)
baltic_ave = Property("Baltic Avenue", 60, 4)
# Light Blue
oriental_ave = Property("Oriental Avenue", 100, 6)
vermont_ave = Property("Vermont Avenue", 100, 6)
conn_ave = Property("Connecticut Avenue", 120, 8)
# Pink
st_charles = Property("St. Charles Place", 140, 10)
states_ave = Property("States Avenue", 140, 10)
virginia_ave = Property("Virginia Avenue", 160, 12)
# Orange
st_james = Property("St. James Place", 180, 14)
tennessee_ave = Property("Tennessee Avenue", 180, 14)
new_york_ave = Property("New York Avenue", 200, 16)
# Red
kentucky_ave = Property("Kentucky Avenue", 220, 18)
indiana_ave = Property("Indiana Avenue", 220, 18)
illinois_ave = Property("Illinois Avenue", 240, 20)
# Yellow
atlantic_ave = Property("Atlantic Avenue", 260, 22)
ventnor_ave = Property("Ventnor Avenue", 260, 22)
marvin_gardens = Property("Marvin Gardens", 280, 24)
# Green
pacific_ave = Property("Pacific Avenue", 300, 26)
north_carolina_ave = Property("North Carolina Avenue", 300, 26)
pennsylvania_ave = Property("Pennsylvania Avenue", 320, 28)
# Dark Blue
park_place = Property("Park Place", 350, 35)
boardwalk = Property("Boardwalk", 400, 50)
# Railroads
reading_rr = Property("Reading Railroad", 200, 25)
pennsylvania_rr = Property("Pennsylvania Railroad", 200, 25)
bno_rr = Property("B&O Railroad", 200, 25)
short_line = Property("Short Line", 200, 25)
# Utilities
electric_company = Property("Electric Company", 150, 10)
water_works = Property("Water Works", 150, 10)

properties_positions = [
    (1, med_ave), (3, baltic_ave), (5, reading_rr),
    (6, oriental_ave), (8, vermont_ave), (9, conn_ave),
    (11, st_charles), (12, electric_company), (13, states_ave), (14, virginia_ave),
    (15, pennsylvania_rr),
    (16, st_james), (18, tennessee_ave), (19, new_york_ave),
    (21, kentucky_ave), (23, indiana_ave), (24, illinois_ave),
    (25, bno_rr),
    (26, atlantic_ave), (27, ventnor_ave), (28, water_works), (29, marvin_gardens),
    (31, pacific_ave), (32, north_carolina_ave), (34, pennsylvania_ave),
    (35, short_line),
    (37, park_place), (39, boardwalk)
]

special_spaces = {
    2: "Community Chest", 4: "Income Tax",
    7: "Chance", 17: "Community Chest",
    22: "Chance", 33: "Community Chest",
    36: "Chance", 38: "Luxury Tax"
}

board = Board()
for pos, prop in properties_positions:
    board.place_property(pos, prop)
for pos, label in special_spaces.items():
    board.place_property(pos, label)
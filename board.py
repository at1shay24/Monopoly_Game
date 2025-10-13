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


# ===== WEST DELHI PROPERTIES (Names only changed) ===== #

# Brown
rani_bagh = Property("Rani Bagh", 60, 2)
shakurpur = Property("Shakurpur", 60, 4)

# Light Blue
pitampura = Property("Pitampura", 100, 6)
kohat_enclave = Property("Kohat Enclave", 100, 6)
saraswati_vihar = Property("Saraswati Vihar", 120, 8)

# Pink
ashok_vihar = Property("Ashok Vihar", 140, 10)
model_town = Property("Model Town", 140, 10)
rohini_sec7 = Property("Rohini Sector 7", 160, 12)

# Orange
rohini_sec13 = Property("Rohini Sector 13", 180, 14)
paschim_vihar = Property("Paschim Vihar", 180, 14)
mangolpuri = Property("Mangolpuri", 200, 16)

# Red
rajouri_garden = Property("Rajouri Garden", 220, 18)
punjabi_bagh = Property("Punjabi Bagh", 220, 18)
tilak_nagar = Property("Tilak Nagar", 240, 20)

# Yellow
kirti_nagar = Property("Kirti Nagar", 260, 22)
janakpuri = Property("Janakpuri", 260, 22)
subhash_nagar = Property("Subhash Nagar", 280, 24)

# Green
vikaspuri = Property("Vikaspuri", 300, 26)
tagore_garden = Property("Tagore Garden", 300, 26)
rajouri_ext = Property("Rajouri Extension", 320, 28)

# Dark Blue
west_delhi_mall = Property("West Delhi Mall", 350, 35)
club_road_west_delhi = Property("Club Road, West Delhi", 400, 50)

# Railroads
outer_ring_road = Property("Outer Ring Road", 200, 25)
rohtak_road = Property("Rohtak Road", 200, 25)
nazafgarh_road = Property("Najafgarh Road", 200, 25)
ring_road = Property("Ring Road", 200, 25)

# Utilities
bSES = Property("BSES Power Station", 150, 10)
djB = Property("Delhi Jal Board Office", 150, 10)


# === PROPERTY POSITIONS ON THE BOARD === #
properties_positions = [
    (1, rani_bagh), (3, shakurpur), (5, outer_ring_road),
    (6, pitampura), (8, kohat_enclave), (9, saraswati_vihar),
    (11, ashok_vihar), (12, bSES), (13, model_town), (14, rohini_sec7),
    (15, rohtak_road),
    (16, rohini_sec13), (18, paschim_vihar), (19, mangolpuri),
    (21, rajouri_garden), (23, punjabi_bagh), (24, tilak_nagar),
    (25, nazafgarh_road),
    (26, kirti_nagar), (27, janakpuri), (28, djB), (29, subhash_nagar),
    (31, vikaspuri), (32, tagore_garden), (34, rajouri_ext),
    (35, ring_road),
    (37, west_delhi_mall), (39, club_road_west_delhi)
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
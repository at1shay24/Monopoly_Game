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
rani_bagh = Property("Rani Bagh", 60, 2, color="Purple")
shakurpur = Property("Shakurpur", 60, 4, color="Purple")

# Light Blue
pitampura = Property("Pitampura", 100, 6, color="Light Blue")
saraswati_vihar = Property("Saraswati Vihar", 100, 6, color="Light Blue")
kohat_enclave = Property("Kohat Enclave", 120, 8, color="Light Blue")

# Pink
rohini_sec3 = Property("Rohini Sector 3", 140, 10, color="Pink")
rohini_sec7 = Property("Rohini Sector 7", 140, 10, color="Pink")
rohini_sec9 = Property("Rohini Sector 9", 160, 12, color="Pink")

# Orange
ashok_vihar = Property("Ashok Vihar", 180, 14, color="Orange")
sadar_bazar = Property("Sadar Bazar", 180, 14, color="Orange")
kamla_nagar = Property("Kamla Nagar", 200, 16, color="Orange")

# Red
karol_bagh = Property("Karol Bagh", 220, 18, color="Red")
rajouri_garden = Property("Rajouri Garden", 220, 18, color="Red")
punjabi_bagh = Property("Punjabi Bagh", 240, 20, color="Red")

# Yellow
janakpuri = Property("Janakpuri", 260, 22, color="Yellow")
tilak_nagar = Property("Tilak Nagar", 260, 22, color="Yellow")
subhash_nagar = Property("Subhash Nagar", 280, 24, color="Yellow")

# Green
hauz_khas = Property("Hauz Khas", 300, 26, color="Green")
greater_kailash = Property("Greater Kailash", 300, 26, color="Green")
defence_colony = Property("Defence Colony", 320, 28, color="Green")

# Dark Blue
chanakyapuri = Property("Chanakyapuri", 350, 35, color="Dark Blue")
gk_mblock = Property("GK M Block Market", 400, 50, color="Dark Blue")

# Railroads
new_delhi_station = Property("New Delhi Railway Station", 200, 25, color="Railroad")
shakur_basti = Property("Shakur Basti Railway", 200, 25, color="Railroad")
nizamuddin_station = Property("Hazrat Nizamuddin Railway", 200, 25, color="Railroad")
delhi_cantt = Property("Delhi Cantt Railway", 200, 25, color="Railroad")

# Utilities
electric_company = Property("BSES Rajdhani Power", 150, 10, color="Utility")
water_supply = Property("Delhi Jal Board", 150, 10, color="Utility")

# Positioning them on the board
properties_positions = [
    (1, rani_bagh), (3, shakurpur), (5, new_delhi_station),
    (6, pitampura), (8, saraswati_vihar), (9, kohat_enclave),
    (11, rohini_sec3), (12, electric_company), (13, rohini_sec7), (14, rohini_sec9),
    (15, shakur_basti),
    (16, ashok_vihar), (18, sadar_bazar), (19, kamla_nagar),
    (21, karol_bagh), (23, rajouri_garden), (24, punjabi_bagh),
    (25, nizamuddin_station),
    (26, janakpuri), (27, tilak_nagar), (28, water_supply), (29, subhash_nagar),
    (31, hauz_khas), (32, greater_kailash), (34, defence_colony),
    (35, delhi_cantt),
    (37, chanakyapuri), (39, gk_mblock)
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
class Settings():
    def __init__(self):
        self.cell_size = 10
        self.cell_number = 48
        self.screen_width = self.cell_size * self.cell_number
        self.screen_height = self.cell_size * self.cell_number
        self.bg_color = (64, 64, 64)
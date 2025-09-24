from colors import Colors
import pygame 

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
        self.row = 0
        


    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1,
            self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

            

    def move_down(self):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            if tile.row >= 19: 
               return False
        for tile in tiles:
            tile.move_down() 
        return True


    def move_right(self):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile.move_right()

    def move_left(self):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile.move_left()



        
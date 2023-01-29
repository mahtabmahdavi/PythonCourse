import random
import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SpaceShip(arcade.Sprite):
    def __init__(self, name):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.name = name
        self.width = 48
        self.height = 48
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 80
        self.speed = 8
       

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.width = 48
        self.height = 48
        self.center_x = random.randint(self.width, SCREEN_WIDTH - self.width)
        self.center_y = SCREEN_HEIGHT + self.height // 2
        self.angle = 180
        self.speed = 4


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Intersteller Game 🚀")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = SpaceShip("Mahtab")
        self.enemy = Enemy()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.me.center_x = self.me.center_x - self.me.speed
        elif symbol == 100:
            self.me.center_x = self.me.center_x + self.me.speed

    def on_update(self, delta_time: float):
        self.enemy.center_y -= self.enemy.speed


game = Game()
game.run()
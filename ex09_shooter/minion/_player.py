"""Your space ship."""
import pyxel

WIDTH = 8
HEIGHT = 8
SPEED = 2


class Player:
  """Player's space ship."""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = WIDTH
    self.h = HEIGHT

  def update(self):
    dx = SPEED * (pyxel.btn(pyxel.KEY_RIGHT) - pyxel.btn(pyxel.KEY_LEFT))
    dy = SPEED * (pyxel.btn(pyxel.KEY_DOWN) - pyxel.btn(pyxel.KEY_UP))
    self.x = min(max(0, self.x + dx), pyxel.width - WIDTH)
    self.y = min(max(0, self.y + dy), pyxel.height - HEIGHT)

  def draw(self):
    pyxel.blt(self.x, self.y, 0, 0, 0, WIDTH, HEIGHT, 0)

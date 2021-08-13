"""Player's bullet."""
import pyxel

WIDTH = 2
HEIGHT = 8
COLOR = 11
SPEED = 4


class Minion:
  """Player's bullet."""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = WIDTH
    self.h = HEIGHT
    self.alive = True

  def update(self):
    self.y -= SPEED

    if self.y + HEIGHT - 1 < 0:
      self.alive = False

  def draw(self):
    pyxel.rect(self.x, self.y, WIDTH, HEIGHT, COLOR)

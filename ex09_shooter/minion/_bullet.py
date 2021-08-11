"""Player's bullet."""
import pyxel

from ex09_shooter import scene

WIDTH = 2
HEIGHT = 8
COLOR = 11
SPEED = 4


class Bullet:
  """Player's bullet."""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = WIDTH
    self.h = HEIGHT
    self.alive = True

    scene.bullet_list.append(self)

  def update(self):
    self.y -= SPEED

    if self.y + self.h - 1 < 0:
      self.alive = False

  def draw(self):
    pyxel.rect(self.x, self.y, self.w, self.h, COLOR)

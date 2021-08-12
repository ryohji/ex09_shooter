"""Alien."""
import pyxel
import random

WIDTH = 8
HEIGHT = 8
SPEED = 1.5


class Enemy:
  """Alien!"""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = WIDTH
    self.h = HEIGHT
    self.dir = 1
    self.alive = True
    self.offset = random.randint(0, 60)

  def update(self):
    self.dir = 1 if (pyxel.frame_count + self.offset) % 60 < 30 else -1
    self.x += SPEED * self.dir
    self.y += SPEED

    if self.y > pyxel.height - 1:
      self.alive = False

  def draw(self):
    pyxel.blt(self.x, self.y, 0, 8, 0, WIDTH * self.dir, HEIGHT, 0)

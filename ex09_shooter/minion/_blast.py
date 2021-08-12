"""Blast when things blown up."""
import pyxel

RADIUS_START = 1
RADIUS_END = 8
COLOR = 7
COLOR_EDGE = 10


class Blast:
  """Blast when things blown up!"""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.radius = RADIUS_START

  def update(self):
    self.radius += 1

  def draw(self):
    pyxel.circ(self.x, self.y, self.radius, COLOR)
    pyxel.circb(self.x, self.y, self.radius, COLOR_EDGE)

  @property
  def alive(self):
    return self.radius <= RADIUS_END

"""Background stars."""
import pyxel
import random

STAR_COUNT = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5


class Stars:
  """Background star management."""

  def __init__(self):
    self.star_list = [(_rand(pyxel.width), _rand(pyxel.height), _rand(1.5) + 1)
                      for _ in range(STAR_COUNT)]

  def update(self):
    renew_star = lambda x, y, speed: (x, (y + speed) % pyxel.height, speed)
    self.star_list = [renew_star(x, y, speed) for x, y, speed in self.star_list]

  def draw(self):
    for x, y, speed in self.star_list:
      color = STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW
      pyxel.pset(x, y, color)


def _rand(upto: float) -> float:
  return random.random() * upto

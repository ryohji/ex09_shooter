"""Your space ship."""
import pyxel

from ex09_shooter import minion

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
    if pyxel.btn(pyxel.KEY_LEFT):
      self.x -= SPEED

    if pyxel.btn(pyxel.KEY_RIGHT):
      self.x += SPEED

    if pyxel.btn(pyxel.KEY_UP):
      self.y -= SPEED

    if pyxel.btn(pyxel.KEY_DOWN):
      self.y += SPEED

    self.x = max(self.x, 0)
    self.x = min(self.x, pyxel.width - self.w)
    self.y = max(self.y, 0)
    self.y = min(self.y, pyxel.height - self.h)

    if pyxel.btnp(pyxel.KEY_SPACE):
      minion.fire_bullet_from(self)
      pyxel.play(0, 0)

  def draw(self):
    pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)

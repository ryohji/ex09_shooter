"""Your space ship."""
import pyxel

import ex09_shooter


class Player:
  """Player's space ship."""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = ex09_shooter.PLAYER_WIDTH
    self.h = ex09_shooter.PLAYER_HEIGHT

  def update(self):
    if pyxel.btn(pyxel.KEY_LEFT):
      self.x -= ex09_shooter.PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_RIGHT):
      self.x += ex09_shooter.PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_UP):
      self.y -= ex09_shooter.PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_DOWN):
      self.y += ex09_shooter.PLAYER_SPEED

    self.x = max(self.x, 0)
    self.x = min(self.x, pyxel.width - self.w)
    self.y = max(self.y, 0)
    self.y = min(self.y, pyxel.height - self.h)

    if pyxel.btnp(pyxel.KEY_SPACE):
      ex09_shooter.minion.Bullet(
          self.x + (self.w - ex09_shooter.BULLET_WIDTH) / 2,
          self.y - ex09_shooter.BULLET_HEIGHT / 2)

      pyxel.play(0, 0)

  def draw(self):
    pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)

"""Player's bullet."""
import pyxel

import ex09_shooter


class Bullet:
  """Player's bullet."""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = ex09_shooter.BULLET_WIDTH
    self.h = ex09_shooter.BULLET_HEIGHT
    self.alive = True

    ex09_shooter.bullet_list.append(self)

  def update(self):
    self.y -= ex09_shooter.BULLET_SPEED

    if self.y + self.h - 1 < 0:
      self.alive = False

  def draw(self):
    pyxel.rect(self.x, self.y, self.w, self.h, ex09_shooter.BULLET_COLOR)

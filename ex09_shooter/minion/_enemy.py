"""Alien."""
import pyxel
import random

import ex09_shooter


class Enemy:
  """Alien!"""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = ex09_shooter.ENEMY_WIDTH
    self.h = ex09_shooter.ENEMY_HEIGHT
    self.dir = 1
    self.alive = True
    self.offset = random.randint(0, 60)

    ex09_shooter.enemy_list.append(self)

  def update(self):
    if (pyxel.frame_count + self.offset) % 60 < 30:
      self.x += ex09_shooter.ENEMY_SPEED
      self.dir = 1
    else:
      self.x -= ex09_shooter.ENEMY_SPEED
      self.dir = -1

    self.y += ex09_shooter.ENEMY_SPEED

    if self.y > pyxel.height - 1:
      self.alive = False

  def draw(self):
    pyxel.blt(self.x, self.y, 0, 8, 0, self.w * self.dir, self.h, 0)

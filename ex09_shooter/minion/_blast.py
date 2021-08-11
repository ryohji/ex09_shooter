"""Blast when things blown up."""
import pyxel

import ex09_shooter


class Blast:
  """Blast when blowed up!"""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.radius = ex09_shooter.BLAST_START_RADIUS

    ex09_shooter.blast_list.append(self)

  def update(self):
    self.radius += 1

  def draw(self):
    pyxel.circ(self.x, self.y, self.radius, ex09_shooter.BLAST_COLOR_IN)
    pyxel.circb(self.x, self.y, self.radius, ex09_shooter.BLAST_COLOR_OUT)

  @property
  def alive(self):
    return self.radius <= ex09_shooter.BLAST_END_RADIUS

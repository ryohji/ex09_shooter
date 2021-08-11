"""Sample shooting game.

Use cursor keys to move your space ship.
Press space to fire and kill aliens up!
"""
import pyxel
import random

from ex09_shooter import scene

STAR_COUNT = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5

score = 0


class Background:
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


class App:
  """Game app main."""

  def __init__(self):
    pyxel.init(120, 160, caption="Pyxel Shooter")

    pyxel.image(0).set(
        0,
        0,
        [
            "00c00c00",
            "0c7007c0",
            "0c7007c0",
            "c703b07c",
            "77033077",
            "785cc587",
            "85c77c58",
            "0c0880c0",
        ],
    )

    pyxel.image(0).set(
        8,
        0,
        [
            "00088000",
            "00ee1200",
            "08e2b180",
            "02882820",
            "00222200",
            "00012280",
            "08208008",
            "80008000",
        ],
    )

    pyxel.sound(0).set("a3a2c1a1", "p", "7", "s", 5)
    pyxel.sound(1).set("a3a2c2c2", "n", "7742", "s", 10)

    def transit(cls):
      self._scene = cls(transit)

    self.background = Background()
    transit(scene.Title)

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

    self.background.update()
    self._scene.update()

  def draw(self):
    pyxel.cls(0)

    self.background.draw()
    self._scene.draw()

    pyxel.text(39, 4, f"SCORE {score:5}", 7)


def _rand(upto: float) -> float:
  return random.random() * upto


App()

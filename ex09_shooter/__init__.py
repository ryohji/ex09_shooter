"""Sample shooting game.

Use cursor keys to move your space ship.
Press space to fire and kill aliens up!
"""
import pyxel

from ex09_shooter import scene

score = 0


class App:
  """Game app main."""

  def __init__(self):
    pyxel.init(120, 160, caption="Pyxel Shooter")
    pyxel.load("assets.pyxres", True, False, True, False)

    def transit(cls):
      self._scene = cls(transit)

    self._background = scene.Background()
    transit(scene.Title)

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

    self._background.update()
    self._scene.update()

  def draw(self):
    pyxel.cls(0)

    self._background.draw()
    self._scene.draw()

    pyxel.text(39, 4, f"SCORE {score:5}", 7)


App()

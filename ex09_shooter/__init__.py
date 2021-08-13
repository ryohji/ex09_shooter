"""Sample shooting game.

Use cursor keys to move your space ship.
Press space to fire and kill aliens up!
"""
import pyxel

from ex09_shooter import scene

score = 0


def main():
  """Game main."""
  pyxel.init(120, 160, caption="Pyxel Shooter")
  pyxel.load("assets.pyxres", True, False, True, False)

  scene_ = None
  background = scene.Background()

  def update():
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

    background.update()
    scene_.update()

  def draw():
    pyxel.cls(0)

    background.draw()
    scene_.draw()

    pyxel.text(39, 4, f"SCORE {score:5}", 7)

  def transit(cls):
    nonlocal scene_
    scene_ = cls(transit)

  transit(scene.Title)

  pyxel.run(update, draw)

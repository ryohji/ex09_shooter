"""Sample shooting game.

Use cursor keys to move your space ship.
Press space to fire and kill aliens up!
"""
import itertools
import pyxel
import random

from typing import Any, Callable, List

from ex09_shooter import minion

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2

STAR_COUNT = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5

enemy_list = []
bullet_list = []
blast_list = []


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

    self.scene = SCENE_TITLE
    self.score = 0
    self.background = Background()
    self.player = minion.Player(pyxel.width / 2, pyxel.height - 20)

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

    self.background.update()

    if self.scene == SCENE_TITLE:
      self.update_title_scene()
    elif self.scene == SCENE_PLAY:
      self.update_play_scene()
    elif self.scene == SCENE_GAMEOVER:
      self.update_gameover_scene()

  def update_title_scene(self):
    if pyxel.btnp(pyxel.KEY_ENTER):
      self.scene = SCENE_PLAY

  def update_play_scene(self):
    global bullet_list, enemy_list, blast_list

    if pyxel.frame_count % 6 == 0:
      minion.spawn_enemy(_rand)

    for enemy, bullet in itertools.product(enemy_list, bullet_list):
      if _is_collided(enemy, bullet):
        enemy.alive = False
        bullet.alive = False

        _make_blast_on_center_of(enemy)

        self.score += 10

    for enemy in enemy_list:
      if _is_collided(self.player, enemy):
        enemy.alive = False

        # 自機の爆発を生成する
        _make_blast_on_center_of(self.player)

        self.scene = SCENE_GAMEOVER

    self.player.update()
    for iterable in [bullet_list, enemy_list, blast_list]:
      _apply(lambda a: a.update(), iterable)

    enemy_list = _filter_alive(enemy_list)
    bullet_list = _filter_alive(bullet_list)
    blast_list = _filter_alive(blast_list)

  def update_gameover_scene(self):
    global bullet_list, enemy_list, blast_list

    for iterable in [bullet_list, enemy_list, blast_list]:
      _apply(lambda a: a.update(), iterable)

    enemy_list = _filter_alive(enemy_list)
    bullet_list = _filter_alive(bullet_list)
    blast_list = _filter_alive(blast_list)

    if pyxel.btnp(pyxel.KEY_ENTER):
      self.scene = SCENE_PLAY
      self.player.x = pyxel.width / 2
      self.player.y = pyxel.height - 20
      self.score = 0

      enemy_list = []
      bullet_list = []
      blast_list = []

  def draw(self):
    pyxel.cls(0)

    self.background.draw()

    if self.scene == SCENE_TITLE:
      self.draw_title_scene()
    elif self.scene == SCENE_PLAY:
      self.draw_play_scene()
    elif self.scene == SCENE_GAMEOVER:
      self.draw_gameover_scene()

    pyxel.text(39, 4, "SCORE {:5}".format(self.score), 7)

  def draw_title_scene(self):
    pyxel.text(35, 66, "Pyxel Shooter", pyxel.frame_count % 16)
    pyxel.text(31, 126, "- PRESS ENTER -", 13)

  def draw_play_scene(self):
    self.player.draw()
    for iterable in [bullet_list, enemy_list, blast_list]:
      _apply(lambda a: a.draw(), iterable)

  def draw_gameover_scene(self):
    for iterable in [bullet_list, enemy_list, blast_list]:
      _apply(lambda a: a.draw(), iterable)

    pyxel.text(43, 66, "GAME OVER", 8)
    pyxel.text(31, 126, "- PRESS ENTER -", 13)


def _rand(upto: float) -> float:
  return random.random() * upto


def _is_collided(a, b) -> bool:
  return a.x + a.w > b.x \
     and b.x + b.w > a.x \
     and a.y + a.h > b.y \
     and b.y + b.h > a.y


def _make_blast_on_center_of(a) -> None:
  minion.Blast(a.x + a.w / 2, a.y + a.h / 2)
  pyxel.play(1, 1)


def _filter_alive(iterable) -> List[Any]:
  return list(filter(lambda a: a.alive, iterable))


def _apply(f: Callable[[Any], None], iterable: List[Any]) -> None:
  for item in iterable:
    f(item)


App()

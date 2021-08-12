"""Scene management."""
import itertools
import pyxel
import random

import ex09_shooter

from typing import Any, Callable, List

from ex09_shooter import minion

enemy_list = []
bullet_list = []
blast_list = []


class Title:
  """Title scene."""

  def __init__(self, transit: Callable[[Any], None]):
    self._transit = transit

  def update(self):
    if pyxel.btnp(pyxel.KEY_ENTER):
      self._transit(Play)

  def draw(self):
    pyxel.text(35, 66, "Pyxel Shooter", pyxel.frame_count % 16)
    pyxel.text(31, 126, "- PRESS ENTER -", 13)


class Play:
  """Play level scene."""

  def __init__(self, transit: Callable[[Any], None]):
    global enemy_list, bullet_list, blast_list

    self._transit = transit

    self.player = minion.Player(pyxel.width / 2, pyxel.height - 20)
    ex09_shooter.score = 0

    enemy_list = []
    bullet_list = []
    blast_list = []

  def update(self):
    if pyxel.frame_count % 6 == 0:
      enemy_list.append(minion.spawn_enemy(_rand))

    for enemy, bullet in itertools.product(enemy_list, bullet_list):
      if _is_collided(enemy, bullet):
        enemy.alive = False
        bullet.alive = False

        _make_blast_on_center_of(enemy)

        ex09_shooter.score += 10

    for enemy in enemy_list:
      if _is_collided(self.player, enemy):
        enemy.alive = False

        _make_blast_on_center_of(self.player)

        self._transit(GameOver)

    self.player.update()
    if pyxel.btnp(pyxel.KEY_SPACE):
      _make_shot_from(self.player)

    for minions in [bullet_list, enemy_list, blast_list]:
      _apply(lambda minion: minion.update(), minions)

    _filter_minions_alive()

  def draw(self):
    self.player.draw()
    for minions in [bullet_list, enemy_list, blast_list]:
      _apply(lambda minion: minion.draw(), minions)


class GameOver:
  """Game is over."""

  def __init__(self, transit: Callable[[Any], None]):
    self._transit = transit

  def update(self):
    for minions in [bullet_list, enemy_list, blast_list]:
      _apply(lambda minion: minion.update(), minions)

    _filter_minions_alive()

    if pyxel.btnp(pyxel.KEY_ENTER):
      self._transit(Play)

  def draw(self):
    for minions in [bullet_list, enemy_list, blast_list]:
      _apply(lambda minion: minion.draw(), minions)

    pyxel.text(43, 66, "GAME OVER", 8)
    pyxel.text(31, 126, "- PRESS ENTER -", 13)


def _filter_minions_alive():
  global enemy_list, bullet_list, blast_list

  enemy_list = _filter_alive(enemy_list)
  bullet_list = _filter_alive(bullet_list)
  blast_list = _filter_alive(blast_list)


def _rand(upto: float) -> float:
  return random.random() * upto


def _is_collided(a, b) -> bool:
  return a.x + a.w > b.x \
     and b.x + b.w > a.x \
     and a.y + a.h > b.y \
     and b.y + b.h > a.y


def _make_shot_from(player) -> None:
  bullet_list.append(minion.fire_bullet_from(player))
  pyxel.play(0, 0)


def _make_blast_on_center_of(obj) -> None:
  blast_list.append(minion.make_blast_on_center_of(obj))
  pyxel.play(1, 1)


def _filter_alive(minions) -> List[Any]:
  return list(filter(lambda minion: minion.alive, minions))


def _apply(f: Callable[[Any], None], minions: List[Any]) -> None:
  for obj in minions:
    f(obj)

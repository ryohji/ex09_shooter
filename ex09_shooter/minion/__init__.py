"""Game objects."""
from __future__ import annotations
import pyxel

from typing import Callable

from ex09_shooter.minion import _blast, _bullet, _enemy, _player

Blast = _blast.Minion
Bullet = _bullet.Minion
Enemy = _enemy.Minion
Player = _player.Minion


def spawn_enemy(rand: Callable[[float], float]) -> Enemy:
  return Enemy(rand(pyxel.width - _enemy.WIDTH), 0)


def fire_bullet_from(player: Player) -> Bullet:
  return Bullet(player.x + (player.w - _bullet.WIDTH) / 2,
                player.y - _bullet.HEIGHT / 2)


def make_blast_on_center_of(minion: Player | Enemy) -> Blast:
  return Blast(minion.x + minion.w / 2, minion.y + minion.h / 2)

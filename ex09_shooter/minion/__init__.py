"""Game objects."""
from typing import Callable

import pyxel

from ex09_shooter.minion import _blast, _bullet, _enemy, _player

Blast = _blast.Blast
Bullet = _bullet.Bullet
Enemy = _enemy.Enemy
Player = _player.Player


def spawn_enemy(rand: Callable[[float], float]) -> Enemy:
  return Enemy(rand(pyxel.width - _enemy.WIDTH), 0)


def fire_bullet_from(player: Player) -> Bullet:
  return Bullet(player.x + (player.w - _bullet.WIDTH) / 2,
                player.y - _bullet.HEIGHT / 2)

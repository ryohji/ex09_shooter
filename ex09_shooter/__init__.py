"""Sample shooting game.

Use cursor keys to move your space ship.
Press space to fire and kill aliens up!
"""
import pyxel
import random

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2

STAR_COUNT = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2

BULLET_WIDTH = 2
BULLET_HEIGHT = 8
BULLET_COLOR = 11
BULLET_SPEED = 4

ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
ENEMY_SPEED = 1.5

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

enemy_list = []
bullet_list = []
blast_list = []


def update_list(iterable):
  for elem in iterable:
    elem.update()


def draw_list(iterable):
  for elem in iterable:
    elem.draw()


def cleanup_list(iterable):
  i = 0
  while i < len(iterable):
    elem = iterable[i]
    if not elem.alive:
      iterable.pop(i)
    else:
      i += 1


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


class Player:
  """Player's space ship."""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = PLAYER_WIDTH
    self.h = PLAYER_HEIGHT
    self.alive = True

  def update(self):
    if pyxel.btn(pyxel.KEY_LEFT):
      self.x -= PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_RIGHT):
      self.x += PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_UP):
      self.y -= PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_DOWN):
      self.y += PLAYER_SPEED

    self.x = max(self.x, 0)
    self.x = min(self.x, pyxel.width - self.w)
    self.y = max(self.y, 0)
    self.y = min(self.y, pyxel.height - self.h)

    if pyxel.btnp(pyxel.KEY_SPACE):
      Bullet(self.x + (PLAYER_WIDTH - BULLET_WIDTH) / 2,
             self.y - BULLET_HEIGHT / 2)

      pyxel.play(0, 0)

  def draw(self):
    pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)


class Bullet:
  """Player's bullet."""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = BULLET_WIDTH
    self.h = BULLET_HEIGHT
    self.alive = True

    bullet_list.append(self)

  def update(self):
    self.y -= BULLET_SPEED

    if self.y + self.h - 1 < 0:
      self.alive = False

  def draw(self):
    pyxel.rect(self.x, self.y, self.w, self.h, BULLET_COLOR)


class Enemy:
  """Alien!"""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = ENEMY_WIDTH
    self.h = ENEMY_HEIGHT
    self.dir = 1
    self.alive = True
    self.offset = random.randint(0, 60)

    enemy_list.append(self)

  def update(self):
    if (pyxel.frame_count + self.offset) % 60 < 30:
      self.x += ENEMY_SPEED
      self.dir = 1
    else:
      self.x -= ENEMY_SPEED
      self.dir = -1

    self.y += ENEMY_SPEED

    if self.y > pyxel.height - 1:
      self.alive = False

  def draw(self):
    pyxel.blt(self.x, self.y, 0, 8, 0, self.w * self.dir, self.h, 0)


class Blast:
  """Blast when blowed up!"""

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.radius = BLAST_START_RADIUS

    blast_list.append(self)

  def update(self):
    self.radius += 1

  def draw(self):
    pyxel.circ(self.x, self.y, self.radius, BLAST_COLOR_IN)
    pyxel.circb(self.x, self.y, self.radius, BLAST_COLOR_OUT)

  @property
  def alive(self):
    return self.radius <= BLAST_END_RADIUS


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
    self.player = Player(pyxel.width / 2, pyxel.height - 20)

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
    if pyxel.frame_count % 6 == 0:
      Enemy(_rand(pyxel.width - PLAYER_WIDTH), 0)

    for enemy in enemy_list:
      for bullet in bullet_list:
        if _is_collided(enemy, bullet):
          enemy.alive = False
          bullet.alive = False

          blast_list.append(
              Blast(enemy.x + ENEMY_WIDTH / 2, enemy.y + ENEMY_HEIGHT / 2))

          pyxel.play(1, 1)

          self.score += 10

    for enemy in enemy_list:
      if _is_collided(self.player, enemy):
        enemy.alive = False

        # 自機の爆発を生成する
        blast_list.append(
            Blast(
                self.player.x + PLAYER_WIDTH / 2,
                self.player.y + PLAYER_HEIGHT / 2,
            ))

        pyxel.play(1, 1)

        self.scene = SCENE_GAMEOVER

    self.player.update()
    update_list(bullet_list)
    update_list(enemy_list)
    update_list(blast_list)

    cleanup_list(enemy_list)
    cleanup_list(bullet_list)
    cleanup_list(blast_list)

  def update_gameover_scene(self):
    update_list(bullet_list)
    update_list(enemy_list)
    update_list(blast_list)

    cleanup_list(enemy_list)
    cleanup_list(bullet_list)
    cleanup_list(blast_list)

    if pyxel.btnp(pyxel.KEY_ENTER):
      self.scene = SCENE_PLAY
      self.player.x = pyxel.width / 2
      self.player.y = pyxel.height - 20
      self.score = 0

      enemy_list.clear()
      bullet_list.clear()
      blast_list.clear()

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
    draw_list(bullet_list)
    draw_list(enemy_list)
    draw_list(blast_list)

  def draw_gameover_scene(self):
    draw_list(bullet_list)
    draw_list(enemy_list)
    draw_list(blast_list)

    pyxel.text(43, 66, "GAME OVER", 8)
    pyxel.text(31, 126, "- PRESS ENTER -", 13)


def _rand(upto: float) -> float:
  return random.random() * upto


def _is_collided(a, b) -> bool:
  return a.x + a.w > b.x \
     and b.x + b.w > a.x \
     and a.y + a.h > b.y \
     and b.y + b.h > a.y


App()

# ex09_shooter

This is a study variant of `09_shooter` distributed as a part of examples of
[Pyxel](https://github.com/kitao/pyxel) game engine.

I break all-in-one script into pieces of scripts for a view of modularity.
Unfortunately, Pyxel game packager does not support making a binary from
separated scripts, so this copy should be executed from source tree.

## How to execute

You need to install Python, Pyxel game engine and its dependent libraries
according to its instruction.

And then in the project root directory, execute a command like below:
```
python -m ex09_shooter
```

Or
```
PYTHONPATH=$PWD python ex09_shooter
```

## How to play

Press `Enter` to start game.

Once game is started, use cursor key to move your space ship and press
space key repeatedly to fire bullets.
A game is over when you and an alien crashes.

## Topics
* Break into small pieces of modules
* Styled according to "Google Python Style Guide" (thanks to "yapf" formatter.)
* Introduce scene objects `Title`, `Play` and `GameOver` to separete concern
* (Tiny bug fix) Append a `Blast` object once to `blast_list`

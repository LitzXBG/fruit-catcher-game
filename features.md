Basic window: initialize Pygame, open a window, draw a static background, quit cleanly. #done
Player bucket: load the bucket sprite, let left/right arrow keys move it, clamp to screen. # done
Single fruit spawn: drop one fruit sprite straight down; reset it when it reaches the bottom.
Scoring + HUD: add score tracking, convert catches into points, render score text.
Multiple fruits: maintain a list of fruits, spawn them on a timer, give each its own position.
Lives system: track misses, show heart icons, end the game when lives hit zero.
Bomb hazard: introduce bomb objects that cost a life (or end game) when caught.
Audio polish: loop background music, play coin/bomb/life-loss sounds on events.
Mouse controls + restart: allow dragging the bucket with the mouse and add click-to-restart after game over.
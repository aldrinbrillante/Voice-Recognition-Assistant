import pygame
import threading
import queue

pygame.init()
screen = pygame.display.set_mode((300, 300))
quit_game = False

commands = queue.Queue()

pos = pygame.Vector2(10, 10)

m = {'w': (0, -10),
     'a': (-10, 0),
     's': (0, 10),
     'd': (10, 0)}

class Input(threading.Thread):
  def run(self):
    while not quit_game:
      command = input()
      commands.put(command)

i = Input()
i.start()

old_pos = []

while not quit_game:
  try:
    command = commands.get(False)
  except queue.Empty:
    command = None

  if command in m:
    old_pos.append((int(pos.x), int(pos.y)))
    pos += m[command]

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      print("press enter to exit")
      quit_game = True

  screen.fill((0, 0, 0))
  for p in old_pos:
      pygame.draw.circle(screen, (75, 0, 0), p, 10, 2)
  pygame.draw.circle(screen, (200, 0, 0), (int(pos.x), int(pos.y)), 10, 2)
  pygame.display.flip()

i.join()
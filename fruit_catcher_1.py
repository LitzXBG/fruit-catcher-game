import pygame,sys

# pygame setup
pygame.init()
HEIGHT = 650
WIDTH = 1000
speed = 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bucket_img = pygame.transform.scale(pygame.image.load("Assets\\imgs\\bucket.png"), (50, 50))
player_y = (9/10)*HEIGHT
def draw_scene(player_x):
    screen.blit(bucket_img,(player_x,player_y))
def handle_input(player_x):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a]:
    player_x -= speed
  if keys[pygame.K_d]:
    player_x += speed
  player_x = max(0, min(player_x, WIDTH - 50))  
  return player_x
def main():
  player_x = WIDTH/2
  running = True
  while running:
    old_x = player_x
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    player_x = handle_input(player_x)
    screen.fill("white")
    draw_scene(player_x)
    pygame.display.flip()
    clock.tick(120) 

  pygame.quit()

main()
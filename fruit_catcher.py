import pygame,sys
import random
# pygame setup


pygame.init()
HEIGHT = 650
WIDTH = 1000
speed = 3
fruit_speed = 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bucket_img = pygame.transform.scale(pygame.image.load("Assets\\imgs\\bucket.png"), (50, 50))
player_y = (9/10)*HEIGHT
fruit_paths = [
"Assets\\imgs\\apple.png",
"Assets\\imgs\\banana.png",
"Assets\\imgs\\bomb.png",
"Assets\\imgs\\heart.png",
"Assets\\imgs\\strawberry.png",
"Assets\\imgs\\watermelon.png"
]
fruit_imgs = [pygame.transform.scale(pygame.image.load(path), (40, 40)) for path in fruit_paths]
bomb_img = pygame.transform.scale(pygame.image.load("Assets\\imgs\\bomb.png"), (40, 40))  
def draw_scene(player_x,fruits):
    screen.blit(bucket_img,(player_x,player_y))
    for fruit in fruits:
      screen.blit(fruit["img"],(fruit["x"],fruit["y"]))
def handle_input(player_x):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a]:
    player_x -= speed
  if keys[pygame.K_d]:
    player_x += speed
  player_x = max(0, min(player_x, WIDTH - 50))  
  return player_x
def create_fruit():
    is_bomb = random.random() < 0.2
    return {
        "x": random.randint(0, WIDTH - 40),
        "y": 0,
        "img": bomb_img if is_bomb else random.choice(fruit_imgs),
        "is_bomb": is_bomb,
    }
def update_fruits(fruits,speed):
  for fruit in fruits:
    fruit["y"]+=speed
def main():
  fruit_interval = 900
  fruit_timer = 0
  fruits = []
  player_x = WIDTH/2
  running = True
  while running:
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    delta_time = clock.tick(120) 
    fruit_timer += delta_time
    if fruit_timer >= fruit_interval:
      fruits.append(create_fruit())
      fruit_timer = 0
    player_x = handle_input(player_x)
    screen.fill("white")
    update_fruits(fruits,fruit_speed)
    draw_scene(player_x,fruits)
    pygame.display.flip()

  pygame.quit()

main()
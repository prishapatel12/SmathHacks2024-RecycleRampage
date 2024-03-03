import pygame, sys
from pygame.constants import MOUSEBUTTONUP
from pygame.locals import QUIT
import random

pygame.init()

# sets the size, color, and name of screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
bg_color = (178, 228, 191)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recycle Sort")

# logo/title image
title = pygame.image.load("title.png")
title = pygame.transform.scale(title, (400, 400))
end_screen = pygame.image.load("endscreen.png")
end_screen = pygame.transform.scale(end_screen, (500, 200))
#---------------------------------------------------------------

# loads each item, scales them, and holds and other attributes (has to be hardcoded since each item is of varying size)
battery = pygame.image.load("battery.png")
battery = pygame.transform.scale(battery, (100, 100))

magazine = pygame.image.load("magazine.png")
magazine = pygame.transform.scale(magazine, (200, 200))

banana = pygame.image.load("banana.png")
banana = pygame.transform.scale(banana, (150, 150))

bottle = pygame.image.load("bottle.png")
bottle = pygame.transform.scale(bottle, (150, 150))

can = pygame.image.load("can.png")
can = pygame.transform.scale(can, (150, 150))

eggs = pygame.image.load("eggs.png")
eggs = pygame.transform.scale(eggs, (200, 200))

cardboard = pygame.image.load("cardboard.png")
cardboard = pygame.transform.scale(cardboard, (175, 175))

wrapper = pygame.image.load("wrapper.png")
wrapper = pygame.transform.scale(wrapper, (175, 175))

takeout = pygame.image.load("takeout.png")
takeout = pygame.transform.scale(takeout, (200, 200))

pizzabox = pygame.image.load("pizzabox.png")
pizzabox = pygame.transform.scale(pizzabox, (175, 175))

ziploc = pygame.image.load("ziploc.png")
ziploc = pygame.transform.scale(ziploc, (200, 200))

foam = pygame.image.load("foam.png")
foam = pygame.transform.scale(foam, (200, 200))

news = pygame.image.load("news.png")
news = pygame.transform.scale(news, (200, 200))

computer = pygame.image.load("computer.png")
computer = pygame.transform.scale(computer, (200, 200))

sauce = pygame.image.load("sauce.png")
sauce = pygame.transform.scale(sauce, (100, 100))

glass = pygame.image.load("glass.png")
glass = pygame.transform.scale(glass, (100, 100))


# lists for each bin holding what items are correctly placed in them
trash = [takeout, wrapper, foam, pizzabox]
recycle = [magazine, bottle, can, cardboard, news, glass]
compost = [banana, eggs]
other = [battery, computer, sauce, ziploc,]

#---------------------------------------------------------------

# loads bin images into a list
bin_images = [
pygame.image.load("trash.png"),
pygame.image.load("recycle.png"),
pygame.image.load("compost.png"),
pygame.image.load("other.png")
]

# scales each bin item 
for j in range(len(bin_images)):
  bin_images[j] = pygame.transform.scale(bin_images[j], (250, 300))

# class used to make each bin a sprite
class Bin(pygame.sprite.Sprite):
  def __init__(self, bin_num, x, y):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = bin_images[bin_num]
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    
# sprite group
bins = pygame.sprite.Group()

# initializes each bin
binx = 120
biny = SCREEN_HEIGHT - 100

trash_bin = Bin(0, binx, biny)
bins.add(trash_bin)
binx += 120

recycle_bin = Bin(1, binx, biny)
bins.add(recycle_bin)
binx += 120

compost_bin = Bin(2, binx, biny)
bins.add(compost_bin)
binx += 120

other_bin = Bin(3, binx, biny)
bins.add(other_bin)

#---------------------------------------------------------------

# sets important gameplay features
clock = pygame.time.Clock()
FPS = 60
pygame.display.set_icon(title)
score = 0

# main game loop
def main():
  global score
  score = 0
  # items to pick from
  items = [can, magazine, bottle, banana, battery, wrapper, eggs, takeout, foam, ziploc, news, cardboard, pizzabox, computer, sauce, glass]
  item_strings = ["can", "magazine", "bottle", "banana", "battery",  "wrapper", "eggs", "takeout", "foam", "ziploc", "news", "cardboard", "pizzabox", "computer", "sauce", "glass"]
  # 5 items/rounds per game
  for k in range(5):
    # picks random item for round
    item_num = random.randint(0, 14)
    item = items[item_num]
    item_string = item_strings[item_num]
    
    run = True
    while run:
      clock.tick(60)
      screen.fill(bg_color)
      
      #txt file of item
      file = item_string + ".txt"

      # displays score
      score_font = pygame.font.SysFont("Segoe", 50)
      score_text = score_font.render("Score: " + str(score), True, (255, 255, 255), (bg_color))
      score_rect = score_text.get_rect()
      score_rect.center = (SCREEN_WIDTH - 85, 30)
      screen.blit(score_text, score_rect)
      
      # draws bins to screen in their respective locations
      bins.update()
      bins.draw(screen)

      # draws item to screen at mouse location
      x, y = pygame.mouse.get_pos()
      screen.blit(item, (x - 80, y - 80))

      hit = False
      correct = False
      # checks what events have occured
      events = pygame.event.get()
      for event in events:
        if event.type == MOUSEBUTTONUP:
          # checks if any bins were hit
          if y > 180:
            # if trash was hit, chacks if item is supposed to be in trash
            if x > 65 and x < 185:
              hit = True
              if item in trash:
                correct = True
                score += 1
            # if recycling was hit, chacks if item is supposed to be in recycling
            elif x > 186 and x < 304:
              #recycle
              hit = True
              if item in recycle:
                correct = True
                score += 1
            # if compost was hit, chacks if item is supposed to be in compost
            elif x > 307 and x < 424:
              #compost
              hit = True
              if item in compost:
                correct = True
                score += 1
            # if other was hit, chacks if item is supposed to be in other
            elif x > 426 and x < 544:
              #other
              hit = True
              if item in other:
                correct = True
                score += 1
            
          # displays if correct or not  
          if hit:
            correct_font = pygame.font.SysFont("Segoe", 75)
            if correct:
              cor_text = correct_font.render("CORRECT!", True, (37, 66, 38), (bg_color))
            else:
              cor_text = correct_font.render("INCORRECT", True, (161, 55, 55), (bg_color))

            cor_text_rect = cor_text.get_rect()
            cor_text_rect.center = (300, 75)
            screen.blit(cor_text, cor_text_rect)
            
            # displays explanation
            txt_file = open(file, "r")
            txt_list= txt_file.readlines()
            explanation = ("").join(txt_list)
            exp_font = pygame.font.SysFont("Segoe", 24)
            exp_text = exp_font.render(explanation, True, (0, 0, 0), (bg_color))
            text_rect = exp_text.get_rect()
            text_rect.center = (300, 125)
            screen.blit(exp_text, text_rect)

            # displays directions to move on
            space_font = pygame.font.SysFont("Segoe", 18)
            space_text = space_font.render("press space to continue", True, (0, 0, 0), (bg_color))
            space_text_rect = space_text.get_rect()
            space_text_rect.center = (300, 150)
            screen.blit(space_text, space_text_rect)

            pygame.display.update()

            #waits until user reads explanation
            waiting = True
            while waiting:
              for event in pygame.event.get():
                user_input = pygame.key.get_pressed()
                if user_input[pygame.K_SPACE]:
                  waiting = False 
  
                if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
            run = False

        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      pygame.display.update()
  end()

#---------------------------------------------------------------

def start():
  run = True
  while run:
    clock.tick(60)
    screen.fill(bg_color)

    # displays title screen design
    title_rect = title.get_rect()
    title_rect.center = (300, 150)
    screen.blit(title, (title_rect))

    #displays directions
    direction = "press space to start"
    dir_font = pygame.font.SysFont("Segoe", 50)
    direction_text = dir_font.render(direction, True, (255, 255, 255), (bg_color))
    text_rect = direction_text.get_rect()
    text_rect.center = (300, 300)
    screen.blit(direction_text, text_rect)

    for event in pygame.event.get():
      user_input = pygame.key.get_pressed()
      if user_input[pygame.K_SPACE]:
        run = False
    
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()
  main()

#---------------------------------------------------------------

def end():
  global score
  run = True
  while run:
    clock.tick(60)
    screen.fill(bg_color)

    #displays end screen
    end_rect = end_screen.get_rect()
    end_rect.center = (300, 150)
    screen.blit(end_screen, (end_rect))
    
    # displays end score
    score_font = pygame.font.SysFont("Segoe", 100)
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255), (bg_color))
    score_rect = score_text.get_rect()
    score_rect.center = (300, 300)
    screen.blit(score_text, score_rect)

    # displays directions
    direction = "press space to restart or return to end game"
    dir_font = pygame.font.SysFont("Segoe", 30)
    direction_text = dir_font.render(direction, True, (255, 255, 255), (bg_color))
    text_rect = direction_text.get_rect()
    text_rect.center = (300, 350)
    screen.blit(direction_text, text_rect)

    for event in pygame.event.get(): 
      user_input = pygame.key.get_pressed()
      if user_input[pygame.K_SPACE]:
        start()
      elif user_input[pygame.K_RETURN]:
        run = False

      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()

#---------------------------------------------------------------


def gameplay():
  start()
  

gameplay()
  
    
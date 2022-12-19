import pygame
pygame.init()

#display 
resoLution = [500, 500] #nastavi rezolucijo zaslona
win = pygame.display.set_mode((resoLution[0],resoLution[1]))
#player graphics
width = 30
height = 30
gamedelay = 5 #to je treba izbrisat pa najd boljši način

#colours RGB
red = 255,0,0
blu = 0,255,0
gren = 0,0,255
pink = 255,0,255
#yes some more colour
SURFACE_COLOR = (167, 255, 1)
COLOR = (255, 100, 98)

#nekdaj se implementira to... ker bo lažje, i guess
conString1 = [pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT]
conString2 = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
conString3 = 0 # nimata še contString-a -->
conString4 = 0 #--> aka nimata še definiranih user inputov

class player(pygame.sprite.player):
    def __init__(self, xpos, ypos,speed, color, controlString):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.colour = color
        self.controlString = controlString

        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
    
    def input(self):
        #skenira za vse trenutno pritisnjene tipke ? 
        keys = pygame.key.get_pressed()
        #logično preveri kva uporabnik hoče kva bi kj mogel narest
        if keys[self.controlString[1]]:
            self.xpos -= self.speed
        if keys[self.controlString[3]]:
            self.xpos += self.speed
        if keys[self.controlString[0]]:
            self.ypos -= self.speed
        if keys[self.controlString[2]]:
            self.ypos += self.speed

    def update(self):
        # win.fill((0,0,0))  # Fills the screen with black, Glej: Line 52
        pygame.draw.rect(win, (self.colour), (self.xpos, self.ypos, width, height))   
        # pygame.display.update() #če to vklopš nazaj bo za vsazga playerja posebej screen updatal in bo flickering mess --> don do it

class Cone:
    def __init__(self, xpos, ypos, colour, Drawn):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.Drawn = Drawn

    def hide(self):
        self.Drawn = 0

    def show(self):
        self.Drawn = 1
    


#naredimo igralce za to igro
player1 = player(0, 0, 1, red,  conString1)
player2 = player(0, 0, 1, blu,  conString2)
player3 = player(0, 0, 1, gren, conString3)
player4 = player(0, 0, 1, pink, conString4)

players = [player1, player2, player3, player4] #player array, cuz lazy

#grafika:
#naredi array kaj vse je na polju kar boš posodobil vsak frame


#making a playing field

#clock, yes it a clock
clock = pygame.time.Clock()

#and here is the screen whatever the fuck that means
size = (resoLution[1], resoLution[2])
screen = pygame.display.set_mode(size)

mainloop = True
while mainloop:

    pygame.time.delay(gamedelay)

    #stops code if exit on exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False


    #calling all player inputs
    player1.input()
    player2.input()
    # player3.input() # nimata še contString-a aka nimata še definiranih user inputov
    # player4.input() # nimata še contString-a aka nimata še definiranih user inputov

    #limiting player movement to screen 
    pCount = 0 #counting thrue all the players
    while pCount <= 3:
        if players[pCount].xpos <= 0:
            players[pCount].xpos += 1
        if players[pCount].xpos >= (resoLution[0] - width):
            players[pCount].xpos -= 1
        if players[pCount].ypos <= 0:
            players[pCount].ypos += 1
        if players[pCount].ypos >= (resoLution[1] - height):
            players[pCount].ypos -= 1
        pCount += 1

    #drawing their commands, update screen
    win.fill((0,0,0))  # Fills the screen with black
    # graphicly updating player position
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    #updating the display (all at once, yes(kako dela, idk))
    pygame.display.update() 

    #sprite drawing
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

<<<<<<< HEAD
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

#nekdaj se implementira to... ker bo lažje, i guess
conString1 = [pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT]
conString2 = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
conString3 = 0 # nimata še contString-a -->
conString4 = 0 #--> aka nimata še definiranih user inputov

class player:

    def __init__(self, xpos, ypos,speed, colour, controlString):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.colour = colour
        self.controlString = controlString
    
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

#naredimo igralce za to igro
player1 = player(0, 0, 1, red,  conString1)
player2 = player(0, 0, 1, blu,  conString2)
player3 = player(0, 0, 1, gren, conString3)
player4 = player(0, 0, 1, pink, conString4)

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
    # player3.input() # nimata še contString-a -->
    # player4.input() #--> aka nimata še definiranih user inputov


    #drawing their commands, update screen
    win.fill((0,0,0))  # Fills the screen with black
    # graphicly updating player position
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    #updating the display (all at once, yes(kako dela, idk))
    pygame.display.update() 


pygame.quit()
=======
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

#nekdaj se implementira to... ker bo lažje, i guess
conString1 = [pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT]
conString2 = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
conString3 = 0 # nimata še contString-a -->
conString4 = 0 #--> aka nimata še definiranih user inputov

class player:

    def __init__(self, xpos, ypos,speed, colour, controlString):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.colour = colour
        self.controlString = controlString
    
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

#naredimo igralce za to igro
player1 = player(0, 0, 1, red,  conString1)
player2 = player(0, 0, 1, blu,  conString2)
player3 = player(0, 0, 1, gren, conString3)
player4 = player(0, 0, 1, pink, conString4)

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
    # player3.input() # nimata še contString-a -->
    # player4.input() #--> aka nimata še definiranih user inputov


    #drawing their commands, update screen
    win.fill((0,0,0))  # Fills the screen with black
    # graphicly updating player position
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    #updating the display (all at once, yes(kako dela, idk))
    pygame.display.update() 


pygame.quit()
>>>>>>> 0a2c0565a0cf90059060c3f6b194b5cc2013b7ba

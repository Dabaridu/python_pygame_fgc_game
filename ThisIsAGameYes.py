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

# basicfield graphic calculation
center = [(resoLution[0]/2),(resoLution[1]/2)]
gridSize = 6 #tiles!
gridspacingx = (resoLution[0]/gridSize)
gridspacingy = (resoLution[1]/gridSize)

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

class Cone:
    def __init__(self, xpos, ypos, colour, Drawn):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
    
    def hide(self):
        self.Drawn = 0

    def show(self):
        self.Drawn = 1
    
class junction:
    def __init__(self, xpos, ypos, numRed, numBlu, tipe, claim = 0, coneNum = 0): #class junction tipe: ground, low, mid, high; 0-3
        self.xpos = xpos
        self.ypos = ypos
        self.numRed = 0
        self.numBlu = 0
        self.tipe = tipe
        self.tipe = claim

    def addRed(self, amount):
        self.numRed += amount 
        coneNUm += 1
    def addBlu(self, amount):
        self.numBlu += amount
        coneNUm += 1
    
#naredimo igralce za to igro
player1 = player(0, 0, 1, red,  conString1)
player2 = player(0, 0, 1, blu,  conString2)
player3 = player(0, 0, 1, gren, conString3)
player4 = player(0, 0, 1, pink, conString4)

players = [player1, player2, player3, player4] #player array, cuz lazy

#grafika:
#naredi array kaj vse je na polju kar boš posodobil vsak frame


#making a playing field



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

    #field graphics:
    #drawing their commands, update screen
    win.fill((150,150,150))  # Fills the screen with black

    #drawing a grid of circles
    gridcountx = 0 #sets a counter for x
    gridDrawx = 0 #set grid start x
    gridDrawy = 0 #set grid start y
    while (gridcountx < 5):
        gridDrawx += gridspacingx
        gridcounty = 0 #sets gridcount for y
        gridDrawy = 0
        gridcountx += 1
        while (gridcounty < 5):
            gridDrawy += gridspacingy
            pygame.draw.circle(win, (0,0,0), (gridDrawx,gridDrawy), 10)     # pygame.draw.circle(win, (0,0,0), (center[0], center[1]),10)   
            gridcounty += 1
    #from grid to array ?


    # graphicly updating player position
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    #updating the display (all at once, yes(kako dela, idk))
    pygame.display.update() 


pygame.quit()

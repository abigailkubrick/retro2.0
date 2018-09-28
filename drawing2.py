import pygame, sys, random
import pygame.event as GAME_EVENT
import pygame.locals as GAME_GLOBALS

pygame.init()

clock = pygame.time.Clock()

windowwidth = 400
windowheight = 400
rectX = 10.0
rectY = 10.0
rectEndX = 200.0
rectEndY = 100.0
#middle = (windowwidth/2, windowheight/2)
rectXmv = 1
rectYmv = 1

def quitgame():
	pygame.quit()
	sys.exit()

window = pygame.display.set_mode((windowwidth,windowheight))  #width & height . could also write (windowwidth,windowheight)
direction = 1
#a while loop is done indefinately or until the condition is no longer true. For loops continue until list is empty.

while True:   #true is always true so it will run indefinately.
	window.fill((0,0,0))
	pygame.draw.rect(window, (232,16,131), (rectX,rectY,rectEndX,rectEndY))  #rect(Surface, color, Rect, width=0). color tuple -(red, green, blue) (position, size)
	pygame.draw.rect(window, (16,232,16), (0,0,100,100))
	pygame.draw.rect(window, (232,124,16), (0,100,100,100))
	pygame.draw.rect(window, (232,228,16), (0,200,100,100))
	pygame.draw.rect(window, (19,214,214), (0,300,100,100))
	pygame.draw.rect(window, (16,232,16), (400,300,100,100))
	pygame.draw.lines(window, (232,124,16), False, [(300,100), (350,50), (400,100)], 3)   #false = not a closed line, [(how far from left, how far from top)], thickness of line
	pygame.draw.lines(window, (232,124,16), False, [(325,75), (375,75)], 3)   #these two lines are meant to make an A.
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2), (windowheight/2)-40), 30)
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2)+40, (windowheight/2)), 30)
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2), (windowheight/2)+40), 30)
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2)-40, windowheight/2), 30)
	pygame.draw.circle(window, (232,228,16), (windowwidth/2, windowheight/2), 30)
	if rectX > windowwidth:
		direction = -1
	if rectX < 0:
		direction = 1
	rectX += direction * random.randint(0,10) #reassign
	if rectY > windowheight:
		direction = -1
	if rectX < 0:
		direction = 1
	rectY += direction * random.randint(0,10)

	
	for event in GAME_EVENT.get():  #to allopw it to quit properly
		if event.type == GAME_GLOBALS.QUIT:
			quitgame()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitgame()
	clock.tick(60)
	pygame.display.update()

#save in retrogaming folder (not the VE folder) - the one from git hub.
#dont save as library names



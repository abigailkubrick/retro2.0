import pygame, sys, random
import pygame.event as GAME_EVENT
import pygame.locals as GAME_GLOBALS

windowwidth = 800
windowheight = 800

#surface = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption('Pygame Keyboard!')

# Square Variables
playerSize =70
playerX = (windowwidth / 2) - (playerSize / 2)
playerY = windowheight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 50.0
moveSpeed = 0.00010
maxSpeed = 10.0
gravity = 0.9

# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False

# Pygame Variables
pygame.init()
clock = pygame.time.Clock()

blob = pygame.image.load('images/catpic.jpg')

#windowwidth = 500
#windowheight = 400
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

	
def move():
	global playerX, playerY, playerVX, playerVY, haveJumped, gravity
	# Move left 
	if leftDown: #If we're already moving to the right, reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX	
		# Make sure our square doesn't leave our window to the left
		if playerX > 0:
			playerX += playerVX	

	# Move right
	if rightDown:
		# If we're already moving to the left reset the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Make sure our square doesn't leave our window to the right
		if playerX + playerSize < windowwidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Is our square in the air? Better add some gravity to bring it back down!
	if playerY < windowheight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowheight - playerSize
		gravity = 1.0

	playerY -= playerVY

	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1

while True:   #true is always true so it will run indefinately.
	window.fill((0,0,0))
	#pygame.draw.rect(window, (255,0,0), (playerX, playerY, playerSize, playerSize))
	window.blit(blob, (playerX, playerY, playerSize, playerSize))
	#pygame.draw.rect(window, (232,16,131), (rectX,rectY,rectEndX,rectEndY))  #rect(Surface, color, Rect, width=0). color tuple -(red, green, blue) (position, size)
	pygame.draw.lines(window, (232,124,16), False, [(300,100), (350,50), (400,100)], 3)   #false = not a closed line, [(how far from left, how far from top)], thickness of line
	pygame.draw.lines(window, (232,124,16), False, [(325,75), (375,75)], 3)   #these two lines are meant to make an A.
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2), (windowheight/2)-40), 30)
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2)+40, (windowheight/2)), 30)
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2), (windowheight/2)+40), 30)
	pygame.draw.circle(window, (164,16,232), ((windowwidth/2)-40, windowheight/2), 30)
	pygame.draw.circle(window, (232,228,16), (windowwidth/2, windowheight/2), 30)
	pygame.draw.rect(window, (16,232,16), (600,600,100,100))
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


	# Get a list of all events that happened since the last redraw
	for event in GAME_EVENT.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed

		if event.type == GAME_GLOBALS.QUIT:
			quitGame()			

	move()
	
	for event in GAME_EVENT.get():  #to allow it to quit properly
		clock.tick(60)
	pygame.display.update()



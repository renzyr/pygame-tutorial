#pygame tutorial episode 1-2
#https://www.youtube.com/watch?v=UdsNBIzsmlI

import pygame
pygame.init()

screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game Test")

width = 40
height = 60
xPos = screenWidth - (screenWidth - 10)
yPos = screenHeight - (height + 10)
vel = 5

isJump = False
jumpCount = 10


#main loop
running = True

while running:
    pygame.time.delay(100) # amount of ticks. integer in milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed() #listens to key press

    if key[pygame.K_a] and xPos > vel: #makes sure that the x position doesn't go negative
        xPos -= vel

    if key[pygame.K_d] and xPos < screenWidth - width - vel:
        xPos += vel

    if not(isJump):
        if key[pygame.K_w] and yPos > vel:
            yPos -= vel

        if key[pygame.K_s] and yPos < screenHeight - height - vel:
            yPos += vel

        if key[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            yPos -= (jumpCount ** 2) * 0.5 * neg
            jumpCount  -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0,0), (xPos, yPos, width, height)) #draw a shape rectangle, first parameter is the surface.
   
    pygame.display.update()

    
pygame.quit()

# pygame tutorial episode 3 above
# https://www.youtube.com/watch?v=UdsNBIzsmlI
import pygame

pygame.init()

screenWidth = 500
screenHeight = 480

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game Test")

walkRight = [pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R1.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R2.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R3.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R4.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R5.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R6.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R7.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R8.png'),
             pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/R9.png')]

walkLeft = [pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L1.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L2.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L3.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L4.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L5.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L6.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L7.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L8.png'),
            pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/L9.png')]

bg = pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/bg.jpg')
char = pygame.image.load('C:/Users/razon/PyGame/pygame-tutorial/assets/standing.png')

clock = pygame.time.Clock()


width = 64
height = 64
xPos = screenWidth - (screenWidth - 10)
yPos = screenHeight - (height + 10)
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (xPos, yPos))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (xPos, yPos))
        walkCount += 1
    else:
        win.blit(char, (xPos, yPos))

    pygame.display.update()


# main loop
running = True

while running:
    clock.tick(27)  # amount of ticks. integer in milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()  # listens to key press

    if key[pygame.K_a] and xPos > vel:  # makes sure that the x position doesn't go negative
        xPos -= vel
        left = True
        right = False
    elif key[pygame.K_d] and xPos < screenWidth - width - vel:
        xPos += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if key[pygame.K_SPACE]:
            isJump = True
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            yPos -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()


pygame.quit()

# pygame tutorial episode 4 above
import pygame

pygame.init()

screenWidth = 500
screenHeight = 480

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game Test")


walkRight = [pygame.image.load('C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R1.png'),
             pygame.image.load(
                 'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R2.png'),
             pygame.image.load(
                 'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R3.png'),
             pygame.image.load(
                 'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R4.png'),
             pygame.image.load(
                 'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R5.png'),
             pygame.image.load(
                 'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R6.png'),
             pygame.image.load(
                 'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R7.png'),
             pygame.image.load(
                 'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R8.png'),
             pygame.image.load('C:/Users/razon/Python/PyGame/pygame-tutorial/assets/R9.png')]

walkLeft = [pygame.image.load('C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L1.png'),
            pygame.image.load(
                'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L2.png'),
            pygame.image.load(
                'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L3.png'),
            pygame.image.load(
                'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L4.png'),
            pygame.image.load(
                'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L5.png'),
            pygame.image.load(
                'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L6.png'),
            pygame.image.load(
                'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L7.png'),
            pygame.image.load(
                'C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L8.png'),
            pygame.image.load('C:/Users/razon/Python/PyGame/pygame-tutorial/assets/L9.png')]

bg = pygame.image.load('C:/Users/razon/Python/PyGame/pygame-tutorial/assets/bg.jpg')
char = pygame.image.load('C:/Users/razon/Python/PyGame/pygame-tutorial/assets/standing.png')

clock = pygame.time.Clock()

class player(object):

    def __init__(self, xPos, yPos, width, height):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.xPos, self.yPos))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.xPos, self.yPos))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.xPos, self.yPos))
            else:
                win.blit(walkLeft[0], (self.xPos, self.yPos))


class projectile(object):

    def __init__(self, xPos, yPos, radius, color, facing):
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.xPos, self.yPos), self.radius)



#every draw happens here
def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw(win)

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# main loop
player = player(300, 410, 64, 64)
running = True
bullets = []

while running:
    clock.tick(32)  # amount of ticks. integer in milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.xPos < 500 and bullet.xPos > 0:
            bullet.xPos += bullet.vel
        else: 
            bullets.pop(bullets.index(bullet)) #remove bullet

    key = pygame.key.get_pressed()  # listens to key presas

    if key[pygame.K_SPACE]:
        if player.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(player.xPos + player.width //2), round(player.yPos + player.height//2), 6, (0,0,0), facing))

    # makes sure that the x position doesn't go negative
    if key[pygame.K_a] and player.xPos > player.vel:
        player.xPos -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif key[pygame.K_d] and player.xPos < screenWidth - player.width - player.vel:
        player.xPos += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not(player.isJump):
        if key[pygame.K_w]:
            player.isJump = True
            player.right = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.yPos -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redrawGameWindow()


pygame.quit()

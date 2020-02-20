import pygame
pygame.init()


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game Test")

x = 50
y = 50
width = 40
height = 60
vel = 5

#write main loop
running = True

while running:
    pygame.time.delay(100) # amount of ticks. integer in milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed() #listens to key press

    if key[pygame.K_LEFT]:
        x -= vel

    if key[pygame.K_RIGHT]:
        x += vel

    if key[pygame.K_UP]:
        y -= vel

    if key[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0,0), (x, y, width, height)) #draw a shape rectangle, first parameter is the surface.
   
    pygame.display.update()

    
pygame.quit()

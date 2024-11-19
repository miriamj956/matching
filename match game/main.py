import pygame

pygame.init()

screen = pygame.display.set_mode([600, 1000])

screen.fill("red")

ludo = pygame.image.load("ludo.png")
screen.blit(ludo, (80,70))

candy = pygame.image.load("candy.jpg")
screen.blit(candy, (80, 200))

subway = pygame.image.load("subway.png")
screen.blit(subway, (80, 330))

temple = pygame.image.load("temple.png")
screen.blit(temple, (80, 470))

honkai = pygame.image.load("hi3.png")
honkai1 = pygame.transform.scale(honkai, (100,100))
screen.blit(honkai1, (80, 620))

resident = pygame.image.load("resident.jpg")
resident1 = pygame.transform.scale(resident, (100,100))
screen.blit(resident1, (80, 790))

font = pygame.font.SysFont("Ariel", 36)
text1 = font.render("Candy Crush", True, (0,0,0))
screen.blit(text1, (300, 100))

text2 = font.render("Temple Run", True, (0,0,0))
screen.blit(text2, (300, 230))

text3 = font.render("Ludo", True, (0,0,0))
screen.blit(text3, (300, 360))

text4 = font.render("Subway Surfers", True, (0,0,0))
screen.blit(text4, (300, 500))

text5 = font.render("Honkai Impact 3rd", True, "black")
screen.blit(text5, (300, 830))

text6 = font.render("Resident Evil: Village", True, (0,0,0))
screen.blit(text6, (300, 660))








while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,0), pos, 10, 0)
        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "black", pos2, 10, 0)
            pygame.draw.line(screen, "purple", pos, pos2, 5)

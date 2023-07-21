import pygame
from render import equation, matrix

size = (500, 500)

pygame.init()
screen = pygame.display.set_mode(size)

test_matrix = matrix([["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]])
test_equation = equation(20, 20)

test_equation.add_part(test_matrix)

test_equation.draw(screen)






pygame.display.flip()
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

pygame.quit()
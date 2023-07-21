import pygame

class equation:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def draw(self, surf):
        for x in self.parts:
            x.draw(surf, self.x, self.y)

class part:
    def __init__(self) -> None:
        pass
    def draw(self):
        raise NotImplementedError()

class matrix(part):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
        self.size = (len(data[0]), len(data))

    def draw(self, surf, x, y):
        # open bracket
        pygame.draw.line(surf, (255, 255, 255), (x, y), (x+10, y), 2)
        pygame.draw.line(surf, (255, 255, 255), (x, y), (x, y+(self.size[1]*25)), 2)
        pygame.draw.line(surf, (255, 255, 255), (x, y+(self.size[1]*25)), (x+10, y+(self.size[1]*25)), 2)

        # content
        mono = pygame.font.Font(r"C:\Users\server\Desktop\projects\maths renderer\NotoSansMono-Regular.ttf", 25)
        for j, m in enumerate(self.data):
            for i, n in enumerate(m):
                text = mono.render(n, False, (255, 255, 255))
                surf.blit(text, (x+5+(i*5), y-5+(j*22.5)))





import pygame
import random
def draw_grid(screen):
    #horizontal lines
    for i in range(1,16):
        pygame.draw.line(
            screen,
            "brown",
            (0,32*i),
            (640,32*i)
        )
    #vertical lines
    for i in range(1,20):
        pygame.draw.line(
            screen,
            "brown",
            (32*i,0),
            (32*i,512)
        )

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and running:
                    x, y = event.pos
                    row = y // 32
                    col = x // 32
                    #print("column: ", col,'row: ', row)

            screen.fill("light green")

            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            draw_grid(screen)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

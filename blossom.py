import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Bubble Effect")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Bubble class
class Bubble:
    def __init__(self):
        self.radius = random.randint(15, 20)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.speed_y = random.uniform(10, 30)
        self.color = BLUE

    def update(self):
        self.y -= self.speed_y
        if self.y + self.radius < 0:
            self.y = HEIGHT + self.radius
            self.x = random.randint(self.radius, WIDTH - self.radius)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)


# Main function
def main():
    bubbles = [Bubble() for _ in range(50)]
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for bubble in bubbles:
            bubble.update()
            bubble.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

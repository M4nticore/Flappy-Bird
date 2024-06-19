import pygame
import random

# Initialize the Pygame
pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()
bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (34, 24))  # Resize bird image
background_img = pygame.image.load('background.png')

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = screen_height // 2
        self.gravity = 0.6
        self.lift = -15
        self.velocity = 0

    def show(self):
        screen.blit(bird_img, (self.x, self.y))

    def update(self):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity

        if self.y > screen_height:
            self.y = screen_height
            self.velocity = 0

        if self.y < 0:
            self.y = 0
            self.velocity = 0

    def up(self):
        self.velocity += self.lift

    def get_rect(self):
        return pygame.Rect(self.x, self.y, bird_img.get_width(), bird_img.get_height())

# Pipe class
class Pipe:
    def __init__(self):
        self.spacing = 150
        self.top = random.randint(50, screen_height - self.spacing - 50)
        self.bottom = screen_height - (self.top + self.spacing)
        self.x = screen_width
        self.w = 20
        self.speed = 5
        self.passed = False  

    def show(self):
        pygame.draw.rect(screen, green, (self.x, 0, self.w, self.top))
        pygame.draw.rect(screen, green, (self.x, screen_height - self.bottom, self.w, self.bottom))

    def update(self):
        self.x -= self.speed

    def offscreen(self):
        return self.x < -self.w

    def hits(self, bird):
        bird_rect = bird.get_rect()
        pipe_top_rect = pygame.Rect(self.x, 0, self.w, self.top)
        pipe_bottom_rect = pygame.Rect(self.x, screen_height - self.bottom, self.w, self.bottom)

        return bird_rect.colliderect(pipe_top_rect) or bird_rect.colliderect(pipe_bottom_rect)


def main():
    bird = Bird()
    pipes = [Pipe()]
    running = True
    game_over = False
    score = 0 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.up()
                if event.key == pygame.K_r and game_over:  # Game restart
                    bird = Bird()
                    pipes = [Pipe()]
                    score = 0  
                    game_over = False

        if not game_over:
            # Update
            bird.update()
            for pipe in pipes:
                pipe.update()

                if pipe.hits(bird):
                    game_over = True

                if pipe.offscreen():
                    pipes.remove(pipe)
                    pipes.append(Pipe())

                if not pipe.passed and pipe.x < bird.x:  # Checking pipes
                    pipe.passed = True
                    score += 1  


        screen.blit(background_img, (0, 0))
        bird.show()
        for pipe in pipes:
            pipe.show()

        # Score display
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f'Score: {score}', True, black)
        screen.blit(score_text, (10, 10))

        if game_over:
            font = pygame.font.SysFont(None, 55)
            text = font.render('Game Over', True, red)
            screen.blit(text, (screen_width // 4, screen_height // 2))
            font_small = pygame.font.SysFont(None, 35)
            text_restart = font_small.render('Restart (Press R)', True, red)
            screen.blit(text_restart, (screen_width // 4 - 20, screen_height // 2 + 60))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()

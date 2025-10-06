import pygame
from .paddle import Paddle
from .ball import Ball

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.winning_score = 5  # default win target

        # --- Sound Effects ---
        self.sound_paddle = pygame.mixer.Sound("assets/sounds/paddle_hit.wav")
        self.sound_wall = pygame.mixer.Sound("assets/sounds/wall_bounce.wav")
        self.sound_score = pygame.mixer.Sound("assets/sounds/score.wav")

        # Pass wall sound to ball
        self.ball.sound_wall = self.sound_wall

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        self.ball.move()

        ball_rect = self.ball.rect()
        player_rect = self.player.rect()
        ai_rect = self.ai.rect()

        # --- Collision with Player Paddle ---
        if ball_rect.colliderect(player_rect) and self.ball.velocity_x < 0:
            self.ball.x = player_rect.right  # move ball out of paddle
            self.ball.velocity_x *= -1
            self.sound_paddle.play()

        # --- Collision with AI Paddle ---
        elif ball_rect.colliderect(ai_rect) and self.ball.velocity_x > 0:
            self.ball.x = ai_rect.left - self.ball.width
            self.ball.velocity_x *= -1
            self.sound_paddle.play()

        # --- Scoring ---
        if self.ball.x <= 0:
            self.ai_score += 1
            self.sound_score.play()
            self.ball.reset()
        elif self.ball.x + self.ball.width >= self.width:
            self.player_score += 1
            self.sound_score.play()
            self.ball.reset()

        # --- AI Tracking ---
        self.ai.auto_track(self.ball, self.height)

    def check_game_over(self, screen):
        if self.player_score >= self.winning_score:
            self.display_winner(screen, "Player Wins!")
            return True
        elif self.ai_score >= self.winning_score:
            self.display_winner(screen, "AI Wins!")
            return True
        return False

    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.ball.reset()

    def display_winner(self, screen, message):
        screen.fill((0, 0, 0))
        text = self.font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

    def replay_menu(self, screen):
        screen.fill((0, 0, 0))
        menu_text = [
            "Press 3 for Best of 3",
            "Press 5 for Best of 5",
            "Press 7 for Best of 7",
            "Press ESC to Exit"
        ]
        for i, line in enumerate(menu_text):
            text = self.font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 60 + i * 40))
            screen.blit(text, text_rect)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        self.winning_score = 2
                        waiting = False
                    elif event.key == pygame.K_5:
                        self.winning_score = 3
                        waiting = False
                    elif event.key == pygame.K_7:
                        self.winning_score = 4
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

    def render(self, screen):
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))

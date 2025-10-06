import pygame
from game.game_engine import GameEngine
pygame.mixer.init()


def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong Game")

    clock = pygame.time.Clock()
    engine = GameEngine(WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        engine.handle_input()
        engine.update()

        screen.fill((0, 0, 0))
        engine.render(screen)
        pygame.display.flip()

        # --- Game Over Check ---
        if engine.check_game_over(screen):
            engine.replay_menu(screen)
            engine.reset_game()
        # ------------------------

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

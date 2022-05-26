import attr
import pygame
from settings import Configuration

pygame.init()
pygame.mixer.init()


@attr.define
class Game:
    config = Configuration()
    settings = config.get_all_settings()
    scr_size = (settings["screen_width"], settings["screen_height"])
    scr = pygame.display.set_mode(scr_size, flags=pygame.FULLSCREEN if settings["fullscreen"] else 0)
    clock = pygame.time.Clock()

    def quit_event(self, event: pygame.event.Event) -> bool:
        if event.mod & pygame.KMOD_ALT and event.key == "f4":
            print("Initiated quit with alt-f4")
            return False
        if event.key == self.settings["pause"]:
            print("Initiated quit with pause key")
            return False
        return True

    def main_menu(self):
        active = True
        while active:
            self.clock.tick(self.settings["fps"])
            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                # QUIT works for alt-f4 at least
                # if event.type == pygame.QUIT:
                #     active = True
                if event.type == pygame.KEYDOWN:
                    event.key = pygame.key.name(event.key)
                    active = self.quit_event(event)

            self.scr.fill((255, 165, 0))

    def start(self):
        self.main_menu()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.start()

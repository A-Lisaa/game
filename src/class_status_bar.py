from __future__ import annotations

import os

import pygame


class Bar:
    def __init__(self,
                 background: str | pygame.surface.Surface,
                 bar: str | pygame.surface.Surface,
                 bar_position: tuple[int, int],
                 vertical: bool = False,
                 level: float = 0,
                 min_level: float = 0,
                 max_level: float = 100,
                 overflow: bool = False
                 ):
        self.background = pygame.image.load(os.path.normpath(background)) if isinstance(background, str) else background
        self.bar = pygame.image.load(os.path.normpath(bar)) if isinstance(bar, str) else bar
        self.bar_position = bar_position
        self.vertical = vertical
        self.level = min(max(level, min_level), max_level) if not overflow else level
        self.min_level = min_level
        self.max_level = max_level
        self.overflow = overflow

    def bar_math(self, new_level: float) -> Bar:
        if not self.overflow:
            new_level = min(max(new_level, self.min_level), self.max_level)
        self.level = new_level
        return self

    def __add__(self, other: float) -> Bar:
        return self.bar_math(self.level + other)

    def __sub__(self, other: float) -> Bar:
        return self.bar_math(self.level - other)

    def __mul__(self, other: float) -> Bar:
        return self.bar_math(self.level * other)

    def __truediv__(self, other: float) -> Bar:
        return self.bar_math(self.level / other)

    def __mod__(self, other: float) -> Bar:
        return self.bar_math(self.level % other)

    def __floordiv__(self, other: float) -> Bar:
        return self.bar_math(self.level // other)

    def __pow__(self, other: float) -> Bar:
        return self.bar_math(self.level ** other)

    def get_surface(self) -> pygame.Surface:
        bar_screen = pygame.Surface(self.background.get_size())
        bar_rect = self.bar.get_rect()
        fullness = (self.level - self.min_level)/(self.max_level - self.min_level)
        if not self.vertical:
            bar_position = self.bar_position
            chopped_bar_rect = (0, 0, round(bar_rect.width*(1 - fullness)), 0)
        else:
            bar_position = (self.bar_position[0], self.bar_position[1] + bar_rect.height*(1 - fullness))
            chopped_bar_rect = (0, 0, 0, round(bar_rect.height*(1 - fullness)))

        bar_screen.blit(self.background, (0, 0))
        bar_screen.blit(pygame.transform.chop(self.bar, chopped_bar_rect), bar_position)

        return bar_screen


if __name__ == "__main__":
    scr = pygame.display.set_mode((800, 600))

    bar1 = Bar("images/gui/bar/bar_horizontal_bg.png", "images/gui/bar/bar_horizontal_fg.png", (9, 8))
    bar2 = Bar("images/gui/bar/bar_vertical_bg.png", "images/gui/bar/bar_vertical_fg.png", (9, 9), vertical=True)

    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.KEYDOWN:
                event.key = pygame.key.name(event.key)
                if event.key == "space":
                    bar1 += 10
                    bar2 += 5

        scr.blit(bar1.get_surface(), (0, 0))
        scr.blit(bar2.get_surface(), (0, 100))
        pygame.display.update()

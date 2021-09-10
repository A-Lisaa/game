import random
import sys
import pygame
pygame.init()


def quit(): sys.exit()
def chance(x): return True if random.random() < x else False


if __name__ == "__main__":
    print(chance(1))
    print("foo", "bar", "baz", sep=" || ")
    quit()
    print(chance(0.5))

from pygame.mixer import music

def bg_music(filename, repeat = -1, volume = 0.1, start = 0):
    music.load(filename)
    music.play(repeat, start)
    music.set_volume(volume)
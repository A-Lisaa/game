from pygame import mixer

def bg_music(filename, repeat = -1, volume = 0.1, start = 0):
    mixer.music.load(filename)
    mixer.music.play(repeat, start)
    mixer.music.set_volume(volume)
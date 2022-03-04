from winsound import *

def playfilesound(filename):
    return PlaySound(str(filename), SND_FILENAME)
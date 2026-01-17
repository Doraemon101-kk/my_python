from .scene import *
from .engine import *

if __name__ == "__main__":
    
    a_map = Map('school_room')
    a_game = Engine(a_map)
    a_game.play()
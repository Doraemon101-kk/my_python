from .scene import *

class Engine(object):
   
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('temple_fair')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Map(object):

    def __init__(self, start_scene):
        self.scenes = {
            'school_room': SchoolRoom(),
            'courtyard': Courtyard(),
            'gate': gate(),
            'wall_climb': WallClimb(),
            'library_detention': LibraryDetention(),
            'temple_fair': TempleFair(),
            'detention': Detention()
        }
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
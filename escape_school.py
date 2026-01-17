from sys import exit
from random import randint
from textwrap import dedent



class Scene(object):

    def enter(self):
        print("前方的路以后再来探索吧")
        print("请在子类中重写enter()方法")
        exit(1)

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

class Detention(Scene):

    def enter(self):
        print("抓到了！回家抄一百遍论语！")
        exit(1)

class SchoolRoom(Scene):

    def enter(self):
        print("先生背着手踱步，戒尺在桌上。你可以：假装肚子疼/偷偷溜走")

        action = input(">")

        if action == "假装肚子疼":
            print("先生允许你离开教室了")
            return 'courtyard'
        
        else:
            return 'detention'
        
class Courtyard(Scene):
     
    def enter(self):
        print("你溜到后院，花盆下露出一张纸条。你可以：挖花盆/装作散步")

        action = input(">")

        if action == "挖花盆":
            print("花盆下挖开，你逃了出来")
            return 'temple_fair'
        else:
            return 'gate'
        
class gate(Scene):
    def enter(self):
        print("你来到门口附近，旺财朝你大吠，先生闻声而来。")
        return 'detention'

class TempleFair(Scene):

    def enter(self):
        print("糖葫芦！皮影戏！你成功了，来到庙会玩了一天")
        return 'temple_fair'
    
class Map(object):

    def __init__ (self, start_scene):
        
        self.scenes = {
            'school_room': SchoolRoom(),
            'courtyard': Courtyard(),
            'gate': gate(),
            'temple_fair': TempleFair(),
            'detention': Detention()
        }
        self.start_scene = start_scene


    
    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    

a_map = Map('school_room')
a_game = Engine(a_map)
a_game.play()
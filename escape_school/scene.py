from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("前方的路以后再来探索吧")
        print("请在子类中重写enter()方法")
        exit(1)


class Detention(Scene):

    def enter(self):

        rand = randint(1, 3)
        if rand == 1:
            print(dedent("""
            啊——！被揪住了！！
            先生怒目一瞪：“子曰：‘少之时，血气未定，戒之在色！’
            尔竟敢逃学嬉戏？《论语》抄一百遍！少一字，加罚《大学》一章！”
            完了完了……庙会的糖葫芦，飞了……
            """))
        elif rand == 2:
            print(dedent("""
                        “子不教，父之过！”
                        先生非常生气，随后喊来了你的父母。
                        督促你要认真念书，从此你再也没有出去玩的日子。
                         """))
        else:
            print(dedent("""
                        “罚站！面壁思过哉！”
                        先生罚你到课室门口站一天。
                        同窗好友纷纷嘲笑你，你感觉颜面扫地，无地自容。
                        """))



        exit(1)


class LibraryDetention(Detention):
    def enter(self):
        print(dedent("""
        刚翻上窗台——
        “咳！”
        我一哆嗦差点摔下去！
        先生捋须冷笑：“《礼记》有云：‘毋不敬，俨若思。’
        汝不读圣贤书，反窥杂戏之册？《孟子》一百遍！明日交来！”
        ……我的庙会啊！！
        """))
        exit(1)


class SchoolRoom(Scene):

    def enter(self):
        print(dedent("""
        戒尺“啪！”又敲桌子了！
        先生背着手转圈，眼睛像鹰一样扫过来。
        今天可是庙会！再不出去就没了！
        快选：假装肚子疼 / 偷偷溜走 / 翻窗
        """))

        action = input("> ")

        if action == "假装肚子疼":
            print(dedent("""
            “先生…我肚子好痛…”
            他皱着眉说：“速去速回，莫要嬉游。”
            成了！我一溜烟跑向后院！
            """))
            return 'courtyard'
        
        elif action == "翻窗":
            return 'library_detention'
    
        else:
            return 'detention'


class Courtyard(Scene):
     
    def enter(self):
        print(dedent("""
        后院没人！太好了！
        哇！花盆底下有张纸！
        上面写着：“挖！通庙会！”
        心跳得好快！
        挖花盆？翻墙？还是装作散步？
        """))

        action = input("> ")

        if action == "挖花盆":
            print(dedent("""
            哗啦！土刨开——下面是个洞！
            我钻进去，眼前全是红灯笼！
            庙会！！我来了！！
            """))
            return 'temple_fair'
        elif action == "翻墙":
            return 'wall_climb'
        else :
            print("我暂时不能理解这个选择")
            return 'courtyard'


class gate(Scene):
    def enter(self):
        print(dedent("""
        刚走到门口——
        “汪汪汪！！！”
        旺财疯了一样冲过来！
        先生提灯而出，厉声喝道：“站住！《弟子规》曰：‘入则孝，出则悌！’
        汝夜奔私逃，成何体统？！”
        完蛋……腿都动不了了……
        """))

        
        return 'detention'

class WallClimb(Scene):

    def enter(self):

        print("你翻过了墙，接下来是向左还是向右呢？")
        action = input(">")

        if action == "向右":
            return 'gate'
        elif action == "向左":
            return 'temple_fair'
        else :
            print("我暂时不能理解这个选择")
            return 'wall_climb'



class TempleFair(Scene):

    def enter(self):
        print(dedent("""
        糖葫芦！糖画！打陀螺！皮影戏！
        我咬一口山楂——酸死啦！哈哈！
        孙悟空在布上翻跟头，锣鼓咚咚响！
        逃学成功！爽！！
        """))
        return 'temple_fair'



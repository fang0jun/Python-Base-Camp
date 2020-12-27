class Game:

    top_score = 0

    @classmethod
    def show_top_score(cls):
        print("历史最高纪录：%d" %cls.top_score)


    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("僵尸来袭，不要被感染！")


    def start_game(self):
        print("开始游戏，请%s，进入游戏" % self.player_name)
# 游戏第一步查看游戏的帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
game = Game("小明")
game.start_game()

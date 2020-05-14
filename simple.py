import random

from player import Player

# このSimplePlayerをひな形にしてください
class SimplePlayer(Player):
    name = "SIMPLE" # 自分の名前ないし好きな名前にしてください

    # self.cards -> 自分の手札 <list(int)>
    # self.hp -> 自分のHP <int>
    # rows -> 各列のカードが並んだリストのリスト <list(list(int))>
    # damages -> 各列に現在あるカードの書かれた牛の頭数の合計 <list(int)>
    # hps -> 各プレイヤーのHPのリスト <list(int)>
    # play_cards -> (lessのみ)プレイヤーが出したカードの列：リストのリストで１つ目の要素にプレイヤーの番号、２つ目の要素に出した数字が書かれる <list(list(int))>
    def choose(self, rows, damages, hps):
        return random.choice(self.cards)

    def less(self, rows, damages, play_cards):
        return random.randrange(4)



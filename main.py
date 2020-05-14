import random

from player import *
from simple import *

class Board:
    rows = []
    players = []
    def __init__(self, _players):
        self.players = _players
        if not (2 <= len(self.players) <= 10):
            print("Player number is invalid.")
            exit()
        for i in range(len(self.players)):
            print(f"{i+1}:{self.players[i].name}")
        input()
        set = 1
        while not self.check_end():
            self.setplay()
            print(f"##### Set{set} END")
            print(f"HPs: {[pl.hp for pl in self.players]}")
            set += 1


    def setplay(self):
        deck = [i for i in range(1,105)]
        random.shuffle(deck)
        self.rows = [[], [], [], []] # 4列で6枚まで
        for pl in self.players :
            pl.cards = []
        for i in range(10):
            for pl in self.players:
                pl.cards.append(deck.pop())
        for r in self.rows:
            r.append(deck.pop())

        for pl in self.players:
            pl.cards.sort()
            print(f"{pl.name}: {pl.cards}")
        for i in range(4):
            print(f"Row{i+1}: {self.rows[i]}")

        for i in range(10):
            self.choose()

    def check_end(self):
        for pl in self.players:
            if pl.hp <= 0:
                return True
        return False
    
    def calc_damage(self, r):
        damage = 0
        for d in self.rows[r]:
            if d == 55:
                damage += 7
            elif d % 11 == 0:
                damage += 5
            elif d % 10 == 0:
                damage += 3
            elif d % 5 == 0:
                damage += 2
            else:
                damage += 1
        return damage
    
    def make_hp_data(self):
        hps = []
        for pl in self.players:
            hps.append(pl.hp)
        return hps

    def choose(self):
        chosen_cards = []
        hps = self.make_hp_data()
        dmgs = [self.calc_damage(i) for i in range(4)]
        for i in range(len(self.players)):
            tmp = self.players[i].cards
            try:
                c = self.players[i].choose(self.rows, dmgs, hps)
                if self.players[i].cards != tmp or self.players[i].hp != hps[i]:
                    print(f"Player{i+1}'s cards or hp changed by player")
                    self.players[i].cards = tmp
                    self.players[i].hp = hps[i]
                    c = random.choice(self.players[i].cards)
                elif not c in self.players[i].cards:
                    print(f"The card chosen by player{i+1} isn't his card")
                    c = random.choice(self.players[i].cards)
            except:
                print(f"Player{i+1}'s program(choose) throw exception")
                c = random.choice(self.players[i].cards)
            chosen_cards.append([i, c])
            self.players[i].cards.remove(c)
        chosen_cards.sort(key=lambda x: x[1])

        print("[Rows]")
        for row in self.rows:
            print("  " + str(row))
        print(f"Chosen: {chosen_cards}")
        print(f"HP: {[pl.hp for pl in self.players]}")

        for cards in chosen_cards:
            select = -1
            last_card = -1
            for i in range(4):
                if self.rows[i][-1] < cards[1]:
                    if last_card < self.rows[i][-1]:
                        select = i
                        last_card = self.rows[i][-1]
            if select == -1:
                tmp = self.players[i].cards
                try:
                    r = self.players[cards[0]].less(self.rows, hps, chosen_cards)
                    if self.players[i].cards != tmp or self.players[i].hp != hps[i]:
                        print(f"Player{i+1}'s cards or hp changed by player")
                        self.players[i].cards = tmp
                        self.players[i].hp = hps[i]
                        r = random.randrange(4)
                    elif not (0 <= r <= 3):
                        r = random.randrange(4)
                except:
                    print(f"Player{i+1}'s program(less) throw exception")
                    r = random.randrange(4)

                damage = self.calc_damage(r)
                self.players[cards[0]].hp -= damage
                self.rows[r] = [cards[1]]
            else:
                if len(self.rows[select]) == 5:
                    damage = self.calc_damage(select)
                    self.players[cards[0]].hp -= damage
                    self.rows[select] = [cards[1]]
                else:
                    self.rows[select].append(cards[1])

#
# ここまでメインの実行プログラム
#
# ####################################
#
# 以下は各プレイヤーの親クラス＆作成例
#


# 実行
if __name__ == "__main__":
    players = [
                BiggerPlayer(),
                BiggerPlayer(),
                SmallerPlayer(),
                SmallerPlayer(),
            ]
    board = Board(players)

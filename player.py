# 親クラス
class Player: 
    cards = []
    hp = 66
    def choose(self, rows, damages, hps):
        # 各ターンにどのカードを捨てるか
        pass

    def less(self, rows, damages, play_cards):
        # 最小値より小さかった場合にどの列を取るか(0~3で指定)
        pass


## 以下作成例

class SmallerPlayer(Player):
    # いちばん小さいカードを出し続ける、全部取るときだけちょっと考えて一番安いのを取る
    name = "SMALLER"
    def choose(self, rows, damages, hps):
        return min(self.cards)

    def less(self, rows, damages, play_cards):
        idx = 0
        dmg = damages[0]
        for i in range(1,4):
            if dmg > damages[i]:
                idx = i
                dmg = damages[i]
        return i


class BiggerPlayer(Player):
    # いちばんでかいカードを出し続ける、全部取るときだけちょっと考える
    name = "BIGGER"
    def choose(self, rows, damages, hps):
        return max(self.cards)

    def less(self, rows, damages, play_cards):
        idx = 0
        dmg = damages[0]
        for i in range(1,4):
            if dmg > damages[i]:
                idx = i
                dmg = damages[i]
        return i


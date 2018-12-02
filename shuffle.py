import random


class Shuffle(object):
    def __init__(self):
        with open("members.txt", mode="r")as f:
            self.members = f.read().split("\n")

        with open("last_seats_positions.txt", mode="r")as f:
            self.old_positions = f.read().split(",")

    def print_seats(self, m):
        # # Table1:6人 Table2:5人 Table3:4人
        # print(f"""\ttable1\t\t\t\ttable2\n1:{m[1]}\t6:{m[6]}\t\t7:{m[7]}\t11:{m[11]}\n2:{m[2]}\t5:{m[5]}\t\t8:{m[8]}\t@kazu.max\n3:{m[3]}\t4:{m[4]}\t\t9:{m[9]}\t10:{m[10]}\n\n\t\t\ttable3\n12:{m[12]}\t13:{m[13]}\t14:{m[14]}\t15:{m[15]}""")

        # Table1:5人 Table2:5人 Table3:5人
        print(f"""\n\ttable1\t\t\t\ttable2\n1:{m[1]}\t5:{m[5]}\t\t 6:{m[6]}\t10:{m[10]}\n2:{m[2]}\t4:{m[4]}\t\t 7:{m[
            7]}\t 9:{m[9]}\n\t3:{m[3]}\t\t\t\t8:{m[8]}\t\t\t\n\n\t\t\ttable3\n11:{m[11]}\t12:{m[12]}\t13:{m[13]}\t14:{m[
            14]}\t15:{m[15]}""")

    def print_no(self, m):
        for i in range(1, 16):
            print(f"{i}:{m[i]}")

    def shuffle(self):
        with open("last_seats_positions.txt", mode="r")as f:  # 前回の座席情報を取得
            self.old_positions = f.read().split(",")

        overlap = False  # 同じ場所の人がいた場合のフラグ

        while overlap == False:  # すべて前回と違う席になるまで繰り返し

            new_positions = random.sample(range(1, 16), 15)  # ランダムで座席を作成

            for i in range(15):
                if int(self.old_positions[i]) == new_positions[i] and overlap == False:  # 前回と同じ座席がないか確認
                    overlap = True

        with open("last_seats_positions.txt", mode="w")as f:  # 座席情報を保存
            for new_position in new_positions:
                f.write(str(new_position) + ",")

        new_positions_members = dict(zip(new_positions, self.members))

        return new_positions_members


if __name__ == "__main__":
    with open("members.txt", mode="r")as f:
        members = f.read().split("\n")

    positions = Shuffle().shuffle()

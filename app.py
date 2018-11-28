import random


def print_seats(m):
    # 座席の並び順で表示
    print(f"""
    \ttable1\t\t\t\ttable2
    1:{m[1]}\t6:{m[6]}\t\t7:{m[7]}\t11:{m[11]}
    2:{m[2]}\t5:{m[5]}\t\t8:{m[8]}\t@kazu.max
    3:{m[3]}\t4:{m[4]}\t\t9:{m[9]}\t10:{m[10]}\n
    \t\t\ttable3
    12:{m[12]}\t13:{m[13]}\t14:{m[14]}\t15:{m[15]}
    """)


def main():
    with open("members.txt", mode="r")as f:
        members = f.read().split("\n")

    positions = random.sample(range(1, 16), 15)

    new_members = dict(zip(positions, members))

    print_seats(new_members)


if __name__ == "__main__":
    main()

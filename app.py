import random


def print_seats(new_members):
    # 課題の並び順で表示
    print("Table1", end=" ")

    for i in range(1, 7):
        print(new_members[i], end=" ")

    print("\nTable2", end=" ")

    for i in range(7, 12):
        print(new_members[i], end=" ")

    print("\nTable3", end=" ")

    for i in range(12, 16):
        print(new_members[i], end=" ")

    print("\n")


def main():
    with open("members.txt", mode="r")as f:
        members = f.read().split("\n")

    positions = random.sample(range(1, 16), 15)

    new_members = dict(zip(positions, members))

    print_seats(new_members)


if __name__ == "__main__":
    main()

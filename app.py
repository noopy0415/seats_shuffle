from shuffle import Shuffle

def main():
    # positions, members = Shuffle().shuffle()
    print("[1]:席替え [2]順番入れ替え")
    command = input("command? > ")

    while command.lower() == "q":
        if command.lower() == "1":
            new_positions_members = Shuffle().shuffle()

            Shuffle().print_seats(new_positions_members)
        elif command.lower() == "2":
            new_positions_members = Shuffle().shuffle()

            Shuffle().print_no(new_positions_members)
        else:
            print(f"{command} command is not found")

        command = input("command? > ")

if __name__ == "__main__":
    main()

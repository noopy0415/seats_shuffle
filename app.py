from shuffle import Shuffle

def main():
    # positions, members = Shuffle().shuffle()

    new_positions_members = Shuffle().shuffle()

    Shuffle().print_seats(new_positions_members)


if __name__ == "__main__":
    main()

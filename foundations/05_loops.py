"""Lesson 05: for loops, while loops, break, and continue."""


def main() -> None:
    print("For loop:")
    for day in range(1, 6):
        print(f"practice day {day}")

    print("\nWhile loop:")
    countdown = 3
    while countdown > 0:
        print(f"starting in {countdown}")
        countdown -= 1

    print("\nBreak and continue:")
    for number in range(1, 8):
        if number == 4:
            print("skip 4")
            continue
        if number == 7:
            print("stop at 7")
            break
        print(number)


if __name__ == "__main__":
    main()

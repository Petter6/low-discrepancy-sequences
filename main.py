from typing import Final

versie: Final = 5.0


def print_greeting() -> None:
    hallo: str = "hallo"
    print(hallo)


def main() -> None:
    print_greeting()


if __name__ == "__main__":
    main()

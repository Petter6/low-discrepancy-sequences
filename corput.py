import argparse


def to_base(base: int, n: int) -> list[str]:
    pow = 1
    getal = []

    while True:
        deler, rest = divmod(n, base**pow)
        n = n - rest

        getal.insert(0, str(int(rest / base ** (pow - 1))))

        if deler == 0:
            print(getal)
            return getal

        pow += 1


def generate_corput_seg(base: int, nr_elements: int):
    to_base(base=5, n=16)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int)
    parser.add_argument("--n", type=int)
    args = parser.parse_args()
    generate_corput_seg(base=args.base, nr_elements=args.n)


if __name__ == "__main__":
    main()

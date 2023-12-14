import argparse


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(dest='dim', type=int)
    args = parser.parse_args()

    N = args.dim
    for l in range(N):
        for k in range(N):
            print('t = x[{}] * f({}, {})'.format(k, k * l, N))
            print('y[{}] = y[{}] + t'.format(l, l))


if __name__ == '__main__':
    main()

"""
Example code: This program takes always random action.
"""
import random
import sys


def main():
    for i in range(3):
        # reset command
        print('r')
        sys.stdout.flush()

        # receive initial observation
        feedback = input()
        feedback = feedback.split()
        sys.stderr.write('Reset: {}\n'.format(feedback))

        while True:
            # send random action
            action = random.randint(0, 1) * 2 - 1
            print('s {}'.format(action))
            sys.stdout.flush()

            # receive observation after the action
            feedback = input()
            feedback = feedback.split()

            sys.stderr.write('{}\n'.format(feedback))

            if feedback[0] == 'done':
                break

    # terminate the program
    print('q')
    sys.stdout.flush()


if __name__ == '__main__':
    main()

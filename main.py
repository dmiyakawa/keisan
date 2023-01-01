#!/usr/bin/env python3

"""\
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from logging import DEBUG, INFO, Formatter, StreamHandler, getLogger
import platform
import sys

def inter(default_num_trials=5):
    import random
    import datetime
    print("1 ... 足し算")
    print("2 ... 引き算")
    print("3 ... 掛け算")
    print("4 ... 色々")
    print("0 ... おしまい")
    ok = False
    n = 0
    while not ok:
        val = input("どの計算を練習するの？ ").strip()
        if val not in ["1", "2", "3", "4", "0"]:
            print("正しい数字を一つ選んでね")
        else:
            n = int(val)
            ok = True
    if n == 0:
        print("おしまい")
        return False

    num_trials = default_num_trials
    while True:
        val = input(f"何問やる？ ({default_num_trials}) ").strip()
        if not val:
            break
        if val.isdigit():
            num_trials = int(val)
            if num_trials <= 30:
                break
            print("数字が大きすぎるよ")
        else:
            print("数字を入れてね")

    print(f"{num_trials} 回問題を出すよ")
    started = datetime.datetime.now()

    num_correct_answers = 0
    for i in range(num_trials):

        if n == 4:
            problem_type = random.randint(1, 3)
        else:
            problem_type = n
        if problem_type == 1:
            op = "+"
            a = random.randint(1, 99)
            b = random.randint(1, 99)
            expected = a + b
        elif problem_type == 2:
            op = "-"
            b = random.randint(1, 99)
            a = random.randint(b, 99)
            expected = a - b
        else:
            op = "x"
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            expected = a * b

        while True:
            actual = input(f"{a} {op} {b} = ").strip()
            if actual.isdigit():
                actual = int(actual)
                break
            print("数字じゃないよ")
        if actual == expected:
            print("正解！")
            num_correct_answers += 1
        else:
            print(f"残念！ {a} {op} {b} は {expected} だよ")
    ended = datetime.datetime.now()
    print(f"{num_trials} 回中 {num_correct_answers} 回正解したよ")
    td = ended - started
    print(f"{td.seconds} 秒かかったよ。1問あたり、{td.seconds/num_trials:.02f} 秒かかっているよ")
    return True


def main():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Show debug log")
    args = parser.parse_args()

    logger = getLogger(__name__)
    handler = StreamHandler()
    logger.addHandler(handler)
    if args.debug:
        logger.setLevel(DEBUG)
        handler.setLevel(DEBUG)
    else:
        logger.setLevel(INFO)
        handler.setLevel(INFO)
    handler.setFormatter(Formatter("%(asctime)s %(levelname)7s %(message)s"))
    logger.debug("Start Running (Python {})".format(platform.python_version()))
    while True:
        if not inter():
            break
        print()


    logger.debug("Finished Running")
    return 0


if __name__ == "__main__":
    sys.exit(main())

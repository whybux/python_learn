"""
综合案例3：井字棋游戏
"""
import os

def print_boart(boart=[]):
    print(boart["TL"], end="|")
    print(boart["TM"], end="|")
    print(boart["TR"], )
    print("-+-+-")
    print(boart["ML"], end="|")
    print(boart["MM"], end="|")
    print(boart["MR"], )
    print("-+-+-")
    print(boart["BL"], end="|")
    print(boart["BM"], end="|")
    print(boart["BR"], )


def main():
    boart = {"TL": " ", "TM": " ", "TR": " ", "ML": " ", "MM": " ", "MR": " ", "BL": " ", "BM": " ", "BR": " "}

    num = 0
    while True:
        if num == 0:
            boartTemp = boart.copy()

        if num < 9:
            if num % 2 == 0:
                input_value = input("o走的位置是")
                boartTemp[input_value] = "o"
            else:
                input_value = input("x走的位置是")
                boartTemp[input_value] = "x"

            os.system("clear")
            print_boart(boartTemp)
            num += 1
        else:
            confirm = input("还要玩一把吗？yes/no")
            if confirm == "no":
                break
            else:
                num = 0


if __name__ == '__main__':
    main()

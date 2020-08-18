#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
 * Name        : the_fate
 * Datetime    : 2020/8/14 14:49
 * Package     : 
 * Description : no regret.
"""


import random


def main():
    action = ["Just do it.", "Give up."]
    choice = random.randint(0, len(action)-1)
    print(action[choice])


def test():
    from choice import action
    choice = random.randint(0, len(action)-1)
    print(action[choice])


if __name__ == '__main__':
    main()
    # test()

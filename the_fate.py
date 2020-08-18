#!/usr/bin/env python3
# -*-coding:utf-8-*-
"""
 * Name        : the_fate
 * Author      : zylj
 * Datetime    : 2020/8/14 14:49
 * Package     : 
 * Description : 
"""

__author__ = 'Zhang Yang Li Jun'


import random


def main():
    action = ["Just do it.", "Give up."]
    choice = random.randint(0, len(action)-1)
    print(action[choice])


def test():
    print("no regret.")


if __name__ == '__main__':
    main()

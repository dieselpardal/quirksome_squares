#!/usr/bin/python

import sys
from src.quirksome import QuirkSome


def main(argv):
    qs = QuirkSome()
    print "Square: \n" + qs.value(int(sys.argv[1]))
    #print collatz.max(int(sys.argv[1]), int(sys.argv[2]))

if __name__ == "__main__":
   main(sys.argv[1:])
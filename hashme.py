#!/usr/bin/python

import sys, errno
import fileinput
import hashlib

# Build list
# FIXME: inefficient -- but gets the job done.
def build_list():
    with open('adjectives.txt', 'r') as f:
        adjectives = [line.rstrip() for line in f]

    with open('colors.txt', 'r') as f:
        colors = [line.rstrip() for line in f]

    with open('animals.txt', 'r') as f:
        animals = [line.rstrip() for line in f]

    biglist=[]
    for adjective in adjectives:
        for color in colors:
            for animal in animals:
                biglist.append('%s_%s_%s' % (adjective, color, animal))
    return(biglist)


biglist=build_list()

for line in fileinput.input():
    try:
        value = hash(line) % len(biglist)
        print(biglist[value])
    except IOError as e:
        # tidy exit
        if e.errno == errno.EPIPE:
            sys.exit()

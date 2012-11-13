#!/usr/bin/env python

def medial(*args):
    '''get the medial value of the arguments'''
    mid = int(len(args) / 2)
    args = list(args)
    args.sort()
    return args[mid]

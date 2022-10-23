#!/usr/bin/env python

import sim
import viewer

import sys as cis

from sim import GameSimulation,Event
#import argparse
#import importlib
#import readconfig as cfg

def main():
    gs = GameSimulation(viewer.CliViewer())
    while True:
        gs.update(Event("new frame", None))
    cis.exit()

####################
##     MAIN       ##
####################

if __name__ == "__main__":
    main()
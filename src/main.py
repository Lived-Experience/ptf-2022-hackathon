#!/usr/bin/env python

import sim
import viewer

import sys as cis

from sim import GameSimulation
#import argparse
#import importlib
#import readconfig as cfg

def main():
    gs = GameSimulation(viewer.CliViewer())
    gs.update()
    cis.exit()

####################
##     MAIN       ##
####################

if __name__ == "__main__":
    main()
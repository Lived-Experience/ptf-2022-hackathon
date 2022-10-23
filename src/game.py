#!/usr/bin/env python

import sim
import viewer

import sys as cis

from sim import GameSimulation,Event

class PygameViewer(viewer.Viewer):
    def set_current_scene(self, text_desc, bg_pic, options):
        print("todo")
    
    def selected_option(self):
        print("todo")
        return False

def main():
    gs = GameSimulation(PygameViewer())
    while True:
        gs.update(Event("new frame", None))
    cis.exit()

####################
##     MAIN       ##
####################

if __name__ == "__main__":
    main()
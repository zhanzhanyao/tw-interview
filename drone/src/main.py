#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from drone import Drone
from strategy import Strategy
from util import arg_parse


def task(area, strategy):

    drone = Drone(area)
    drone.draw_area()
    if area != (1, 1):
        strategy = Strategy(strategy, area)
        route = strategy.select_strategy()
        drone.is_full_photographed(route)
        drone.photograph(route)
    else:
        route = [(0, 0)]
        drone.photograph(route)


if __name__ == "__main__":
    area, strategy = arg_parse()
    task(area, strategy)

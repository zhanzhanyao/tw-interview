import logging

import numpy as np

from util import export_log

export_log()


class Strategy:
    def __init__(self, strategy_name, area):
        self.strategy_name = strategy_name
        self.area = area

    def select_strategy(self):
        if self.strategy_name == "snake shape":
            logging.info("Selecting {} to photograph...".format(self.strategy_name))
            return self.snake_move()
        else:
            pass

    def snake_move(self):
        translate = 4
        right_move, up_move = 2, 1
        m = self.area[0]
        n = self.area[1]
        start_x, start_y = 0, 1
        coords_list = []
        for x_value in range(start_x, m, translate):
            x, y = [], []
            x_desc, y_desc = [], []
            for index, y_value in enumerate(range(start_y, n + 1, 2)):
                if index % 2 == 0:
                    x.append(x_value)
                    x_desc.append(x_value + right_move)
                else:
                    x.append(x_value + 1)
                    x_desc.append(x_value + 1 + right_move)
                y.append(y_value)
                y_desc.append(y_value - up_move)
            coords = list(zip(x, y))
            coord_desc = list(reversed(list(zip(x_desc, y_desc))))
            coords_list.append(coords)
            coords_list.append(coord_desc)
        coords_list = [(x, y) for i in coords_list for x, y in i]
        logging.info("The route is {}".format(coords_list))
        return coords_list

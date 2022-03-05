import logging

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

from util import export_log

export_log()


class Drone:
    drone_height = 3
    drone_width = 3

    def __init__(self, area):
        self.area = area

    def draw_area(self):
        pic = np.zeros(self.area)
        logging.info("Task area is {}. Drawing area...\n {}".format(self.area, pic))
        return pic

    def is_full_photographed(self, route):
        pic = np.zeros((self.area[0], self.area[1]))
        up = [(x, y - 1) for x, y in route]
        down = [(x, y + 1) for x, y in route]
        left = [(x - 1, y) for x, y in route]
        right = [(x + 1, y) for x, y in route]
        pictured_area = route + up + down + left + right
        for i, j in pictured_area:
            if i < self.area[0] and j < self.area[1]:
                pic[j, i] += 1
        if np.any(pic == 0):
            logging.info(
                "Still somepoint don't been photographed. Drawing result\n{}".format(
                    pic
                )
            )
            return False
        else:
            logging.info(
                "This area is fill photographed. Drawing result\n{}".format(pic)
            )
            return True

    def photograph(self, route):
        if self.is_full_photographed(route):
            b = 4  # border
            pic = np.zeros((self.area[0] + 2 * b, self.area[1] + 2 * b))
            up = [(x, y - 1) for x, y in route]
            down = [(x, y + 1) for x, y in route]
            left = [(x - 1, y) for x, y in route]
            right = [(x + 1, y) for x, y in route]
            pictured_area = route + up + down + left + right
            for i, j in pictured_area:
                pic[j + b, i + b] += 1
            x_ticks = (
                [""] * b
                + list(map(lambda x: str(x), list(range(self.area[0]))))
                + [""] * b
            )
            y_ticks = (
                [""] * b
                + list(map(lambda x: str(x), list(range(self.area[1]))))
                + [""] * b
            )
            df = pd.DataFrame(pic, index=x_ticks, columns=y_ticks)
            plt.figure()
            sns.heatmap(df, annot=True, linewidths=0.3, ax=None, cbar=False)
            plt.savefig("files/map.png")
            logging.info("Please check photo.jpg to see full photo.")
            plt.show()

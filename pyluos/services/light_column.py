from .service import Service, interact
import numpy as np


class LightColumn(Service):
    def __init__(self, id, alias, device):
        Service.__init__(self, 'LightColumn', id, alias, device)
        self._time = None
        self._color_table = ["blue", "green", "yellow"]
        self._color = 0

    @property
    def color(self):
        return self._color_table[self._color]

    @color.setter
    def color(self, new_color):
        self._color = new_color
        self._push_value('lightstate', new_color)

    def blue(self):
        self.color = 0

    def green(self):
        self.color = 1

    def yellow(self):
        self.color = 2

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, new_time):
        self._time = new_time
        self._push_value('time', new_time)

    def _update(self, new_state):
        Service._update(self, new_state)

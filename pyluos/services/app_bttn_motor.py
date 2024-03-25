from .service import Service


class AppBttnMotor(Service):

    def __init__(self, id, alias, device):
        Service.__init__(self, 'AppBttnMotor', id, alias, device)
        self._alias = alias
        self._sampling_period = 10

    def _update(self, new_state):
        Service._update(self, new_state)

    @property
    def sampling_period(self):
        return self._sampling_period

    @sampling_period.setter
    def sampling_period(self, sampling_period):
        print('ok')
        self._sampling_period = sampling_period
        self._push_value("time", sampling_period / 1000)

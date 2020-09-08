import time


def check_data(data, minimum, name):
    if isinstance(data, (int, float)):
        if data >= minimum:
            return True
        else:
            raise ValueError(f"{name}: Значение {data} не должно быть меньше {minimum}.")
    else:
        raise TypeError(f"{name}: Тип {data} = {type(data)}, а должен быть int или float.")


class TimerPlus:
    """
    sec - число секунд.
    Отдаёт True, если прошло времени >= sec. Если <, то False.
    """
    def __init__(self, sec):
        self.name = "TimerPlus"
        self.minimum = 0.05
        check_data(sec, self.minimum, self.name)
        self.last_time = None
        self.sec = sec
        self.restart()

    def set_sec(self, sec):
        check_data(sec, self.minimum, self.name)
        self.sec = sec

    def restart(self):
        self.last_time = time.monotonic()

    def get_bool(self):
        if time.monotonic() - self.last_time >= self.sec:
            return True
        else:
            return False

    def get_sec(self):
        return time.monotonic() - self.last_time


class TimerMinus:
    """
    sec - число секунд.
    Отдаёт True, если прошло времени <= sec. Если >, то False.
    """
    def __init__(self, sec):
        self.name = "TimerMinus"
        self.minimum = 0.05
        check_data(sec, self.minimum, self.name)
        self.last_time = None
        self.sec = sec
        self.restart()

    def set_sec(self, sec):
        check_data(sec, self.minimum, self.name)
        self.sec = sec

    def restart(self):
        self.last_time = time.monotonic()

    def get_bool(self):
        if time.monotonic() - self.last_time <= self.sec:
            return True
        else:
            return False

    def get_sec(self):
        return time.monotonic() - self.last_time

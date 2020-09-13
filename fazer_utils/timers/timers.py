import time


def check_data(data, minimum, name):
    if isinstance(data, (int, float)):
        if data >= minimum:
            return True
        else:
            raise ValueError(f"{name}: Значение {data} не должно быть меньше {minimum}.")
    else:
        raise TypeError(f"{name}: {data} имеет {type(data)}, а должен быть int или float.")


class TimerPlus:
    """
    sec - число секунд.
    Отдаёт True, если прошло времени >= sec. Если <, то False.
    """
    def __init__(self, sec):
        self.name = "TimerPlus"
        self.minimum = 0.0000000001
        check_data(sec, self.minimum, self.name)
        self.last_time = None
        self.sec = sec
        self.restart()

    def set_sec(self, sec):
        check_data(sec, self.minimum, self.name)
        self.sec = sec

    def restart(self):
        """Сбросить таймер в минимум"""
        self.last_time = time.monotonic()

    def get(self):
        s = self.sec - (time.monotonic() - self.last_time)
        if time.monotonic() - self.last_time >= self.sec:
            return True, s
        else:
            return False, s


class TimerMinus:
    """
    sec - число секунд.
    Отдаёт True, если прошло времени <= sec. Если >, то False.
    """
    def __init__(self, sec):
        self.name = "TimerMinus"
        self.minimum = 0.0000000001
        check_data(sec, self.minimum, self.name)
        self.last_time = None
        self.sec = sec
        self.restart()

    def set_sec(self, sec):
        check_data(sec, self.minimum, self.name)
        self.sec = sec

    def restart(self):
        """Сбросить таймер в минимум"""
        self.last_time = time.monotonic()

    def get(self):
        s = self.sec - (time.monotonic() - self.last_time)
        if time.monotonic() - self.last_time <= self.sec:
            return True, s
        else:
            return False, s


class TimerStep:
    """
    Класс таймера с шагом по множителю.
    min_s - минимальный таймаут. Число больше 0
    max_s - максимальный таймаут. Число больше 0 и больше или равно min_s
    multiplier - множитель. Число больше или равно 1
    Отдаёт True, если прошло времени >= current_delay. Если <, то False.
    """
    def __init__(self, min_s, max_s, multiplier):
        self.name = "TimerStep"
        self.minimum = 0.0000000001
        check_data(min_s, self.minimum, self.name + " arg(1)")
        check_data(max_s, min_s, self.name + " arg(2)")
        check_data(multiplier, 1, self.name + " arg(3)")
        self.min_s = min_s
        self.max_s = max_s
        self.multiplier = multiplier
        self.last_time = None
        self.current_delay = None
        self.restart()

    def set_timer(self, min_s, max_s, multiplier):
        check_data(min_s, self.minimum, self.name + " arg(1)")
        check_data(max_s, min_s, self.name + " arg(2)")
        check_data(multiplier, 1, self.name + " arg(3)")
        self.min_s = min_s
        self.max_s = max_s
        self.multiplier = multiplier

    def restart(self):
        """Сбросить таймер в минимум"""
        self.last_time = time.monotonic()
        self.current_delay = self.min_s

    def step(self):
        """Начать отсчёт следующего временного отрезка"""
        self.last_time = time.monotonic()
        self.current_delay = self.current_delay * self.multiplier
        if self.current_delay > self.max_s:
            self.current_delay = self.max_s

    def get(self):
        s = self.current_delay - (time.monotonic() - self.last_time)
        if time.monotonic() - self.last_time >= self.current_delay:
            return True, s
        else:
            return False, s


class TimerLast:
    """Отдаёт количество секунд прошедшее с момента последнего запроса."""
    def __init__(self):
        self.time_last = None
        self.time_left = None

    def restart(self):
        self.time_last = time.monotonic()

    def get(self):
        if not self.time_last:
            self.time_last = time.monotonic()
            return 0
        else:
            self.time_left = time.monotonic() - self.time_last
            return self.time_left


import time

class GameTime:
    a = 20

    def __init__(self) -> None:
        self.a = 10

    @classmethod
    def get_time_now(cls):
        cls.get_time_now_2(cls)
        return time.time()

    def get_time_now_2(self):
        print(f'Calling instance method on: {self}')
        print(self.a)
        return time.time()

GameTime.get_time_now()

g_t = GameTime()
g_t.get_time_now_2()




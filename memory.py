import math
from colorama import Fore
from utils import clear_console


class Memory:
    memory_object = None
    algorith = None
    ratio = 15

    def __init__(self, capacity):
        self.capacity = capacity
        self.left_memory = capacity
        self.page_size = None
        self.page_left = None
        self.page_count = None

    @classmethod
    def get_memory(cls):
        if cls.memory_object:
            return cls.memory_object
        capacity = cls.get_memory_capacity()
        cls.memory_object = Memory(capacity)
        return cls.memory_object

    @staticmethod
    def get_memory_capacity():
        clear_console()
        again = True
        capacity = None
        while again:
            print(f'Input the {Fore.GREEN}memory{Fore.RESET} capacity(KB): ', end='')
            capacity = int(input())
            if capacity <= 15:
                clear_console()
                print(f'{Fore.RED}Memory size is too small! please enter a number bigger than 15{Fore.RESET}')
                again = True
            else:
                again = False
        return capacity

    def get_page_size(self):
        again = True
        page_size = None
        while again:
            print(f'Input the {Fore.GREEN}page size in (KB){Fore.RESET}: ', end='')
            page_size = int(input())
            if self.capacity / page_size < 15:
                clear_console()
                print(f'{Fore.RED}Memory capacity must be at least 15 times to page size{Fore.RESET}')
                again = True
            else:
                again = False
        self.page_size = page_size
        self.page_count = math.floor(self.capacity / self.page_size)
        self.page_left = self.page_count

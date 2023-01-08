import random
from colorama import Fore
from utils import *


class Process:
    DONE = False
    process_number = 20
    PROCESS_STATUS = ['NS', 'P', 'D', 'T']

    def __init__(self, kwargs):
        self.id = kwargs['id'] + 1
        self.memory = kwargs['memory']
        self.status = 'NS'
        self.duration = kwargs['duration']
        self.first_duration = self.duration
        self.start_time = None
        self.page_count = None
        self.page_used = None

    def __str__(self):
        return f'{self.memory} {self.duration}'

    @classmethod
    def get_process_count(cls):
        again = True
        print(f'input the {Fore.GREEN}amount of process{Fore.RESET}. leave it blank if you want: ', end='')
        while again:
            process_count = input()
            if process_count == '':
                clear_console()
                print(f'{Fore.GREEN}{cls.process_number} is the amount of the processes')
                again = False
            else:
                if process_count.isdigit():
                    if int(process_count) > 1:
                        print(f'{Fore.GREEN}process count is:{Fore.RESET} {process_count}')
                        again = False
                        Process.process_number = int(process_count)
                    else:
                        clear_console()
                        again = True
                        print(f'{Fore.RED}enter a number bigger than 1: {Fore.RESET}', end='')
                else:
                    clear_console()
                    print(f'{Fore.RED}only int numbers are allowed. waiting for process count: {Fore.RESET}', end='')
                    again = True

    def get_start_time(self):
        if self.start_time:
            return self.start_time
        return '-'

    def get_status(self):
        if self.status == 'NS':
            return f'{Fore.RESET}not started{Fore.YELLOW}'
        elif self.status == 'P':
            return f'{Fore.RED}processing{Fore.YELLOW}'
        elif self.status == 'D':
            return f'{Fore.LIGHTGREEN_EX}done{Fore.YELLOW}'
        elif self.status == 'T':
            return f'{Fore.LIGHTYELLOW_EX}terminated{Fore.YELLOW}'

    def get_page_count(self):
        if self.page_count:
            return self.page_count
        return '-'

    def get_page_used(self):
        if self.page_used is not None:
            return self.page_used
        return '-'

    @classmethod
    def generate_process(cls):
        process_array = []
        for proc in range(cls.process_number):
            memory = random.randint(1, 10)
            duration = random.randint(1, 2)
            process_array.append(Process({'id': proc, 'memory': memory, 'duration': duration}))
        return process_array

    @classmethod
    def check_program(cls, process_arr):
        if cls.DONE:
            return cls.DONE
        for proc in process_arr:
            if proc.status == 'NS' or proc.status == 'P':
                return False
            if proc == process_arr[-1] and (proc.status == 'D' or proc.status == 'T'):
                cls.DONE = True
                return cls.DONE

    @staticmethod
    def get_log(process_arr, paging=False):
        log = []
        if paging:
            for proc in process_arr:
                log.append(
                    [f'{Fore.CYAN}{proc.id}{Fore.YELLOW}',
                     f'{Fore.LIGHTMAGENTA_EX}{proc.memory}{Fore.YELLOW}',
                     f'{Fore.RESET}{proc.get_status()}{Fore.YELLOW}',
                     f'{Fore.LIGHTBLUE_EX}{proc.duration}{Fore.YELLOW}',
                     f'{Fore.LIGHTBLUE_EX}{proc.first_duration}{Fore.YELLOW}',
                     f'{Fore.RESET}{proc.get_start_time()}{Fore.YELLOW}',
                     f'{Fore.RESET}{proc.get_page_count()}{Fore.YELLOW}',
                     f'{Fore.RESET}{proc.get_page_used()}{Fore.YELLOW}'])
        else:
            for proc in process_arr:
                log.append([f'{Fore.CYAN}{proc.id}{Fore.YELLOW}',
                            f'{Fore.LIGHTMAGENTA_EX}{proc.memory}{Fore.YELLOW}',
                            f'{Fore.RESET}{proc.get_status()}{Fore.YELLOW}',
                            f'{Fore.LIGHTBLUE_EX}{proc.duration}{Fore.YELLOW}',
                            f'{Fore.LIGHTBLUE_EX}{proc.first_duration}{Fore.YELLOW}',
                            f'{Fore.RESET}{proc.start_time}{Fore.YELLOW}'])
        return log

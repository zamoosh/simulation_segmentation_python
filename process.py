import random


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

    def get_start_time(self):
        if self.start_time:
            return self.start_time
        return '-'

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
                    [proc.id,
                     proc.memory,
                     proc.status,
                     proc.duration,
                     proc.first_duration,
                     proc.get_start_time(),
                     proc.get_page_count(),
                     proc.get_page_used()])
        else:
            for proc in process_arr:
                log.append([proc.id, proc.memory, proc.status, proc.duration, proc.first_duration, proc.start_time])
        return log

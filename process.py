import random


class Process:
    DONE = False
    process_number = 100
    PROCESS_STATUS = ['NS', 'P', 'D']

    def __init__(self, kwargs):
        self.id = kwargs['id'] + 1
        self.memory = kwargs['memory']
        self.status = 'NS'
        self.duration = kwargs['duration']
        self.first_duration = self.duration
        self.start_time = None

    def __str__(self):
        return f'{self.memory} {self.duration}'

    @classmethod
    def generate_process(cls):
        process_array = []
        for proc in range(cls.process_number):
            memory = random.randint(1, 20)
            duration = random.randint(1, 5)
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
    def get_log(process_arr):
        log = []
        for proc in process_arr:
            log.append([proc.id, proc.memory, proc.status, proc.duration, proc.first_duration, proc.start_time])
        return log

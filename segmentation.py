from process import Process
from memory import Memory
from log import Log
from tabulate import tabulate


def segmenting(process_arr, memory):
    time = 1
    logs = []
    program_status = Process.DONE

    while not program_status:
        for proc in process_arr:
            if proc.status == 'D' or proc.status == 'T':
                continue
            if proc.status == 'P':
                proc.duration -= 1
            if proc.duration == 0:
                proc.status = 'D'
                memory.left_memory += proc.memory
            if memory.left_memory >= proc.memory and proc.status == 'NS':
                memory.left_memory -= proc.memory
                proc.status = 'P'
                proc.start_time = time
            if memory.capacity < proc.memory and proc.status == 'NS':
                proc.status = 'T'

        logs.append(Log(time=time, content=Process.get_log(process_arr)))

        program_status = Process.check_program(process_arr)
        time += 1

    return logs


def get_sys_pref():
    capacity = int(input('Input memory capacity(KB): '))
    return Memory(capacity)


def show_result(logs):
    for log in logs:
        print(f'time: {log.time}')
        print(tabulate(tabular_data=log.content, headers=['#', 'proc memory', 'status', 'duration', 'first duration', 'start time'], tablefmt="fancy_grid"))
        print('\n\n\n')


def main():
    memory = get_sys_pref()
    process_arr = Process.generate_process()
    logs = segmenting(process_arr, memory)
    show_result(logs)


if __name__ == '__main__':
    main()

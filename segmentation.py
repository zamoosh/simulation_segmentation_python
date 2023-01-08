import math
from process import Process
from memory import Memory
from log import Log
from tabulate import tabulate
from colorama import Fore
from utils import *


def segmenting(process_arr):
    time = 1
    logs = []
    program_status = Process.DONE
    memory = Memory.get_memory()

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


def paging(process_arr):
    time = 1
    logs = []
    program_status = Process.DONE
    memory = Memory.get_memory()

    while not program_status:
        for proc in process_arr:
            page_required = math.ceil(proc.memory / memory.page_size)
            if proc.status == 'D' or proc.status == 'T':
                continue
            if proc.status == 'P':
                proc.duration -= 1
            if proc.duration == 0:
                proc.status = 'D'
                proc.page_used = 0
                memory.page_left += proc.memory
            if memory.page_left >= page_required and proc.status == 'NS':
                memory.page_left -= page_required
                proc.page_count = page_required
                proc.page_used = page_required
                proc.status = 'P'
                proc.start_time = time
            if memory.page_count < page_required and proc.status == 'NS':
                proc.status = 'T'

        logs.append(Log(time=time, content=Process.get_log(process_arr, paging=True)))
        program_status = Process.check_program(process_arr)
        time += 1
    return logs


def run(process_arr):
    logs = None
    if Memory.algorith == 1:
        logs = paging(process_arr)
    elif Memory.algorith == 2:
        logs = segmenting(process_arr)

    return logs


def get_paging_pref():
    memory = Memory.get_memory()
    memory.get_page_size()
    return memory


def get_segmenting_pref():
    memory = Memory.get_memory()
    return memory


def show_results_file(logs, headers):
    with open('result.txt', 'w') as f:
        for log in logs:
            f.write(f'time: {log.time} \n')
            f.write(
                tabulate(tabular_data=log.content, headers=headers, tablefmt="fancy_grid")
            )
            f.write('\n\n\n')


def show_results_console(logs, headers):
    for log in logs:
        print(f'\n\n\n{Fore.RESET}time: {log.time}{Fore.RESET}')
        print(f'{Fore.YELLOW}{tabulate(tabular_data=log.content, headers=headers, tablefmt="fancy_grid")}')
        print('\n\n\n')


def show_result(logs):
    show_result_method = None
    again = True
    headers = []
    print(f'{Fore.CYAN}select 1 to show result in file and 2 for showing in console: {Fore.RESET}', end='')
    while again:
        show_result_method = int(input())
        if show_result_method == 1:
            again = False
        elif show_result_method == 2:
            again = False
        else:
            clear_console()
            print(f'{Fore.RED}please enter 1 to show results in file and 2 for showing in console: {Fore.RESET}',
                  end='')
            again = True

    if Memory.get_memory().algorith == 1:
        headers = [f'{Fore.RESET}#{Fore.YELLOW}', f'{Fore.RESET}proc memory{Fore.YELLOW}',
                   f'{Fore.RESET}status{Fore.YELLOW}', f'{Fore.RESET}duration{Fore.YELLOW}',
                   f'{Fore.RESET}init duration{Fore.YELLOW}', f'{Fore.RESET}start time{Fore.YELLOW}',
                   f'{Fore.RESET}page count{Fore.YELLOW}', f'{Fore.RESET}page used{Fore.YELLOW}']
    elif Memory.get_memory().algorith == 2:
        headers = [f'{Fore.RESET}#{Fore.YELLOW}', f'{Fore.RESET}proc memory{Fore.YELLOW}',
                   f'{Fore.RESET}status{Fore.YELLOW}', f'{Fore.RESET}duration{Fore.YELLOW}',
                   f'{Fore.RESET}init duration{Fore.YELLOW}', f'{Fore.RESET}start time{Fore.YELLOW}']

    if show_result_method == 1:
        show_results_file(logs, headers)
    elif show_result_method == 2:
        show_results_console(logs, headers)


def select_algorithm():
    again = True
    memory = None
    print(f'{Fore.CYAN}select 1 for paging and 2 for segmenting run: {Fore.RESET}', end='')
    while again:
        algorithm = int(input())
        if algorithm == 1:
            Memory.algorith = 1
            memory = get_paging_pref()
            again = False
        elif algorithm == 2:
            Memory.algorith = 2
            memory = get_segmenting_pref()
            again = False
        else:
            clear_console()
            print(f'{Fore.RED}please enter 1 for paging or 2 for segmentation only: {Fore.RESET}', end='')
            again = True
    return memory


def main():
    print(f'For simplicity, process count is {Fore.GREEN}100{Fore.RESET}')
    print(f'Change it in {Fore.GREEN}process.py{Fore.RESET} file \n')
    select_algorithm()
    process_arr = Process.generate_process()
    logs = run(process_arr)
    show_result(logs)


if __name__ == '__main__':
    main()

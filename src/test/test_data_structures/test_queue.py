#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Function Name: test_queue.py

Author: Alex Hu
Create date: 2020/1/11    
'''

import random
from algorithm.data_structures.queue import Queue
from algorithm.data_structures.queue import Deque


def juessive(users, gap):
    uq = Queue()
    seq = []
    for usr in users:
        uq.enqueue(usr)

    while uq.size() > 1:
        for i in range(gap - 1):
            uq.enqueue(uq.dequeue())
        seq.append(uq.dequeue())

    seq.append(uq.dequeue())
    return seq


class Printer:
    def __init__(self, ppm):
        self._ppm = ppm
        self._current_task = None
        self._time_remaining = 0

    def tick(self):
        if self._current_task is not None:
            self._time_remaining -= 1
            if self._time_remaining <= 0:
                self._current_task = None

    def busy(self):
        return self._current_task is not None

    def start_next_task(self, task):
        self._current_task = task
        self._time_remaining = task.get_pages() * 60 // self._ppm


class Task:
    def __init__(self, time):
        self._time_stamp = time
        self._pages = random.randrange(1, 21)

    def get_time_stamp(self):
        return self._time_stamp

    def get_pages(self):
        return self._pages

    def wait_time(self, curtime):
        return curtime - self._time_stamp


def new_print_task():
    return random.randrange(1, 181) == 180


def printer_simulation(simtime, ppm):
    printer = Printer(ppm)
    pq = Queue()
    waiting_times = []
    for curtime in range(simtime):
        if new_print_task():
            task = Task(curtime)
            pq.enqueue(task)

        if (not printer.busy()) and (not pq.is_empty()):
            nexttask = pq.dequeue()
            waiting_times.append(nexttask.wait_time(curtime))
            printer.start_next_task(nexttask)

        printer.tick()

    average_wait_time = sum(waiting_times) / len(waiting_times)
    print("Average wait time {} secs {} task remaining.".format(average_wait_time, pq.size()))


def pal_checker(s):
    chkq = Deque()
    for ch in s:
        chkq.add_rear(ch)

    checked = True
    while chkq.size() > 1 and checked:
        fn = chkq.remove_front()
        rr = chkq.remove_rear()
        if fn != rr:
            checked = False

    return checked


if __name__ == "__main__":
    print(juessive(["bill", "mary", "tom", "jerry", "john", "jack", "smith"], 7))

    for i in range(10):
        printer_simulation(3600, 5)

    for i in range(10):
        printer_simulation(3600, 10)
#!/usr/bin/env python3
import time
import csv

DATA_FILE = "data.csv"

def load(tasks):
    with open(DATA_FILE) as csvfile:
        timesheetData = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in timesheetData:
            try:
                tasks.append({"name": row[0], "estimate": row[1], "time_taken": float(row[2])*(60*60)})
            except:
                raise Exception("error parsing row: {}".format(row))

def save(tasks):
    with open(DATA_FILE, 'w') as csvfile:
        timesheetData = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for task in tasks:
            timesheetData.writerow([task["name"], task["estimate"], task["time_taken"]/(60*60)])

def choose_task(tasks):
    while True:
        print("Available tasks:")
        for index, task in enumerate(tasks):
            print("{}: {}".format(index, task["name"]))
        task_index = input("Choose task:")
        try:
            task_index = int(task_index)
        except:
            continue

        if 0 <= task_index < len(tasks):
            return task_index

if __name__ == "__main__":

    tasks = []

    load(tasks)

    while True:
        task_index = choose_task(tasks)
        start_time = time.time()
        answer = input("New task? (n for no)").lower()
        stop_time = time.time()
        tasks[task_index]["time_taken"] += stop_time - start_time
        save(tasks)
        if answer == "n":
            break

    save(tasks)
import openpyxl

filename = '22_58333 (1).xlsx'
workbook = openpyxl.load_workbook(filename)
sheet = workbook.active

processes = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    process_id = row[0]
    execution_time = row[1]
    dependencies = row[2]
    processes.append((process_id, execution_time, dependencies))


def calculate_finish_times(t):
    finish_times = {}

    for process_id, exec_time, dependencies in processes:
        if exec_time == 't':
            exec_time = t
        else:
            exec_time = int(exec_time)

        if dependencies == 0 or dependencies is None:
            finish_times[process_id] = exec_time
        else:
            deps = [int(dep) for dep in str(dependencies).split(';')]
            max_dep_time = max(finish_times[dep] for dep in deps)
            finish_times[process_id] = max_dep_time + exec_time

    return max(finish_times.values())


max_t = 0
for t in range(1, 100):
    if calculate_finish_times(t) <= 22:
        max_t = t

print(max_t)

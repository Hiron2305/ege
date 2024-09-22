import openpyxl

wb = openpyxl.load_workbook('18.xlsx')
sheet = wb.active

table = []
for row in sheet.iter_rows(values_only=True):
    table.append(list(row))

N = len(table)
table_max = [[-float('inf')] * N for _ in range(N)]
table_min = [[float('inf')] * N for _ in range(N)]

table_max[0][0] = table[0][0]
table_min[0][0] = table[0][0]

for i in range(1, N):
    table_max[0][i] = table_max[0][i - 1] - table[0][i]
    table_min[0][i] = table_min[0][i - 1] - table[0][i]

    table_max[i][0] = table_max[i - 1][0] - 2 * table[i][0]
    table_min[i][0] = table_min[i - 1][0] - 2 * table[i][0]

for i in range(1, N):
    for j in range(1, N):
        v_hor_max = table_max[i][j - 1] - table[i][j]
        v_hor_min = table_min[i][j - 1] - table[i][j]

        v_vert_max = table_max[i - 1][j] - 2 * table[i][j]
        v_vert_min = table_min[i - 1][j] - 2 * table[i][j]

        table_max[i][j] = max(v_hor_max, v_vert_max)
        table_min[i][j] = min(v_hor_min, v_vert_min)

print(table_max[-1][-1], table_min[-1][-1])

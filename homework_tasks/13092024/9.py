import openpyxl

df = openpyxl.load_workbook("107_9.xlsx")["09"]

counter = 0

for row in range(1, df.max_row + 1):
    list_of_values = [df[f"A{row}"].value, df[f"B{row}"].value, df[f"C{row}"].value, df[f"D{row}"].value]
    summ = max(list_of_values)
    min_value = min(list_of_values)
    list_of_values.remove(min_value)
    s_min_value = min(list_of_values)

    summ -=  (min_value + s_min_value)

    if summ > 0:
        counter += 1

print(counter)
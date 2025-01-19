a = sorted("МАТВЕЙ")

stack = []

counter = 0

for i in range(6):
    if a[i] not in stack and a[i] != "Й":
        stack.append(a[i])
 #   else:
 #       continue
    for j in range(6):
        if a[j] not in stack:
            stack.append(a[j])
#        else:
#            continue
        for k in range(6):
            if a[k] not in stack:
                stack.append(a[k])
#            else:
#                continue
            for l in range(6):
                if a[l] not in stack:
                    stack.append(a[l])
#                else:
#                    continue
                for s in range(6):
                    if a[s] not in stack:
                        stack.append(a[s])
#                    else:
#                        continue
                    if "АЕ" not in "".join(stack):
                        counter += 1
                        stack = []
print(counter)
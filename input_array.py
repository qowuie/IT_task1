arr = []
while True:
    i = input()
    if i.isdigit() and int(i) > 0:
        arr.append(int(i))
    elif i == '!':
        if len(arr) < 3:
            print("Надо ввести как минимум 3 числа")
            continue
        else:
            break
    else:
        print("Водите только положительные числа ")


triangle = False
arr.sort(reverse=True)

for i in range(len(arr) - 2):
    a, b, c = arr[i], arr[i + 1], arr[i + 2]
    if a + b > c and a + c > b and b + c > a:
        triangle = True
        break
if triangle:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(a, b, c, s)
else:
    print("В заданных числах нет подходящих сторон треугольника")


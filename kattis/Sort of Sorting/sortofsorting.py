fl = []
iterations = int(input())
while True:

    l = []
    if iterations == 0:
        break

    for i in range(iterations):
        l.append(str(input()))
    l.sort(key = lambda x: x[0:2])
    for i in l:
        fl.append(i)
    iterations = int(input())
    if iterations != 0:
        fl.append('')
for i in fl:
    print(i)

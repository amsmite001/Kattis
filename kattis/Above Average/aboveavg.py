#!/usr/bin/env python3
import sys
def solve(st):
    runavg = 0
    base = 0
    ravg = 0
    total = 0
    for i in range(len(st)):
        if i == 0:
            base = int(st[i])
        else:
            total += int(st[i])
    classAvg = total/base
    for i in range(len(st)):
        if i != 0:
            if int(st[i]) > classAvg:
                runavg += 1
    ravg = round((runavg/base)*100, 3)
    newString = "{:.3f}".format(ravg)
    newString += '%'
    return str(newString)

def regular():
    l = []
    for _ in range(int(input())):
        st = input().split()
        l.append(solve(st))
    for t in l:
        print(t)
def test():
    assert(solve('4 90 91 92 80'.split())) == '75.000%'
    assert(solve('10 25 50 75 45 92 91 32 67 89 100'.split())) == '60.000%'
    assert(solve('3 71 90 80'.split())) == '33.333%'
    #assert(solve('3 70 90 80'.split())) == '33.333%'
    print('All test cases passed!')
if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
  else:
      regular()

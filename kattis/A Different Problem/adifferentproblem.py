#!/usr/bin/env python3
#Done
import sys
import math
    
def solve(int1,int2):
    if int1 > int2:
        return (int1 - int2)
    else:
        return (int2 - int1)


def test():
  assert(int(solve(100,2))) == 98
  assert(int(solve(80, 100))) == 20
  assert(int(solve(1000000000, 1000000000))) == 0
  print('All test cases passed')
  
def regular():
    l = []
    int1, int2 = map(int, input().split())
    while int1 is not None or int2 is not None:
        l.append(solve(int1,int2))
        try:
            int1, int2 = map(int,input().split())
        except:
            break
    for t in l:
        print(t)

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
  else:
      regular()



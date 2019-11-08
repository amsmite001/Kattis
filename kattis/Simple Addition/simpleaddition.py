#!/usr/bin/env python3
import sys
#Done
def problem(int1,int2):
    return(int1+int2)
def regular():
    int1 = int(input())
    int2 = int(input())
    print(problem(int1,int2))
def test():
    assert(problem(1,2)) == 3
    assert(problem(1000000000,1)) == 1000000001
    assert(problem(999999999,2)) == 1000000001
    print('All test cases passed!')
if __name__ == '__main__':
  if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
  else:
      regular()

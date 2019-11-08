#!/usr/bin/env python3
import sys
#Done, some test states are wonky.
def solve(inp):
  return (hex(int(inp,8))[2:])

def test():
  assert(int(solve('124'))) == 54
  assert(int(solve('20'))) == 10
  assert(str(solve('16'))) == 'e'
  print('All test cases passed.')
  
def regular():
    print(solve(input()))

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
  else:
      regular()



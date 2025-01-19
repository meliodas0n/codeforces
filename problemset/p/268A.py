from itertools import combinations

def main(inputs): 
  total_comb = [i for i in combinations(inputs, 2)]
  no_of_changes = 0
  for comb in total_comb:
    a, b = comb[0], comb[1]
    if a[0] == b[1]:
      no_of_changes += 1
    if a[1] == b[0]:
      no_of_changes += 1
  return no_of_changes

if __name__ == "__main__":
  n = int(input())
  inputs = [input().split() for x in range(n)]
  print(main(inputs))
  
  
"""
100 100 -> 42
42 42 -> 5
5 5 -> 100
100 5
"""
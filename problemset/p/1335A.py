def main(inp):
  for candles in inp:
    if candles >= 2 * 1e9:
      print(int(1e9 - 1))
    elif candles < 3:
      print(0)
    else:
      print(int((candles / 2) - 1) if candles % 2 == 0 else int(candles // 2))

if __name__ == '__main__':
  n = int(input())
  inputs = [int(input()) for _ in range(n)]
  main(inputs)
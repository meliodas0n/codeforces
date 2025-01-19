#!/usr/bin/env bash

name=$1
echo "def main(inp):
  return

if __name__ == '__main__':
  n = int(input())
  inputs = [input() for _ in range(n)]
  print(main(inputs))
" > ${name}.py
git add ${name}.py
git commit -m "$name init"
git push

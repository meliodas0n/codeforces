def main(l):
  d = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
  }
  return sum([d[x] for x in l])
    
if __name__ == "__main__":
  n = int(input())
  l = []
  for i in range(n):
     l.append(input())
  print(main(l))
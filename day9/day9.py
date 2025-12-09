from itertools import combinations

def read_input():
  with open('input.txt', 'r') as f:
    return f.read().strip().split('\n')
  
def area(p1, p2):
  return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)


def part_one(coords):
  formatted_coords = [list(map(int, coord.split(','))) for coord in coords]
  return max(area(p1, p2) for p1, p2 in combinations(formatted_coords, 2))  

def main():
  coords = read_input()
  ans = part_one(coords)
  print(f"Part One: {ans}")

if __name__ == '__main__':
  main()
from itertools import combinations
from shapely.geometry import Polygon, box
from shapely.prepared import prep

def read_input():
  with open('input.txt', 'r') as f:
    return f.read().strip().split('\n')
  
def area(p1, p2):
  return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def part_one(coords):
  formatted_coords = [list(map(int, coord.split(','))) for coord in coords]
  return max(area(p1, p2) for p1, p2 in combinations(formatted_coords, 2))  

def part_two(coords):
  formatted_coords = [tuple(map(int, coord.split(','))) for coord in coords]
  
  polygon = Polygon(formatted_coords)
  prep_polygon = prep(polygon)

  max_area = 0
  for p1, p2 in combinations(formatted_coords, 2):
    rect = box(min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1]))
    if prep_polygon.contains(rect):
      max_area = max(max_area, area(p1, p2))

  return max_area


def main():
  coords = read_input()
  ans = part_one(coords)
  print(f"Part One: {ans}")

  ans = part_two(coords)
  print(f"Part Two: {ans}")

if __name__ == '__main__':
  main()
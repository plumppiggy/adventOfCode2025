import heapq

def read_input():
  with open("input.txt", "r") as f:
    return f.read().strip().split("\n")
  
def part_one(boxes, n):
  max_heap = []
  hp_size = 0

  for idx, box in enumerate(boxes):
    dimensions = list(map(int, box.split(',')))
    x, y, z = dimensions
    print(f"Box dimensions: {x} x {y} x {z}")

    for j in range(idx + 1, n):
      other_box = boxes[j]
      other_dim = list(map(int, other_box.split(',')))
      ox, oy, oz = other_dim

      # euclidean distance squared
      dist_sq = (x - ox) ** 2 + (y - oy) ** 2 + (z - oz) ** 2
      if hp_size >= 1000:
        biggest = -max_heap[0][0]
        if dist_sq < biggest:
          heapq.heappop(max_heap)
          heapq.heappush(max_heap, (-dist_sq, (box, other_box)))

      else:
        heapq.heappush(max_heap, (-dist_sq, (box, other_box)))
        hp_size += 1

  # keep track of connected boxes
  parent = {}
  def find(box):
    if parent.get(box, box) != box:
      parent[box] = find(parent[box])
    return parent.get(box, box)
  
  while max_heap:
    dist_sq_neg, (box1, box2) = heapq.heappop(max_heap)
    dist_sq = -dist_sq_neg
    root1 = find(box1)
    root2 = find(box2)
    if root1 != root2:
      parent[root2] = root1

  # find the size of the biggest three connected components
  component_size = {}
  for box in boxes:
    root = find(box)
    component_size[root] = component_size.get(root, 0) + 1
  largest_sizes = sorted(component_size.values(), reverse=True)[:3]

  res = 1
  for size in largest_sizes:
    res *= size

  print(f"Part One: {res}")

def part_two(boxes, n):
  part_two_ans = 0

  min_heap = []

  for idx, box in enumerate(boxes):
    dimensions = list(map(int, box.split(',')))
    x, y, z = dimensions
    print(f"Box dimensions: {x} x {y} x {z}")

    for j in range(idx + 1, n):
      other_box = boxes[j]
      other_dim = list(map(int, other_box.split(',')))
      ox, oy, oz = other_dim

      # euclidean distance squared
      dist_sq = (x - ox) ** 2 + (y - oy) ** 2 + (z - oz) ** 2
      heapq.heappush(min_heap, (dist_sq, (box, other_box)))

  # keep track of connected
  parent = {}
  def find(box):
    if parent.get(box, box) != box:
      parent[box] = find(parent[box])
    return parent.get(box, box)
  
  connections = 0
  while min_heap:
    dist_sq_neg, (box1, box2) = heapq.heappop(min_heap)
    dist_sq = -dist_sq_neg
    root1 = find(box1)
    root2 = find(box2)
    if root1 != root2:
      parent[root2] = root1
      connections += 1
      component_size = {}
      for box in boxes:
        root = find(box)
        component_size[root] = component_size.get(root, 0) + 1
      largest_sizes = sorted(component_size.values(), reverse=True)[0]
      if largest_sizes == n:
        last_x = box1
        last_x_2 = box2
        x_coord = list(map(int, last_x.split(',')))[0]
        x_coord_2 = list(map(int, last_x_2.split(',')))[0]
        part_two_ans = x_coord * x_coord_2
        break
  print(f"Part Two: {part_two_ans}")


def main():
  boxes = read_input()
  n = len(boxes)

  part_one(boxes, n)
  part_two(boxes, n)
  
if __name__ == "__main__":
  main()
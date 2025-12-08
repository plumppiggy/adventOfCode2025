import heapq

def read_input():
  with open("input.txt", "r") as f:
    return f.read().strip().split("\n")
  

def main():
  boxes = read_input()
  n = len(boxes)

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

  res = 0

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


      

if __name__ == "__main__":
  main()
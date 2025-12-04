def read_input():
  with open("test.txt") as f:
    return f.read().strip().split("\n")
  
def count_rolls(graph, n, m):
  remove = []
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        cnt = 0
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in neighbours:
          x, y = i + dx, j + dy

          if 0 <= x < n and 0 <= y < m and graph[x][y] == 1:
            cnt += 1

        if cnt < 4:
          remove.append((i, j))

  return remove

def main():
  rows = read_input()
  part_one = 0
  part_two = 0

  n = len(rows)
  m = len(rows[0])

  graph = [[0 for _ in range(m)] for _ in range(n)]

  for i in range(n):
    for j in range(m):
      graph[i][j] = 0 if rows[i][j] == '.' else 1

  print(graph)
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        cnt = 0
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in neighbours:
          x, y = i + dx, j + dy

          if 0 <= x < n and 0 <= y < m and graph[x][y] == 1:
            cnt += 1

        if cnt < 4:
          part_one += 1

  print("Part one:", part_one)

  remove = count_rolls(graph, n, m)
  while remove:
    for i, j in remove:
      part_two += 1
      graph[i][j] = 0

    remove = count_rolls(graph, n, m)

  print("Part two:", part_two)

  


  



if __name__ == "__main__":
  main()
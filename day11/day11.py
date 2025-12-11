def read_input():
  with open("input.txt", "r") as f:
    return f.read().strip()
  

def main():
  data = read_input()

  part_one_ans = 0
  graph = []

  for line in data.splitlines():
    src = line.split(':')[0]
    dsts = line.split(':')[1].strip().split(' ')
    graph.append((src, dsts))

  src = "you"
  memo = {"out": 1}
  def dfs(node):
    if node in memo:
      return memo[node]
    memo[node] = sum([dfs(child) for child in dict(graph)[node]])
    return memo[node]

  part_one_ans = dfs(src)
  print("Part One:", part_one_ans)

if __name__ == "__main__":
  main()
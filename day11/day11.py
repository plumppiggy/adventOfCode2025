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

  src = "svr"
  memo2 = {}
  # keep track of paths, have to go to fft and dac and end up at out
  def dfs2(node):
    if node[0] == "out": 
      return 1 if node[1] and node[2] else 0
    if node in memo2:
      return memo2[node]
    memo2[node] = 0
    for child in dict(graph)[node[0]]:
      has_fft = node[1] or (child == "fft")
      has_dac = node[2] or (child == "dac")
      memo2[node] += dfs2((child, has_fft, has_dac))

    return memo2[node]
    
  part_two_ans = dfs2((src, False, False))
  print("Part Two:", part_two_ans)
  
if __name__ == "__main__":
  main()
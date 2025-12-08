def read_input():
  with open("input.txt", "r") as f:
    return f.read().strip().split("\n")


def main():
  lines = read_input()
  n = len(lines)
  m = len(lines[0]) if n > 0 else 0

  beam = [0 for _ in range(m)]
  grid = [list(line) for line in lines]

  part_one_ans = 0
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 'S':
        beam[j] = 1
      if grid[i][j] == '^':
        if beam[j] == 1:
          part_one_ans += 1
          beam[j] = 0
        if j - 1 >= 0:
          beam[j-1] = 1
        if j + 1 < m:
          beam[j+1] = 1

  print(f"Part One: {part_one_ans}")

  day_two_ans = 0
  memo = {}

  def dfs(i, j):
    if (i, j) in memo:
      return memo[(i, j)]
    
    if i >= n:
      return 1 # end
    
    ans = 0
    if grid[i][j] == '^':
      ans += dfs(i, j + 1) + dfs(i, j-1)

    else:
      ans += dfs(i + 1, j)

    memo[(i, j)] = ans
    return ans
  
  beam = grid[0].index('S')
  day_two_ans = dfs(0, beam)
  print(f"Part Two: {day_two_ans}")


if __name__ == "__main__":
  main()
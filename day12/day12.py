def read_input():
  with open("input.txt", "r") as f:
    return f.read().strip()


def main():
  lines = read_input()

  part_one_ans = 0

  grids = [line for line in lines.split("\n") if 'x' in line]
  
  for grid in grids:
    g = [int(n) for n in grid.strip().replace('x', ' ').replace(":", '').split()]
    res = sum(g[2:]) * 9 <= g[0] * g[1]
    if res:
      part_one_ans += 1

  print("Part One:", part_one_ans)


if __name__ == "__main__":
  main()
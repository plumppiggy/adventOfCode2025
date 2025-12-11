from collections import deque

def read_input():
  with open("input.txt", "r") as f:
    return f.read().strip()

def bfs(indicator, buttons):
  seen = set()
  queue = deque([(0, 0)])

  while queue:
    state, cnt = queue.popleft()
    if state not in seen:
      if state == indicator:
        return cnt
      seen.add(state)
      cnt += 1
      for b in buttons:
        next_state = state ^ b
        queue.append((next_state, cnt))

  return None

def main():
  data = read_input()

  machines = []
  part_one_ans = 0

  for line in data.splitlines():
    indicator = line.split(" ")[0]
    binary = indicator.strip("[]").replace("#", "1").replace(".", "0")
    # reverse
    binary = binary[::-1]
    number = int(binary, 2)

    button_str = line.split(" ")[1:-1]
    buttons = []
    for btn in button_str:
      pos = btn.strip("()").split(",")
      pos = [int(p) for p in pos]

      num = 0
      for p in pos:
        num |= (1 << p)
      buttons.append(num)

    machines.append((number, buttons))

  for machine in machines:
    ans = bfs(machine[0], machine[1])
    part_one_ans += ans if ans is not None else 0

  print("Part One:", part_one_ans)

if __name__ == "__main__":
  main()
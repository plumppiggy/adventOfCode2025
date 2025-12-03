def read_input():
  with open("input.txt") as f:
    return f.read().strip().split("\n")
  
def get_max_idx(line, start, end):
  max_s = -1
  max_idx = -1
  for i in range(start, end):
    battery = int(line[i])
    if battery > max_s:
      max_s = battery
      max_idx = i

  return max_idx

def largest_twelve(bank):
  n = len(bank)
  skip = n - 12

  res = []
  start = 0

  for i in range(12):
    remaining = 12 - i - 1
    end = n - remaining

    max_digit = -1
    max_idx = -1

    for j in range(start, end):
      digit = int(bank[j])
      if digit > max_digit:
        max_digit = digit
        max_idx = j

    res.append(bank[max_idx])
    start = max_idx + 1

  return int("".join(res))


def main():
  banks = read_input()
  part_one = 0
  part_two = 0

  for bank in banks:
    print(bank)
    n = len(bank)
    p1 = get_max_idx(bank, 0, n - 1)
    p2 = get_max_idx(bank, p1 + 1, n)

    part_one += 10 * int(bank[p1]) + int(bank[p2])
    part_two += largest_twelve(bank)

  print("Part one:", part_one)
  print("Part two:", part_two)


if __name__ == "__main__":
  main()
  
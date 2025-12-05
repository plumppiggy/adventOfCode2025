def read_input():
  with open("input.txt") as f:
    content = f.read()

  parts = content.strip().split("\n\n")
  text = parts[0]
  ranges = []
  for line in text.split("\n"):
    start, end = line.split("-")
    ranges.append((int(start), int(end)))

  text = parts[1]
  ids = [int(line) for line in text.split("\n")]

  return ranges, ids

def is_in_ranges(num, merged_range):
  l, r = 0, len(merged_range) - 1
  while l <= r:
    mid = (l + r) // 2
    start, end = merged_range[mid]
    if start <= num <= end:
      return True
    elif num < start:
      r = mid - 1
    else:
      l = mid + 1

  return False

def merge_ranges(ranges):
  if not ranges:
    return []
  
  ranges.sort()
  merged = [ranges[0]]

  for start, end in ranges[1:]:
    last_start, last_end = merged[-1]
    if start <= last_end + 1:
      merged[-1] = (last_start, max(last_end, end))
    else:
      merged.append((start, end))

  return merged

def main():
  ranges, ids = read_input()
  merged_range = merge_ranges(ranges)

  part_one_ans = 0

  for id in ids:
    if is_in_ranges(id, merged_range):
      part_one_ans += 1

  print("Part one:", part_one_ans)

  part_two_ans = 0
  
  for start, end in merged_range:
    part_two_ans += end - start + 1

  print("Part two:", part_two_ans)


if __name__ == "__main__":
  main()
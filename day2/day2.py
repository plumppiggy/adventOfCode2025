def read_input():
  with open("input.txt") as f:
    return f.read().strip().split(",")
  
def is_invalid_id_pt2(num):
  s = str(num)
  n = len(s)

  for i in range(1, n // 2 + 1):
    if n % i == 0:
      pattern = s[:i]

      if pattern[0] == '0':
        continue

      reps = n // i
      if reps >= 2 and pattern * reps == s:
        return True
      
  return False
  
def is_invalid_id(num):
  s = str(num)
  n = len(s)

  if n % 2 == 0:
    mid = n // 2
    first_half = s[:mid]
    second_half = s[mid:]

    return first_half == second_half and first_half[0] != '0'
  

def main():
  ids = read_input()
  part_one_ans = 0
  part_two_ans = 0
  print(ids)
  for id in ids:
    start = id.split("-")[0]
    end = id.split("-")[1]
    print(f"Start: {start}, End: {end}")

    for num in range(int(start), int(end) + 1):
      if is_invalid_id(num):
        part_one_ans += num

      if is_invalid_id_pt2(num):
        part_two_ans += num


  print("Part one:", part_one_ans)
  print("Part two:", part_two_ans)


if __name__ == "__main__":
  main()
def read_input():
  with open("input.txt", "r") as f:
    return f.read().strip().split("\n")


def main():
  text_lines = read_input()
  lines = [line.strip() for line in text_lines if line.strip()]
  print(f"Number of lines: {len(lines)}")

  for idx, line in enumerate(lines):
    print(line)
    nums = line.split()
    print(f"Numbers in line: {nums}")
    lines[idx] = nums
  

  day_one_ans = 0

  for i in range(len(lines[0])):
    symbol = lines[4][i]
    if symbol == "+":
      for j in range(4):
        print( lines[j][i])
        day_one_ans += int(lines[j][i])
    elif symbol == "*":
      product = 1
      for j in range(4):
        product *= int(lines[j][i])
      day_one_ans += product

  print(f"Day 1 Answer: {day_one_ans}")



if __name__ == "__main__":
  main()
def read_input():
  file = "input.txt"
  with open(file, "r") as f:
    data = f.read().splitlines()

  return data


def main():
  input = read_input()
  print(input)

  part_one = 0
  part_two = 0
  pos = 50 

  for line in input:
    number = int(line[1:])

    if line[0] == "L":
      part_two += abs(pos - number) // 100 + (pos != 0 and pos <= number)
      pos = (pos - number) % 100

    else:
      part_two += (pos + number) // 100
      pos = (pos + number) % 100

    if pos == 0:
      part_one += 1

  print("Part one:", part_one) 
  print("Part two:", part_two)

if __name__ == "__main__":
  main()
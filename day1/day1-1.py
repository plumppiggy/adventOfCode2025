def read_input():
  file = "input.txt"
  with open(file, "r") as f:
    data = f.read().splitlines()

  return data


def main():
  input = read_input()
  print(input)

  cnt = 0
  pos = 50 

  for line in input:
    number = int(line[1:])

    if line[0] == "L":
      cnt += abs(pos - number) // 100 + (pos != 0 and pos <= number)
      pos = (pos - number) % 100

    else:
      cnt += (pos + number) // 100
      pos = (pos + number) % 100



  print(f"Count: {cnt}")

if __name__ == "__main__":
  main()
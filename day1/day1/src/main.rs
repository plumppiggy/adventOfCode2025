use std::fs;


fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed");
    let lines: Vec<&str> = input.lines().collect();

    for line in &lines {
        println!("{}", line);
    }

    let mut part_one = 0;
    let mut part_two = 0;
    let mut pos = 50;

    for line in &lines {
        let direction = line.chars().nth(0).unwrap();
        let number: i32 = line[1..].parse().unwrap();

        if direction == 'L' {
            part_two += (pos - number).abs() / 100 + if pos != 0 && pos <= number {1} else {0};
            pos = (pos - number).rem_euclid(100);
        } else {
            part_two += (pos + number) / 100;
            pos = (pos + number).rem_euclid(100);
        }

        if pos == 0 {
            part_one += 1;
        }

    }

    println!("Part one: {}", part_one);
    println!("Part two: {}", part_two);
}

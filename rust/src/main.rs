mod two_sums;

fn main() {
    let numbers = vec![3, 2, 4];
    let target: i32 = 6;
    two_sums::two_sums(numbers, target);
    println!("Hello, world!");
}

fn main() {
    let mut x = 5; // x is a mutable variable, it's type cannot be changed
    x += 6;

    let y = 4;  // assign y to 4
    let y = y + 4; // You can reassign values (with different types) with another let statment

    // Data types
    // Ints
    // 8 bit    | i8   | u8
    // 16 bit   | i16  | u16
    // 32 bit   | i32  | u32
    // 64 bit   | i64  | u64
    // 128 bit  | i128 | u128
    // arch     | isize| usize (Based on os)

    // Number literals
    // Decimal  | 100_000
    // Hex      | 0xff
    // Octal    | 0o77
    // Binary   | 0b1111_0000
    // Byte     | b'A' (u8 only)

    // Char types exist and are denoted with single quotes
    let d = 'a';
    let heart_eyed_cat = '😻'; // Also emoji work

    // Tuple type; which is a fixed-length collection
    let tup = (500, 6.4, 1);
    let (a, b, c) = tup; // Can unpack values
    let five_hundred = tup.0; // Grab the first value of tup

    // Array type; fixed-length, and fixed-type
    let months: [&str; 12] = ["January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"];

    let set_of_threes = [3;5]; // Initialize a 5 element array with all values set to 3
    let first = set_of_threes[1]; // Access using index

    // Continue from 3.3; https://doc.rust-lang.org/book/ch03-03-how-functions-work.html

    // To return from a loop assign a variable to the loop statement then specify the return value after the break
    let mut counter = 1;
    let result = loop{
        counter += 1;
        if counter == 10{
            break counter;
        }
    };
    println!("Counter value is {}", counter);

    // Iterate through a collection using collection.iter()
    for month in months.iter(){
        println!("Current month is {}", month);
    };

    // x..y is used to yield a range of [x, y)
    for number in 1..11{
        println!("Current number is {}", number);
    };

    // You can reverse the range like this
    for number in (1..11).rev(){
        println!("Current number is {}", number);
    };

}
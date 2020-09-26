fn main() {
    println!("Hello, world!");
    let s = String::from("hello world");

    let hello = &s[..5]; // Get the value of s at index 0 to index 4
    let world = &s[6..]; // Get the value of s at index 6 to the end

    // For parameters using &str is better because it allows String & str types
    // Since you can pass in a full string as a slice
}

fn first_word(s: &String) -> &str { //Takes in a reference to a string and returns a string slice
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

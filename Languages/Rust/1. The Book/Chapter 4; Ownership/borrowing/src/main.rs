fn main() {
    println!("Hello, world!");
    // & are used to denote references, which allow you to borrowing the variable value 
    // instead of taking ownership of the whole variable

    let s1 = String::from("hello");

    // Just a reference to "Hello" is passed, but s1 is still owned by main()
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);

    // Borrowing allows you to read a value but not modify it to modify it, you need a mutable reference
    // See add_last_name() for an example of a mutable reference

    let mut name = String::from("Kieran");
    add_last_name(&mut name); // Pass a mutable reference of name
    println!("Name is now {}", name);

    // // This code will error because only one mutable reference to a variable IN THE SAME SCOPE is allowed
    // let mut s = String::from("hello");

    // let r1 = &mut s;
    // let r2 = &mut s;

    // println!("{}, {}", r1, r2);

    // You can have multiple mutable references in different scopes, such as this
    let mut s = String::from("hello");

    {
        let r1 = &mut s;
    } // r1 goes out of scope here, so we can make a new reference with no problems.

    let r2 = &mut s;


}

/// Takes in a reference to a string and returns it's length as a usize
fn calculate_length(s: &String) -> usize { 
    s.len()
}

fn add_last_name(some_string: &mut String) {
    some_string.push_str(" Wood");
}

// // Example of a dangling pointer error that won't compile in rust
// fn dangle() -> &String {
//     let s = String::from("hello");

//     &s // Can't be returned because it will disapear in this scope
// }
fn main() {
    println!("Hello, world!");

    // A mutable string type
    let mut name = String::from("Kieran");

    name.push_str(" Wood"); // Append Wood to the end of name
    println!("{}", name);

    // // This code errors out because s1 is borrowed by s2 and therefore is no longer a valid variable
    // let s1 = String::from("hello");
    // let s2 = s1;

    // println!("{}, world!", s1);

    // To clone data you would need to use the clone() method
    let s1 = String::from("hello");
    let s2 = s1.clone();

    // Copy types are able to be assigned to multiple variables without issue

    // Here is the list of Copy types
    // All integers, booleans, floating points, char, tuples with only other Copy types

}

fn takes_ownership(some_string: String) { // some_string comes into scope
    println!("{}", some_string);
} // Here, some_string goes out of scope and `drop` is called. The backing memory is freed.

fn makes_copy(some_integer: i32) { // some_integer comes into scope
    println!("{}", some_integer);
} // Here, some_integer goes out of scope. Nothing special happens.

fn gives_ownership() -> String {             
    // gives_ownership will move its return value into the function that calls it

    let some_string = String::from("hello"); // some_string comes into scope

    some_string  // some_string is returned and moves out to the calling function
}

// takes_and_gives_back will take a String and return one
fn takes_and_gives_back(a_string: String) -> String { 
    // a_string comes into scope
    a_string  // a_string is returned and moves out to the calling function
}

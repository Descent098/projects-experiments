

fn main() {
    // =========== Vectors ===========

    // Vectors only contain one type, but an unspecified number of values
    let mut v: Vec<i32> = Vec::new();

    // You can instantiate a vector without type specification if you have a starting value
    let _q = vec![1, 2, 3];

    // You can push values onto a vector, which appends them to the end
    v.push(5);
    v.push(6);
    v.push(7);
    v.push(8);

    // You can access the vector in one of two ways
    let third: &i32 = &v[2]; // Using a index accessor
    println!("The third element is {}", third);

    match v.get(2) { // Using a match to deal with potential None types
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element."),
    }

    // Iteration over values
    for i in &v {
        println!("Current iteration value is {}", i);
    }

    // Mutable iteration over values
    for i in &mut v {
        *i += 50;
    }
    println!("After mutable changes vector is {:#?}", v);

    // You can get around the type limitations of vectors with enums
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let _row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];

    // =========== String ===========

    let mut s = String::new();

    let data = "initial contents";

    let s = data.to_string(); // Convert string literal to a String

    // The method also works on a literal directly
    let s = "initial contents".to_string();

    // String::From() and "".to_srting() are the same

    // Can add to a string using str.push_str()
    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(s2);
    println!("s2 is {}", s2);

    // Can also concatenate using +
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let _s3 = s1 + &s2; // note s1 has been moved here and can no longer be used

    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let _s = s1 + "-" + &s2 + "-" + &s3;

    // Can also use format!
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let _s = format!("{}-{}-{}", s1, s2, s3);

    // Iterating over strings
    for c in "नमस्ते".chars() {
        println!("{}", c);
    }

    for b in "नमस्ते".bytes() {
        println!("{}", b); // Byte value representations
    }

    // =========== HashMap ===========
    use std::collections::HashMap;

    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    scores.insert(String::from("Yellow"), 20);

    // Accessing scores based on team name
    let team_name = String::from("Blue");
    let score = scores.get(&team_name);

    let mut jobs = HashMap::new();

    jobs.insert(String::from("James"), String::from("Researcher"));
    jobs.insert(String::from("Becca"), String::from("Secretary"));
    jobs.insert(String::from("Terry"), String::from("Forklift Operator"));

    println!("Jobs: {:#?}", jobs);

    // Iterating a Hash Map
    println!("Jobs Iteration:");
    for (key, value) in &jobs {
        println!("\tName: {} \n\tJob: {}", key, value);
    }
    jobs.get("James");

    // Conditionally insert values if value is empty
    scores.entry(String::from("Orange")).or_insert(50);
    scores.entry(String::from("Blue")).or_insert(50); // Already exists
    println!("Orange value is: {:?}\nBlue value is: {:?}", &scores.get("Orange"),  &scores.get("Blue"));

    // Conditional update; Creating a counter loop for word frequency
    let text = "hello world wonderful world";

    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1; // Dereferences count
    }

    println!("{:?}", map);
    
}


// ========== Generics ==========
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

// Is conditionally implemented assuming the T type used in pair has both Display and PartialOrd implmeneted
impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}

fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

// // Single generic type struct
// struct Point<T> { // This says the struct is generic for T in all places, meaning x and y MUST be the same type, but can be any type
//     x: T,
//     y: T,
// }

// Multi Generic type struct
struct Point<T, U> {    // x and y can be any types
    x: T,
    y: U,
}

impl<T, U> Point<T, U> {
    fn x(&self) -> &T {
        &self.x
    }
}

impl Point<f32, f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}



// =============== Traits ============

pub trait Summary { // A trait with a defualt implementation
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}

pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }

}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}

pub fn notify(item: &impl Summary) { // This function accepts any types that implement Summary
    println!("Breaking news! {}", item.summarize());
}

// // Uses a trait bound, which allows us to force both types to be the same, but also any type that implments summary
// pub fn notify<T: Summary>(item1: &T, item2: &T) {}

// // You can specify multiple trait bounds with + 
// pub fn notify(item: &(impl Summary + Display)) {}

// // You can make a complex function with lots of trait bounds like this:
// fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {}
// //Much simpler, like this:
// fn some_function<T, U>(t: &T, u: &U) -> i32
//     where T: Display + Clone,
//           U: Clone + Debug
// {

// Specifies a function returns a type that implements Summary. Note you can only return one type this way
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}


// ============ Lifetimes =============

// The lifetime anotation of 'a here specifies the lifetime lasts for all 'a values (The scope the function was called from)
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
struct ImportantExcerpt<'a> {
    part: &'a str, // The ImportantExcerpt instance can't outlive it's part param
}


impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }

    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {}", announcement);
        self.part
    }
}

// It is possible to specify a global lifetime using 'static which is a program lifetime for the entire runtime


fn main() {

    // ========== Generics ==========
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };

     // ========== Traits ==========
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());

    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {}", result);

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {}", result);

    // ========== Lifetimes ==========
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let _i = ImportantExcerpt { // The exerpt, and it's part attribute are created within the same lifetime, making it valid.
        part: first_sentence,
    };
}
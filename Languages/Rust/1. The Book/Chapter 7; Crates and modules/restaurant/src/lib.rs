mod front_of_house; // Import front_of_house.rs

// This re-exports the scope and allows use of this scope from your crate
pub use crate::front_of_house::hosting;

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        super::serve_order(); // Goes up a layer in module tree to get serve_order()
    }

    fn cook_order() {

    }

    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }

    pub enum Appetizer {
        Soup,
        Salad,
    }
}

fn serve_order() {}

// The idiomatic way to bring in a module scope for methods see 78 for better way
// use crate::front_of_house::hosting;

// For structs and enums bring in the full path
use std::collections::HashMap;

// This is the exception to the enum/struct convention, when you have two of the same named structs/enums from different packages
// use std::fmt;
// use std::io;

// fn function1() -> fmt::Result {
//     // --snip--
// }

// fn function2() -> io::Result<()> {
//     // --snip--
// }


// You can shorten imports from the same crate, for example this:
// use std::cmp::Ordering;
// use std::io;
// Can become:
use std::{cmp::Ordering, io};

// Globbed paths also work
use std::collections::*;

pub fn eat_at_restaurant() {
    // Order a breakfast in the summer with Rye toast
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // Change our mind about what bread we'd like
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // The next line won't compile if we uncomment it; we're not allowed
    // to see or modify the seasonal fruit that comes with the meal
    // meal.seasonal_fruit = String::from("blueberries");

    // Can be accessed because Appetizer is public
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;

    // Can be done because of line 61
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
}
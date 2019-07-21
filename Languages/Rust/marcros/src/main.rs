
//! # Macros
//! This is the documentation for the overall file
//! Note there is also a macro:
//! 
//! ### shout_name
//! ## Purpose:
//! Takes the argument provided and prints 'Hello, $name!' with the name capitalized for emphasis.
//! ## Arguments:
//! name; a String with the name to print
//! ```
//! macro_rules! shout_name {($name:expr) => {
//! print!("Hey, {}!", $name.to_uppercase());
//!   }
//!}
//! ```
use std::io;


macro_rules! shout_name {($name:expr) => {
    print!("Hey, {}!", $name.to_uppercase());
        }
    }



/** ## Purpose:
Reads user input from stdin and passes given parameter to print_name
*/
pub fn get_name(){
    println!("Gimme your name: ");
    let mut name = String::new();

    io::stdin().read_line(&mut name)
        .expect("That's not a name fam");

    shout_name!(name)
}

/** The main function, runs the get_name function
 */
pub fn main() {
    get_name()
    
}
//! # Chapter 14
//!
//! Two slashes and an exclamation point ```//!``` indicate a
//! crate level docstring to outline the high level details 
//! about a crate

use more_cargo::kinds::PrimaryColor;

/// Adds one to the number given.
///
/// # Examples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```
pub fn add_one(x: i32) -> i32 {
    x + 1
}

/// Triple slashes ```///``` indicate docstrings that can be written
/// in markdown and generated as docs using ```cargo doc --open```
fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
}

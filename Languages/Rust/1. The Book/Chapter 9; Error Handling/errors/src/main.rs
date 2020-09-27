// A note about Panic!
// By default, when a panic occurs, the program starts unwinding, which means Rust walks back up the stack and cleans up
// the data from each function it encounters. But this walking back and cleanup is a lot of work. The alternative is to 
// immediately abort, which ends the program without cleaning up. Memory that the program was using will then need to be 
// cleaned up by the operating system. If in your project you need to make the resulting binary as small as possible, you 
// can switch from unwinding to aborting upon a panic by adding panic = 'abort' to the appropriate [profile] sections in your Cargo.toml file. 
// For example, if you want to abort on panic in release mode, add this:
// [profile.release]
// panic = 'abort'

// For a full traceback use ```RUST_BACKTRACE=1 cargo run```

use std::fs::File;
use std::io;
use std::io::Read;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");

    let _f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() { // Catch general error and match for specific error kinds
            ErrorKind::NotFound => match File::create("hello.txt") { // On NotFound errors, create new file
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e), // Panic if it can't be created
            },
            other_error => { // Other errors just give up and panic
                panic!("Problem opening the file: {:?}", other_error)
            }
        },
    };

    let _f = File::open("hello.txt").unwrap(); // Instead of matching, if value is Ok will return value, if not then panics
    let _f = File::open("hello.txt").expect("Failed to open hello.txt"); // Same as unwrap but let's us specify panic! message

    panic!("crash and burn"); // Will kill the program
}

fn read_username_from_file() -> Result<String, io::Error> { // Might throw an error, so include it in Result return typing
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    // // This can be written more consisely
    // match f.read_to_string(&mut s) {
    //     Ok(_) => Ok(s),
    //     Err(e) => Err(e),
    // }

    // This is equivalent to lines 50-54
    f.read_to_string(&mut s)?;
    Ok(s)
}

// This is an even shorter implementation of read_username_from_file using 2 questionmarks on line 65
fn short_read_username_from_file() -> Result<String, io::Error> {
    let mut s = String::new();

    File::open("hello.txt")?.read_to_string(&mut s)?;

    Ok(s)
}

// // You can use ? in main if you assign it's return type to a result like this:
// fn main() -> Result<(), Box<dyn Error>> {
//     let f = File::open("hello.txt")?;

//     Ok(())
// }

// Error checking in types
pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 || value > 100 { // Panics if input value of Guess::new() is not 1 < value < 100
            panic!("Guess value must be between 1 and 100, got {}.", value);
        }

        Guess { value }
    }

    pub fn value(&self) -> i32 {
        self.value
    }
}
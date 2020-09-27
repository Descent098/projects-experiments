// You can organize tests into a tests directory, details here: https://doc.rust-lang.org/book/ch11-03-test-organization.html#the-tests-directory

// Test optional flags
// Can run with ```cargo test RUST_BACKTRACE=1```
// If tests use share state, you can force them to run in squence with ```cargo test -- --test-threads=1```
// You can show the sys.stdout output using ```cargo test -- --show-output```
// You can run individual tests using ```cargo test <function name>```
// You can specify to run all tests with name match, such as all tests with "add" using ```cargo test add```
// You can specify to only run ignored tests ```cargo test -- --ignored```

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

pub fn add_two(a: i32) -> i32 {
    a + 2
}

pub fn greeting(name: &str) -> String {
    format!("Hello {}!", name)
}

pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Guess value must be between 1 and 100, got {}.", value);
        }

        Guess { value }
    }
}

// You can test private functions directly
pub fn add_two_func(a: i32) -> i32 {
    internal_adder(a, 2) // Call to private function
}

// Private function
fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

// Tests can use two assertion types assert_eq! and assert_ne!

// #[cfg(test)] states to only run this code during testing
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    use super::*; // Bring Rectangle into module scope

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(larger.can_hold(&smaller));
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }

    
    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{}`", // Custom failure message
            result
        );
    }

    // Checking for Panics with should_panic
    #[test]
    #[should_panic]
    fn greater_than_100() {
        Guess::new(200);
    }

    // Testing the output error message is correct
    #[test]
    #[should_panic(expected = "Guess value must be between 1 and 100, got 200.")]
    fn greater_than_100_2() {
        Guess::new(200);
    }

    // Can use a Result with an Err to fail a test instead of assert statements
    #[test]
    fn it_works_2() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }

    // You can specify tests to ignore
    #[test]
    #[ignore]
    fn expensive_test() {
        // code that takes an hour to run
    }

    // Run private function, so long as it's in scope
    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }

}


use std::io;            // Used to deal with input and output
use rand::Rng;          // Used to generate random numbers
use std::cmp::Ordering; // Used to compare values

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    loop{
        println!("Please input your guess.");
        
        let mut guess = String::new(); // Initialize guess variable

        io::stdin()
            .read_line(&mut guess) // Read input to guess variable
            .expect("Failed to read line"); // Handle exceptions

        // Convert string guess to a u32
        let guess: u32 = match guess.trim().parse(){
            // Does error checking through match
            Ok(num) => num,
            Err(_) => continue,    
        };

        println!("You guessed: {}", guess);

        // Compare secret number to guess
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
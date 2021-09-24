use std::io;

enum Coin{
    Penny,
    Nickle,
    Dime,
    Quarter,
    Loonie,
    Toonie,
}

impl Coin{
    fn to_string(&self)-> &str{
        match self{
            Coin::Penny => "Penny",
            Coin::Nickle => "Nickle",
            Coin::Dime => "Dime",
            Coin::Quarter => "Quarter",
            Coin::Loonie => "Loonie",
            Coin::Toonie => "Toonie",
        }
    }

    fn to_int(&self)-> u8{
        match self{
            Coin::Penny => 1,
            Coin::Nickle => 5,
            Coin::Dime => 10,
            Coin::Quarter => 25,
            Coin::Loonie => 100,
            Coin::Toonie => 200,
        }
    }
}

fn main() {
    let penny = Coin::Penny;
    println!("Coin is a {}, and is worth {}", penny.to_string(), penny.to_int());
}

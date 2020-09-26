struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

// derive allows us to print using {:?} or {:#?}
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle{
    fn area(&self) -> u32{
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    // Associated function to create an instance of a rectangle that's a square
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}

fn main() {
    println!("Hello, world!");

    // Instantiate a user struct instance
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };

    // Instantiate another instance with values from user1
    let user2 = User {
        email: String::from("another@example.com"),
        username: String::from("anotherusername567"),
        ..user1 // Copies remaining values from user1
    };

    // You can use tuples as pseudo structs
    struct Color(i32, i32, i32);
    let black = Color(0,0,0);

    // Struct use with function
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("Rect 1 is {:#?}", rect1);

    println!("The area of rect 1 is {}", rect1.area());

    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}

// Function taking custom struct as param
fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

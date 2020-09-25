# File basics

## Pure Rust files

Rust files have the ```.rs``` extension. Once you write a file you can opt to compile it using ```rustc <file>.rs``` then run the resulting binary.

## Cargo

Here are the steps for setting up a cargo package:

1. Create new crate using ```cargo new <name>```
2. cd into ```/<name>```
3. To check if your code is compile able run ```cargo check```
4. Run using ```cargo run```
5. Alternately to compile use ```cargo build``` then run the resulting binary
6. When ready for release run ```cargo build --release``` to build with optimizations
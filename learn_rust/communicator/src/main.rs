extern crate communicator;

use std::collections::HashMap;

fn main() {
    // let s1 = String::from("Either the well is\
    // very deep, or she fell very slowly");

    // let mut h1 = HashMap::new();

    // for word in s1.split_whitespace() {
    //     let value = h1.entry(word).or_insert(0);
    //     *value += 1;
    // }

    // println!("{:?}", h1);
    let number_list = vec![12, 42, 23, 43, 44];
    largest(&number_list);

    fn largest<T>(list: &[T]) -> T {
        let mut largest = list[0];
            for &number in list {
                if number > largest {
                    largest = number;
                }
            }
        println!("the largest number is {:?}", largest);
        largest
    }
}
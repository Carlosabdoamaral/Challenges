//
//  FizzBuzz.swift
//  Challenges
//
//  Created by Carlos Amaral on 29/12/21.
//

import Foundation

func FizzBuzz(x: Int) -> Int {
    if x % 3 == 0 && x % 5 == 0 {
        print("FizzBuzz")
    }
    else if x % 3 == 0 {
        print("Fizz")
    }
    else if x % 5 == 0 {
        print("Buzz")
    }
    else {
        print(x)
    }
    
    return 0
}

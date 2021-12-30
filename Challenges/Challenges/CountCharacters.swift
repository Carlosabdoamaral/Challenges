//
//  CountCharacters.swift
//  Challenges
//
//  Created by Carlos Amaral on 29/12/21.
//

import Foundation

func CountCharacters(input : String) -> Int {
    var i : Int = 0
    
    for letter in input {
        i += 1
    }
    
    print(i)
    return i
}

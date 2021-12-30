//
//  RandomNumber.swift
//  Challenges
//
//  Created by Carlos Amaral on 29/12/21.
//

import Foundation

func RandomNumber(max : Int, min : Int) -> Int {
    print(Int(arc4random_uniform(UInt32(max - min + 1))) + min)
    return Int(arc4random_uniform(UInt32(max - min + 1))) + min
}

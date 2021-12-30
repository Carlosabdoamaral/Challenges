//
//  Swap.swift
//  Challenges
//
//  Created by Carlos Amaral on 29/12/21.
//

import Foundation

func SwapNumbers(x : Int, y : Int) -> Int {
    var a : Int = x
    var b : Int = y
    print(swap(&a, &b))
    return 0    
}

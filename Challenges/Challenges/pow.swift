//
//  pow.swift
//  Challenges
//
//  Created by Carlos Amaral on 29/12/21.
//

import Foundation

func MyPow(x: Int, y:Int) -> Int {
    
    guard x > 0, y > 0 else { return 0 }
    var v = x
    for _ in 1..<y {
        v *= x
    }
    
    print(v)
    return v
}

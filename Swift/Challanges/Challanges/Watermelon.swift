//
//  Watermelon.swift
//  Challanges
//
//  Created by Carlos Amaral on 19/12/21.
//  https://codeforces.com/problemset/problem/4/A
//

import Foundation

func Watermelon() {
    if let x : Int = Int(readLine()!) {
        if x <= 0 || x >= 100 {
            return
        } else {
            if (x%2) == 0 {
                print("YES")
            } else {
                print("NO")
            }
        }
    }
}

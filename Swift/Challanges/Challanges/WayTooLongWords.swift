//
//  WayTooLongWords.swift
//  Challanges
//
//  Created by Carlos Amaral on 19/12/21.
//  https://codeforces.com/problemset/problem/71/A
//

import Foundation

func WayTooLongWords() {
    var words : [String] = []
    
    var i = 0
    if var x = Int(readLine()!) {
        while i < x {
            let s : String = String(readLine()!)
            let qtd : Int = s.count - 2
            let first = s.prefix(1)
            let last = s.suffix(1)
            let all = "\(first)\(qtd)\(last)"
            words.append(all)
            i = i + 1
        }
    }
    
    print(words)
}

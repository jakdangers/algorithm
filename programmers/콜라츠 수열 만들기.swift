import Foundation

func solution(_ n:Int) -> [Int] {
   	var res: [Int] = []
   	var x = n

   	res.append(x)
    while x != 1 {
        if x % 2 == 0 {
            x = x / 2
        } else {
            x = 3 * x + 1
        }
        res.append(x)
    }

    return res
}
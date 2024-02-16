import Foundation

func solution(_ rny_string:String) -> String {
   	var res = ""

    for c in rny_string {
        if c == "m" {
            res += String("r")
            res += String("n")
        } else {
            res += String(c)
        }

    }

    return res
}
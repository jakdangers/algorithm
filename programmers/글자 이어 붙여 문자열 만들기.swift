import Foundation

func solution(_ my_string:String, _ index_list:[Int]) -> String {
    var res = ""

    for idx in index_list {
        var curr = my_string.index(my_string.startIndex, offsetBy: idx)
        res += String(my_string[curr])
    }

    return res
}
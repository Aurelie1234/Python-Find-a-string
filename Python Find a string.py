count = 0
    for i in range (len(string)):
        count += string.count(sub_string, i , len(sub_string)+i)
    return count

def longest_unique_substring(text):
    test_str = text
    res = [test_str[i: j] for i in range(len(test_str))
            for j in range(i + 1, len(test_str) + 1)]
    
    resNoRepeat = [i for i in res if len(set(i)) == len(i)]
    
    return len(max(resNoRepeat,key=len))
    
#https://iq.opengenus.org/prefix-table-lps/
def calc_lps(s):
    prefix = [0]
    i = 1
    j = 0
    
    while len(prefix) < len(s):
        if s[i] == s[j]:
            i += 1
            j += 1
            prefix.append(j)
        else:
            if j == 0:
                prefix.append(0)
                i += 1
            if j != 0:
                j = prefix[j-1]

    return prefix

#https://towardsdatascience.com/pattern-search-with-the-knuth-morris-pratt-kmp-algorithm-8562407dba5b
def kmp(string, search):
    lps = calc_lps(search)
    matched = []
    j = 0
        
    for i in range(len(string)):
        while j != 0 and search[j] != string[i]:
            j = lps[j-1]

        if j == len(lps) - 1:
            matched.append(i - j)
            j = lps[j]

        if string[i] == search[j]:
            j += 1

    if matched:
        return matched
    else:
        return [-1] 

def search_n_print(string, search):
    print()
    print(f"Input: {string}")
    print(f"Looking for: '{search}'")
    print("Using algorithm: kmp")

    matched = kmp(string, search)
    for index in matched:
        print("Pattern found at index: ", index)

string = "This is a CMPSC 412 lab course. Students take this course along with CMPSC 462"

search_n_print(string, "CMPSC")
search_n_print(string, "course")
search_n_print("AABAACAADAABAABAABBBBBAAABDCBA", "BBBBBA")

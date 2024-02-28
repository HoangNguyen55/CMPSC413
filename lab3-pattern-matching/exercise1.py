def native_search_string(s, w):
    matched_index = []

    for n in range(len(s)):
        i = n
        matched = True
        for j in range(len(w)):
            i += 1
            if (n+len(w) > len(s)) or (s[i] != w[j]):
                matched = False
                break

        if matched:
            matched_index.append(i - len(w) + 1)

    if matched_index:
        return matched_index
    else:
        return [ -1 ]

def search_n_print(string, search):
    print()
    print(f"Input: {string}")
    print(f"Looking for: '{search}'")
    print("Using algorithm: native_search_string")

    matched = native_search_string(string, search)
    for index in matched:
        print("Pattern found at index: ", index)

string = "This is a CMPSC 412 lab course. Students take this course along with CMPSC 462"

search_n_print(string, "CMPSC")
search_n_print(string, "course")
search_n_print("AABAACAADAABAABAABBBBBAAABDCBA", "BBBBBA")

import re

with open("input.txt", "r") as f:
    # Read number of regular expressions
    n = int(f.readline().strip())

    # Read regular expressions and compile them
    regex_list = []
    for i in range(n):
        regex_list.append(re.compile(f.readline().strip()))

    # Read number of strings
    m = int(f.readline().strip())

    # Match strings against regular expressions
    for i in range(m):
        string = f.readline().strip()
        matches = []
        for j, regex in enumerate(regex_list):
            if regex.search(string):
                matches.append(j+1)
        if matches:
            print("YES, {}".format(matches[0]))
        else:
            print("NO, 0")

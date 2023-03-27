import re

# Read the input file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Regular expression pattern to match method name and parameter list
pattern = r'(\w+)\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)\s*'

# Find all matches of the pattern in the input text

matches = re.findall(pattern, input_text)
# Extract method names and parameter list from the matches
methods = []
print("Methods: ")
for x in matches:
    if x[0] == 'new':
        continue
    if x[1] == 'main':
        continue

    print("{}".format(x[1])+" ({}".format(x[2])+"),"+" return type: {}".format(x[0]))
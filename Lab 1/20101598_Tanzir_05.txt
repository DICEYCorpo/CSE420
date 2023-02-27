import re

def lexical_analyzer():
    f = ([line.strip() for line in open("lab1.txt")])
    temp = ""
    for i in f:
        temp += i
    keywords = ['if', 'else', 'while', 'for', 'int', 'float', 'char', 'double', 'return']
    math_operators = ['+', '-', '*', '/', '%', '=']
    logical_operators = ['&&', '||', '!', '<', '>', '==']
    symbol_table = {}

    tokens = re.findall(r'\b\w+\b|[+\-*/%=<>!&|(){},;]', temp)
    index = 0
    caution = False
    for token in tokens:
        if token in keywords:
            if 'Keyword' not in symbol_table:
                symbol_table['Keyword'] = [token]
            elif token not in symbol_table['Keyword']:
                symbol_table['Keyword'].append(token)
        elif token in math_operators:
            if 'Math Operator' not in symbol_table:
                symbol_table['Math Operator'] = [token]
            elif token not in symbol_table['Math Operator']:
                symbol_table['Math Operator'].append(token)
        elif token in logical_operators:
            if 'Logical Operator' not in symbol_table:
                symbol_table['Logical Operator'] = [token]
            elif token not in symbol_table['Logical Operator']:
                symbol_table['Logical Operator'].append(token)
        elif token.isdigit():
            temp = tokens[index + 1]
            if 'Numerical Value' not in symbol_table:
                symbol_table['Numerical Value'] = []
            if (token not in symbol_table['Numerical Value']):
                if caution == False:
                    if temp.isdigit():
                        symbol_table['Numerical Value'].append(token+"."+temp)
                        caution = True
                    else:
                        symbol_table['Numerical Value'].append(token)
            elif (token in symbol_table['Numerical Value']) and temp.isdigit():
                symbol_table['Numerical Value'].append(token+"."+temp)
                caution = True
            else:
                caution = False
        elif re.match(r'\b\w+\b', token):
            if 'Identifier' not in symbol_table:
                symbol_table['Identifier'] = [token]
            elif token not in symbol_table['Identifier']:
                symbol_table['Identifier'].append(token)
        else:
            if 'Others' not in symbol_table:
                symbol_table['Others'] = [token]
            elif token not in symbol_table['Others']:
                symbol_table['Others'].append(token)
        index += 1



    return symbol_table

symbol_table = lexical_analyzer()
for i, j in symbol_table.items():
    if i == "Others":
        print(i + " :", end=" ")
        for k in j:
            print(k, end=" ")
        print()
    else:
        print(i + " :", end=" ")
        print(*j, sep=" , ")



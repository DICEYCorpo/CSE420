



def web(str):
    state = 0
    checker = False
    for i in range (0, len(str)):
        if state == 0:
            if str[i] == 'w':
                state = 1
            else:
                break
        elif state == 1:
            if str[i] == 'w':
                state = 2
            else:
                break
        elif state == 2:
            if str[i] == 'w':
                state = 3
            else:
                break
        elif state == 3:
            if str[i] == '.':
                state = 4
            else:
                break
        elif state == 4:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122:
                state = 5
            else:
                break

        elif state == 5:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122 or 48 <= ord(str[i]) <= 57:
                state = 5

            elif str[i] == '.':
                state = 6
            else:
                break

        elif state == 6:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122 or 48 <= ord(str[i]) <= 57:
                state = 6
                checker = True
            elif str[i] == '.' or str[i] == '/':
                state = 7
                checker = False
            else:
                break

        elif state == 7:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122 or 48 <= ord(str[i]) <= 57:
                state = 7
                checker = True
            else:
                checker = False
                break

        i += 1
    return checker

def mail(str):
    state = 0
    email = False
    for i in range (0, len(str)):
        if state == 0:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122:
                state = 1
            else:
                break

        elif state == 1:
            if (65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122 or 48 <= ord(str[i]) <= 57):
                state = 1
            elif str[i] == '@':
                state = 2
            else:
                break

        elif state == 2:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122:
                state = 2
            elif str[i] == '.':
                state = 3
            else:
                break


        elif state == 3:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122:
                state = 3
                email = True
            elif str[i] == '.':
                state = 4
                email = False
            else:
                break


        elif state == 4:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122:
                state = 4
                email = True
            elif str[i] == '.':
                state = 5
                email = False
            else:
                break


        elif state == 5:
            if 65 <= ord(str[i]) <= 90 or 97 <= ord(str[i]) <= 122:
                state = 5
                email = True
            else:
                email = False
                break
        i += 1
    return email
def main():
    with open("input.txt", "r") as rf:
        inp = int(rf.readline())

        line = 1
        while line <= inp:
            stringg = rf.readline().strip()
            if web(stringg):
                print("Website, "+ str(line))
            elif mail(stringg):
                print("Mail, "+str(line))
            line += 1


main()
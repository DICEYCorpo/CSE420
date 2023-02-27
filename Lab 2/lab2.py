



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
            if str[i] == 'c':
                state = 7
            else:
                break

        elif state == 7:
            if str[i] == 'o':
                state = 8
            else:
                break

        elif state == 8:
            if str[i] == 'm':
                checker = True
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
            if str[i] == 'c':
                state = 4
            else:
                break

        elif state == 4:
            if str[i] == 'o':
                state = 5
            else:
                break

        elif state == 5:
            if str[i] == 'm':
                email = True
                state = 0
            else:
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
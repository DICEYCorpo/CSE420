def switch_case(argument):
    switcher = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five"
    }
    return switcher.get(argument, "Invalid choice")

# example usage
choice = 7
result = switch_case(choice)
print(result)

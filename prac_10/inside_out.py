def inside_out(phrase):

    # if len(phrase) == 1:
    #     return phrase
    # elif phrase == "":
    #     return phrase

    if len(phrase) <= 1:
        return phrase
    return phrase[0] + phrase[-1] + inside_out(phrase[1:-1])  # Returns string objects


print(inside_out("programming"))  # Odd amount
print(inside_out("programs"))  # Even amount
print(inside_out("a"))
print(inside_out(""))
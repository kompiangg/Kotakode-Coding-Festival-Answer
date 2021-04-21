def hurufBergantian(inputString):
    output = 0
    for i in range(len(inputString) - 1):
        if inputString[i] is inputString[i + 1]: output += 1
    return output
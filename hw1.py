def intToRoman(num):
    dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    s = ""
    if type(num) is not int:
        print("Please Input an Integer")
        return -1

    if type(num) is float:
        print("Please Input an Integer Rather Than a Float")
        return -1

    if num<0:
        print("Please Input a Number Bigger Than Zero")
        return -1

    for k in dict:
        if (num // k) != 0:
            count = num // k
            num %= k
            s += dict[k] * count
    return s

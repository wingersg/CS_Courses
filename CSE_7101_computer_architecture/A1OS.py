# A1OS.py - a python program to convert:
# 1. an integer to hexadecimal
# 2. an integer to binary
# 3. a binary to integer
# SMU ID:47502277
# Name: Zhengwen Zhang
# Class: CSE 7101

def main():
    # TEST: intToHex - test with an integer
    x = 175
    expected = 'AF'
    actual = intToHex(x)

    if expected == actual:
        print("intToHex : PASSED")
    else:
        print("intToHex :  FAILED,expected = " + expected +
              ",Actual = " + actual +
              ",Parameter=" + str(x))

    # TEST: intToBinary - test with an integer
    x = 213
    expected = '0000000011010101'
    actual = intToBinary(x)

    if expected == actual:
        print("intToBinary : PASSED")
    else:
        print("intToBinary :  FAILED,expected = " + expected +
              ",Actual = " + actual +
              ",Parameter=" + str(x))

    # TEST: binaryToInt - test with a binary
    x = '1010100000000010'
    expected = 43010
    actual = binaryToInt(x)

    if expected == actual:
        print("binaryToInt : PASSED")
    else:
        print("binaryToInt :  FAILED,expected = " +
              str(expected) + ",Actual = " +
              str(actual) + ",Parameter=" + x)


def intToHex(x):
    # create a list of characters to be used in hexadecimal
    slist = ['A', 'B', 'C', 'D', 'E', 'F']
    # find the hex value on the left
    if x/16 >= 10:
        hexvalue1 = slist[x/16 - 10]
    else:
        hexvalue1 = str(x/16)
    # find the hex value on the right
    if x % 16 >= 10:
            hexvalue2 = slist[x%16 - 10]
    else:
            hexvalue2 = str(x%16)

    hexvalue = hexvalue1+hexvalue2
    return hexvalue

def intToBinary(x):
    # create a list of sixteen zeros
    # replace 0 with 1 when the modulo is not 0
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(15,-1,-1):
        if x < 2**i:
            list[15-i] = 0
        else:
            x = x%2**i
            list[15-i] = 1
    result = ''.join(str(e) for e in list)
    return result

def binaryToInt(x):
    x = str(x)
    n = len(x)
    # use for loop to get the sum of from left to right
    result = 0
    for i in range(n):
        # a is the binary data
        # b is 2's exponential value at a
        a = int(x[i])
        b = 2**(n-1-i)
        result +=a*b
    return result


if __name__ == "__main__":
    main()

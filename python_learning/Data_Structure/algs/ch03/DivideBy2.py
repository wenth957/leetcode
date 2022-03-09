from Stack import Stack


def DivideBy2(dec_num):
    remstack = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        remstack.push(rem)
        dec_num = dec_num // 2
    bin_str = ""
    while not remstack.isEmpty():
        bin_str = bin_str + str(remstack.pop())
    return bin_str


def baseConverter(dec_num, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while dec_num > 0:
        rem = dec_num % base
        remstack.push(rem)
        dec_num = dec_num // base
    new_str = ""
    while not remstack.isEmpty():
        new_str = new_str + digits[remstack.pop()]

    return new_str


if __name__ == "__main__":
    print(DivideBy2(233))
    print(baseConverter(233, 16))

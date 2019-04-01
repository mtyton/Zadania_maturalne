#  for serious it's 59


#  all
def read_file():
    """
    Simply reads given file
    :return:
    """
    numbs = []
    file = open("liczby.txt", "r")
    for line in file.readlines():
        numbs.append(int(line.strip()))
    return numbs


#  1 - invoke this method
def to_primals(numb):
    """
    :param numb:
    :return:
    """
    dividor = 3
    used = []
    if numb % 2 == 0:
        return False
    while numb > 1:
        if numb % dividor == 0:
            if dividor not in used:
                used.append(dividor)
            numb /= dividor
        else:
            dividor += 2
        if len(used) > 3:
            return False
    if len(used) == 3:
        return True
    else:
        return False


#  2 - invoke this method
def pali_sum(numb):
    """
    Checks if sum of number and reversed number is a palindrome
    :param numb:
    :return:
    """
    rnumb = rev(numb)
    score = numb + rnumb
    rscore = rev(score)
    if score == rscore:
        return True
    else:
        return False


#  2
def rev(numb):

    """
    simply reverse given number
    :param numb:
    :return:
    """
    text_numb = str(numb)
    rev_text = "".join(reversed(text_numb))
    return int(rev_text)


#  3 - invoke this method
def count_power(numbs):
    """
    Using algorithm from task 3 checks if
    :param numbs:
    :return:
    """
    powers = [0, 0, 0, 0, 0, 0, 0, 0]
    single_powers = []
    for numb in numbs:
        power = 1
        digits = to_digits(numb)
        score = multiplier(digits)
        while score > 9:
            power += 1
            digits = to_digits(score)
            score = multiplier(digits)
        if power in range(1, 9):
            powers[power-1] += 1
        if power == 1:
            single_powers.append(numb)
    print(powers, max(single_powers), min(single_powers))


#  3
def multiplier(digits):
    """
    multiplies every digit in a number
    :param digits:
    :return:
    """
    score = 1
    for dig in digits:
        score *= dig
    return score


#  3
def to_digits(numb):
    """
    changes number in a list of digits
    :param numb:
    :return:
    """
    digits = []
    while numb > 1:
        digits.append(numb % 10)
        numb = int(numb/10)
    return digits


if __name__ == "__main__":
    numbs = read_file()
    iterator = 0
    count_power(numbs)
    print("end")

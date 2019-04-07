def read_file():
    """
    simply reads data from file
    :return:
    """
    file=open("dane_ulamki.txt")
    counters, denominators = [], []
    for line in file.readlines():
        line = line.rstrip()
        counter, divider = line.split(" ")
        counters.append(int(counter))
        denominators.append(int(divider))
    file.close()
    return counters, denominators


# task 65.1
def count_min(counters, denominators):
    """
    Counts the smallest value of fractions
    :param counters:
    :param denominators:
    :return:
    """
    scores = []
    dividors_min, counters_min = [], []
    minimum = counters[0] / denominators[0]
    for x in range(1, len(counters)):
        score = counters[x] / denominators[x]
        if score < minimum:
            scores = []
            dividors_min, counters_min = [], []
            dividors_min.append(denominators[x])
            counters_min.append(counters[x])
            scores.append(score)
            minimum = score
        elif score == minimum:
            dividors_min.append(denominators[x])
            counters_min.append(counters[x])
            scores.append(score)
    print(scores, dividors_min, counters_min)

#task 65.2
def reduced(counters, denominators):
    """
    checks if the fraction is in the reduced form
    :param counters:
    :param denominators:
    :return:
    """
    iterator = 0
    for x in range(1, len(counters)):
        if nwd(counters[x], denominators[x]) == 1:
            iterator+=1
    print(iterator)
    
#task 65.3
def reduce(counters, denominators):
    """
    simply reduce the fraction
    :param counters:
    :param denominators:
    :return:
    """
    score = 0
    for x in range(1, len(counters)):
        highest_dividor = nwd(counters[x], denominators[x])
        score += counters[x]/highest_dividor
    print(score)
    
##task 65.2
def nwd(number, second_number):
    """
    counts greatest common divisor in polish (nwd)
    :param number:
    :param second_number:
    :return:
    """
    while second_number!=0:
        number, second_number = second_number, number%second_number
    #print(number, second_number)
    return number


#task 65.3
def summary(counters, denominators):
    """
    :param counters:
    :param denominators:
    :return:
    """
    score=0
    shared_dividor = (2**2)*(3**2)*(5**2)*(7**2)*13
    for x in range(len(counters)):
        score+= shared_dividor * counters[x] / denominators[x]
    print(score)


if __name__ == "__main__":
    counters, dividers = read_file()
    #count_min(counters,dividers)
    reduced(counters,dividers)
    reduce(counters,dividers)
    summary(counters, dividers)
    

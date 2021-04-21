# isogram = input("Which word would you like to test for being an isogram? ").lower()

def iso_test(word):
    isogram = word.replace(" ", "").replace("-", "")
    if isogram and len(set(isogram)) == len(isogram) or len(word) == 0:
        return True
    else:
        return False


def iso_test2(string):

    for item in string:
        if string.count(item) > 1:
            return False
        elif string.count(" ") > 1 or string.count("-") > 1:
            return True
        else:
            pass
    return True



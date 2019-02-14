def fizzbuzz(a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        return "Invalid input"

    newlist = a+b
    Ownlist = len(newlist)

    if(Ownlist % 5 == 0 and Ownlist % 3 == 0):
        return "fizzbuzz"

    if (Ownlist % 5 == 0):
        return "buzz"

    if (Ownlist % 3 == 0):
        return "fizz"

    return len(newlist)
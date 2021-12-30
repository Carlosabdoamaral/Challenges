def WayTooLongWords():
    x = int(input("Linhas"))
    arr = []
    i = 0

    while i < x :
        word = str(input())
        size = len(word)
        word = f"{word[0]}{size - 2}{word[-1]}"

        arr.append(word)
        i += 1

    print(*arr)
    return arr

WayTooLongWords()
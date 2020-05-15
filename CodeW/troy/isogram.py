def is_isogram(string):
    word = "swetha"
    le = len(word)
    for i in range(0, le - 1):
        if word[i] not in word[i + 1:le]:
            return True
            continue
        else:
            return False
            break


if is_isogram(str) == True:
    print(str,' is an isogram')
else:
    print(str,' is NOT an isogram')
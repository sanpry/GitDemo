class Test:

    def is_isogram(self):
        str = input("please input a word: ")
        le = len(str)
        isIso = ""

        for i in range(0, le-1):
            if str[i] not in str[i +1:le]:
                isIso = "True"
                continue
            else:
                isIso = "False"
                print(str + " is NOT an isogram")
                break

        if isIso == "True":
            print(str + " is an isogram")
            return True
        else:
            return False


obj = Test()
print(obj.is_isogram())
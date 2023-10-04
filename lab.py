def finddouble(s):

    dict = {}

    for letter in s:
        if letter in dict:
            return letter
        if letter not in dict:
            dict[f"{letter}"] = 1
    return None

print(finddouble("DBCABA"))

dict = {
    "": ,
    "": ,
    "": ,
    "": ,
    "": ,
    "": ,
    "":
}
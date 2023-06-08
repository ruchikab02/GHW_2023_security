import re
def passwordCheck(str):
    isMinLength = False
    hasSpecialChar = False
    hasNumber = False
    hasLower = False
    hasUpper = False
    # check length
    minLength = 12
    if len(str) >= minLength:
        isMinLength = True
    x = re.search("[a-z]", str)
    if x:
        hasLower = True
    x = re.search("[A-Z]", str)
    if x:
        hasUpper = True
    x = re.search("[0-9]", str)
    if x:
        hasNumber = True
    x = re.search("[\.\+\*\?\^\$\(\)\[\]\{\}\|#%@!&]", str)
    if x:
        hasSpecialChar = True
    if isMinLength and hasSpecialChar and hasNumber and hasLower and hasUpper:
        return ("Strong password")
    elif isMinLength and hasLower and hasUpper and hasNumber and not hasSpecialChar:
        return ("Medium. Needs at least one special character.")
    elif isMinLength and hasUpper and hasLower:
        return ("Medium. Needs at least one number.")
    elif isMinLength and hasLower:
        return ("Medium. Needs at least one uppercase letter.")
    elif isMinLength and not hasLower:
        return ("Medium. Needs at least one lowercase letter.")
    else:
        return ("Poor. Needs at least twelve letters.")



if __name__ == "__main__":
    p1 = "hiweoriwflaAkdjfoaisdfGAhgaio2567"
    p2 = ""
    p3 = "hiweoriwflaAkdjfoaisdfGAhgaio2567!"
    p4 = "aaaaaaa"
    p5 = "AAAAAA"
    p5 = "$$$@#%"
    password = "abcdefghijklmnopqrstuvwxyz"
    l = [p1, p2, p3, p4, p5, password]
    for el in l:
        print(passwordCheck(el))
    
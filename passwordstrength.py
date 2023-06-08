import re
def passwordCheck(str):
    isMinLength = False
    hasSpecialChar = False
    hasNumber = False
    hasLower = False
    hasUpper = False
    # check length
    minLength = 12
    if len(str) >= 12:
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
    x = re.search("[\.\+\*\?\^\$\(\)\[\]\{\}\|]", str)
    if x:
        hasSpecialChar = True
    if isMinLength and hasSpecialChar and hasNumber and hasLower and hasUpper:
        return ("Strong password")
    elif isMinLength and hasLower and hasUpper and hasNumber:
        return ("Medium. Needs at least one special character.")
    elif isMinLength and hasUpper and hasLower:
        return ("Medium. Needs at least one number.")
    elif isMinLength and hasLower:
        return ("Medium. Needs at least one uppercase letter.")
    elif isMinLength and not hasLower:
        return ("Medium. Needs at least one lowercase letter.")
    else:
        return ("Poor. Needs at least six letters.")



if __name__ == "__main__":
    password = "abcdefghijklmnopqrstuvwxyz"
    check = passwordCheck(password)
    print(check)
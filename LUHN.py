def menu():
    print("Welcome to ABC credit card company")

goon = ""

def creditcardformat(card):
    # Non-digits in card (anything not digit or '-')
    for checkfornondigit in card:
        if not (checkfornondigit.isdigit() or checkfornondigit == "-"):
            return False, "Non digits in card"

    # Too many / too few tokens (count tokens by counting dashes)
    tokens = 1
    for countdash in card:
        if countdash == "-":
            tokens += 1

    if tokens > 4:
        return False, "Too many tokens !"
    if tokens < 4:
        return False, "Too few tokens !"

    # Must be exact length 19 for xxxx-xxxx-xxxx-xxxx
    if len(card) != 19:
        return False, "Invalid length"

    # Dashes must be exactly at positions 4, 9, 14 and everything else digits
    for position, checkofcc in enumerate(card):
        if position in (4, 9, 14):
            if checkofcc != "-":
                return False, "Invalid length"
        else:
            if not checkofcc.isdigit():
                return False, "Non digits in card"
    return True, "OK"

def userinput(userinputqn):
    while goon != "T":
        userinput = input(userinputqn).upper()
        ok, errormsg = creditcardformat(userinput)
        if userinput == "TERMINATE":
            return "T"
        if ok:
            return userinput
        print(errormsg)

# removing of -
def removingofdash(creditcardinfo):
    creditcardinfo = creditcardinfo.replace("-", " ")
    return creditcardinfo

# Reversing the credit card
def creditcardrev(creditcardinfo):

    result = ""
    groupof4 = ""

    for checkdash in creditcardinfo:
        if checkdash == "-":
            result += groupof4[::-1] + "-"
            groupof4 = ""
        else:
            groupof4 += checkdash

    # reverse the last group
    result += groupof4[::-1]

    return result
    # print(result)

def find2ndand4thplacement(creditcard):
    result = ""
    positionoftoken = 1 # position inside each token

    for checkdigit in removingofdash(creditcard):
        if checkdigit.isdigit():
            digit = int(checkdigit)

            # even position
            if positionoftoken % 2 == 0:          
                result += str(digit * 2)
            else: 
                result += checkdigit

            positionoftoken += 1
        else:
            # space or dash → reset position for next token
            result += checkdigit
            positionoftoken = 1

    return result

def token_sums(transformed):
    token_sum = 0
    outputofeachcctoken = ""

    for checkifdigit in transformed:
        if checkifdigit.isdigit():
            token_sum += int(checkifdigit)
        else:
            # end of token
            outputofeachcctoken += str(token_sum) + " "
            token_sum = 0

    # last token
    outputofeachcctoken += str(token_sum)

    return outputofeachcctoken

def sumofstring(token_sum_string):
    total = 0
    current = ""

    for checkifdigit in token_sum_string:
        if checkifdigit.isdigit():
            current += checkifdigit
        else:
            total += int(current)
            current = ""

    # add last number
    total += int(current)

    return total

def is_valid(total):
    return total % 10 == 0

def conclusionvalidornotvalid(reversedcc, creditcardtotalsum):
    start = 5
    if is_valid == True:
        print(f"{'':>{start}} {reversedcc} is a valid credit card because {creditcardtotalsum} % 10 = 0")
    else:
        print(f"{'':>{start}} {reversedcc} is a valid credit card because {creditcardtotalsum} % 10 != 0")

def Analysis(reversedcc):
    start = 5
    end = 5

    userinputofcc = removingofdash(reversedcc)
    cc2ndand4thplacementtimes2 = find2ndand4thplacement(ccreversed)
    theadded4tokens = token_sums(find2ndand4thplacement(ccreversed))
    thetotalsumofall4tokens = sumofstring(token_sums(find2ndand4thplacement(ccreversed)))

    print("Analysis: \n")
    print(f"{'(a)':>{start}} To get the reverse of each 4 digit\n {'':>{end}}{userinputofcc}")
    print(f"{'(b)':>{start}} To multiply by 2 of each even digit pattern\n {'':>{end}}{cc2ndand4thplacementtimes2}")
    print(f"{'(c)':>{start}} To get the sum of all digits in card elements\n {'':>{end}}{theadded4tokens}")
    print(f"{'(d)':>{start}} To find the sum of all elements in card\n {'':>{end}} This special sum is {thetotalsumofall4tokens}")

    print("Conclusion: ")
    conclusionvalidornotvalid(reversedcc, thetotalsumofall4tokens)

def continuationofcc():
    while True:
        userinput = input("Another card (y/Y/n/N): ").upper()
        if userinput == "Y":
            break
        if userinput == "N":
            return "T"
        else:
            print("Enter a valid input !")

while goon != "T":
    menu()
    usercc = userinput("Enter a credit card: ")
    if usercc == "T":
        exit()

    else: 
        ccreversed = creditcardrev(usercc)
        Analysis(ccreversed)
        goon = continuationofcc()

# 2323-2005-7766-3554
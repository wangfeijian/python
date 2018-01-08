def check_str(str):
    bracket_front = ['(', '[', '{']
    bracket_end = [')', ']', '}']
    dict_bracket = {"(":")", "[":"]", "{":"}"}
    bracket = []
    for i in str:
        if i in bracket_front:
            bracket.append(i)
        elif i in bracket_end:
            if i == dict_bracket[bracket[-1]]:
                bracket.pop()
            else:
                break
        #print(bracket)
    #print(bracket)
    if len(bracket) > 0:
        print(False)
    else:
        print(True)

check_str("(((([[[{{{3}}}]]]]))))")
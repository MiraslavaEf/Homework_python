def tc(args, p="left", l=100, s='-'):
    if p == "center":
        p = "^"
    elif p == "right":
        p = ">"
    else:
        print("Wrong position, position is _default left_")
        p = "<"
    return ''.join([("{0:%s%s%ss}" % (s, p, str(l))).format(c) for c in args])


print(tc(open("top_words.txt", 'r').readlines(), "center", 110, "^"))
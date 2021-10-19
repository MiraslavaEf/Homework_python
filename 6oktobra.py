def p():
    d = {}
    while True:
        print('введите свое имя(для выхода нажмите q):')
        b = input()
        if b == 'q':
            print(d)
            break
        else:
            print('введите номер:')
            a = int(input())
            d[b] = a
            if (a[0] == "+" and a[2] == "-" and a[6] == "-" and a[10] == "-" and a[13] == "-"):
            	if a[1:].replace("-","").isdigit():
            	p[b] = a
    return 0
p()

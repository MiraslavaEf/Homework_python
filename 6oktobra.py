def p():
    d = {}
    while True:
        print('введите свое имя(для выхода нажмите q):')
        b = input()
        if b == 'q':
            print(d)
            break
        else:
            a = str(input("Введите номер: "))
            if len(a) == 16:
                if (a[0] != "+" and a[1] != "7" and a[2] != "-" and a[6] != "-" and a[10] != "-" and a[13] != "-"):
                    print("Ошибка")
                    break
            else:
                print("Ошибка, введите номер в правильном формате(+7-ххх-хх-хх)")
                break          	
            d[b] = a                
    return 0
p()

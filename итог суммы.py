print('Выберите тариф: приватный или публичный(1 или 2)')
a = int(input())
if a==1:
    print('Приватный')
    def cal_parking_fee(a):
        if a<=1:
            fee1 = 15
        else:
            fee1 = a *15
        return(fee1)

    hours = int(input("Введите минуты пути автобуса: "))
    totaa_fee = cal_parking_fee(hours)
    print(totaa_fee,'руб. ')

    def cal_parking_fee(b):
        if b<= 1:
            fee2 = 23
        else:
            fee2 = b * 23
        return(fee2)

    hours = int(input("Введите минуты удалённой стоянки: "))
    totab_fee = cal_parking_fee(hours)
    print(totab_fee,'руб. ')
    def cal_parking_fee(c):
        if c<= 1:
            fee3 = 25
        else:
            fee3 = c * 25
        return(fee3)

    hours = int(input("Введите минуты  стоянки через телетрап: "))
    totac_fee = cal_parking_fee(hours)
    print(totac_fee,'руб. ')
    def cal_parking_fee(d):
        if d<= 1:
            fee4 = 30
        else:
            fee4 = d * 30
        return(fee4)

    hours = int(input("Введите минуты полёта: "))
    totad_fee = cal_parking_fee(hours)
    print(totad_fee,'руб. ')
    ob_fee =totad_fee+totac_fee+totab_fee+totaa_fee
    print('Общая стоимость: ',ob_fee, 'руб. ')
    input()


    
if a==2:
    print('Публичный')
    def cal_parking_fee(a):
        if a<=1:
            fee1 = 10
        else:
            fee1 = a *10
        return(fee1)

    hours = int(input("Введите минуты пути автобуса: "))
    totaa_fee = cal_parking_fee(hours)
    print(totaa_fee,'руб. ')

    def cal_parking_fee(b):
        if b<= 1:
            fee2 = 20
        else:
            fee2 = b * 20
        return(fee2)

    hours = int(input("Введите минуты удалённой стоянки: "))
    totab_fee = cal_parking_fee(hours)
    print(totab_fee,'руб. ')
    def cal_parking_fee(c):
        if c<= 1:
            fee3 = 25
        else:
            fee3 = c * 25
        return(fee3)

    hours = int(input("Введите минуты  стоянки через телетрап: "))
    totac_fee = cal_parking_fee(hours)
    print(totac_fee,'руб. ')
    def cal_parking_fee(d):
        if d<= 1:
            fee4 = 30
        else:
            fee4 = d * 30
        return(fee4)

    hours = int(input("Введите минуты полёта: "))
    totad_fee = cal_parking_fee(hours)
    print(totad_fee,'руб. ')
    ob_fee =totad_fee+totac_fee+totab_fee+totaa_fee
    print('Общая стоимость: ',ob_fee, 'руб. ')
    input()






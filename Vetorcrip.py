calcula_numero_da_senha = ["0110100000","1001011111","1110001010","0111010101","0011100110","1010011001","1101100100","1011010100","1001100111","1000011000"]





def calcula_numero_da_senha(senha):
    # Refazer cada string numma variavel, pegar cada elemento e add na lista

    lo1 = str(senha[0])
    l1a = []

    lo2 = str(senha[1])
    l2a = []

    lo3 = str(senha[2])
    l3a = []

    lo4 = str(senha[3])
    l4a = []

    lo5 = str(senha[4])
    l5a = []

    lo6 = str(senha[5])
    l6a = []

    lo7 = str(senha[6])
    l7a = []

    lo8 = str(senha[7])
    l8a = []

    lo9 = str(senha[8])
    l9a = []

    lo10 = str(senha[9])
    l10a = []

    for digito in lo1:
        l1a.append(digito)
    for digito in lo2:
        l2a.append(digito)
    for digito in lo3:
        l3a.append(digito)
    for digito in lo4:
        l4a.append(digito)
    for digito in lo5:
        l5a.append(digito)
    for digito in lo6:
        l6a.append(digito)
    for digito in lo7:
        l7a.append(digito)
    for digito in lo8:
        l8a.append(digito)
    for digito in lo9:
        l9a.append(digito)
    for digito in lo10:
        l10a.append(digito)

    n1 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []
    n6 = []
    n7 = []
    n8 = []
    n9 = []
    n10 = []

    if n1 == []:
        n1.append(l1a[0])
        n1.append(l2a[0])
        n1.append(l3a[0])
        n1.append(l4a[0])
        n1.append(l5a[0])
        n1.append(l6a[0])
        n1.append(l7a[0])
        n1.append(l8a[0])
        n1.append(l9a[0])
        n1.append(l10a[0])

    if n2 == []:
        n2.append(l1a[1])
        n2.append(l2a[1])
        n2.append(l3a[1])
        n2.append(l4a[1])
        n2.append(l5a[1])
        n2.append(l6a[1])
        n2.append(l7a[1])
        n2.append(l8a[1])
        n2.append(l9a[1])
        n2.append(l10a[1])

    if n3 == []:
        n3.append(l1a[2])
        n3.append(l2a[2])
        n3.append(l3a[2])
        n3.append(l4a[2])
        n3.append(l5a[2])
        n3.append(l6a[2])
        n3.append(l7a[2])
        n3.append(l8a[2])
        n3.append(l9a[2])
        n3.append(l10a[2])

    if n4 == []:
        n4.append(l1a[3])
        n4.append(l2a[3])
        n4.append(l3a[3])
        n4.append(l4a[3])
        n4.append(l5a[3])
        n4.append(l6a[3])
        n4.append(l7a[3])
        n4.append(l8a[3])
        n4.append(l9a[3])
        n4.append(l10a[3])

    if n5 == []:
        n5.append(l1a[4])
        n5.append(l2a[4])
        n5.append(l3a[4])
        n5.append(l4a[4])
        n5.append(l5a[4])
        n5.append(l6a[4])
        n5.append(l7a[4])
        n5.append(l8a[4])
        n5.append(l9a[4])
        n5.append(l10a[4])

    if n6 == []:
        n6.append(l1a[5])
        n6.append(l2a[5])
        n6.append(l3a[5])
        n6.append(l4a[5])
        n6.append(l5a[5])
        n6.append(l6a[5])
        n6.append(l7a[5])
        n6.append(l8a[5])
        n6.append(l9a[5])
        n6.append(l10a[5])

    if n7 == []:
        n7.append(l1a[6])
        n7.append(l2a[6])
        n7.append(l3a[6])
        n7.append(l4a[6])
        n7.append(l5a[6])
        n7.append(l6a[6])
        n7.append(l7a[6])
        n7.append(l8a[6])
        n7.append(l9a[6])
        n7.append(l10a[6])

    if n8 == []:
        n8.append(l1a[7])
        n8.append(l2a[7])
        n8.append(l3a[7])
        n8.append(l4a[7])
        n8.append(l5a[7])
        n8.append(l6a[7])
        n8.append(l7a[7])
        n8.append(l8a[7])
        n8.append(l9a[7])
        n8.append(l10a[7])

    if n9 == []:
        n9.append(l1a[8])
        n9.append(l2a[8])
        n9.append(l3a[8])
        n9.append(l4a[8])
        n9.append(l5a[8])
        n9.append(l6a[8])
        n9.append(l7a[8])
        n9.append(l8a[8])
        n9.append(l9a[8])
        n9.append(l10a[8])

    if n10 == []:
        n10.append(l1a[9])
        n10.append(l2a[9])
        n10.append(l3a[9])
        n10.append(l4a[9])
        n10.append(l5a[9])
        n10.append(l6a[9])
        n10.append(l7a[9])
        n10.append(l8a[9])
        n10.append(l9a[9])
        n10.append(l10a[9])

    bin_des = []

    if n1.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n2.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n3.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n4.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n5.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n6.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n7.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n8.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n9.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    if n10.count('1') >= 5:
        bin_des.append(1)
    else:
        bin_des.append(0)

    b1 = bin_des[0]
    b2 = bin_des[1]
    b3 = bin_des[2]
    b4 = bin_des[3]
    b5 = bin_des[4]
    b6 = bin_des[5]
    b7 = bin_des[6]
    b8 = bin_des[7]
    b9 = bin_des[8]
    b10 = bin_des[9]

    rs = str(b1) + str(b2) + str(b3) + str(b4) + str(b5) + str(b6) + str(b7) + str(b8) + str(b9) + str(b10)

    r = int(rs)

    n = len(str(r))

    decimal = 0
    i = 0

    while n >= 0:
        resto = r % 10
        decimal = decimal + (resto * (2 ** i))
        n = n - 1
        i = i + 1
        r = r // 10

    return decimal


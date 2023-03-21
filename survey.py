def survey():
    pyt1 = ["Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ", "Oglądanie telewizji", "Czytanie książek", "słuchanie muzyki"]
    pyt2 = ["W jakich okolicznościach czytasz książki najczęściej? ", "podczas podróży", "w czasie wolnym", "podczas pracy/nauki"]
    pyt3 = ["Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ", "chęć poszerzenia wiedzy", "czytanie to moje hobby", "czytanie mnie relaksuje"]
    pyt4 = ["Po książki w jakiej formie sięgasz najczęściej?", "papierowej", "e-booki na komputerze", "e-booki na specjalnym czytniku"]
    pyt5 = ["Ile książek czytasz średnio w ciągu roku? ", "0", "1-2", "3 lub więcej"]
    pyt6 = ["Jak często czytasz książki?", "codziennie", "raz w tygodniu", 'raz na miesiąc']
    pyt7 = ["Po jakie gatunki książek sięgasz?", "naukowe", "podróżnicze", "science fiction"]


    print(pyt1[0])
    print('1 ', pyt1[1])
    print('2 ', pyt1[2])
    print('3 ', pyt1[3])
    q1a = int(input())


    print(pyt2[0])
    print('1 ', pyt2[1])
    print('2 ', pyt2[2])
    print('3 ', pyt2[3])
    q2a = int(input())


    print(pyt3[0])
    print('1 ', pyt3[1])
    print('2 ', pyt3[2])
    print('3 ', pyt3[3])
    q3a = int(input())


    print(pyt4[0])
    print('1 ', pyt4[1])
    print('2 ', pyt4[2])
    print('3 ', pyt4[3])
    q4a = int(input())


    print(pyt5[0])
    print('1 ', pyt5[1])
    print('2 ', pyt5[2])
    print('3 ', pyt5[3])
    q5a = int(input())


    print(pyt6[0])
    print('1 ', pyt6[1])
    print('2 ', pyt6[2])
    print('3 ', pyt6[3])
    q6a = int(input())


    print(pyt7[0])
    print('1 ', pyt7[1])
    print('2 ', pyt7[2])
    print('3 ', pyt7[3])
    q7a = int(input())


    print("ODPOWIEDZI:")


    print(pyt1[0])
    print(pyt1[q1a])
    print("")


    print(pyt2[0])
    print(pyt2[q2a])
    print("")


    print(pyt3[0])
    print(pyt3[q3a])
    print("")


    print(pyt4[0])
    print(pyt4[q4a])
    print("")


    print(pyt5[0])
    print(pyt5[q5a])
    print("")


    print(pyt6[0])
    print(pyt6[q6a])
    print("")


    print(pyt7[0])
    print(pyt7[q7a])
    print("")

survey()
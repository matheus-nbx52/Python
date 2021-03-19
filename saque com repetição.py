saque = int(input())
nota = 0

while True:
    saque -= 200
    nota += 1
    if saque < 200:
        print(saque)
        print(nota)
        nota = 0

        if saque == 0:
            break

        while True:
            saque -= 100
            nota += 1
            if saque < 100:
                print(saque)
                print(nota)
                nota = 0

                while True:
                    saque -= 50
                    nota += 1
                    if saque < 50:
                        print(saque)
                        print(nota)
                        nota = 0

                        while True:
                            saque -= 20
                            nota += 1
                            if saque < 20:
                                print(saque)
                                print(nota)
                                nota = 0

                                while True:







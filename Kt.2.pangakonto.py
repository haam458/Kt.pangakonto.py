algne_saldo = 100
print("Pangakontol on: " + str(algne_saldo) + " €")
toiming = input("Kas soovite toiminguga raha (sisse) või (välja): ")

summa = int(input("Sisestage summa: "))

while algne_saldo <= 100:
    if toiming == "sisse":
        algne_saldo += summa
        print("Kontojääk: " + str(algne_saldo) + " €")
    else:
         if toiming == "välja":
            algne_saldo -= summa
            print("Kontojääk: " + str(algne_saldo) + " €")
    toiming +=  toiming     

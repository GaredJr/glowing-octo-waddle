from termcolor import colored
import random
printArray = []



# Oppgave 1
printArray.append("Hello World")

#Oppgave 2
fetvariabel2 = 3.1415
fetvariabel1 = 86

fetutskrift = str(fetvariabel1) + " plus " + str(fetvariabel2) + " er lik " + str(fetvariabel1 + fetvariabel2)
printArray.append(fetutskrift)

#Oppgave 3
fetutskrift2 = str(fetvariabel1) + " ganger " + str(fetvariabel2) + " er lik " + str(fetvariabel1 * fetvariabel2)
printArray.append(fetutskrift2)

#Oppgave 4
fetInputString = str(input("Skriv noe kult: "))
fetutskrift3 = "Du skrev: " + fetInputString
printArray.append(fetutskrift3)

#Oppgave 5
fetInputString2 = float(input("Skriv en temperatur: "))
fetInputString3 = float(input("Skriv enda en temperatur: "))
fetInputString4 = float(input("Skriv siste temperatur: "))
fetutskrift4 = "Den gjennomsnittlige temperaturen er: " + str(round((fetInputString2 + fetInputString3 + fetInputString4) / 3))
printArray.append(fetutskrift4)

#Oppgave 6
fetTimesLonn = eval(str(input("Hva er timeslønnen din og hvor mange timer jobber du? (Skriv i format [Timeslønn * Antall Timer på jobb]) ")))
fetSkatt = float(input("Hvor mye skatter du i prosent? (f.eks 0.22 for 22%) "))
fetutskrift5 = "Din bruttolønn per dag er: " + str(fetTimesLonn) + "\n Din nettolønn per dag er: " + str(fetTimesLonn - fetTimesLonn * fetSkatt) + "\n Du betaler " + str(fetTimesLonn * fetSkatt) + " i skatt hver arbeidsdag."
printArray.append(fetutskrift5)

#Oppgave 7
printArray.append(colored("Denne oppgaven blir gjort i neste oppgave", color="yellow"))

#Oppgave 7 og 8
print("KALKULATOR!!!!")
print(colored("(+ for pluss, - for minus, / for deling, ** for eksponential)", attrs=["dark"]))
kalkulatorStr = str(input("Skriv ut regnestykket ditt her: "))
kalkulatorSum = eval(kalkulatorStr)
printArray.append(kalkulatorStr + " = " + str(kalkulatorSum))


#Oppgave 9
e = 2.71828
pi = 3.14159

if e > pi:
    printArray.append(str(e) + " > " + str(pi) + " True")
else:
    printArray.append(str(e) + " > " + str(pi) + " False")


#Oppgave 10
feteTall = [
    12.2,
    312.65,
    -42.123,
    -76.13,
    28.99,
    -199.999       
]

fetStringTilFeteTall = str("Fete Tall: " + str(feteTall) + "\nMax: " + str(max(feteTall)) + "\nMin: " + str(min(feteTall)) + "\nAbsolutt: " + str(abs(feteTall[random.randint(1, len(feteTall))])) + "\nAvrundet: " + str(round(feteTall[random.randint(1, len(feteTall))])))
printArray.append(fetStringTilFeteTall)


#Oppgave 11
brukerNavn = str(input("Hva er ditt fulle navn? "))
fetStringTilBrukerNavn = "Navnet ditt har en lengde på: " + str(len(brukerNavn))
printArray.append(fetStringTilBrukerNavn)


#Oppgave 12
if 50/3 > 20:
    printArray.append("50" + " > " + "20" + " True")
else:
    printArray.append("50" + " > " + "20" + " False")


#Oppgave 13
moduloString = "Modulo sjekker hvor mange ganger f.eks 2 går opp i 5, \n og gir det som skal til for å fullføre tallet 5.\n\n 2 går 2 ganger opp i 5, og mangler 1 for å fullføre tallet. \n 2 % 5 gir derfor 1."
printArray.append(moduloString)



#Oppgave 14
printArray.append(colored("Denne oppgaven ble gjort i tidligere oppgaver", color="yellow"))


#Oppgave 15

#printArray
printString = ""
printSeparator = colored("/==/==/==/==/==/==/==/==/", "grey")
for i in range(len(printArray)):
    printString += printSeparator + "\n" +  colored("Oppgave Nr." + str(i+1), "cyan", attrs=["bold", "underline"]) + "\n" + printArray[i] + "\n"

print(printString)


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
    12,
    312,
    -42,
    -76,
    28,
    -199       
]

fetStringTilFeteTall = str("Fete Tall: " + str(feteTall) + "\nMax: " + str(max(feteTall)) + "\nMin: " + str(min(feteTall)) + "\nAbsolutt: " + str(abs(feteTall[random.randint(1, len(feteTall))])) + "\nAvrundet: " + str(round(feteTall[random.randint(1, len(feteTall))])))
printArray.append(fetStringTilFeteTall)



#printArray
printString = ""
printSeparator = colored("/==/==/==/==/==/==/==/==/", "grey")
for i in range(len(printArray)):
    printString += printSeparator + "\n" +  colored("Oppgave Nr." + str(i+1), "cyan", attrs=["bold", "underline"]) + "\n" + printArray[i] + "\n"

print(printString)


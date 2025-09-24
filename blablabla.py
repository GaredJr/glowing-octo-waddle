from termcolor import colored
import random
import math

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

fetStringTilFeteTall = str("Fete Tall: " + str(feteTall) + "\nMax: " + str(max(feteTall)) + "\nMin: " + str(min(feteTall)) + "\nAbsolutt: " + str(abs(feteTall[random.randint(1, len(feteTall)-1)])) + "\nAvrundet: " + str(round(feteTall[random.randint(1, len(feteTall)-1)])))
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
bilerSolgt = int(input("Hvor mange biler har du solgt? "))
bonus = 0
if bilerSolgt >= 70:
    bonus = 5000

bilLonn = 500 * bilerSolgt + bonus
printArray.append(f"Du tjente {bilLonn}kr på {bilerSolgt} biler solgt, du fikk {bonus}kr i bonus.")


#Oppgave 16
printArray.append(colored("Denne oppgaven ble gjort i tidligere oppgaver", color="yellow"))


#Oppgave 17
brusOgGodis = int(input("Hvor mye penger har du til brus og godis? "))
printArray.append(f"Du kan kjøpe {round(brusOgGodis/30)} godis og {round(brusOgGodis/20)} brus med {brusOgGodis}kr.")


#Oppgave 18
nostetVariabel = 5
if nostetVariabel > 4 and nostetVariabel % 2:
    printArray.append("Partall!")
else:
    printArray.append("Hmm!")


#Oppgave 2.1
strForRange = ""
for i in range(5):
    strForRange += "Dette printes! \n"

printArray.append(strForRange)


#Oppgave 2.2
printArray.append("Boolean er en True eller False verdi. \n String er en tekstverdi. \n Integer er et helt tall. \n Float er et tall med desimaler.")


#Oppgave 2.3
whileIntBleh = 0
while whileIntBleh < 7:
    whileIntBleh += 1

printArray.append(colored("Sjekk koden", color="yellow"))


#Oppgave 2.4
whileIntBleh1 = 10
while whileIntBleh1 < 20:
    whileIntBleh1 += 1

printArray.append(colored("Sjekk koden igjen", color="yellow"))


#Oppgave 2.5
whileStrBleh = ""
whileArrayBleh = []
whiletest = True
while whileStrBleh.upper() != "EXIT" :
    whileStrBleh = str(input("Skriv exit når du vil stoppe. "))
    whileArrayBleh.append(whileStrBleh)

printArray.append(str(whileArrayBleh))


#Oppgave 2.6
printArray.append(colored("Sjekk tidligere kode", color="yellow"))

#Oppgave 2.7
printArray.append(colored("Sjekk tidligere kode", color="yellow"))


#Oppgave 2.8
forArrayTwoPointEightBleh = []
for i in range(1, 10, 2):
    forArrayTwoPointEightBleh.append(i)

printArray.append(str(forArrayTwoPointEightBleh))


#Oppgave 2.9
forArrayTwoPointNineBleh = []
for i in range(5):
    forArrayTwoPointNineBleh.append(5-i)


#Oppgave 2.10
rutenettStr = ""
rutenettRange = 9
for i in range(rutenettRange):
    rutenettStr += f" {i+1} "
    if i+1 == math.sqrt(rutenettRange) or i+1 == math.sqrt(rutenettRange) * 2:
        rutenettStr += "\n"

printArray.append(str(rutenettStr))


#Oppgave 2.11
if "e" in "Steep":
    printArray.append("Bokstaven E er i Steep")

#Oppgave 2.12
tekstGreie = "Uten mat og drikke, duger helten ikke"
vokalGreier = "aeiouyæøå"

sumVokaler = []
sumKonstonanter = []


for l in vokalGreier:
    if l in tekstGreie:
        sumVokaler.append(l)
    else:
        tekstGreie.replace(l, "")

tekstGreie.replace(" ", "")
tekstGreie.replace(",", "")
for i in tekstGreie:
    if i not in sumKonstonanter:
        sumKonstonanter.append(i)

printArray.append(f"Vokaler: {str(sumVokaler)}, \nKonstonanter: {str(sumKonstonanter)}")


#Oppgave 2.13
blehhh = f""

for i in range(10):
    i+=1
    if i == 6:
        continue
    blehhh += f"{i}, \n"

printArray.append(blehhh)


#Oppgave 2.14

kkj = 0
for i in range(10, 20):
    kkj += i
    if kkj >= 50:
        break

printArray.append(str(kkj))

#printArray
printString = ""
printSeparator = colored("/==/==/==/==/==/==/==/==/", "grey")
for i in range(len(printArray)):
    printString += printSeparator + "\n" +  colored("Oppgave Nr." + str(i+1), "cyan", attrs=["bold", "underline"]) + "\n" + printArray[i] + "\n"

print(printString)


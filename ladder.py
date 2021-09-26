#Imas skali,pocnuvas od 0-tata skala i treba da se iskacis do gore. Na sekoja skala ima broj napisan po red 1....n vo eden cekor mozis da skoknis ili 1 ili 2 skali, kako so
#se kacvas po sklaite gi sobiras rednite broevi za daden broj n so e brojot na skali, treba da vratis maximum suma kolku mozes da soberes. Sekoja skala ima i svoja vrednost 
#Treba da se resi so brute force, a ovaj nacin na resavanje e greedy(neraboti)
skala = [-1,2,1] 
n = len(skala)
result = 0
i = 0
a1 = skala[0]
a2 = skala[1]
while i < n:
    if a1 > 0:
        i += 1
        a1 += 1
        a2 += 1
        result += a1
    if a1 > a2:
        i += 1
        a1 += 1
        a2 += 1
        result += a1
    else:
        i += 2
        a1 += 2
        a2 += 2
        result += a2
print(result)


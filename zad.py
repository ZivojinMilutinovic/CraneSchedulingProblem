
#FINAL VERSION 1
import os



f = open('ulaz.txt','r')
f1 = open('izlaz.txt','w+')
bay1 = int(f.readline().strip())
bay2 = int(f.readline().strip())
bay3 = int(f.readline().strip())
bay4 = int(f.readline().strip())
k = int(f.readline().strip()) # pretovarni kapacitet
t = 60.0 / 25.0
qc1 = 0 # koliko je prvi kran pretovario
qc2 = 0 # koliko je drugi kran pretovario
# posto smo sortirali niz prvi kran ce da pretovaruje prvi i poslednji u nizu a drugi dva srednja
# tako postizemo medjusubni balans i dolazimo do optimalnijeg resenje
# posto se na poslednjem elementu u nizu nalazi kran sa najvecim brojem 
# mi cemo prvim kranom da uzimamo sto je vise moguce od drugog da bi se izjednacili
# kako bi izgedalo sa 2 krana i sa 4 luke koje redom imaju broj kontejnera [bay1=100,bay2=125,bay3=150,bay4=100]
# 1. korak posle sortianja [100,100,125,150]
# qc1 ce obradjivati kranove na indeksnim pozicijama 0 i 3 to jest one sa kontejnerima 100 i 150,tj bay1 i bay3
# qc2 ce obradjivati kranove na pozicijama 1 i 2 tj bay2 i bay4
# ako se ne izvrsi optimizacija prvi kran ce obraditi 250 kontejera a drugi ce obraditi 225 kontejnera
# nama je cilj da obrade sto priblizniji broj kontejnera
# tako dakle dok qc1 pretovario bay3  sa 150 kranova onda ce qc2 uzete od qc1 da pretovario bay1 sa 100 kranova 
# on treba da uzme od njega 12  da bi bio priblizno stanje nakon toga
# nakon obrade 12 kranova stanje u lukama je [88,100,138125,] , QC1 = 12 i QC2 = 12
# qc2 obradi svih 125 kranova, a qc1 obradi 125 od 138 kranova nakon toga je stanje [88,100,0,13] QC1=137 i Qc2 = 137
# QC1 obradi svih 88 dok qc2 obradi 88 od 100 posle toga je stanje [0,12,0,13] i qc1 = 225 i qc2 = 225
# nakon obrade preostalo broja kranova dosli smo do najoptimalnijeg resenja

def names_for_bays(bay1,bay2):
    if bay1.number > bay2.number:
        return [bay2.name,bay1.name]
    else:
        return [bay1.name,bay2.name]

class Bay:
    def __init__(self, number, name, capacity):
        self.number = number
        self.name = name
        self.capacity = capacity

b1 = Bay(1, "Bay1", bay1)
b2 = Bay(2, "Bay2", bay2)  
b3 = Bay(3, "Bay3", bay3)  
b4 = Bay(4, "Bay4", bay4)

arr1 = sorted([b1,b2,b3,b4], key=lambda x: x.capacity)        
arr = list(map(lambda x: x.capacity, arr1)) 


total1 = arr[0] + arr[3]
total2 = arr[1] + arr[2]


how_much_to_take = 0
name1 = ""
name2 = ""
f1.write('Stanje u lukama pre obrade Bay1 = {0}, Bay2 = {1}, Bay3 = {2}, Bay4 = {3}\n'.format(b1.capacity, b2.capacity, b3.capacity,b4.capacity))
while (total1 - how_much_to_take) > total2 + how_much_to_take and (arr[0] - how_much_to_take) > 0:
    how_much_to_take+=1
if how_much_to_take > 0:
    arr1[0].capacity -= how_much_to_take
    arr1[3].capacity -= how_much_to_take
    qc1+=how_much_to_take
    qc2+=how_much_to_take
    name1,name2 = names_for_bays(arr1[0],arr1[3])
    f1.write('Kran1 pretovario {0},Kran2 pretovario {1}\n'.format(name1,name2))
    f1.write('Stanje posle obrade Bay1 = {0}, Bay2 = {1}, Bay3 = {2}, Bay4 = {3}\n'.format(b1.capacity, b2.capacity, b3.capacity,b4.capacity))
    name1,name2 = names_for_bays(arr1[2],arr1[3])
    f1.write('Kran1 pretovario {0}, Kran2 pretovario {1}\n'.format(name1,name2))
    pom1 = arr1[2].capacity
    arr1[2].capacity = 0 
    arr1[3].capacity -= pom1
    qc1+=pom1
    qc2+=pom1
    f1.write('Stanje posle obrade Bay1 = {0}, Bay2 = {1}, Bay3 = {2}, Bay4 = {3}\n'.format(b1.capacity, b2.capacity, b3.capacity,b4.capacity))
    name1,name2 = names_for_bays(arr1[0],arr1[1])
    f1.write('Kran1 pretovario {0},Kran2 pretovario {1}\n'.format(name1,name2))
    pom1 = arr1[0].capacity
    arr1[0].capacity -= pom1
    arr1[1].capacity -= pom1
    qc1+=pom1
    qc2+=pom1
    f1.write('Stanje posle obrade Bay1 = {0}, Bay2 = {1}, Bay3 = {2}, Bay4 = {3}\n'.format(b1.capacity, b2.capacity, b3.capacity,b4.capacity))
    name1,name2 = names_for_bays(arr1[1],arr1[3])
    f1.write('Kran1 pretovario {0},Kran2 pretovario {1}\n'.format(name1,name2))
    if name1 == arr1[1].name:
        qc2+=arr1[3].capacity
        qc1+=arr1[1].capacity
    else:
        qc1+=arr1[3].capacity
        qc2+=arr1[1].capacity
    
else:
    while (total2 - how_much_to_take) > total1 + how_much_to_take and (arr[1] - how_much_to_take) > 0:
        how_much_to_take+=1
    arr1[1].capacity-=how_much_to_take
    arr1[2].capacity-=how_much_to_take
    qc1+=how_much_to_take
    qc2+=how_much_to_take
    name1,name2 = names_for_bays(arr1[1],arr1[2])
    f1.write('Kran1 pretovario {0},Kran2 pretovario {1}\n'.format(name1,name2))
    f1.write('Stanje posle obrade Bay1 = {0}, Bay2 = {1}, Bay3 = {2}, Bay4 = {3}\n'.format(b1.capacity, b2.capacity, b3.capacity,b4.capacity))
    name1,name2 = names_for_bays(arr1[0],arr1[1])
    f1.write('Kran1 pretovario {0}, Kran2 pretovario {1}\n'.format(name1,name2))
    pom1 = arr1[0].capacity
    arr1[0].capacity = 0
    arr1[1].capacity -= pom1
    qc1+=pom1
    qc2+=pom1
    f1.write('Stanje posle obrade Bay1 = {0}, Bay2 = {1}, Bay3 = {2}, Bay4 = {3}\n'.format(b1.capacity, b2.capacity, b3.capacity,b4.capacity))
    name1,name2 = names_for_bays(arr1[1],arr1[3])
    f1.write('Kran1 pretovario {0}, Kran2 pretovario {1}\n'.format(name1,name2))
    pom1 = arr1[1].capacity
    arr1[1].capacity = 0
    arr1[3].capacity -= pom1
    qc1+=pom1
    qc2+=pom1
    f1.write('Stanje posle obrade Bay1 = {0}, Bay2 = {1}, Bay3 = {2}, Bay4 = {3}\n'.format(b1.capacity, b2.capacity, b3.capacity,b4.capacity))
    name1,name2 = names_for_bays(arr1[2],arr1[3])
    f1.write('Kran1 pretovario {0}, Kran2 pretovario {1}\n'.format(name1,name2))
    if name1 == arr1[2].name:
        qc2+=arr1[3].capacity
        qc1+=arr1[2].capacity
    else:
        qc2+=arr1[2].capacity
        qc1+=arr1[3].capacity
f1.write('Kran 1 je pretovario {0}, dok je kran 2 pretovario {1}\n'.format(qc1,qc2))
total_time = (t * min([qc1,qc2]) + abs(qc1 - qc2) * t) / 60.0
f1.write('Ukupno vreme pretovarivanja {0}h'.format(total_time))
f.close()
f1.close()



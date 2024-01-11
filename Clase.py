import math

'''1. Clasa Calculator
Atribute: a, b
Constructor pentru ambele atribute
Metode:
● adunare
● scadere
● inmultire
● impartire
'''
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def adunare(self):
        return self.a + self.b
    def scadere(self):
        return self.a - self.b
    def inmultire(self):
        return self.a * self.b
    def impartire(self):
        return self.a / self.b

'''
2.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()'''
class Cerc :
    raza = None
    culoare = None
    def __init__(self,raza,culoare):
        self.raza = int(raza)
        self.culoare = culoare
    def descrie_cerc(self):
        return 'Cercul are culoarea',self.culoare,'si raza:',self.raza
    def arie_cerc(self):
        return math.pi ** self.raza
    def diametru_cerc(self):
        return 2 * self.raza
    def circumferinta_cerc(self):
        return 2 * self.raza * math.pi


'''3. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul'''
class Dreptunghi:
    lungime = None
    latime = None
    culoare = None
    def __init__(self,lungime, latime, culoare):
        self.lungime = int(lungime)
        self.latime = int(latime)
        self.culoare = culoare
    def descriere_dreptunghi(self):
        return 'Dreptunghiul are lungimea', self.lungime, ',latimea',self.latime, 'si culoarea', self.culoare

    def arie_dreptunghi(self):
        return self.lungime * self.latime

    def perimetrul_dreptunghi(self):
        return 2*(self.lungime+self.latime)

    def schimbă_culoarea_dreptunghi(noua_culoare):
        noua_culoare.culoare = 'Galben'#suprascrie atributul
        return noua_culoare

'''4. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu
● prima bianuala - salariu anual recalculare
'''

class Angajat:
    nume = None
    prenume = None
    salariu = None
    def __init__(self,nume,prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = int(salariu)

    def descriere(self):
        return 'Descriere angajat:','Numele este',self.nume,'; Prenumele :',self.prenume,';Saraiul:',self.salariu

    def nume_complet(self):
        return self.nume +' '+ self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self,marire):
        salariul_marit = marire + self.salariu
        return salariul_marit

    def prima_bianuala(prima):
        return prima.salariu_anual()


'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)'''
class Cont:
    iban = None
    titular_cont = None
    sold = None
    def __init__(self,iban,titular_cont,sold):
        self.titular_cont = str(titular_cont)
        self.iban = iban
        self.sold = int(sold)
    def afisare_cont(self):
        return 'Titularul',self.titular_cont, 'are in contul',self.iban, 'suma de',self.sold,'lei'
    def debitare_cont(self,suma_debitata):
        self.suma_debitata = int(suma_debitata)
        sold_dupa_debitare = self.sold - self.suma_debitata
        if sold_dupa_debitare < 0:
            return 'Fonduri insuficiente!'
        else:
            return sold_dupa_debitare
    def creditare_cont(self,suma_creditata):
        self.suma_debitata = int(suma_creditata)
        sold_dupa_creditare = self.sold + suma_creditata
        return sold_dupa_creditare




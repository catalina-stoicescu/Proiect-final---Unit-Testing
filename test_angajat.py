from Clase import Angajat
#1
def test_descriere():
    test = Angajat('Ion','Ionescu',20000)
    assert test.descriere() == ('Descriere angajat:','Numele este','Ion','; Prenumele :','Ionescu',';Saraiul:',20000 )
#2
def test_nume_complet():
    test = Angajat('Ion','Ionescu',20000)
    assert test.nume_complet() == ('Ion Ionescu')
#3
def test_salariul_lunar():
    test = Angajat('Ion','Ionescu',20000)
    assert test.salariu_lunar() == 20000
#4
def test_salariul_anual():
    test = Angajat('Ion','Ionescu',20000)
    assert test.salariu_anual() == 240000
#5
def test_marire_salariu():
    test = Angajat('Ion','Ionescu',20000)
    assert test.marire_salariu(2000) == 22000
#6
def test_verificare_ca_suma_primita_este_mai_mare():
    test = Angajat('Ion','Ionescu',20000)
    assert test.marire_salariu(50) > 20000
#7
def test_salariu_anual_cu_prima():
    test = Angajat('Ion','Ionescu',20000)
    assert test.prima_bianuala(500) == 21000
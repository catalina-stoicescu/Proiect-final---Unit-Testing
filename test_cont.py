from Clase import Cont
#1
def test_afisare_cont():
    test = Cont(333444555,'Ion Ionescu',305599)
    assert test.afisare_cont() == ('Titularul','Ion Ionescu', 'are in contul',333444555, 'suma de',305599,'lei')
#2
def test_debitare_cont():
    test = Cont(333444555,'Ion Ionescu',305599)
    assert test.debitare_cont(500) == 305099
#3
def test_verificare_debitare_cont():
    test = Cont(333444555,'Ion Ionescu',305599)
    assert test.debitare_cont(500) < 305599
#4
def test_debitare_cont_fonduri_insuficiente():
    test = Cont(333444555,'Ion Ionescu',305599)
    assert test.debitare_cont(500000) == ('Fonduri insuficiente!')
#5
def test_creditare_cont():
    test = Cont(333444555,'Ion Ionescu',305599)
    assert test.creditare_cont(50000) == 355599
#6
def test_verificare_creditare_cont():
    test = Cont(333444555,'Ion Ionescu',305599)
    assert test.creditare_cont(50000) > 305599
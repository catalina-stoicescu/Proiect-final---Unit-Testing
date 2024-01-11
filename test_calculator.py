from Clase import Calculator
#1
def test_adunare():
    calc = Calculator(1,2)
    assert calc.adunare() == 3
#2
def test_adunare_valoare_negativa():
    calc = Calculator(1,-3)
    assert calc.adunare() == -2
#3
def test_scadere():
    calc = Calculator(5,2)
    assert calc.scadere() == 3
#4
def test_scadere_rezultat_negativ():
    calc = Calculator(1,2)
    assert calc.scadere() == -1
#5
def test_inmultire():
    calc = Calculator(1,2)
    assert calc.inmultire() == 2
#6
def test_inmultire_cu_zero():
    calc = Calculator(1,0)
    assert calc.inmultire() == 0
#7
def test_inmultire_cu_numar_negativ():
    calc = Calculator(1,-3)
    assert calc.inmultire() == -3
#8
def test_impartire():
    calc = Calculator(1,2)
    assert calc.impartire() == 0.5
#9
def test_impartire_numere_negative():
    calc = Calculator(-24,-6)
    assert calc.impartire() == 4
#10
def test_impartire_la_numar_negative():
    calc = Calculator(24,-6)
    assert calc.impartire() == -4



from Clase import Cerc
#1
def test_descriere_cerc():
    test = Cerc(2, 'galben')
    assert test.descrie_cerc() == ('Cercul are culoarea','galben','si raza:',2)
#2
def test_arie():
    test = Cerc(2, 'galben')
    assert test.arie_cerc() == 9.869604401089358
#3
def test_arie_pozitiva():
    test = Cerc(2, 'galben')
    assert test.arie_cerc() > 0
#4
def test_diametru():
    test = Cerc(2, 'galben')
    assert test.diametru_cerc() == 4
#5
def test_diametru_pozitiv():
    test = Cerc(2, 'galben')
    assert test.diametru_cerc() > 0
#6
def test_diametru_pozitiv_Failed():
    test = Cerc(-2, 'galben')
    assert test.diametru_cerc() > 0
#7
def test_circumferinta():
    test = Cerc(2, 'galben')
    assert test.circumferinta_cerc() == 12.566370614359172
#8
def test_circumferinta_pozitiva():
    test = Cerc(2, 'galben')
    assert test.circumferinta_cerc() > 0


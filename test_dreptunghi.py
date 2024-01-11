from Clase import Dreptunghi
#1
def test_descriere():
    test = Dreptunghi(2,3,'rosu')
    assert test.descriere_dreptunghi() == ('Dreptunghiul are lungimea', 2, ',latimea',3, 'si culoarea', 'rosu')
#2
def test_arie_dreptunghi():
    test = Dreptunghi(2,3,'rosu')
    assert test.arie_dreptunghi() == 6,'Aria nu se calculeaza corect'
#3
def test_arie_dreptunghi_diferita_de_0():
    test = Dreptunghi(2,3,'rosu')
    assert test.arie_dreptunghi() != 0
#4
def test_arie_dreptunghi_mai_mare_de_0():
    test = Dreptunghi(2,3,'rosu')
    assert test.arie_dreptunghi() > 0
#5
def test_perimetru():
    test = Dreptunghi(2,3,'rosu')
    assert test.perimetrul_dreptunghi() == 10
#6
def test_perimetru_diferita_de_0():
    test = Dreptunghi(2,3,'rosu')
    assert test.perimetrul_dreptunghi() != 0
#7
def test_perimetru_mai_mare_de_0():
    test = Dreptunghi(2,3,'rosu')
    assert test.perimetrul_dreptunghi() > 0
#8
def test_schimbare_culoarea_dreptunghi():
    test = Dreptunghi(2,3,'rosu')
    assert test.schimbă_culoarea_dreptunghi() != 'rosu'

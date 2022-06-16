import logging
logging.basicConfig(level=logging.INFO)

def dodaj(a, b):
    logging.info("wybrałeś dodawanie")
    return a + b
  
def odejmij(c, d):
    logging.info("Wybrałeś odejmowanie")
    return c - d

def mnozenie(e, f):
    logging.info("wybrałeś mnozenie")
    return e * f
  
def dzielenie(g, h):
    logging.info("Wybrałeś dzielenie")
    return g / h
  

typ_obliczenia = input("Podaj działanie, posługując się odpowiednią liczbą: 1: Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
typ = {
    "1": dodaj,
    "2": odejmij,
    "3": mnozenie,
    "4": dzielenie
}

x = float(input("Podaj pierwszą zmienną x:"))
y = float(input("Podaj drugą zmienną y:"))

print(f"Wynik to {typ[typ_obliczenia](x, y)}")





                    

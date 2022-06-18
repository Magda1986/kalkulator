import logging
logging.basicConfig(level=logging.INFO)

def dodaj(a, b):
    logging.info("wybrałeś dodawanie")
    return a + b
  
def odejmij(a, b):
    logging.info("Wybrałeś odejmowanie")
    return a - b

def mnozenie(a, b):
    logging.info("wybrałeś mnozenie")
    return a * b
  
def dzielenie(a, b):
    if b == 0: 
        logging.error("nie dziel przez 0!!")
        return 
    logging.info("Wybrałeś dzielenie")
    return a / b
  
def pobierz_dane():
    typ_obliczenia = input("Podaj działanie, posługując się odpowiednią liczbą: 1: Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    x = float(input("Podaj pierwszą wartość:"))
    y = float(input("Podaj drugą wartość:"))
    return typ_obliczenia, x, y

def main():
    dzialanie, a, b = pobierz_dane()
    wynik = operations[dzialanie](a, b)
    logging.info(f"Wynik to {wynik}")

operations = {
    "1": dodaj,
    "2": odejmij,
    "3": mnozenie,
    "4": dzielenie
}

main()






                    

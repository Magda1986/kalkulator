import logging
logging.basicConfig(level=logging.INFO)

def dodaj(a, b):
    return a + b
  
def odejmij(c, d):
    return c - d
  
def mnozenie(e, f):
    return e * f

def dzielenie(g, h):
    return g / h

typ_obliczenia = input("Podaj działanie, posługując się odpowiednią liczbą: 1: Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

if typ_obliczenia == "1":
    logging.info("Wybrałeś dodawanie!")
elif typ_obliczenia == "2":
    logging.info("Wybrałeś odejmowanie!")
elif typ_obliczenia == "3":
    logging.info("Wybrałeś mnożenie!")
elif typ_obliczenia == "4":
    logging.info("Wybrałeś dzielenie!")
else:
    logging.error("Nie ma takiej opcji w kalkulatorze")

if typ_obliczenia in ["1", "2", "3", "4"]:
  
    x = float(input("Podaj pierwszą zmienną x:"))
    y = float(input("Podaj drugą zmienną y:"))
                    
    if typ_obliczenia == "1":
        logging.info(f"Dodaję {x} + {y}")
        print(f"Wynik dodawania {x} + {y} =", dodaj(x, y))
    elif typ_obliczenia == "2":
        logging.info(f"Odejmuję {x} - {y}")
        print(f"Wynik odejmowania{x} - {y} =", odejmij(x, y))
    elif typ_obliczenia == "3":
        logging.info(f"Mnożę {x} * {y}")
        print(f"Wynik mnożenia {x} * {y} =", mnozenie(x, y))
    elif typ_obliczenia == "4":
        logging.info(f"Dzielę {x} / {y}")
        try:
            result = dzielenie(x, y)
            print(f"Wynik dzielenia {x} / {y} =", result)
        except ZeroDivisionError:
            logging.error("Nie dziel przez zero!")
      

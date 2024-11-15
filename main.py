import json

#TODO: dodati type hinting na sve funkcije


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers:list, products:list, customers:list)->list:
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    print("Za kreiranje nove ponude potrebno je izabrati kupca, upisati datum, izabrati proizvode")
    print("Odaberite kupca među ponuđenim:")
    
    #odabir kupca iz liste kupaca
    i = 0
    for kupac in customers:
        i = i + 1
        print(f"{i}.Kupac: {kupac["name"]}")
        print("\n")
    
    odabir_kupca = input("Unesite ime kupca:")
    
    datum = input("Unesite datum:")
    
    
    print("PONUDA PROIZVODA:")
    for proizvod in products:
      print(f"Naziv: {proizvod["name"]}\nOpis proizvoda: {proizvod["description"]}\nCijena proizvoda: {proizvod["price"]}")
      print("\n")
    
    nova_lista2 = []
    ukupna_cijena = 0
    while True:
        
        #odabir proizvoda
        proizvod = input("\nUnesite naziv željenog proizvoda:")
        
        #suma cijena proizvoda
        for product in products:
           if product["name"] == proizvod:
              ukupna_cijena = ukupna_cijena + product["price"]
              #dodavanje dictionaria odabranih proizvoda u novu zasebnu listu
              nova_lista2.append(product)
        
        nastavak = input("Zelite li jos jedan proizvod:(Da/Ne):")
        if nastavak != "Da":
            break
        
      #izracun poreza i ukupne cijene  
    tax = ukupna_cijena/10
    total = ukupna_cijena + tax
    

    nova_lista1 = {
        "offer_number": len(offers) + 1,
        "customer": odabir_kupca,
        "date": datum,
        "items": nova_lista2,
        "sub_total": ukupna_cijena,
        "tax": tax,
        "total": total
    }
    
    offers.append(nova_lista1)
    
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products:list)->list:
    """
    Allows the user to add a new product or modify an existing product.
    """
    print("\n1.Zelite li dodati novi proizvod")
    print("2.Zelite li izmjeniti proizvod")
    
    odabir = input("Unesite broj ispred naredbe za koju zelite da se izvrsi:")
    
    #dodavanje novog proizvoda
    if odabir == "1":
        naziv_proizvoda = input("Upisite naziv novog proizvoda:")
        opis_proizvoda = input("Dodajte opis proizvoda:")
        cijena_proizvoda = float(input("Dodajte cijenu proizvoda:"))
        
        product = {
            
            "id":len(products) + 1,
            "name":naziv_proizvoda,
            "description":opis_proizvoda,
            "price":cijena_proizvoda
            
        }
        products.append(product)
    
    #izmjena proizvoda
    elif odabir == "2":
        print("Lista svih proizvoda:(prema id-u proizvoda odaberite proizvod se kojem zelite napraviti izmjenu)")
        for product in products:
             
            print(f"\nId proizvoda: {product["id"]}\nNaziv proizvoda: {product["name"]}\nOpis_proizvoda: {product["description"]}\nCijena proizvoda: {product["price"]}")
            print("\n")
            
        id_izmjene = int(input("Unesite id proizvoda koji zelite izmjeniti:"))
            
    #izmjena prvobitne liste
        for product in products:
            if product["id"]==id_izmjene:
                product["name"] = input("Unesite izmjene naziva proizvoda:")
                product["description"] = input("Unesite izmjene opisa proizvoda:")
                product["price"] = int(input("Unesite izmjene cijene proizvoda:"))
        
        print("Ažuriranje podataka završeno")
            
    
        
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers:list)->list:
    """
    Allows the user to add a new customer or view all customers.
    """
    print("\n1.Zelite li unijeti novoga kupca")
    print("2.Prikaz svih kupaca")
    
    odabir = input("Unesite broj neredbe za koju zelite da se izvrsi:")
    
    #unos novog kupca i njegovih podataka
    if odabir == "1":
        
        ime_kupca = input("Unesite ime kupca:")
        email = input("Unesite email kupca:")
        vat_id = input("Unsite vat id:")
        
        kupac = {
            
            "name": ime_kupca,
            "email": email,
            "vat_id":vat_id
            
        }
       
        customers.append(kupac)
        
        
    elif odabir == "2":
        for kupac in customers:
            print(f"Ime kupca: {kupac["name"]}\nEmail kupca:{kupac["email"]}\nVat id kupca:{kupac["vat_id"]}")
            print("\n")
    
    
    
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers:list)->list:
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    print("\n1.Zelite li prikazati ponude prema ID-u?")
    print("2.Zelite li prikazati ponude prema zeljenom mjesecu?")
    print("3.Zelite li prikazati sve ponude?")
    
    broj_odabira = input("Upisite broj ispred napredbe koju zelite da se izvrsi:")
    
   #trazenje ponude prema id-u 
    if broj_odabira == "1":
        id_ponude =int(input("Upiste id ponude:"))
        for offer in offers:
            if offer["offer_number"] == id_ponude:
                print_offer(offer)
    #trazenje ponuda prema mjesecu       
    elif broj_odabira == "2":
        mjesec = input("Unesite broj željenog mjeseca:")
        for offer in offers:
            if offer["date"][5:7] == mjesec:
                print_offer(offer)
            else:
                print("Traženog mjeseca nema!")
                break
    #prikaz svih ponuda
    elif broj_odabira == "3":
        for offer in offers:
            print_offer(offer)
    
    
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer:list)->list:
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()

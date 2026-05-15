class mobil:
  def __init__(self, model, vyrobce, rok_vyroby):
    self.model = model
    self.vyrobce = vyrobce
    self.rok_vyroby = rok_vyroby
    print(f" Model: {self.model}, Vyrobce: {self.vyrobce}, Rok: {self.rok_vyroby}")

  def info(self, cislo, majitel):
    self.cislo = cislo
    self.majitel = majitel
    print(f"Cislo majitele: {self.cislo}, Majitel: {self.majitel}")
  
  def zavolej(self):
    print(f"Mobil majitele {self.majitel}:  bzzzz bzzzzz bzzzz")

class Majitel(mobil):
 def __init__(self, jmeno, prijmeni, adresa, vek):
    self.jmeno = jmeno
    self.prijmeni = prijmeni
    self.adresa = adresa
    self.vek = vek
    print(f"Clovek jmenem: {self.jmeno} bydli na adrese {self.adresa} a ma vek {self.vek}.")



my_phone = mobil("S25", "Samsung", "2025")
my_phone.info("+42055869887", "Kolja")
friends_phone = mobil("Iphone 17 Pro", "Apple", "2026")
friends_phone.info("+4201478287", "Dan")

my_phone.zavolej()

Kolja = Majitel('Kolja', 'Pepsi', 'Andel', '17')

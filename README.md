#  Analýza a Vizualizace Hustoty Zalidnění

Tento projekt je jednoduchý Python skript pro analýzu demografických dat. Jeho hlavním cílem je vypočítat **hustotu zalidnění** (počet obyvatel na km²) pro různé země světa a vizualizovat výsledky formou přehledného grafu.

##  Popis projektu

Skript zpracovává seznam zemí, kde každá země je definována jako n-tice (tuple) s následujícími atributy:
- Název země
- Rozloha (km²)
- Počet obyvatel
- Kontinent

### Hlavní funkce:
1. **Výpočet hustoty:** Automaticky vypočítá hustotu zalidnění (`Populace / Rozloha`).
2. **Řazení:** Seřadí země od nejvyšší hustoty po nejnižší.
3. **Filtrace:** Vybere **Top 15** zemí s nejvyšší hustotou.
4. **Vizualizace:** Vykreslí horizontální sloupcový graf (Bar Chart) s popisky v češtině.

## 🛠️ Požadavky (Requirements)

Pro spuštění tohoto projektu potřebujete nainstalovaný **Python 3** a následující knihovny:

* [Pandas](https://pandas.pydata.org/) (manipulace s daty)
* [Seaborn](https://seaborn.pydata.org/) (vizualizace)
* [Matplotlib](https://matplotlib.org/) (vykreslování grafů)

## 🚀 Instalace a spuštění

1. **Naklonujte si repozitář:**
   ```bash
   git clone [https://github.com/keeeglya123/stocks]

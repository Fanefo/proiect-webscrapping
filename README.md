# Web Scraper pentru eBihoreanul.ro

Acesta este un proiect Scrapy conceput pentru a extrage articole de pe site-ul de știri `ebihoreanul.ro`.

## Descriere

Proiectul folosește un "spider" (un robot de crawling) pentru a naviga pe site-ul `ebihoreanul.ro`, a identifica articolele de pe o pagină dată (cum ar fi prima pagină sau o pagină de categorie), a vizita fiecare link de articol și a extrage informații relevante.

**Notă:** Extragerea textului complet al articolelor a eșuat din cauza structurii complexe și dinamice a site-ului. Scraper-ul în starea actuală extrage cu succes titlurile și link-urile.

## Funcționalități

- Extrage **titlul** și **link-ul** fiecărui articol.
- Navighează automat de pe pagina de start/categorie pe paginile individuale ale articolelor.
- Salvează datele extrase într-un format structurat (`.csv`), compatibil cu Microsoft Excel.
- Permite specificarea unui URL de start direct din linia de comandă pentru flexibilitate.

## Cerințe

- Python 3.x
- Scrapy

## Instalare

1.  Asigură-te că ai Python instalat.
2.  Instalează Scrapy folosind pip:
    ```shell
    py -m pip install scrapy
    ```

## Utilizare

Pentru a rula scraper-ul, deschide o linie de comandă în directorul `web_scraper` și folosește una din comenzile de mai jos.

**1. Rulare cu URL-ul implicit**

Această comandă va extrage articolele de pe prima pagină (`https://www.ebihoreanul.ro/`) și le va salva în `articles.csv`.

```shell
py -m scrapy crawl ebihoreanul -o articles.csv
```

**2. Rulare cu un URL personalizat**

Poți specifica orice pagină de start (de exemplu, o categorie) folosind argumentul `-a url="..."`. 

Exemplu pentru categoria "Știri Oradea":
```shell
py -m scrapy crawl ebihoreanul -a url=https://www.ebihoreanul.ro/stiri_oradea/ -o stiri_oradea.csv
```

ESHOP

Databaza
- Zákazník (Customer)
  - id zákazníka (customer_id)
  - meno (first_name)
  - priezvisko (last_name)
  - pohlavie 
  - heslo (password)
  - adresa (adress)
  - email (email)
  - dátum narodenia (birth_date)
  - tel. číslo (phone_number)

- Košík (Cart)
  - id košíka (cart_id)
  - id produktu  (product_id)
  - množstvo (quantity)
  
- Produkty (Product)
  - názov
  - popis
  - parametre(FK)
  - príslušenstvo (FK)
  - typ produktu
  - cena
  - stav na sklade/dostupnosť
  - hodnotenie
  - komentáre
  - obrázky
  
- Objednávka (Order)
  - id objednávky (order_id)
  - id_košíka (FK)
  - dátum vytvorenia (order_date)
  - vásledná suma (total_price)
  - stav objednávky (stock)
  
- Platba (Payment)
  - id platby (payment_id)
  - dátum plátby (payment_date)
  - spôsob platby (payment_method)
  - suma (amount)
  
- Kategórie produktov (Category)
  - id kategórie (category_id)
  - názov kategórie (category_name)
  - popis (description)
  - rodič (FK)  

- Parametre
  - id produktu
  - parameter
  - value

- Príslušenstvo
  - id produktu
  - príslušenstvo
  - hodnota
  
- Hodnotenie
  - id produktu
  - id uživateľa
  - hodnotenie
  
- Komentár
  - id produktu
  - id uživateľa
  - komentár
  
- Obrazky
  - id produktu
  - obrazok
  - popis

Funkce (views + templates)
  - zobrazit novinky (homepage/akcie)
  - zobrazit seznam všech produktov
  - filtrování produktov (zoznam)
     - podľa ceny (vzostupne, zostupne, najpredávanejšie)
     - stav tovaru
     - podľa dostupnosti
     - podľa hodnotenia
  - zobrazit detail produktu
  - prihlásený uživateľ môže:
     - vytvoriť objednávky
     - 
     - hodnotit produkty 
     - komentovať produkty
    - objednávka môže:
      - obsahovať viac produktov

- admin může:
     - pridať/editovať/zmazať produkt/uživateľa/cenu/dostupnosť/obrázky/video/komentáre

  

- Doručenie
  - id doručenia
  - dátum odoslania
  - dátum doručenia
  - stav doručenia

- Zľavy
  - id zľavy
  - typ zľavy
  - percento zľavy
  - dátum platnosti


- História nákupov
  - id histórie
  - id zákazníka
  - dátum nákupu
  - celková cena

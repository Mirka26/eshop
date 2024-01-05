ESHOP

Databaza
- Zákazník (Customer)
  - id zákazníka (customer_id)
  - meno (first_name)
  - priezvisko (last_name)
  - pohlavie (sex)
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
  - parametre
  - príslušenstvo 
  - typ produktu
  - cena
  - stav na sklade
  - hodnotenie
  - komentáre
  - obrázky
- Objednávka (Order)
  - id objednávky (order_id)
  - dátum vytvorenia (order_date)
  - vásledná suma (total_price)
  - stav objednávky (stock)
- Platba (Payment)
  - id platby (payment_id)
  - dátum plátby (payment_date)
  - spôsob platby (payment_method)
  - suma (amount)
- Kategórie produktov (Catefory)
  - id kategórie (category_id)
  - názov kategórie (category_name)
  - popis (description)
- Parametre
  - id produktu
  - Typ spotrebiča
  - Značka a výrobca 
  - Hodnotenie energetického výkonu spotrebiča 
  - Funkcie a programy 
  - Rozmery 
  - Hmotnosť 
  - Pripojenie a kompatibilita 
  - Hlučnosť 
  - Spotreba energie (vody)
  - Materiál a dizajn
  - Ovládanie a interakcia
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
     - podle herce
     - podle režiséra
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

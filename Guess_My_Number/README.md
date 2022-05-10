# Daugiau - Mažiau (Atspėk skaičių)

![Fizz Buzz](https://raw.githubusercontent.com/lajmcourses/Images/master/guess_my_number.png)

Daugiau - Mažiau yra vaikiškas matematinis žaidymas. Pirmas žaidėjas sugalvoja skaičių ir antras žaidėjas
turi tą skaičių atspėti. Antras žaidėjas pasako savo spėjimą pirmam žaidėjui, ir pirmasis žaidėjas gali 
duoti vieną atsakymą iš trijų galimų:

    1. Teisingai - jei spėjimas teisingas;
    2. Daugiau - jei sugalvotas skaičius yra didesnis nei spėjimo skaičius
    3. Mažaiu - jei sugalvotas skaičius yra mažesnis nei spėjimo skaičius

Žaidimas baigiasi, jeigu 

    - antras žaidėjas atspėja skaičių teisingai, šiuo atveju antrasis žaidėjas laimi;
    - antras žaidėjas išnauduoja 10 spėjimo bandymų, šiuo atveju antrasis žaidėjas pralaimi.


## Užduotis

1) Parašykite funkciją **guess_processor**. 


    Funkcijos parametrai **actual_number** (sugalvotas skaičius) ir **guess_number** (skaičiaus spėjimas)

    
    Funkcija grąžina žodį:

        - "Correct", jeigu spėjimas buvo teisingas;

        - "Higher", jeigu sugalvotas skaičius yra didesnis už spėjimą;

        - "Lower", jeigu sugalvotas skaičius yra mažesnis neis spėjimas.


3) Parašykite programą, imituojančią žaidymą "Daugia-Mažiau". Panudokite savo programoje aukščiau parašytą funkciją.
#uzduotis atliekama per DB Browser (SQLite)
# Parsisiųskite lentelę "darbuotojai2.db",() atsidarykite ją programoje DB Browser for SQLite ir skiltyje "Execute SQL" atlikite šias SQL užklausas:
#
# Išrinkite duomenis apie darbuotoją (asmens kodą, vardą ir pavarde) iš lenteles DARBUOTOJAS, kuris gimęs 1988 m. liepos 20 d.
# Išrinkite duomenis apie darbuotojus (nuo kada dirba, asmens kodą) iš lentelės DARBUOTOJAS, kurie būtų įsidarbinę nuo 2009 m. spalio 30 d. iki 2012 m. lapkričio 11d.
# Išrinkite duomenis apie darbuotojus (vardą, Skyriaus ID ir Projekto ID) iš lentelės DARBUOTOJAS, kurie dirba 2 ir 3 skyriuose (panaudoti IN operatorių).
# Išrinkite duomenis (vardą, pavarde ir asmens kodą) apie visas moteris iš lentelės DARBUOTOJAS (panaudojant operatorių LIKE).
# Išrinkite visus duomenis apie visus darbuotojus iš lentelės DARBUOTOJAS, kurie yra gimę 12 dieną (panaudojant operatorių LIKE). išrinkite visus projektus iš lentelės PROJEKTAS, kurių pavadinime antra raidė būtų ‘a’.
# Išrinkite visus darbuotojus iš lentelės DARBUOTOJAS, kuriems nepaskirtos jokios pareigos.
# Išrinkite duomenis apie darbuotojus (vardą, pavarde, nuo kada dirba ir pareigas), kurie dirba nuo 2011-02-12 ir jų pareigos yra Programuotojai.
# Išrinkite duomenis apie darbuotojus (vardą, pavardę, Skyriaus ID ir Projekto ID) iš lentelės DARBUOTOJAS, kurie yra iš Gamybos (2) skyriaus arba 1 projekto.
# Išrinkite visus darbuotojų vardus, išskyrus tuos, kurių vardai prasideda raide ‘A’ .
# Išrinkite duomenis apie darbuotojus (vardą, pavardę ir nuo kada dirba) iš lentelės DARBUOTOJAS ir išrikiuokite visus duomenis nuo dirbančio seniausiai iki naujausiai.
# Išrinkite duomenis apie darbuotojus (vardą, pavardę ir nuo kada dirba) iš lentelės DARBUOTOJAS ir išrikiuokite visus duomenis nuo dirbančio naujausiai iki seniausiai.
# Išrinkite iš lentelės DARBUOTOJAS projektų ID, kurie būtų minimalus ir maksimalus skaičius.
# Išrinkite duomenis apie tai, kiek kiekviename projekte yra priskirta žmonių (projekto numeris ir skaičius, kiek jame dalyvauja žmonių).
# #14 punkto užklausą pataisykite taip, kad rodytų tik tuos projektus, kuriems priskirti daugiau nei 3 darbuotojai.
# Išrinkite duomenis (projekto numeris, pareigos, skaičius) iš lentelės DARBUOTOJAS, kiek programuotojų dirba kiekvienam projekte.

# SELECT ASMENS_KODAS, VARDAS, PAVARDĖ FROM DARBUOTOJAS WHERE ASMENS_KODAS like '_880720%'
# SELECT * FROM DARBUOTOJAS WHERE DIRBA_NUO BETWEEN '2009-10-30' AND '2012-11-11'
# SELECT VARDAS, SKYRIUS_ID, PROJEKTAS_ID FROM DARBUOTOJAS WHERE SKYRIUS_ID IN(2,3)
# SELECT VARDAS, PAVARDĖ, ASMENS_KODAS FROM DARBUOTOJAS WHERE ASMENS_KODAS like '4%' or ASMENS_KODAS like '6%'
# SELECT * FROM DARBUOTOJAS WHERE ASMENS_KODAS like '_____12%'
# SELECT * FROM PROJEKTAS WHERE PAVADINIMAS like '_a%'
# SELECT * FROM DARBUOTOJAS WHERE PAREIGOS is NULL
# SELECT VARDAS, PAVARDĖ, DIRBA_NUO, PAREIGOS FROM DARBUOTOJAS WHERE DIRBA_NUO > '2011-02-12' AND PAREIGOS = 'Programuotojas'
# SELECT VARDAS, PAVARDĖ, SKYRIUS_ID, PROJEKTAS_ID FROM DARBUOTOJAS WHERE SKYRIUS_ID is '2' or PROJEKTAS_ID is '1'
# SELECT VARDAS FROM DARBUOTOJAS WHERE VARDAS NOT like 'A%'
# SELECT VARDAS, PAVARDĖ, DIRBA_NUO FROM DARBUOTOJAS ORDER by DIRBA_NUO
# SELECT VARDAS, PAVARDĖ, DIRBA_NUO FROM DARBUOTOJAS ORDER by DIRBA_NUO DESC
# SELECT min(PROJEKTAS_ID), max(PROJEKTAS_ID) from DARBUOTOJAS
# SELECT PROJEKTAS_ID, count() FROM DARBUOTOJAS GROUP by PROJEKTAS_ID
# SELECT PROJEKTAS_ID, count() FROM DARBUOTOJAS GROUP by PROJEKTAS_ID HAVING count() > 3
# SELECT PROJEKTAS_ID, PAREIGOS, count() FROM DARBUOTOJAS WHERE PAREIGOS = 'Programuotojas' group by PROJEKTAS_ID

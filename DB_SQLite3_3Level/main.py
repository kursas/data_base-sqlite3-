# /*Parsisiųskite lentelę "darbuotojai3.db", atsidarykite ją programoje DB Browser for SQLite ir skiltyje "Execute SQL" atlikite šias SQL užklausas:
# --1.Išrinkite darbuotojų vardus ir pavardes kartu su projekto pavadinimu, kuriame jie dirba.*/
# --SELECT VARDAS, PAVARDĖ, PROJEKTAS.PAVADINIMAS FROM DARBUOTOJAS JOIN PROJEKTAS on PROJEKTAS.ID = DARBUOTOJAS.PROJEKTAS_ID
#
# --2.Išsirinkite darbuotojų dirbančių projekte Galerija vardus, pavardes ir projekto pavadinimą.
# --SELECT VARDAS, PAVARDĖ, PAVADINIMAS from DARBUOTOJAS JOIN PROJEKTAS on PROJEKTAS.ID = DARBUOTOJAS.PROJEKTAS_ID WHERE PROJEKTAS.PAVADINIMAS = "Galerija"
#
# --3.Išrinkite visus projekto Projektų valdymas vykdytojus dirbančius Pardavimų skyriuje.
# --SELECT * from DARBUOTOJAS JOIN SKYRIUS on SKYRIUS.id = DARBUOTOJAS.SKYRIUS_ID JOIN PROJEKTAS ON PROJEKTAS.ID = DARBUOTOJAS.PROJEKTAS_ID WHERE SKYRIUS.PAVADINIMAS = "Gamybos" AND PROJEKTAS.PAVADINIMAS = "Projektų valdymas"
#
# --4.Išrinkite visas moteris, dirbančias projekte Projektų valdymas ir išveskite į ekraną jų vardus, pavardes ir projekto pavadinimą.
# --SELECT VARDAS, PAVARDĖ, PAVADINIMAS FROM DARBUOTOJAS JOIN PROJEKTAS ON PROJEKTAS.ID = DARBUOTOJAS.PROJEKTAS_ID WHERE (ASMENS_KODAS LIKE "4%" OR ASMENS_KODAS like "6%") AND PROJEKTAS.PAVADINIMAS = "Projektų valdymas"
#
# --5.Išrinkite skyrių pavadinimus su juose dirbančių darbuotojų skaičiumi.
# --SELECT SKYRIUS.PAVADINIMAS, count(*) FROM DARBUOTOJAS JOIN SKYRIUS on SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID GROUP by SKYRIUS.PAVADINIMAS
#
# --6.Apribokite #5 užklausos rezultatą taip, kad rodytų tik tuos skyrius kur dirba bent 5 darbuotojai.
# --SELECT SKYRIUS.PAVADINIMAS, count(*) FROM DARBUOTOJAS JOIN SKYRIUS on SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID GROUP by SKYRIUS.PAVADINIMAS HAVING count(*) > 5
#
# --7.Išrinkite darbuotojus (vardus, pavardes, pareigas) kartu su skyrių, kuriuose jie dirba pavadinimais, tačiau nesančius tų skyrių vadovais.
# --SELECT VARDAS, PAVARDĖ, PAREIGOS, SKYRIUS.PAVADINIMAS FROM DARBUOTOJAS JOIN SKYRIUS on SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID WHERE NOT PAREIGOS="Vadovas"
#
# --8.Sukurkite naują įrašą lentelėje “DARBUOTOJAS” (asmens kodas: 38807117896, vardas: Pranas, pavardė:Logis, Dirba nuo: 2009-11-12, visa kita - Null).
# --INSERT INTO DARBUOTOJAS VALUES (NULL, "Pranas", "Logis", 38807117896, NULL, "2009-11-12", NULL, NULL, NULL, NULL)
#
# --9.Išrinkite darbuotojų vardus, pavardes ir skyriaus pavadinimą. Rodykite, net ir tuos darbuotojus, kurie nedirba jokiame skyriuje (skyriaus pavadinimą pasiimkite iš lentelės SKYRIUS).
# --SELECT VARDAS, PAVARDĖ, PAVADINIMAS FROM DARBUOTOJAS LEFT JOIN SKYRIUS on DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
#
# --10.1# punkto užklausą pataisykite taip, kad rodytų tik tuos vardus ir projektų pavadinimus kuriuose dirba daugiau nei 4 darbuotojai.
# --SELECT VARDAS, PAVARDĖ, PROJEKTAS.PAVADINIMAS FROM DARBUOTOJAS JOIN PROJEKTAS on PROJEKTAS.ID = DARBUOTOJAS.PROJEKTAS_ID where PROJEKTAS_ID in (SELECT PROJEKTAS_ID FROM DARBUOTOJAS GROUP by PROJEKTAS_ID HAVING count() > 4)
#
# --11.Naujame stulpeyje parodyti kiekvieno darbuotojo bazinio atlyginimo ir priedų sumą.
# --SELECT VARDAS, PAVARDĖ, BAZINIS_ATLYGINIMAS, PRIEDAI, BAZINIS_ATLYGINIMAS + PRIEDAI as "Suma" FROM DARBUOTOJAS
#
# --12.Parodyti bendrą atlyginimų, priedų sumą, vidutinį, maksimalų, minimalų atlyginimą.
# --SELECT sum(BAZINIS_ATLYGINIMAS), sum(PRIEDAI), count(), max(BAZINIS_ATLYGINIMAS), min(BAZINIS_ATLYGINIMAS) FROM DARBUOTOJAS

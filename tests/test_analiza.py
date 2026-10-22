import pandas as pd
from analiza import wyczysc_dane, podsumowanie, sprzedaz_wg_kanalu


def przykladowe_dane():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "kanal": ["Internet", "internet ", "SKLEP"],
        "segment": ["A", "B", "A"],
        "wartosc": [100, 200, 60],
    })


def test_wyczysc_dane_ujednolica_kanaly():
    wynik = wyczysc_dane(przykladowe_dane())
    assert set(wynik["kanal"]) == {"internet", "sklep"}


def test_wyczysc_dane_nie_modyfikuje_wejscia():
    df = przykladowe_dane()
    wyczysc_dane(df)
    assert df["kanal"].tolist() == ["Internet", "internet ", "SKLEP"]


def test_podsumowanie():
    wynik = podsumowanie(wyczysc_dane(przykladowe_dane()))
    assert isinstance(wynik, dict)
    assert wynik["liczba_zamowien"] == 3
    assert wynik["suma_sprzedazy"] == 360
    assert wynik["srednia_wartosc"] == 120
    assert wynik["mediana"] == 100


def test_sprzedaz_wg_kanalu():
    wynik = sprzedaz_wg_kanalu(wyczysc_dane(przykladowe_dane()))
    assert isinstance(wynik, pd.DataFrame)
    internet = wynik[wynik["kanal"] == "internet"]["suma_sprzedazy"].iloc[0]
    assert internet == 300
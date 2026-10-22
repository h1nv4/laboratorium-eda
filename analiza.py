import pandas as pd


def wczytaj_dane(sciezka):
    return pd.read_csv(
        sciezka,
        sep=";"
    )


def wyczysc_dane(df):
    wynik = df.copy()

    wynik["kanal"] = (
        wynik["kanal"]
        .str.strip()
        .str.lower()
    )

    return wynik


def podsumowanie(df):
    return {
        "liczba_zamowien": len(df),
        "suma_sprzedazy": df["wartosc"].sum(),
        "srednia_wartosc": df["wartosc"].mean(),
        "mediana": df["wartosc"].median(),
    }


def sprzedaz_wg_kanalu(df):
    return (
        df.groupby("kanal")["wartosc"]
        .sum()
        .reset_index(name="suma_sprzedazy")
    )
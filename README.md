# Segmentacija kupaca (Customer Segmentation)

Ovaj pojekat implementira RFM (Recency, Frequency, Monetary) analizu i K-Means klasterovanje za automatsku segmentaciju kupaca e-commerce kompanije.

Tehnicke informacije:
Projekat je razvijen u Python-u koristeci Streamlit framework za web interfejs, pandas za obradu podataka i scikit-learn za masinsko ucenje.

Instalacija:
1 Kloniraj repozitorijum: `git clone [https://github.com/lukas11fullhd/Segmentacija_Kupaca]`
2 Instaliraj zavisnosti: `pip install -r requirements.txt`
3 Pokreni aplikaciju: `python -m streamlit run app.py`

Koriscenje:
Ucitaj CSV fajl koji sadrzi kolone: `CustomerID`, `InvoiceDate`, `Amount`.
Sistem automatski vrsi RFM proracun i primjenjuje K-Means algoritam (k=3).
Rezultati se prikazuju kroz tabelarni pregled i interaktivnu vizuelizaciju.

AUtor:
Luka Tačić, 23/101
Fakultet za informacione sisteme i tehnologije, UDG
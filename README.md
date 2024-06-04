# Monitoring pre zavlažovací systém

Tento projekt je jednoduchá Flasková webová aplikácia na zaznamenávanie údajov o teplote a vlhkosti a ich zobrazenie pre používateľa. Dáta sú ukladané do Redis databázy.

## Funkcie

- Zaznamenávanie údajov o teplote a vlhkosti do Redis databázy.
- Poskytovanie webového rozhrania na zobrazenie zaznamenaných údajov.

## Predpoklady

Pred spustením tejto aplikácie budete musieť mať nainštalované nasledujúce:

- Python (verzia 3.6 alebo vyššia)
- Flask
- Flask-SocketIO
- Redis
- Redis-py (Pythonový Redis klient)

## Inštalácia

1. Vyklonujte tento repozitár na svoj lokálny stroj:
```
git clone https://github.com/your-username/zavlazovaci-system.git

```

3. Prejdite do adresára projektu:
```
cd zavlazovaci-system

```
3. Nainštalujte potrebné Python balíčky pomocou pip:

```
pip install -r requirements.txt

```

## Použitie

1. Spustite Redis server. Ak nemáte nainštalovaný Redis, môžete si ho stiahnuť z [redis.io](https://redis.io/download) a postupovať podľa inštrukcií pre váš operačný systém.

2. Spustite Flask aplikáciu:

```
python app.py

```

3. Otvorte webový prehliadač a prejdite na [http://localhost:5000](http://localhost:5000), aby ste sa dostali k aplikácii.

4. Kliknite na tlačidlo "Štart", aby ste začali zaznamenávať údaje o teplote a vlhkosti. Kliknite na tlačidlo "Stop", aby ste prestali zaznamenávať údaje.

5. Zaznamenané údaje môžete zobraziť prechodom na záložky "Graf" alebo "Ciferník".

## Prispievanie

Príspevky sú vítané! Ak objavíte akékoľvek problémy alebo máte návrhy na vylepšenie, otvorte prosím problém alebo pošlite požiadavku na zlúčenie (pull request).

## Licencia

Tento projekt je licencovaný pod MIT licenciou - pozrite si súbor [LICENSE](LICENSE) pre viac informácií.

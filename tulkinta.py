

def main():

    import sys
    with open(sys.argv[1], "r") as f:
        data = f.read()

    for peli in data.split("\n"):
        if not peli.strip():
            continue
        pvm, tyyppi, lyonnit = peli.strip().split(":")

        print(pvm, tyyppi)
        histogrammi = {}
        for a in "1234567890":
            histogrammi[a] = lyonnit.count(a)

        pussitus_kpl = histogrammi["0"]
        lyonnit = sum(histogrammi.values()) - pussitus_kpl

        pussitus_p = pussitus_kpl / lyonnit * 100.0
        vasemmalle_p = sum(histogrammi[a] for a in "1234") / lyonnit * 100.0
        keskelle_p = sum(histogrammi[a] for a in "5") / lyonnit * 100.0
        oikealle_p = sum(histogrammi[a] for a in "6789") / lyonnit * 100.0

        print(f"Lyönnit {lyonnit} kpl, pussitukset {pussitus_kpl} kpl / {pussitus_p:.1f} %")
        print(f"vasemmalle {vasemmalle_p:.1f} %, keskelle {keskelle_p:.1f} %, oikealle {oikealle_p:.1f} %")



    pass

if __name__ == "__main__":
    main()

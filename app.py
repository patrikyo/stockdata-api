from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

tickers = [
    "AAK.ST",
    "ABB.ST",
    "ACAD.ST",
    "ALIF-B.ST",
    "ANOD-B.ST",
    "ADDT-B.ST",
    "AFRY.ST",
    "ALFA.ST",
]

@app.route('/api/stocks/names', methods=['GET'])
def get_all_stock_names():
    """Returnerar en lista med alla tickers som har ett longName."""
    results = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            if info.get("longName"):
                results.append({"ticker": ticker, "name": info["longName"]})
        except Exception:
            continue  # hoppa över om yfinance kastar fel
    return jsonify(results)


@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        name = info.get("longName", "N/A")
        price = info.get("currentPrice", "N/A")
        change = info.get("regularMarketChangePercent")
        currency = info.get("currency", "N/A")

        if change is not None:
            change = f"{change:+.2f}%"
        else:
            change = "N/A"

        return jsonify({
            "ticker": ticker,
            "name": name,
            "change": change,
            "price": str(price) if price != "N/A" else None,
            "currency": currency,
            "market_cap": info.get("marketCap"),
            "enterprise_value": info.get("enterpriseValue"),
            "trailing_pe": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "peg_ratio": info.get("pegRatio"),
            "ps_ratio": info.get("priceToSalesTrailing12Months"),
            "pb_ratio": info.get("priceToBook"),
            "ev_revenue": info.get("enterpriseToRevenue"),
            "ev_ebitda": info.get("enterpriseToEbitda")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)









# const stockholmLargeMidCap = [
#   "AAK.ST",
#   "ABB.ST",
#   "ACAD.ST",
#   "ALIF-B.ST",
#   "ANOD-B.ST",
#   "ADDT-B.ST",
#   "AFRY.ST",
#   "ALFA.ST",
#   "ALIG.ST",
#   "ALLEI.ST",
#   "ALLIGO-B.ST",
#   "ALVO-SDB.ST",
#   "AMBEA.ST",
#   "APOTEA.ST",
#   "AQ.ST",
#   "Arctic Paper",
#   "Arion Banki SDB",
#   "Arise",
#   "Arjo B",
#   "Asker Healthcare Group",
#   "Asmodee Group B",
#   "ASSA ABLOY B",
#   "AstraZeneca",
#   "Atlas Copco A",
#   "Atlas Copco B",
#   "Atrium Ljungberg B",
#   "Attendo",
#   "Autoliv SDB",
#   "Avanza Bank Holding",
#   "Axfood",
#   "Bactiguard Holding B",
#   "Beijer Alma B",
#   "Beijer Ref B",
#   "Bergman & Beving B",
#   "Besqab",
#   "Besqab Pref B",
#   "Betsson B",
#   "Better Collective",
#   "BHG Group",
#   "BICO Group",
#   "Bilia A",
#   "Billerud",
#   "BioArctic B",
#   "BioGaia B",
#   "BioInvent International",
#   "Boliden",
#   "Bonava A",
#   "Bonava B",
#   "BONESUPPORT HOLDING",
#   "Boozt",
#   "Bravida Holding",
#   "Brinova Fastigheter B",
#   "BTS Group B",
#   "Bufab",
#   "Bure Equity",
#   "Byggmax Group",
#   "Byggmästare A J Ahlström H",
#   "Camurus",
#   "Castellum",
#   "Catella A",
#   "Catella B",
#   "Catena",
#   "Cavotec Group",
#   "CellaVision",
#   "Cibus Nordic Real Estate",
#   "Cinclus Pharma Holding",
#   "Cint Group",
#   "Clas Ohlson B",
#   "Cloetta B",
#   "CoinShares International",
#   "Coor Service Management Hold",
#   "Corem Property Group A",
#   "Corem Property Group B",
#   "Corem Property Group D",
#   "Corem Property Group Pref",
#   "Creades A",
#   "CTT Systems",
#   "Diös Fastigheter",
#   "Dometic Group",
#   "Duni",
#   "Dustin Group",
#   "Dynavox Group",
#   "Eastnine",
#   "Elanders B",
#   "Electrolux A",
#   "Electrolux B",
#   "Electrolux Professional B",
#   "Elekta B",
#   "Embracer Group B",
#   "Enea",
#   "engcon B",
#   "Enity Holding",
#   "Eolus B",
#   "Ependion",
#   "Epiroc A",
#   "Epiroc B",
#   "EQT",
#   "Ericsson A",
#   "Ericsson B",
#   "Essity A",
#   "Essity B",
#   "Evolution",
#   "Ework Group",
#   "Fabege",
#   "Fagerhult Group",
#   "Fasadgruppen Group",
#   "Fast. Balder B",
#   "Fastighetsbolag. Emilshus Pref",
#   "Fastighetsbolaget Emilshus B",
#   "Fastpartner A",
#   "Fastpartner D",
#   "Fenix Outdoor International B",
#   "Flerie",
#   "FM Mattsson B",
#   "Genova Property Group",
#   "Gentoo Media",
#   "Getinge B",
#   "Green Landscaping Group",
#   "Gruvaktiebolaget Viscaria",
#   "Gränges",
#   "Hacksaw",
#   "Hansa Biopharma",
#   "HANZA",
#   "HEBA B",
#   "Hemnet Group",
#   "Hennes & Mauritz B",
#   "Hexagon B",
#   "Hexatronic Group",
#   "HEXPOL B",
#   "HMS Networks",
#   "Hoist Finance",
#   "Holmen A",
#   "Holmen B",
#   "Hufvudstaden A",
#   "Humana",
#   "Humble Group",
#   "Husqvarna A",
#   "Husqvarna B",
#   "I.A.R Systems Group",
#   "Industrivärden A",
#   "Industrivärden C",
#   "Indutrade",
#   "Instalco",
#   "Intea Fastigheter B",
#   "Intea Fastigheter D",
#   "International Petroleum Corp",
#   "Intrum",
#   "Investor A",
#   "Investor B",
#   "INVISIO",
#   "Inwido",
#   "ITAB Shop Concept",
#   "JM",
#   "John Mattson Fastighetsföret",
#   "K-Fast Holding B",
#   "KABE Group B",
#   "Karnov Group",
#   "Kinnevik A",
#   "Kinnevik B",
#   "KlaraBo Sverige B",
#   "Knowit",
#   "Lagercrantz Group B",
#   "Latour B",
#   "Lifco B",
#   "Lime Technologies",
#   "Linc",
#   "Lindab International",
#   "Logistea A",
#   "Logistea B",
#   "Loomis",
#   "Lundbergföretagen B",
#   "Lundin Gold",
#   "Lundin Mining Corporation",
#   "MedCap",
#   "Medicover B",
#   "MEKO",
#   "Meren Energy",
#   "Mildef Group",
#   "Mips",
#   "Modern Times Group A",
#   "Modern Times Group B",
#   "Momentum Group B",
#   "Munters Group",
#   "Mycronic",
#   "NCAB Group",
#   "NCC A",
#   "NCC B",
#   "Nederman Holding",
#   "Neobo Fastigheter",
#   "Net Insight B",
#   "New Wave B",
#   "NIBE Industrier B",
#   "Nivika Fastigheter B",
#   "Nobia",
#   "Nolato B",
#   "Nordea Bank Abp",
#   "Nordic Paper Holding",
#   "Nordnet",
#   "Norion Bank",
#   "NOTE",
#   "NP3 Fastigheter",
#   "NP3 Fastigheter Pref",
#   "Nyfosa",
#   "OEM International B",
#   "Orrön Energy",
#   "Pandox B",
#   "Peab B",
#   "Platzer Fastigheter Holding B",
#   "PowerCell Sweden",
#   "Pricer B",
#   "Prisma Properties",
#   "Proact IT Group",
#   "Profoto Holding",
#   "Ratos A",
#   "Ratos B",
#   "RaySearch Laboratories B",
#   "Rejlers B",
#   "Resurs Holding",
#   "Rottneros",
#   "Rusta",
#   "RVRC Holding",
#   "Röko B",
#   "SAAB B",
#   "Sagax A",
#   "Sagax B",
#   "Sagax D",
#   "Samhällsbyggnadsbo. i Norden B",
#   "Samhällsbyggnadsbo. i Norden D",
#   "Sampo Oyj SDB",
#   "Sandvik",
#   "SCA A",
#   "SCA B",
#   "Scandi Standard",
#   "Scandic Hotels Group",
#   "Sdiptech B",
#   "Sdiptech Pref",
#   "SEB A",
#   "SEB C",
#   "SECTRA B",
#   "Securitas B",
#   "Sedana Medical",
#   "Sinch",
#   "Skanska B",
#   "SKF A",
#   "SKF B",
#   "SkiStar B",
#   "SSAB A",
#   "SSAB B",
#   "Stendörren Fastigheter B",
#   "Stenhus Fastigheter i Norden",
#   "Stillfront Group",
#   "Stora Enso A",
#   "Stora Enso R",
#   "Storskogen Group B",
#   "Sv. Handelsbanken A",
#   "Sv. Handelsbanken B",
#   "Sveafastigheter",
#   "Svolder A",
#   "Svolder B",
#   "SWECO A",
#   "SWECO B",
#   "Swedbank A",
#   "Swedish Logistic Property B",
#   "Swedish Orphan Biovitrum",
#   "Synsam",
#   "Systemair",
#   "Tele2 A",
#   "Tele2 B",
#   "Telia Company",
#   "TF Bank",
#   "Thule Group",
#   "TietoEVRY Oyj",
#   "Traction B",
#   "TRATON",
#   "Trelleborg B",
#   "Trianon B",
#   "Troax Group",
#   "Truecaller B",
#   "VBG GROUP B",
#   "VEF",
#   "Vestum",
#   "Viaplay Group A",
#   "Viaplay Group B",
#   "Vimian Group",
#   "Vitec Software Group B",
#   "Vitrolife",
#   "VNV Global",
#   "Volati",
#   "Volati Pref",
#   "Volvo A",
#   "Volvo B",
#   "Volvo Car B",
#   "Wallenstam B",
#   "Wihlborgs Fastigheter",
#   "XANO Industri B",
#   "Xvivo Perfusion",
#   "Yubico",
#   "Öresund"
# ];























													
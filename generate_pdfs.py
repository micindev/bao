import subprocess
import os

pdf_defs = [
    {
        'id': 'streetfood',
        'title': 'STREETFOOD',
        'subtitle': 'KDE N\u00c1JDE\u0160 N\u00c1\u0160 FOOD TRUCK NA CEST\u00c1CH',
        'icon': 'extracted_assets/icon_streetfood.svg',
        'perex': 'N\u00e1\u0161 food truck prin\u00e1\u0161a autentick\u00fa chu\u0165 nad\u00fdchan\u00fdch bao \u017eemli\u010diek priamo do ul\u00eds, na festivaly a kult\u00farne podujatia po celom Slovensku.',
        'sections': [
            ('AKTU\u00c1LNE ZAST\u00c1VKY & LOK\u00c1CIE', [
                'Pravideln\u00e9 zast\u00e1vky na street food festivaloch v Bratislave, Trnave, Ko\u0161iciach a \u017diline',
                'Firemn\u00e9 pop-up obedy a gastro z\u00f3ny v biznis centr\u00e1ch',
                'Kult\u00farne akcie, hudobn\u00e9 festivaly a sez\u00f3nne mestsk\u00e9 trhy',
                'Pre dennospevn\u00e9 aktu\u00e1lne lok\u00e1cie v re\u00e1lnom \u010dase sleduj n\u00e1\u0161 Instagram @baobrothers.sk'
            ]),
            ('OB\u013d\u00daBEN\u00c9 STREETFOOD MENU', [
                'PORK BELLY BAO \u2014 Pomalinky pe\u010den\u00fd brav\u010dov\u00fd b\u00f4\u010dik, hoisin majo, nakladan\u00e1 uhorka, ara\u0161idy, koriander',
                'CRISPY CHICKEN BAO \u2014 Chrumkav\u00e9 kuracie stehno v panko str\u00fahanke, sriracha mayo, nakladan\u00e1 re\u010fkovka',
                'MUSHROOM BAO (VEGAN) \u2014 Karamelizovan\u00e1 hliva na s\u00f3jovo-z\u00e1zvorovom z\u00e1klade, jarn\u00e1 cibu\u013eka, sezam',
                'KIMCHI FRIES \u2014 Dom\u00e1ce chrumkav\u00e9 hranolky s na\u0161im remeseln\u00fdm kimchi a togarashi koren\u00edm'
            ]),
            ('PRENAJMI SI FOOD TRUCK NA VLASTN\u00da AKCIU', [
                'Plne auton\u00f3mny street food trailer s profesion\u00e1lnou kuchy\u0148ou',
                'Kapacita v\u00fddaja a\u017e 200 porci\u00ed za hodinu',
                'Mo\u017enos\u0165 zostavenia tematick\u00e9ho menu pod\u013ea v\u00e1\u0161ho \u017eelania'
            ])
        ],
        'cta': 'Chcete Bao Brothers food truck na va\u0161om festivale alebo s\u00fakromnom evente? Nap\u00ed\u0161te n\u00e1m na streetfood@baobrothers.sk alebo volajte +421 900 123 456.'
    },
    {
        'id': 'catering',
        'title': 'CATERING',
        'subtitle': 'ORIGIN\u00c1LNY \u00c1ZIJSK\u00dd CATERING PRE FIREMN\u00c9 AJ S\u00daKROMN\u00c9 AKCIE',
        'icon': 'extracted_assets/icon_catering.svg',
        'perex': 'Priprav\u00edme pre v\u00e1s nezabudnute\u013en\u00fd gastronomick\u00fd z\u00e1\u017eitok. Nad\u00fdchan\u00e9 bao buchti\u010dky, finger food bufet a live cooking stanice obohatia ka\u017ed\u00fa udalos\u0165.',
        'sections': [
            ('MO\u017dNOSTI CATERINGU', [
                'LIVE COOKING BAO STANICA \u2014 Na\u0161i kuch\u00e1ri naparuj\u00fa a plnia \u017eemli\u010dky priamo pred va\u0161imi hos\u0165ami',
                'FINGER FOOD & BUFETOV\u00dd SERVIS \u2014 Mini bao, gyoza ta\u0161ti\u010dky, jarn\u00e9 rolky a \u00e1zijsk\u00e9 \u0161al\u00e1tov\u00e9 misky',
                'FOOD TRUCK CATERING \u2014 Mobiln\u00fd street food priamo pred va\u0161ou budovou alebo v z\u00e1hrade',
                'OFFICE DROP-OFF \u2014 Pohodln\u00e9 doru\u010denie tepl\u00e9ho balen\u00e9ho cateringov\u00e9ho boxu do kancel\u00e1rie'
            ]),
            ('CATERINGOV\u00c9 BAL\u00cdKY', [
                'STARTER PACK (od 20 os\u00f4b) \u2014 2x bao na osobu + mini pr\u00edlohy + dom\u00e1ce dipy a om\u00e1\u010dky',
                'FULL EXPERIENCE (od 50 os\u00f4b) \u2014 3x bao na osobu + mix tapas (edamame, gyoza, krevety) + sladk\u00e9 vypr\u00e1\u017ean\u00e9 bao s karamelom',
                'CUSTOM EVENT \u2014 Menu na mieru vr\u00e1tane remeseln\u00fdch nealko n\u00e1pojov, yuzu limon\u00e1d a \u00e1zijsk\u00fdch p\u00edv'
            ]),
            ('DI\u00c9TY A PREFERENCIE', [
                'Plnohodnotn\u00e9 veg\u00e1nske a vegetari\u00e1nske verzie ka\u017ed\u00e9ho chodu',
                'Detailn\u00e9 ozna\u010denie alerg\u00e9nov a individu\u00e1lne prisp\u00f4sobenie recept\u00far'
            ])
        ],
        'cta': 'Z\u00edskajte nez\u00e1v\u00e4zn\u00fa cenov\u00fa ponuku pre va\u0161u akciu: catering@baobrothers.sk | +421 900 123 456'
    },
    {
        'id': 'restauracia',
        'title': 'RE\u0160TAUR\u00c1CIA',
        'subtitle': 'U\u017d 1. DECEMBRA OTV\u00c1RAME NA\u0160U PRV\u00da KAMENN\u00da PREV\u00c1DZKU NA DUNAJSKEJ 7',
        'icon': 'extracted_assets/icon_restauracia.svg',
        'perex': 'Z ulice do vlastn\u00e9ho priestoru! Prv\u00e1 st\u00e1la kamenn\u00e1 re\u0161taur\u00e1cia Bao Brothers otv\u00e1ra svoje dvere u\u017e 1. decembra na Dunajskej ulici 7 v Bratislave.',
        'sections': [
            ('LOK\u00c1CIA & OTV\u00c1RACIE HODINY', [
                'Adresa: Dunajsk\u00e1 7, 811 08 Bratislava \u2013 Star\u00e9 Mesto',
                'Sl\u00e1vnostn\u00e9 otvorenie: 1. decembra 2026',
                'Otv\u00e1racie hodiny: Pondelok a\u017e Nede\u013ea: 11:00 \u2013 22:00',
                'Pr\u00edjemn\u00e9 sedenie v modernom industri\u00e1lnom dizajne s otvorenou kuchy\u0148ou'
            ]),
            ('NA \u010cO SA M\u00d4\u017dETE TE\u0160I\u0164 V MENU', [
                '\u0160IROK\u00dd V\u00ddBER BAO \u017dEMLI\u010cIEK \u2014 Trhan\u00e9 brav\u010dov\u00e9, pomaly pe\u010den\u00e9 hov\u00e4dzie, marinovan\u00e9 tofu, chrumkav\u00fd b\u00f4\u010dik',
                'POLIEVKY & RAMEN \u2014 12 hod\u00edn \u0165ahan\u00e9 siln\u00e9 v\u00fdvary s dom\u00e1cimi rezancami a marinovan\u00fdm vaj\u00ed\u010dkom',
                'SHARING BOWLS & TAPAS \u2014 Edamame s morskou so\u013eou, dom\u00e1ce kimchi, krevety v tempure, jarn\u00e9 rolky',
                'DRINKY A DEZERTY \u2014 Yuzu dom\u00e1ca limon\u00e1da, li\u010di \u013eadov\u00fd \u010daj, v\u00fdberov\u00e1 k\u00e1va, sladk\u00e9 bao s karamelom'
            ]),
            ('REZERV\u00c1CIE A PRIESTORY', [
                'Rezerv\u00e1cie stolov a men\u0161\u00edch skup\u00edn vopred online',
                'Mo\u017enos\u0165 pren\u00e1jmu cel\u00e9ho priestoru pre uzavret\u00fa spolo\u010dnos\u0165'
            ])
        ],
        'cta': 'Pr\u00ed\u010fte ochutna\u0165! Rezerv\u00e1cie a inform\u00e1cie: restauracia@baobrothers.sk | Dunajsk\u00e1 7, Bratislava'
    },
    {
        'id': 'donaska',
        'title': 'DON\u00c1\u0160KA',
        'subtitle': '\u010cERSTV\u00c9 A TEPL\u00c9 BAO PRIAMO K V\u00c1M DOMOV ALEBO DO PR\u00c1CE',
        'icon': 'extracted_assets/icon_donaska.svg',
        'perex': 'Nenechajte sa obmedzova\u0165. Na\u0161e v\u00fdnimo\u010dn\u00e9 bao buchty si m\u00f4\u017eete vychutna\u0165 kdeko\u013evek v\u010faka spo\u013eahlivej a r\u00fdchlej don\u00e1\u0161ke.',
        'sections': [
            ('KDE N\u00c1S OBJEDN\u00c1TE', [
                'WOLT \u2014 R\u00fdchle doru\u010denie v r\u00e1mci Bratislavy so sledovan\u00edm kuri\u00e9ra v re\u00e1lnom \u010dase',
                'BOLT FOOD \u2014 Expresn\u00fd rozvoz a pravideln\u00e9 zv\u00fdhodnen\u00e9 ponuky',
                'BISTRO.SK \u2014 Tradi\u010dn\u00e9 a preh\u013eadn\u00e9 objedn\u00e1vanie cez web aj mobiln\u00fa aplik\u00e1ciu',
                'FIREMN\u00dd ROZVOZ \u2014 Pl\u00e1novan\u00e9 obedov\u00e9 dod\u00e1vky v\u00e4\u010d\u0161\u00edch po\u010dtov priamo z kuchyne'
            ]),
            ('KVALITA A BALENIE', [
                '\u0160peci\u00e1lne paropriepustn\u00e9 termo-obaly zaru\u010duj\u00fa, \u017ee \u017eemli\u010dky zostan\u00fa nad\u00fdchan\u00e9 a nezvlhn\u00fa',
                'Om\u00e1\u010dky, pos\u00fdpky a bylinky s\u00fa balen\u00e9 samostatne pre maxim\u00e1lnu chrumkavos\u0165',
                'Ekologick\u00e9 100% kompostovate\u013en\u00e9 gastro balenia'
            ]),
            ('ZV\u00ddHODNEN\u00c9 COMBO MENU', [
                'SOLO COMBO \u2014 2x Bao pod\u013ea v\u00fdberu + hranolky s dipom + n\u00e1poj',
                'DUO COMBO \u2014 4x Bao pod\u013ea v\u00fdberu + 2x pr\u00edloha + 2x dom\u00e1ca limon\u00e1da',
                'BAO PARTY BOX (10 ks) \u2014 Skvel\u00e1 vo\u013eba na rodinn\u00fa ve\u010deru alebo firemn\u00fd meeting'
            ])
        ],
        'cta': 'Otvorte aplik\u00e1ciu Wolt, Bolt Food alebo Bistro.sk a zadajte Bao Brothers! Don\u00e1\u0161ka: donaska@baobrothers.sk'
    }
]

with open('Public/BAO_LOGO.svg', 'r') as f:
    logo_svg = f.read()

os.makedirs('pdf_build', exist_ok=True)
os.makedirs('pdf', exist_ok=True)

for p in pdf_defs:
    with open(p['icon'], 'r') as f:
        icon_svg = f.read()

    sections_html = ''
    for stitle, slist in p['sections']:
        items_html = ''.join(f'<li>{item}</li>' for item in slist)
        sections_html += f'''
        <div class="section-block">
          <div class="section-title">{stitle}</div>
          <ul class="section-list">
            {items_html}
          </ul>
        </div>
        '''

    html = f'''<!DOCTYPE html>
<html lang="sk">
<head>
<meta charset="utf-8">
<title>BAO BROTHERS — {p['title']}</title>
<style>
  @font-face {{
    font-family: 'DIN Condensed';
    src: url('../Public/DIN Condensed Bold.ttf') format('truetype');
    font-weight: bold;
  }}
  @page {{
    size: A4 portrait;
    margin: 12mm 18mm;
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #111111;
    margin: 0;
    padding: 0;
    background: #ffffff;
    line-height: 1.4;
  }}
  .header {{
    text-align: center;
    padding-bottom: 14px;
    border-bottom: 2px solid #000000;
  }}
  .logo {{
    max-width: 320px;
    height: auto;
    display: inline-block;
  }}
  .hero {{
    text-align: center;
    margin-top: 18px;
    margin-bottom: 18px;
  }}
  .icon-img {{
    width: 150px;
    height: 120px;
    object-fit: contain;
    margin: 0 auto 10px auto;
    display: block;
  }}
  .title {{
    font-family: 'DIN Condensed', sans-serif;
    font-size: 46px;
    letter-spacing: 2px;
    margin: 0 0 4px 0;
    text-transform: uppercase;
    color: #000000;
  }}
  .subtitle {{
    font-family: 'DIN Condensed', sans-serif;
    font-size: 20px;
    letter-spacing: 1px;
    margin: 0 0 10px 0;
    text-transform: uppercase;
    color: #333333;
  }}
  .perex {{
    font-size: 14px;
    color: #222222;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.5;
  }}
  .content-grid {{
    margin-top: 14px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .section-block {{
    background: #f8f8f8;
    border-left: 4px solid #000000;
    padding: 12px 18px;
    border-radius: 0 8px 8px 0;
  }}
  .section-title {{
    font-family: 'DIN Condensed', sans-serif;
    font-size: 21px;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin: 0 0 6px 0;
    color: #000000;
  }}
  .section-list {{
    margin: 0;
    padding-left: 20px;
    font-size: 13px;
    color: #222222;
    line-height: 1.5;
  }}
  .section-list li {{
    margin-bottom: 4px;
  }}
  .cta-box {{
    margin-top: 18px;
    padding: 14px 20px;
    background: #000000;
    color: #ffffff;
    border-radius: 30px;
    text-align: center;
    font-size: 13.5px;
    font-weight: 500;
  }}
  .footer {{
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #e0e0e0;
    text-align: center;
    font-family: 'DIN Condensed', sans-serif;
    font-size: 16px;
    letter-spacing: 1.5px;
    color: #666666;
    text-transform: uppercase;
  }}
</style>
</head>
<body>
  <div class="header">
    <img src="../assets/images/bao-brothers-logo.svg" alt="Bao Brothers" class="logo">
  </div>

  <div class="hero">
    <img src="../assets/images/icon-{p['id']}.svg" alt="{p['title']}" class="icon-img">
    <h1 class="title">{p['title']}</h1>
    <h2 class="subtitle">{p['subtitle']}</h2>
    <p class="perex">{p['perex']}</p>
  </div>

  <div class="content-grid">
    {sections_html}
  </div>

  <div class="cta-box">
    {p['cta']}
  </div>

  <div class="footer">
    Bao Brothers • Food Lab., s.r.o. • Dunajská 7, Bratislava • www.baobrothers.sk
  </div>
</body>
</html>'''

    html_file = f"pdf_build/{p['id']}.html"
    pdf_file = f"pdf/{p['id']}.pdf"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    cmd = [
        '/Applications/Chromium.app/Contents/MacOS/Chromium',
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_file}',
        html_file
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated {pdf_file}, size: {os.path.getsize(pdf_file)} bytes")

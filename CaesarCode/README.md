#Шифр Цезаря

Шифрование сообщения происходит при помощи ключевого символа. Данный шифр относится к моноалфавитным и проще поддается 
криптоанализу. 

Возможности для криптоанализа: 
1. Анализ перебором. (Здесь нам поможет известный друг Цезаря - БРУТ (force) )
2. Частотный анализ, который применим для длинных сообщений. UDP: можно применять комбинационное решение для
поиска и проверки решения

##### На данный момент доступен лишь **Английский Язык**.

### Как с этим работать?

Модель состоит из нескольких частей:
* caesar - обработчик параметров командной строки.

```bash
caesar.py --help
Usage: caesar.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  crack
  crypt
  decrypt
  testcrack
```


* Crypt - содержит в себе функцию шифрования сообщения. На вход подается открытый текст, ключ символ и алфавит.
```bash
caesar.py crypt --help
Usage: caesar.py crypt [OPTIONS]

Options:
  -txt, --text TEXT  The text with which the operation will be performed
  -l, --lang TEXT    Source language
  -k, --key TEXT     Encryption key
  --help             Show this message and exit.
```
* Пример работы crypt:
```bash
caesar.py crypt -txt "HELLO CEASAR" -l eng -k T
AXEEHVXTLTK
```

* Decrypt - содержит в себе функцию для расшифрования сообщения. На вход подается зашифрованный текст, ключ-символ и
алфавит.
```bash
caesar.py decrypt --help
Usage: caesar.py decrypt [OPTIONS]

Options:
  -txt, --text TEXT  The text with which the operation will be performed
  -l, --lang TEXT    Source language
  -k, --key TEXT     Decryption key
  --help             Show this message and exit.
```
* Пример работы decrypt:
```bash
caesar.py decrypt -txt AXEEHVXTLTK -l eng -k T
HELLOCEASAR
```

* Bruteforce (crack) - осуществляет пепребор всех возможных значений для данного алфавита. На вход подается шифрованный 
текст, алфавит и тип частотного анализа. (Тип частотного анализа указывается при помощи цифры от 0 до 4, 
где 0 - отсутствие анализа) 
```bash
caesar.py crack --help
Usage: caesar.py crack [OPTIONS]

Options:
  -txt, --text TEXT  The text with which the operation will be performed
  -l, --lang TEXT    Source language
  -t, --type TEXT    Type of Frequency analise: 0-without analise,
                     1-monogramms, 2-bigramms, 3-trigramms, 4-quadgramms
  --help             Show this message and exit.
```
* Пример работы crack (без анализа):
```bash
caesar.py crack -txt AXEEHVXTLTK -l eng -t 0
A AXEEHVXTLTK
B ZWDDGUWSKSJ
C YVCCFTVRJRI
D XUBBESUQIQH
E WTAADRTPHPG
F VSZZCQSOGOF
G URYYBPRNFNE
H TQXXAOQMEMD
I SPWWZNPLDLC
J ROVVYMOKCKB
K QNUUXLNJBJA
L PMTTWKMIAIZ
M OLSSVJLHZHY
N NKRRUIKGYGX
O MJQQTHJFXFW
P LIPPSGIEWEV
Q KHOORFHDVDU
R JGNNQEGCUCT
S IFMMPDFBTBS
T HELLOCEASAR
U GDKKNBDZRZQ
V FCJJMACYQYP
W EBIILZBXPXO
X DAHHKYAWOWN
Y CZGGJXZVNVM
Z BYFFIWYUMUL
```
* Пример работы crack (анализ квадграмм, самый медленный, но на мой взгляд самый точный):
```bash
caesar.py crack -txt AXEEHVXTLTK -l eng -t 4
T HELLOCEASAR -37.02526840824202
P LIPPSGIEWEV -47.41187553696612
Q KHOORFHDVDU -54.97332440183301
E WTAADRTPHPG -56.647835478612535
X DAHHKYAWOWN -57.03410418808369
D XUBBESUQIQH -61.78000442944493
J ROVVYMOKCKB -62.61601612469385
L PMTTWKMIAIZ -62.63482048616097
S IFMMPDFBTBS -62.84418259173528
Z BYFFIWYUMUL -63.19443237915769
C YVCCFTVRJRI -64.5712119100042
B ZWDDGUWSKSJ -65.18801344718048
N NKRRUIKGYGX -65.23759363883855
F VSZZCQSOGOF -67.51929929338637
G URYYBPRNFNE -67.88885729451206
V FCJJMACYQYP -68.74635385752262
M OLSSVJLHZHY -70.4650856864941
A AXEEHVXTLTK -70.72237816406563
H TQXXAOQMEMD -71.99276884466659
I SPWWZNPLDLC -72.38032040955274
R JGNNQEGCUCT -73.92241020601092
W EBIILZBXPXO -75.95128343118454
U GDKKNBDZRZQ -76.70140595796794
K QNUUXLNJBJA -76.96450380058319
O MJQQTHJFXFW -80.47462199067607
Y CZGGJXZVNVM -90.30692648140541
```
* Testcrack - функция тестирования анализа. Осуществляет шифрование открытого текста случайным ключом и перебор.
При указании типа частотного анализа - проводит частотный анализ.
```bash
caesar.py testcrack --help
Usage: caesar.py testcrack [OPTIONS]

Options:
  -txt, --text TEXT  The text with which the operation will be performed
  -l, --lang TEXT    Source language
  -t, --type TEXT    Type of Frequency analise: 0-without analise,
                     1-monogramms, 2-bigramms, 3-trigramms, 4-quadgramms
  --help             Show this message and exit.
```
* Пример работы testcrack (частотный анализ монограмм):
```bash
caesar.py testcrack -txt "HELLO CEASAR" -l eng -t 1
Случайный ключ: U
Зашифрованое сообщение: BYFFIWYUMUL
U HELLOCEASAR -13.024688370026384
F WTAADRTPHPG -14.937800388683844
Q LIPPSGIEWEV -15.41713178929925
Y DAHHKYAWOWN -15.762671957832413
H URYYBPRNFNE -15.843380333973602
R KHOORFHDVDU -16.186216100953416
T IFMMPDFBTBS -16.559699201523614
M PMTTWKMIAIZ -17.090572479383013
B AXEEHVXTLTK -17.184627854005257
D YVCCFTVRJRI -17.61347611458535
A BYFFIWYUMUL -17.63597056136379
J SPWWZNPLDLC -17.771471038364332
S JGNNQEGCUCT -17.827916606203132
N OLSSVJLHZHY -18.174123179260206
K ROVVYMOKCKB -18.24236253892907
O NKRRUIKGYGX -18.275921813038902
X EBIILZBXPXO -19.344991815354827
C ZWDDGUWSKSJ -19.592293601666057
E XUBBESUQIQH -19.94579752685979
I TQXXAOQMEMD -20.170127606837877
G VSZZCQSOGOF -20.285316199271996
L QNUUXLNJBJA -20.687588919116884
W FCJJMACYQYP -20.83809291975522
V GDKKNBDZRZQ -21.69760833476668
Z CZGGJXZVNVM -22.81695284614081
P MJQQTHJFXFW -23.012222553494695
```

### Таблица частот для Английского алфавита.

| Буква | Частота % |
|:-----:|:---------:|
| E     | 12,7 
| T     | 9,06 
| A     | 8,17 
| O     | 7,51 
| I     | 6,97 
| N     | 6,75 
| S     | 6,33 
| H     | 6,09 
| R     | 5,99 
| D     | 4,25 
| L     | 4,03 
| C     | 2,78 
| U     | 2,76	 
| M     | 2,41 
| W     | 2,36 
| F     | 2,23 
| G     | 2,02 
| Y     | 1,97 
| P     | 1,93 
| B     | 1,49 
| V     | 0,98 
| K     | 0,77 
| X     | 0,15 
| J     | 0,15 
| Q     | 0,10 
| Z     | 0,05 
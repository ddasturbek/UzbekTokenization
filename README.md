# UzbekTokenization
O‘zbek tilidagi matnlarni belgilarga, bo‘g‘inlarga, affikslarga (qo‘shimchalarga), so‘zlarga, gaplarga va tinish belgilariga ajratish uchun mo‘ljallangan kutubxona. Ushbu kutubxona, O‘zbek tilidagi matnlarni tokenlarga ajratish, so‘zlarning morfologik tuzilishini tahlil qilish va o‘zbek tilida matnni yaxshiroq tushunish uchun zarur bo‘lgan vositalarni taqdim etadi.

## Maqsad
Ushbu loyiha O‘zbek tilidagi matnlarni tokenlash (ajratish) jarayonini amalga oshiradi. Tokenizatsiya – bu matnni kichikroq, tahlil qilinishi mumkin bo‘lgan qismlarga ajratish jarayonidir. Ushbu loyiha asosan tabiiy tilni qayta ishlash (NLP) sohasida ishlatilishi mumkin.

## Xususiyatlar
* **Char Tokenization**: Matnni belgilarga ajratish.
* **Syllable Tokenization**: So‘zni bo‘g‘inlarga ajratish.
* **Affix Tokenization**: So‘zni affikslarga ajratish.
* **Word Tokenization**: Matnni so‘zlarga ajratish.
* **Sent Tokenization**: Matnni gaplarga ajratish.
* **Punc Tokenization**: Matnni tinish begilargacha ajratish.

## GitHub
Loyiha bilan ishlash uchun uni [GitHubdan](https://github.com/ddasturbek/UzbekTokenization) yuklab olish mumkin:
```bash
git clone https://github.com/ddasturbek/UzbekTokenization.git
```

## O‘rnatish
Kutubxonalarni o‘rnatish: Loyihani ishlatish uchun [PyPIdan](https://pypi.org/project/UzbekTokenization) ushbu kutubxonani o‘rnating:
```bash
pip install UzbekTokenization
```

# Foydalanish
Loyihadan foydalanish juda oson. Quyidagi kod namunalari orqali tokenlash jarayonlarini amalga oshirishingiz mumkin.

## Char Tokenization

```Python
from UzCharTokenization import UzCharTokenizer as UCT

print(UCT.tokenize("o‘g‘ri"))  # ['o‘', 'g‘', 'r', 'i']
print(UCT.tokenize("choshgoh"))  # ['ch', 'o', 'sh', 'g', 'o', 'h']
print(UCT.tokenize("bodiring"))  # ['b', 'o', 'd', 'i', 'r', 'i', 'ng']
print(UCT.tokenize("Salom, dunyo!"))  # ['S', 'a', 'l', 'o', 'm', ',', 'd', 'u', 'n', 'y', 'o', '!']
print(UCT.tokenize("Salom, dunyo!", True))  # ['S', 'a', 'l', 'o', 'm', ',', ' ', 'd', 'u', 'n', 'y', 'o', '!']
```
Ushbu **Char Tokenization** dasturi O‘zbek tili harflari uchun to‘g‘ri ishlaydi, chunki O‘zbek tilida **O‘o‘ G‘g‘** harf va belgilar birikmasi va **ShshChchng** digraflar bitta harf hisoblanadi. Agar *tokenize* funksiyasiga ikkinchi parametr sifatida **True** qiymati berilsa, bo‘sh joylarni ham inobatga olgan holda ajratadi.

## Affix Tokenization

```Python
from UzAffixTokenization import UzAffixTokenizer as UAT

print(UAT.tokenize("Serquyosh"))  # Ser-quyosh
print(UAT.tokenize("KITOBLAR"))  # KITOB-LAR
print(UAT.tokenize("o‘qiganman"))  # o‘qi-gan-man
print(UAT.tokenize("Salom odamlar"))  # Salom odamlar
```
Ushbu **Affixes Tokenization** dasturi O‘zbek tili so‘zlarini affikslarga (qo‘shimchalarga) ajratadi. O‘zbek tilida qo‘shimchalar ikki xil bo‘ladi: *so‘z yasovchi* va *shakl yasovchi*. Shakl yasovchi qo‘shimchalar ham o‘z navbatida ikkiga bo‘linadi: *lug‘aviy shakl yasovchi* va *sintaktik shakl yasovchi* qo‘shimchalarga. Dastur aynan sintaktik shakl yasovchi qo‘shimchalarning ikki va undan ko‘p belgidan iborat bo‘lganlarini ajratadi. Chunki so‘z yasovchi, lug‘aviy shakl yasovchi qo‘shimchalar va bitta harfdan iborat sintaktik shakl yasovchi qo‘shimchalar so‘z tarkibidagi harflarga o‘xshash bo‘ladi, bunday holda qo‘shimcha va so‘z tarkibidagi harflarni ajratish murakkab bo‘lib qoladi. Dastur faqat so‘zlarni affikslarga ajratadi, agar matn berilsa uni o‘z holicha qaytaradi. Katta-kichik harflarga sezgir.

## Syllable Tokenization

```Python
from UzSyllabTokenization import UzSyllabTokenizer as UST

print(UST.tokenize("Gul"))  # Gul
print(UST.tokenize("Yulduz"))  # Yul-duz
print(UST.tokenize("shashlik"))  # shash-lik
print(UST.tokenize("BOG‘BON"))  # BOG‘-BON
print(UST.tokenize("kelinglar"))  # ke-ling-lar
print(UST.tokenize("yangilik"))  # yan-gi-lik
print(UST.tokenize("Agglyutinativ"))  # ag-glyu-ti-na-tiv
print(UST.tokenize("Salom barchaga"))  # Salom barchaga
```
Ushu **Syllable Tokenization** dasturi O‘zbek tili so‘zlarini bo‘g‘inlarga ajratadi. Bunda **O‘o‘ G‘g‘** harf va belgilar birikmasi va **ShshChchng** digraflarni to‘g‘ri ajratadi. Bundan tashqari *ng* digraf yoki *n* va *g* alohida harf bo‘lib so‘z tarkibida keladi, bunday hollarda digraf bo‘lsa ular ajralmaydi, alohida kelsa ular ajratilishi mumkin. Ba'zi murakkab so‘zlar qoidalarga tushmaydi, shuning uchun ularning ro‘yhati dastur tarkibida shakllantirilgan. Katta-kichik harflarga sezgir.

## Word Tokenization

```Python
from UzWordTokenization import UzWordTokenizer as UWT

text = "Dasturlash – kompyuterlar va boshqa mikroprotsessorli elektron mashinalar uchun dasturlar tuzish"

print(UWT.tokenize(text))  # ['Dasturlash', '–', 'kompyuterlar', 'va', 'boshqa', 'mikroprotsessorli', 'elektron', 'mashinalar', 'uchun', 'dasturlar', 'tuzish']
print(UWT.tokenize(text, False))  # ['Dasturlash', 'kompyuterlar', 'va', 'boshqa', 'mikroprotsessorli', 'elektron', 'mashinalar', 'uchun', 'dasturlar', 'tuzish']

```
Ushbu **Word Tokenization** dasturi O‘zbek tili matnlarini so‘zlarga ajratadi. Bunda **qo‘shma so‘zlar** (fe'l, ravish, olmosh va undov) va KFSQ (ko‘makchi fe'lli so‘z qo‘shilmasi) larni birgalikda ajratib oladi, masalan, *'idrok etmoq', 'mana bu', 'hech narsa', 'sevib boshlamoq'*. Bundan tashqari *tokenize* funksiyasiga ikkinchi parametr sifatida *False* qiymatini berish orqali, tinish belgilarsiz faqat so‘zlardan iborat tokenlarni olish mumkin.

## Sent Tokenization

```Python
from UzSentTokenization import UzSentTokenizer as UST

text = "Bugun bog‘da sayr qildik. Atrofdagi daraxtlar yam-yashil, " \
       "qushlar esa chug‘urlab sayrayapdi. Bahorning iliq havosi butun " \
       "olamni jonlantirganday tuyuladi. Sen hech shunday sokin va go‘zal " \
       "manzarani ko‘rganmisan? Bu yerda hamma narsa ajib bir go‘zallikka " \
       "ega! Nahotki tabiat bunday mo‘jizalarni yaratishga qodir bo‘lsa? Oh, " \
       "qanday ajoyib kun! Shu lahzalarning hech qachon tugashini istamayman!"

print(UST.tokenize(text))

"""
[
    'Bugun bog‘da sayr qildik.',
    'Atrofdagi daraxtlar yam-yashil, qushlar esa chug‘urlab sayrayapdi.',
    'Bahorning iliq havosi butun olamni jonlantirganday tuyuladi.',
    'Sen hech shunday sokin va go‘zal manzarani ko‘rganmisan?',
    'Bu yerda hamma narsa ajib bir go‘zallikka ega!',
    'Nahotki tabiat bunday mo‘jizalarni yaratishga qodir bo‘lsa?',
    'Oh, qanday ajoyib kun!',
    'Shu lahzalarning hech qachon tugashini istamayman!'
]
"""
```
Ushbu **Sent Tokenization** dasturi matnlarni gaplarga ajratadi. Bunda dastur O‘zbek tili grammatikasining sintaksis qoidalariga asosan bu ishni amalga oshiradi. O‘zbek tilida gaplar, umuman ko‘p tillarda gaplar *[.!?]* belgilari bilan yoki ularni birgalikda ishlatish bilan tugaydi.

## Punc Tokenization

```Python
from UzPuncTokenization import UzPuncTokenizer as UPT

text = """  Bugun juda qiziq voqea ro‘y berdi! Do‘stim bilan shahar bo‘ylab sayr qilayotgan edik, to‘satdan u to‘xtadi-da:

            — Hey, bu yerga qarang! — dedi hayajon bilan.
            
            Men nigohimni u ko‘rsatgan tomonga burdim... Nahotki?! Qarshimda bolalikdagi eng yaxshi do‘stim turardi. U bilan qancha yillardan beri ko‘rishmaganmiz!
            
            — Bu senmisan? — dedim hayrat bilan.
            
            U kulimsirab bosh irg‘adi:
            
            — Ha, menman! Axir, qancha vaqt o‘tdi-a?!
            
            Biz uzoq suhbatlashdik; eski xotiralarni esladik. O‘sha lahzalar men uchun unutilmas bo‘ldi...
        """

print(UPT.tokenize(text))
#  ['Bugun juda qiziq voqea ro‘y berdi', '!', 'Do‘stim bilan shahar bo‘ylab sayr qilayotgan edik', ',', 'to‘satdan u to‘xtadi', '-', 'da', ':', '—', 'Hey', ',', 'bu yerga qarang', '!', '—', 'dedi hayajon bilan', '.', 'Men nigohimni u ko‘rsatgan tomonga burdim', '.', '.', '.', 'Nahotki', '?', '!', 'Qarshimda bolalikdagi eng yaxshi do‘stim turardi', '.', 'U bilan qancha yillardan beri ko‘rishmaganmiz', '!', '—', 'Bu senmisan', '?', '—', 'dedim hayrat bilan', '.', 'U kulimsirab bosh irg‘adi', ':', '—', 'Ha', ',', 'menman', '!', 'Axir', ',', 'qancha vaqt o‘tdi', '-', 'a', '?', '!', 'Biz uzoq suhbatlashdik', ';', 'eski xotiralarni esladik', '.', 'O‘sha lahzalar men uchun unutilmas bo‘ldi', '.', '.', '.']

print(UPT.tokenize(text, False))
# ['Bugun juda qiziq voqea ro‘y berdi', 'Do‘stim bilan shahar bo‘ylab sayr qilayotgan edik', 'to‘satdan u to‘xtadi', 'da', 'Hey', 'bu yerga qarang', 'dedi hayajon bilan', 'Men nigohimni u ko‘rsatgan tomonga burdim', 'Nahotki', 'Qarshimda bolalikdagi eng yaxshi do‘stim turardi', 'U bilan qancha yillardan beri ko‘rishmaganmiz', 'Bu senmisan', 'dedim hayrat bilan', 'U kulimsirab bosh irg‘adi', 'Ha', 'menman', 'Axir', 'qancha vaqt o‘tdi', 'a', 'Biz uzoq suhbatlashdik', 'eski xotiralarni esladik', 'O‘sha lahzalar men uchun unutilmas bo‘ldi']
```
Ushbu **Punc Tokenization** dasturi matnlarni tinish belgilarigacha ajratadi. Tokenni tinish belgilarisiz chiqarish uchun esa, *tokenize* funksiyasiga ikkinchi parametr sifatida *False* qiymati berish lozim.

# Litsenziya
Bu loyiha [MIT License](https://opensource.org/license/mit) litsenziyasiga ega.

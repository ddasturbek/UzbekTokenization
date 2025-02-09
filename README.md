## UzbekTokenization
O‘zbek tilidagi matnlarni belgilarga, bo‘g‘inlarga, affikslarga, so‘zlarga, gaplarga va tinish belgilariga ajratish uchun mo‘ljallangan dastur.

# Maqsad
Ushbu loyiha O‘zbek tilidagi matnlarni tokenlash (ajratish) jarayonini amalga oshiradi. Tokenizatsiya – bu matnni kichikroq, tahlil qilinishi mumkin bo‘lgan qismlarga ajratish jarayonidir. Ushbu loyiha asosan tabiiy tilni qayta ishlash (NLP) sohasida ishlatilishi mumkin.

# Xususiyatlar
* **Char Tokenization**: So‘zni belgilarga ajratish.
* **Syllable Tokenization**: So‘zni bo‘g‘inlarga ajratish.
* **Affix Tokenization**: So‘zni affikslarga ajratish.
* **Word Tokenization**: Matnni so‘zlarga ajratish.
* **Sent Tokenization**: Matnni gaplarga ajratish.
* **Punc Tokenization**: Matnni tinish begilargacha ajratish.

# GitHub
Loyiha bilan ishlash uchun uni [GitHubdan](https://github.com/ddasturbek/UzbekTokenization) yuklab olish mumkin:
```bash
git clone https://github.com/ddasturbek/UzbekTokenization.git
```

# O‘rnatish
Kutubxonalarni o‘rnatish: Loyihani ishlatish uchun [PyPIdan](https://pypi.org/project/UzbekTokenization) ushbu kutubxonani o‘rnating:
```bash
pip install UzbekTokenization
```

## Foydalanish
Loyihadan foydalanish juda oson. Quyidagi kod namunalari orqali tokenlash jarayonlarini amalga oshirishingiz mumkin:

# Char Tokenization

```Python
from UzCharTokenization import UzCharTokenizer as UCT

print(UCT.tokenize("o‘g‘ri"))  # ['o‘', 'g‘', 'r', 'i']
print(UCT.tokenize("choshgoh"))  # ['ch', 'o', 'sh', 'g', 'o', 'h']
print(UCT.tokenize("bodiring"))  # ['b', 'o', 'd', 'i', 'r', 'i', 'ng']
print(UCT.tokenize("Salom, dunyo!"))  # ['S', 'a', 'l', 'o', 'm', ',', 'd', 'u', 'n', 'y', 'o', '!']
print(UCT.tokenize("Salom, dunyo!", True))  # ['S', 'a', 'l', 'o', 'm', ',', ' ', 'd', 'u', 'n', 'y', 'o', '!']
```
Ushbu **Char Tokenization** dasturi O‘zbek tili harflari uchun to‘g‘ri ishlaydi, chunki O‘zbek tilida **O‘o‘ G‘g‘** harf va belgilar birikmasi va **ShshChchng** digraflar bitta harf hisoblanadi. Agar *tokenize* funksiyasiga ikkinchi parametr sifatida **True** qiymati berilsa, bo‘sh joylarni ham inobatga olgan holda ajratadi.

# 

## Litsenziya
Bu loyiha [MIT License](https://github.com/ddasturbek/UzbekTokenization?tab=MIT-1-ov-file) litsenziyasiga ega.

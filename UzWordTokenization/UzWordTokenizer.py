import re


def __division(tokens):
    new_tokens = []

    for token in tokens:
        # Separating characters at the beginning and end
        match = re.match(r'^(\W*)(.*?)(\W*)$', token)
        if match:
            start_punct, content, end_punct = match.groups()

            # If there are beginning and ending characters, they are added separately
            if start_punct:
                # If there are multiple characters at the beginning, they are separated separately
                if len(start_punct) > 1:
                    for char in start_punct:
                        new_tokens.append(char)
                else:
                    new_tokens.append(start_punct)
            if content:
                new_tokens.append(content)
            if end_punct:
                # If there are multiple characters at the ending, they are separated separately
                if len(end_punct) > 1:
                    for char in end_punct:
                        new_tokens.append(char)
                else:
                    new_tokens.append(end_punct)

    return new_tokens


def __gerund(tokens):
    # Save the original tokens to refer back to them later after transformations
    original_tokens = tokens

    tokens = [item.lower() for item in tokens]
    new_tokens = [original_tokens[0]]

    # Iterate over the tokens starting from the second token
    for i in range(1, len(tokens)):
        # Check if the previous token ends with '-(u)v' and the current token is one of the key words
        if tokens[i-1][-1] == 'v' and (tokens[i] in ['kerak', 'lozim', 'shart', 'darkor']):
            del new_tokens[len(new_tokens)-1]
            new_tokens.append(original_tokens[i-1] + ' ' + original_tokens[i])

        elif tokens[i-1][-2:] == 'sh' and (tokens[i] in ['kerak', 'lozim', 'shart', 'darkor']):
            del new_tokens[len(new_tokens)-1]
            new_tokens.append(original_tokens[i-1] + ' ' + original_tokens[i])

        elif tokens[i-1][-3:] == 'moq' and (tokens[i] in ['kerak', 'lozim', 'shart', 'darkor']):
            del new_tokens[len(new_tokens)-1]
            new_tokens.append(original_tokens[i-1] + ' ' + original_tokens[i])

        elif tokens[i-1][-3:] == 'mak' and (tokens[i] in ['kerak', 'lozim', 'shart', 'darkor']):
            del new_tokens[len(new_tokens)-1]
            new_tokens.append(original_tokens[i-1] + ' ' + original_tokens[i])

        # If none of the conditions are met, just add the current token to the new token list
        else:
            new_tokens.append(original_tokens[i])

    return new_tokens


def __change_apostrophe(text):
    # Function to swap the sign of the letters O‘o‘ and G‘g‘

    text = text.replace(f"O{chr(39)}", f"O{chr(8216)}")  # ord("'") -> ord("‘")
    text = text.replace(f"o{chr(39)}", f"o{chr(8216)}")
    text = text.replace(f"G{chr(39)}", f"G{chr(8216)}")
    text = text.replace(f"g{chr(39)}", f"g{chr(8216)}")

    text = text.replace(f"O{chr(96)}", f"O{chr(8216)}")  # ord("`") -> ord("‘")
    text = text.replace(f"o{chr(96)}", f"o{chr(8216)}")
    text = text.replace(f"G{chr(96)}", f"G{chr(8216)}")
    text = text.replace(f"g{chr(96)}", f"g{chr(8216)}")

    text = text.replace(f"O{chr(699)}", f"O{chr(8216)}")  # ord("ʻ") -> ord("‘")
    text = text.replace(f"o{chr(699)}", f"o{chr(8216)}")
    text = text.replace(f"G{chr(699)}", f"G{chr(8216)}")
    text = text.replace(f"g{chr(699)}", f"g{chr(8216)}")

    text = text.replace(f"O{chr(700)}", f"O{chr(8216)}")  # ord("ʼ") -> ord("‘")
    text = text.replace(f"o{chr(700)}", f"o{chr(8216)}")
    text = text.replace(f"G{chr(700)}", f"G{chr(8216)}")
    text = text.replace(f"g{chr(700)}", f"g{chr(8216)}")

    text = text.replace(f"O{chr(8217)}", f"O{chr(8216)}")  # ord("’") -> ord("‘")
    text = text.replace(f"o{chr(8217)}", f"o{chr(8216)}")
    text = text.replace(f"G{chr(8217)}", f"G{chr(8216)}")
    text = text.replace(f"g{chr(8217)}", f"g{chr(8216)}")

    return text


def __compound(tokens):
    # List of compound words
    compound_words = [
        # Adverb (71 units)
        [
            "bir dam", "bir kam", "bir payt", "bir qancha", "bir safar", "bir yo‘la",
            "bir yo‘lasi", "bir zamon", "bir zumda", "bu joyda", "bu kunda", "bu oyda",
            "bu vaqtda", "hali beri", "hali zamon", "har birsi", "har chorshanba", "har damda",
            "har doim", "har dushanba", "har juma", "har kechasi", "har kun", "har oqshom",
            "har payshanba", "har peshinda", "har safar", "har seshanba", "har shanba", "har soat",
            "har soniya", "har tun", "har vaqt", "har yakshanba", "har yer", "har yil",
            "har zamon", "hech bir", "hech kimsa", "hech mahal", "hech narsa", "hech vaqt",
            "hech zamon", "o‘sha daqiqada", "o‘sha joyda", "o‘sha kunda", "o‘sha oyda", "o‘sha safar",
            "o‘sha soatda", "o‘sha soniyada", "o‘sha tongda", "o‘sha tunda", "o‘sha yerda", "o‘sha zamonda",
            "shu daqiqada", "shu haftada", "shu joyda", "shu kunda", "shu oqshomda", "shu orada",
            "shu oyda", "shu payt", "shu safar", "shu soatda", "shu soniyada", "shu tongda",
            "shu vaqtda", "shu yaqinda", "shu yer", "shu zamonda", "tez orada"
        ],
        # Pronoun (26 units)
        [
            "ana o‘sha", "ana shu", "ana shular", "ana u", "bir kishi", "bir nima",
            "har bir", "har kim", "har narsa", "har nima", "har qachon", "har qanday",
            "har qaysi", "hech bir", "hech kim", "hech narsa", "hech nima", "hech qachon",
            "hech qanaqa", "hech qanday", "hech qayer", "hech qaysi", "mana bu",
            "mana bular", "mana shu", "mana shular"
        ],
        # Interjection (12 units)
        [
            "assalomu alaykum", "bor bo‘ling", "omon bo‘ling", "osh bo‘lsin",
            "salomat bo‘ling", "sog‘ bo‘ling", "vaalaykum assalom", "xush kelibsiz",
            "xush ko‘rdik", "xushvaqt bo‘ling", "xo‘p bo‘ladi", "yaxshi boring"
        ]
    ]

    # List of verb compound words (383 units)
    verb_compound_words = [
        "a’zo bo‘l", "a’zo qil", "ado et", "ahd qil", "aks et", "aks qil", "amal bajar", "amal qil", "amalga osh",
        "amalga oshir", "aniq bo‘l", "aniq qil", "aslini olmoq", "asos sol", "avj ol", "ayon bo‘l", "band bo‘l",
        "band et", "band qil", "bartaraf et", "bartaraf qil", "bas qil", "bayon ayla", "bayon et", "bayon qil",
        "bayram bo‘l", "bayram qil", "befarq bo‘l", "befarq tut", "begona bo‘l", "bir bo‘l", "birga bo‘l",
        "birga kel", "birga qol", "bo‘sa ol", "bor kel", "buyruq ber", "buyruq qil", "chegara tort", "chiq ket",
        "chiqar kel", "chirs et", "chop et", "chop qil", "dahshat sol", "darak ber", "darak qil", "davom et",
        "davom qil", "do‘q qil", "dod qil", "dod sol", "duch bo‘l", "duch kel", "duchor ayla", "duchor bo‘l",
        "duchor qil", "e’lon qil", "e’tibor ber", "e’tibor qarat", "e’tibor qil", "esga ol", "esga sol",
        "faol bo‘l", "faol qil", "faraz ayla", "faraz et", "faraz qil", "farmon ber", "farq qil", "fikr ber",
        "fikr qil", "foyda ber", "foyda ol", "foyda qil", "gapga qo‘y", "gapga sol", "gapga tut", "gumbur et",
        "gumon qil", "gunoh ayla", "gunoh qil", "hadik qil", "hal qil", "halok ayla", "halok bo‘l", "halok qil",
        "haqorat et", "haqorat qil", "harakat ayla", "harakat qil", "harakatda bo‘l", "hayron bo‘l", "himoya qil",
        "himoyaga ol", "hisobga ol", "hojatini chiq", "hosil ber", "hosil bo‘l", "hosil kir", "hosil qil",
        "hozir qil", "hurmat ayla", "hurmat et", "hurmat qil", "hushidan ket", "hushiga kel", "hushyor bo‘l",
        "ibrat bo‘l", "ichiga ol", "idrok et", "idrok qil", "ijod et", "ijod qil", "iltimos ayla", "iltimos qil",
        "imkon ber", "imkon qil", "imzo chek", "imzo qo‘y", "iqror bo‘l", "ishla chiq", "ixlos qil",
        "jahlidan tush", "javob ol", "jazavaga ayla", "jazavaga tush", "jim bo‘l", "joriy et", "joriy qil",
        "joyga tush", "kasal bo‘l", "kasal qil", "kasb et", "katta qil", "kir bo‘l", "kir chiq", "kir qil",
        "ko‘z yum", "ko‘zdan kechir", "kuchga kir", "kuchli bo‘l", "kuchli qil", "ma’lum qil", "ma’ruza et",
        "ma’ruza qil", "madad ber", "mahrum ayla", "mahrum bo‘l", "mahrum qil", "meros bo‘l", "meros qil",
        "mohir bo‘l", "mohir qil", "mushohada qil", "natija ber", "natija ol", "natija qil", "nazar sol",
        "nazarda tut", "o‘pich ol", "o‘rnidan tur", "o‘rniga kel", "o‘sal bo‘l", "o‘sal qil", "o‘yga tol",
        "o‘zi kel", "obod ayla", "obod bo‘l", "obod et", "obod qil", "ogoh ayla", "ogoh bo‘l", "ogoh et",
        "ogoh qil", "oh sol", "oh tort", "ol bor", "ol kel", "olib kel", "olib kir", "or qil", "orqaga tush",
        "oson bo‘l", "oson qil", "ovora bo‘l", "ovora qil", "ovoza et", "ovoza qil", "oz bo‘l", "ozod qil",
        "ozod qil", "ozor chek", "pand ber", "parvarish ayla", "parvarish et", "parvarish qil", "pastga tush",
        "paydo bo‘l", "paydo qil", "po‘pisa qil", "qabul ayla", "qabul qil", "qadr top", "qanday bo‘l",
        "qanday qil", "qaror ayla", "qaror ber", "qaror qil", "qayd et", "qayd qil", "qayt qil", "qidir chiq",
        "qiymat ayla", "qiymat ber", "qo‘l ur", "qo‘yib yubor", "qoyil qil", "qoyil qol", "qul qil", "quloq ber",
        "quloq os", "quloq sol", "quloq tut", "rahm ayla", "rahm qil", "ravshan bo‘l", "rioya qil", "ro‘yxat qil",
        "ro‘yxatdan o‘t", "ro‘yxatga ol", "rozi bo‘l", "ruxsat et", "ruxsat qil", "sabab bo‘l", "saboq chiqar",
        "saboq ol", "sabr qil", "salom ayt", "salom ber", "samimiy bo‘l", "sarf et", "sarf qil", "sarson bo‘l",
        "sarson qil", "savo ber", "savol ayla", "savol ber", "savol tug‘", "savolga tut", "sayr ayla", "sayr qil",
        "shafqat ayla", "shafqat qil", "sharh qil", "shod et", "shod qil", "shunday bo‘l", "shunday qil",
        "silliq qil", "so‘z ber", "so‘zga sol", "sodir bo‘l", "sodir et", "sodir qil", "sog‘ bo‘l", "sot ol",
        "sovuq qot", "sukut ayla", "sukut qil", "sukut saqla", "ta’lim ber", "ta’lim qil", "ta’rif ayt",
        "ta’rif et", "ta’rif qil", "ta’sir ayla", "ta’sir et", "ta’sir ko‘r", "ta’sir qil", "ta’sir qil",
        "ta’sis et", "ta’sis qil", "tadbiq qil", "tafovut qil", "tahrir ayla", "tahrir qil", "tajang bo‘l",
        "tajang qil", "tajriba o‘tkaz", "tajriba oshir", "taklif et", "talab et", "talab etil", "talab qil",
        "talif qil", "tamom bo‘l", "tamom qil", "tan ber", "tan ol", "tanbeh ber", "taqdim et", "taqdim qil",
        "taraq et", "tarbiya ber", "tarbiya qil", "tark ayla", "tark qil", "tarkib top", "tartib qil",
        "tartibga sol", "tartibga solin", "tasdiq et", "tasdiq qil", "tashkil qil", "tashla ket", "tashrif ayla",
        "tashrif buyur", "tasnif qil", "tavba qil", "tavsiya et", "tavsiya qil", "taxmin ayla", "taxmin et",
        "taxmin qil", "tekis qil", "telefon qil", "tez qil", "tinch et", "tinch tur", "to‘q bo‘l", "to‘y qildi",
        "tort ol", "toza bo‘l", "toza qil", "turmush qil", "turmush qur", "turmushga chiq", "turt ket", "uf de",
        "uf tort", "uh ur", "uyal qol", "uyatga qol", "va’da qil", "vada ber", "vada et", "vada qil", "vafo ayla",
        "vafo et", "vafo qil", "vertikal tush", "vujudga kel", "xabar ayla", "xabar ber", "xabar ol", "xabar qil",
        "xafa bo‘l", "xafa qil", "xarid ayla", "xarid qil", "xizmat ko‘rsat", "xizmat qil", "xulosa ber",
        "xulosa chiqar", "xulosaga kel", "xursand bo‘l", "xuruj qil", "yangi bo‘l", "yangi qil", "yetarli bo‘l",
        "yetarli qil", "yo‘l ber", "yordam ayla", "yordam ber", "yordam qil", "yordam so‘ra", "yosh to‘k",
        "yoz qoldir", "yuz ber", "yuzaga kel", "zabt et", "zabt qil"
    ]

    # Flatten the compound_words list for easier checking
    all_compound_words = []
    for category in compound_words:
        all_compound_words.extend(category)

    # Initialize an empty list to store the new tokens
    new_tokens = []
    i = 0
    while i < len(tokens):
        # Check for compound words with 2 tokens
        if i + 1 < len(tokens):
            two_word = tokens[i] + ' ' + tokens[i + 1]
            if __change_apostrophe(two_word).lower() in [word for word in all_compound_words]:
                new_tokens.append(two_word)
                i += 2
                continue

        # Check for verb compound words (with affixes)
        if i + 1 < len(tokens):
            # Check if the current token and the next token form a verb compound
            for lemma in verb_compound_words:
                if __change_apostrophe(tokens[i]).lower().startswith(lemma.split()[0]) and __change_apostrophe(tokens[i + 1]).lower().startswith(lemma.split()[1]):
                    new_tokens.append(tokens[i] + ' ' + tokens[i + 1])
                    i += 2
                    break
            else:
                # If no compound word is found, add the current token as is
                new_tokens.append(tokens[i])
                i += 1
        else:
            # If no compound word is found, add the current token as is
            new_tokens.append(tokens[i])
            i += 1

    return new_tokens


def __kfsq(tokens):  # noqa

    # Total 485 units
    kfsq = [  # Uzbek: Ko‘makchi fe'lli so‘z qo‘shilmasi
        "alahsira chiq", "angla tur", "angla yet", "art bo‘l", "art boshla", "art chiq", "art ol", "ayir chiq", "ayir ol",
        "aylan chiq", "aylan kel", "aylan yur", "ayt qol", "ayt tashla", "ayt tur", "aytib berdi", "aytib yubordi",
        "baqir chiq", "baqir tashla", "belgila chiq", "belgila ol", "belgila qo‘y", "belgila tashla", "ber tur", "bil yur",
        "bo‘l o‘t", "bo‘l qol", "bo‘l tashla", "bo‘zray tur", "boq tur", "boq yur", "bor tur", "bor yur", "borib keldi",
        "bukilib-bukilib ketdi", "buzil ket", "chaqir kel", "charcha boshla", "chay boshla", "chay ol", "chay qo‘y",
        "chay tashla", "chiq ket", "chiq qol", "chiz tur", "cho‘chi ket", "cho‘zil ket", "dikkay qol", "dikkay tur",
        "dodla boshla", "dodla chiq", "durilla ket", "eskir ket", "eskir qol", "foydalan kel", "gapir boshla", "gapir chiq",
        "gapir ket", "gapir qo‘y", "gapir tashla", "hilpira boshla", "hilpirab tur", "hisobla chiq", "hisobla tashla",
        "hurk boshla", "hurk ket", "hurk qol", "hurpay ket", "hurpay tur", "ich tashla", "il qo‘y", "ishla qol",
        "ishla tashla", "ishla tur", "ishla yot", "ishla yur", "jo‘na boshla", "jo‘na ket", "jo‘na qol", "jo‘nat ber",
        "jo‘nat tashla", "jo‘nat tur", "jo‘nat yubor", "kech chiq", "kech o‘t", "kechik kel", "kechik qol", "keksay qol",
        "kel qol", "kel tur", "kel yur", "keltir tashla", "keltir tur", "keng boshla", "keng ket", "keng qol",
        "kengayib ketdi", "kirit ol", "kirit qol", "kiy ol", "kiy yur", "ko‘ch ket", "ko‘chir ol", "ko‘chir tashla",
        "ko‘kar ket", "ko‘kar qol", "ko‘pay ket", "ko‘paytir tur", "ko‘r chiq", "ko‘r ol", "ko‘r qol", "ko‘r tashla",
        "ko‘r tur", "ko‘rib chiq", "ko‘rsat qo‘y", "ko‘rsat tashla", "ko‘rsat tur", "ko‘tarib oldi", "ko‘taril tur",
        "kuchaytir ber", "kuchaytir qo‘y", "kul boshla", "kul chiq", "kul ol", "kul tur", "kul yot", "kula boshla",
        "kut boshla", "kut ol", "kut tur", "kut yur", "kuyla ber", "kuyla bo‘l", "kuyla boshla", "kuyla ket", "kuzat qol",
        "maqta boshla", "maqta tashla", "o‘l tashla", "o‘qi chiq", "o‘qi olmoq", "o‘qi tashla", "o‘qi tur", "o‘qi yur",
        "o‘qib chiqdim", "o‘tir chiq", "o‘tir qol", "o‘yla chiq", "o‘yla ket", "o‘yla ko‘r", "o‘yla tur", "o‘yla yur",
        "o‘ylab turibdi", "o‘ylab yuripti", "o‘ylan qol", "o‘ylanib", "o‘ylanib qoldi", "o‘zgar ket", "o‘zgar qol",
        "o‘zlashtir ol", "och qo‘y", "och tashla", "olib keldi", "oqar ket", "oqib ket", "oqsa tur", "oqsa yur", "osh bor",
        "osh ket", "otilib chiq", "ozay ket", "ozay qol", "pasay ket", "pasay qol", "qama qo‘y", "qama tashla", "qara tur",
        "qarash yur", "qaytar ber", "qazi boshla", "qazi tashla", "qil qo‘y", "qil tashla", "qilib ber", "qir tashla",
        "qir yur", "qirq tashla", "qisqart qo‘y", "qiyna tashla", "qizarib ket", "qizarib qol", "qo‘ng‘iroq qilib tur",
        "qo‘rq ket", "qo‘rq tur", "qo‘rq yur", "qo‘sh ayt", "qo‘sh tashla", "qo‘sh yubor", "qopla ol", "qoq kel", "qot qol",
        "ranjit qo‘y", "sakra yur", "sana boshla", "sana chiq", "sana keta", "saqla tur", "saqla yur", "sarg‘ay ket",
        "sarg‘ay qol", "sayra chiq", "sev boshla", "shalpay qol", "shil tashla", "shosh qol", "so‘k tashla", "so‘ra tur",
        "so‘ra yur", "so‘zla tashla", "sog‘ay boshla", "sog‘ay ket", "sog‘ay olmoq", "sot tashla", "supur tashla",
        "supur tur", "supur yur", "sur qo‘y", "sur tashla", "susay qol", "suvsira qol", "suyul ket", "ta’minla ber",
        "ta’minla ol", "ta’minla tur", "tarqat ber", "tarqat tur", "tarqat yur", "tebrat tur", "tebrat yur", "tekshir boshla",
        "tekshir chiq", "tekshir ol", "tekshir qol", "termul tur", "tezlat qo‘y", "tinch qol", "titrat tur", "to‘k tashla",
        "to‘la tur", "to‘la yur", "to‘ldir bo‘l", "to‘ldir tashla", "to‘zg‘it tashla", "top ber", "tort tashla",
        "tortish boshla", "turtil ket", "tush boshla", "tush qol", "tushin ol", "tushir ber", "tushir yubor", "tushun tur",
        "tutib qol", "tuzla boshla", "tuzla chiq", "tuzla qo‘y", "tuzla tashla", "uch yur", "uchrash boshla", "uchrash kel",
        "uchrash qol", "uchrash tur", "uchrash yur", "ulg‘ay ket", "ur tashla", "ur tur", "urish boshla", "urish ket",
        "urish tur", "urish yur", "ushla boshla", "ushla ol", "ushla qol", "ushla tur", "uxlab qoldi", "uyqisira chiq",
        "yarat bo‘l", "yarat chiq", "yarat ol", "yarat tashla", "yarqira ket", "yasha boshla", "yashir tashla",
        "yashirin tur", "yashirin yur", "ye tashla", "ye tur", "yeb qo‘ydi", "yech ol", "yech qo‘y", "yech tashla",
        "yetkaz ber", "yig‘ boshla", "yig‘la ket", "yiqil ket", "yiqila yozdi", "yodla boshla", "yodla chiq", "yodla tashla",
        "yomonla tashla", "yoq qol", "yoq tashla", "yoqib tush", "yorit tur", "yorit yur", "yot qol", "yoz ber", "yoz chiq",
        "yoz o‘tir", "yoz ol", "yoz tashla", "yoz tur", "yoz yur", "yoza boshladi", "yozib tashladi", "yugur tur",
        "yur boshla", "yur ket", "yura boshladi", "yura ketti", "yuv tashla", "yuvin tur", "yuvintir qo‘y", "achin boshla",
        "achin ol", "achin qo‘y", "ajrat ko‘rsat", "art qo‘y", "art tashla", "art yubor", "art yur", "ayt ber", "bil boshla",
        "bil ol", "bil qol", "bo‘g‘a ol", "bo‘l ol", "bo‘shash boshla", "bo‘shash ol", "bo‘shash qol", "bog‘a boshla",
        "bog‘la qo‘y", "bos boshla", "bos ol", "bos qol", "bos tashla", "bukilib-bukil ket", "charcha bo‘l", "charcha qol",
        "duch kel", "ich chiq", "ich ol", "ich qo‘y", "ich to‘xta", "ich yubor", "i̇shlab chiqar", "kel boshla", "kelish ol",
        "kelish qo‘y", "kelish yubor", "kelish yur", "kes ol", "kesib o‘t", "ket boshla", "ket qol", "ko‘tar qo‘y",
        "kut yur", "kuy boshla", "kuydir ol", "kuydir qo‘y", "o‘r tur", "o‘tkaz ko‘r", "og‘ri boshla", "og‘ri qol",
        "ol chiq", "ol sot", "ot boshla", "ot ol", "ot yubor", "otil chiq", "pishir ol", "pishir qo‘y", "qaytar boshla",
        "qaytar chiq", "qaytar ol", "qaytar qo‘y", "qaytar yubor", "qaytar yur", "qo‘y yubor", "qotir boshla", "qotir qo‘y",
        "quvon boshla", "quvonib ket", "quyil boshla", "rivojlan bor", "saqla chiq", "saqla ol", "saqla qol", "saqla yubor",
        "savala boshla", "savala ol", "savala qo‘y", "savala tashla", "shakllan bor", "shalvira qol", "shalvira tur",
        "shalvira tush", "shamolla bo‘l", "shamolla boshla", "shamolla qol", "silkit boshla", "silkit ol", "silkit qo‘y",
        "sirg‘al ket", "sirg‘al tush", "so‘zla boshla", "so‘zla o‘tir", "so‘zla yubor", "so‘zla yur", "suz ket",
        "tasdiqni kir", "tashla ko‘r", "tashla yubor", "teg tur", "tekisla qo‘y", "tekisla yur", "ter ber", "ter bo‘l",
        "ter boshla", "ter chiq", "ter ol", "ter qo‘y", "ter tashla", "ter tur", "tinch tur", "to‘xta ol", "to‘xta qol",
        "to‘xtat qo‘y", "to‘xtat yubor", "tug qol", "tuga qol", "tur ol", "tur qol", "tutoqi ket", "tutoqi qol", "uqi ol",
        "uqi qol", "ur o‘t", "ur qol", "urini ko‘r", "uz ol", "uzoqlash bor", "yarat bil", "yarat yubor", "yarat yur",
        "yasha o‘t", "yasha qol", "yasha tur", "yet bor", "yet boshla", "yet qol", "yopilir kel", "yopiril boshla",
        "yopiril ket", "yopiril ol", "yopish boshla", "yopish ol", "yopish qol", "yorish ket", "yorish ko‘rin",
        "yoz qol", "yukla ol", "zerik ket", "zerik qol"
    ]

    new_tokens = []
    i = 0
    while i < len(tokens):
        if i + 1 < len(tokens):
            # Check if the current token and the next token form a kfsq
            for f in kfsq:
                if __change_apostrophe(tokens[i]).lower().startswith(f.split()[0]) and __change_apostrophe(tokens[i + 1]).lower().startswith(f.split()[1]):
                    new_tokens.append(tokens[i] + ' ' + tokens[i + 1])
                    i += 2
                    break
            else:
                # If no kfsq is found, add the current token as is
                new_tokens.append(tokens[i])
                i += 1
        else:
            # If no kfsq is found, add the current token as is
            new_tokens.append(tokens[i])
            i += 1

    return new_tokens


def tokenize(text, punctuation=True):
    # Split the input text into individual tokens by whitespace
    tokens = text.split()

    # Process the tokens for division (like: ["(yangilik)"] to ["(", "yangilik", ")"])
    tokens = __division(tokens)

    # Process the tokens for gerunds (like: "-(u)v, -(i)sh, -moq, -mak" + "kerak, lozim, shart, darkor")
    tokens = __gerund(tokens)

    # Process the tokens for compound words (e.g., handling hyphenated words like 'high-end')
    tokens = __compound(tokens)

    # Process the tokens for keyword and special query handling (likely related to search optimization)
    tokens = __kfsq(tokens)

    # If the punctuation flag is set to True, return the tokens including punctuation
    if punctuation:
        return tokens
    else:
        # If punctuation flag is False, filter out punctuation tokens
        no_punc_tokens = []

        # Loop through each token and include only alphanumeric tokens (words)
        for token in tokens:
            if re.match(r'\w+', token):  # It's a word (alphanumeric)
                no_punc_tokens.append(token)

        return no_punc_tokens

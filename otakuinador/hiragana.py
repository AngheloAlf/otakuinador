# https://es.wikipedia.org/wiki/Hiragana
# https://en.wikipedia.org/wiki/Hiragana


hiraganas_monographs = {
     "a": "あ",   "i": "い",   "u": "う",  "e": "え",  "o": "お",
    "ka": "か",  "ki": "き",  "ku": "く", "ke": "け", "ko": "こ",  # k-
    "sa": "さ", "shi": "し",  "su": "す", "se": "せ", "so": "そ",  # s-
    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",  # t-
    "na": "な",  "ni": "に",  "nu": "ぬ", "ne": "ね", "no": "の",  # n-
    "ha": "は",  "hi": "ひ",  "hu": "ふ", "he": "へ", "ho": "ほ",  # h-
                              "fu": "ふ",                         # f- # h-
    "ma": "ま",  "mi": "み",  "mu": "む", "me": "め", "mo": "も",  # m-
    "ya": "や",               "yu": "ゆ",             "yo": "よ",  # y-
    "ra": "ら",  "ri": "り",  "ru": "る", "re": "れ", "ro": "ろ",  # r-
    "wa": "わ",                                       "wo": "を", # w-
    "n": "ん",                                                    # n
}

hiraganas_digraphs = {
     "ya": "ゃ",    "yu": "ゅ",    "yo": "ょ",
    "kya": "きゃ", "kyu": "きゅ", "kyo": "きょ", # ky- # k-
    "sha": "しゃ", "shu": "しゅ", "sho": "しょ", # sh- # s-
    "cha": "ちゃ", "chu": "ちゅ", "cho": "ちょ", # ch- # t-
    "nya": "にゃ", "nyu": "にゅ", "nyo": "にょ", # ny- # n-
    "hya": "ひゃ", "hyu": "ひゅ", "hyo": "ひょ", # hy- # h-
                                                # h-  # h-
    "mya": "みゃ", "myu": "みゅ", "myo": "みょ", # my- # m-
                                                # y-  # y-
    "rya": "りゃ", "ryu": "りゅ", "ryo": "りょ", # ry- # r-
                                                # w-  # w-
                                                # n   # n
}

hiraganas_monographs_diacritics = {
    "ga": "が",  "gi": "ぎ",  "gu": "ぐ", "ge": "げ", "go": "ご", # g-
    "za": "ざ",  "ji": "じ",  "zu": "ず", "ze": "ぜ", "zo": "ぞ", # z-
    "da": "だ", "dji": "ぢ", "dzu": "づ", "de": "で", "do": "ど", # d-
    "ba": "ば",  "bi": "び",  "bu": "ぶ", "be": "べ", "bo": "ぼ", # b-
    "pa": "ぱ",  "pi": "ぴ",  "pu": "ぷ", "pe": "ぺ", "po": "ぽ", # p-
}

hiraganas_digraphs_diacritics = {
    "gya": "ぎゃ", "gyu": "ぎゅ", "gyo": "ぎょ", # gy- # g-
     "ja": "じゃ",  "ju": "じゅ",  "jo": "じょ", # j-  # z-
    "dja": "ぢゃ", "dju": "ぢゅ", "djo": "ぢょ", # dj- # d-
    "bya": "びゃ", "byu": "びゅ", "byo": "びょ", # by- # b-
    "pya": "ぴゃ", "pyu": "ぴゅ", "pyo": "ぴょ", # py- # p-
}

deprecated_hiraganas = {"wa": "ゎ", "kwa": "くゎ", "wi": "ゐ", "we": "ゑ", "gwa": "ぐゎ" }


def syllable_as_hiragana(syllable: str) -> str:
    assert(0 < len(syllable) <= 3)
    if syllable in hiraganas_monographs:
        return hiraganas_monographs[syllable]
    if syllable in hiraganas_digraphs:
        return hiraganas_digraphs[syllable]
    if syllable in hiraganas_monographs_diacritics:
        return hiraganas_monographs_diacritics[syllable]
    if syllable in hiraganas_digraphs_diacritics:
        return hiraganas_digraphs_diacritics[syllable]
    if syllable in deprecated_hiraganas:
        return deprecated_hiraganas[syllable]
    return syllable


hira = {
     "a": "あ",   "i": "い",   "u": "う",  "e": "え",  "o": "お",  "ya": "ゃ",    "yu": "ゅ",    "yo": "ょ",
    "ka": "か",  "ki": "き",  "ku": "く", "ke": "け", "ko": "こ", "kya": "きゃ", "kyu": "きゅ", "kyo": "きょ",  # k-
    "sa": "さ", "shi": "し",  "su": "す", "se": "せ", "so": "そ", "sha": "しゃ", "shu": "しゅ", "sho": "しょ",  # s-
    "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と", "cha": "ちゃ", "chu": "ちゅ", "cho": "ちょ",  # t-
    "na": "な",  "ni": "に",  "nu": "ぬ", "ne": "ね", "no": "の", "nya": "にゃ", "nyu": "にゅ", "nyo": "にょ",  # n-
    "ha": "は",  "hi": "ひ",  "hu": "ふ", "he": "へ", "ho": "ほ", "hya": "ひゃ", "hyu": "ひゅ", "hyo": "ひょ",  # h-
                              "fu": "ふ",                                                                     # h-
    "ma": "ま",  "mi": "み",  "mu": "む", "me": "め", "mo": "も", "mya": "みゃ", "myu": "みゅ", "myo": "みょ",  # m-
    "ya": "や",               "yu": "ゆ",             "yo": "よ",                                             # y-
    "ra": "ら",  "ri": "り",  "ru": "る", "re": "れ", "ro": "ろ", "rya": "りゃ", "ryu": "りゅ", "ryo": "りょ",  # r-
    "wa": "わ",                                       "wo": "を",                                             # w-
     "n": "ん",                                                                                                # n
    "ga": "が",  "gi": "ぎ",  "gu": "ぐ", "ge": "げ", "go": "ご", "gya": "ぎゃ", "gyu": "ぎゅ", "gyo": "ぎょ",  # g-
    "za": "ざ",  "ji": "じ",  "zu": "ず", "ze": "ぜ", "zo": "ぞ",  "ja": "じゃ",  "ju": "じゅ",  "jo": "じょ",  # z-
    "da": "だ", "dji": "ぢ", "dzu": "づ", "de": "で", "do": "ど", "dja": "ぢゃ", "dju": "ぢゅ", "djo": "ぢょ",  # d-
    "ba": "ば",  "bi": "び",  "bu": "ぶ", "be": "べ", "bo": "ぼ", "bya": "びゃ", "byu": "びゅ", "byo": "びょ",  # b-
    "pa": "ぱ",  "pi": "ぴ",  "pu": "ぷ", "pe": "ぺ", "po": "ぽ", "pya": "ぴゃ", "pyu": "ぴゅ", "pyo": "ぴょ",  # p-
}


# https://espanolplus.com/pronunciacion/correspondencia-letras-sonidos/
# http://www.haakonkrohn.com/afi/
spanish_sounds_as_hiraganas = {
      "n": "ん",     "y": "、い、",                                            # n
      "a": "あ",     "i": "い",     "u": "う",     "e": "え",     "o": "お",   # -
     "ka": "か",    "ki": "き",    "ku": "く",    "ke": "け",    "ko": "こ",   # k-
     "sa": "さ",    "si": "すぃ",  "su": "す",    "se": "せ",    "so": "そ",   # s-
     "ta": "た",    "ti": "てぃ",  "tu": "てゅ",  "te": "て",    "to": "と",   # t-
     "na": "な",    "ni": "に",    "nu": "ぬ",    "ne": "ね",    "no": "の",   # n-
     "ha": "あ",    "hi": "い",    "hu": "う",    "he": "え",    "ho": "お",   # h- # h is mute.
     "ma": "ま",    "mi": "み",    "mu": "む",    "me": "め",    "mo": "も",   # m-
     "ya": "じゃ",  "yi": "じ",    "yu": "じゅ",  "ye": "じぇ",  "yo": "じょ", # y-
     "ra": "ら",    "ri": "り",    "ru": "る",    "re": "れ",    "ro": "ろ",   # r-
     "wa": "わ",    "wi": "ぐい",  "wu": "ぐ",    "we": "ぐえ",  "wo": "ぐお", # w-
     "za": "ざ",    "zi": "ずぃ",  "zu": "ず",    "ze": "ぜ",    "zo": "ぞ",   # z-
     "da": "だ",    "di": "でぃ",  "du": "でゅ",  "de": "で",    "do": "ど",   # d-
     "ba": "ば",    "bi": "び",    "bu": "ぶ",    "be": "べ",    "bo": "ぼ",   # b-
     "pa": "ぱ",    "pi": "ぴ",    "pu": "ぷ",    "pe": "ぺ",    "po": "ぽ",   # p-
     "ca": "か",    "ci": "すぃ",  "cu": "く",    "ce": "せ",    "co": "こ",   # c-
     "fa": "ふぁ",  "fi": "ふぃ",  "fu": "ふ",    "fe": "ふぇ",  "fo": "ふぉ", # f-
     "la": "ら",    "li": "り",    "lu": "る",    "le": "れ",    "lo": "ろ",   # l-
     "va": "ば",    "vi": "び",    "vu": "ぶ",    "ve": "べ",    "vo": "ぼ",   # v-
     "xa": "さ",    "xi": "すぃ",  "xu": "す",    "xe": "せ",    "xo": "そ",   # x-
     "ja": "は",    "ji": "ひ",    "ju": "ふ",    "je": "へ",    "jo": "ほ",   # j-
     "ga": "が",    "gi": "ひ",    "gu": "ぐ",    "ge": "へ",    "go": "ご",   # g-
                   "gui": "ぎ",    "gü": "ぐ",   "gue": "げ",                  # gu-
                   "qui": "き",                  "que": "け",                  # qu-
    "cha": "ちゃ", "chi": "ち",   "chu": "ちゅ", "che": "ちぇ", "cho": "ちょ", # ch-
    "lla": "じゃ", "lli": "じ",   "llu": "じゅ", "lle": "じぇ", "llo": "じょ", # ll-
    "rra": "ら",   "rri": "り",   "rru": "る",   "rre": "れ",   "rro": "ろ",   # rr-
     "ña": "にゃ",  "ñi": "にぃ",  "ñu": "にゅ",  "ñe": "にぇ",  "ño": "にょ", # ñ-
    " xa": "くさ", " xi": "くし", " xu": "くす", " xe": "くせ", " xo": "くそ", # -x-

    # why not?
    "kya": "きゃ",                "kyu": "きゅ",                "kyo": "きょ", # ky-
    "nya": "にゃ",                "nyu": "にゅ",                "nyo": "にょ", # ny- # n-
    "hya": "ひゃ",                "hyu": "ひゅ",                "hyo": "ひょ", # hy-
    "mya": "みゃ",                "myu": "みゅ",                "myo": "みょ", # my-
    "rya": "りゃ",                "ryu": "りゅ",                "ryo": "りょ", # ry-
    "dja": "ぢゃ",                "dju": "ぢゅ",                "djo": "ぢょ", # dj-
    "gya": "ぎゃ",                "gyu": "ぎゅ",                "gyo": "ぎょ", # gy-
    "bya": "びゃ",                "byu": "びゅ",                "byo": "びょ", # by-
    "pya": "ぴゃ",                "pyu": "ぴゅ",                "pyo": "ぴょ", # py-
}

def sp_syllable_hiragana(syllable: str) -> str:
    if syllable in spanish_sounds_as_hiraganas:
        return spanish_sounds_as_hiraganas[syllable]
    return syllable


def replace_punctuations(sentence: str) -> str:
    sentence = sentence.replace("{", "｛")
    sentence = sentence.replace("}", "｝")
    sentence = sentence.replace("(", "（")
    sentence = sentence.replace(")", "）")
    sentence = sentence.replace("[", "［")
    sentence = sentence.replace("]", "］")
    # sentence = sentence.replace("[", "【")
    # sentence = sentence.replace("]", "】")
    sentence = sentence.replace(",", "、")
    sentence = sentence.replace("...", "…")
    sentence = sentence.replace("..", "‥")
    sentence = sentence.replace(".", "。")
    sentence = sentence.replace(" ", "　")
    sentence = sentence.replace("~", "〜")
    sentence = sentence.replace(":", "：")
    sentence = sentence.replace("!", "！")
    sentence = sentence.replace("?", "？")

    sentence_list = list(sentence)
    i = 0
    single = True
    double = True
    while i < len(sentence_list):
        if sentence_list[i] == "'":
            if single:
                sentence_list[i] = "「"
            else:
                sentence_list[i] = "」"
            single = not single
        elif sentence_list[i] == '"':
            if double:
                sentence_list[i] = "『"
            else:
                sentence_list[i] = "』"
            double = not double
        i += 1
    sentence = "".join(sentence_list)
    return sentence


def japanese_space() -> str:
    return "　"


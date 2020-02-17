from typing import List

def remove_accents(string: str) -> str:
    string = string.replace("á", "a").replace("Á", "A")
    string = string.replace("í", "i").replace("Í", "I")
    string = string.replace("ú", "u").replace("Ú", "U")
    string = string.replace("é", "e").replace("É", "E")
    string = string.replace("ó", "o").replace("Ó", "O")
    return string


def is_consonant(char):
    return char in tuple("bcdfghjklmnpqrstvwxyz")

def is_vocal(char):
    return char in tuple("aeiou")

def _split_syllables(word: str) -> List[str]:
    syllables = list()
    i = 0
    while i < len(word):
        char = word[i]
        if not is_consonant(word[i]):
            pass
        elif is_consonant(word[i]) and i+1 < len(word):
            if is_vocal(word[i+1]):
                i += 1
                char += word[i]
        syllables.append(char)
        i += 1
    return syllables

def is_digraph(syllable1: str, syllable2: str) -> bool:
    digraphs = [("c", "h"), ("l", "l"), ("r", "r")]
    for a, b in digraphs:
        if syllable1 == a and syllable2[0] == b:
            return True
    if syllable1 in ("gu", "qu") and is_vocal(syllable2):
        return True
    return False

def is_consonants_group(syllable1: str, syllable2: str) -> bool:
    group = [("c", "n"), ("g", "n"), ("m", "n"), ("p", "n"), ("p", "s"), ("p", "t")]
    for a, b in group:
        if syllable1 == a and syllable2[0] == b:
            return True
    return False

# https://espanolplus.com/pronunciacion/correspondencia-letras-sonidos/
def split_syllables(word: str) -> List[str]:
    syllables_list = _split_syllables(word)
    result = []
    i = 0
    while i < len(syllables_list):
        syll = syllables_list[i]
        if i+1 < len(syllables_list):
            if is_digraph(syll, syllables_list[i+1]):
                syll += syllables_list[i+1]
                i += 1
            elif is_consonants_group(syll, syllables_list[i+1]):
                syll = syllables_list[i+1]
                i += 1
        if i > 0:
            if syll[0] == "x" and is_vocal(syllables_list[i-1][-1]):
                syll = " " + syll
        result.append(syll)
        i += 1
    return result


def alone_consonant_to_japanese_sound(syllable: str) -> str:
    if syllable == "h":
        return ""
    if syllable == "n":
        return "n"
    if syllable == "y":
        return "y"
    if is_consonant(syllable) or syllable == " x":
        return syllable + "u"
    return syllable

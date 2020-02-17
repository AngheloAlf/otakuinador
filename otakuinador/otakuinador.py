import hiragana
import spanish


frase = input("Ingresa una frase: ").lower()
sentence = hiragana.replace_punctuations(spanish.remove_accents(frase)).split(hiragana.japanese_space())

new_sentence = []
for word in sentence:
    syllables_list = spanish.split_syllables(word)
    new_word = ""
    # print(syllables_list)
    # print("<", end="")
    for syll in syllables_list:
        syll = spanish.alone_consonant_to_japanese_sound(syll)
        # print(syll, end="")
        new_word += hiragana.sp_syllable_hiragana(syll)
    new_sentence.append(new_word)
    # print(">")

print(hiragana.japanese_space().join(new_sentence))

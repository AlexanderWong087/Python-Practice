import string
def ubbidubbi_word(eword):
    vowels = 'aeiouy'
    result = []
    i = 0
    length = len(eword)
    punctuation = ''
    while i < length and eword[i] in string.punctuation:
        punctuation += eword[i]
        i += 1
    if punctuation:
        eword = eword[:-len(punctuation)]
    while i < length:
        if eword[i] in vowels:
            start = i
            while i < length and eword[i] in vowels:
                i += 1
            result.append('ub' + eword[start:i])
        else:
            result.append(eword[i])
            i += 1
    if result and result[-1] == 'ub' and eword.endswith('e'):
        result.pop()
    return ''.join(result) + punctuation
def ubbidubbi_sentence(esentence):
    words = esentence.split()
    translated_words = [ubbidubbi_word(word) for word in words]
    return ' '.join(translated_words)
def ubbidubbi_translator():
    print("---------------------------")
    print("   Ubbi Dubbi Translator   ")
    print("---------------------------")
    while True:
        esentence = input("Enter the English sentence: ").lower()
        translation = ubbidubbi_sentence(esentence)
        print("Translation:", translation)
        do_another = input("Do another? [y/n] ").lower()
        if do_another != 'y':
            print("gubo ubin pubeace! guboodbubye!")
            break
ubbidubbi_translator()
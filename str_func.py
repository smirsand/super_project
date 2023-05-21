def capital_letters_of_words(text):
    '''
    Принимает слова с маленькими буквами и возвращает слова с большими буквами
    '''
    text = text.upper()
    return text

def first_letter(text_):
    '''
    Принимает слова с маленькими буквами и возавращает слова с большой буквы
    '''
    text = text_.title()
    return text


text = "слово"
text_ = "второе слово"
capital_letters_of_words(text)
first_letter(text_)

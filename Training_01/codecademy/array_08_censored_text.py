'''
Created on Jul 18, 2016

@author: trannh08
'''
def censor(text, word):
    list_words = text.split(" ")
    new_word = ""
    for single_word in list_words:
        temp_word = single_word
        if single_word == word:
            temp_word = "*"*len(single_word)
        new_word += temp_word + " "
    return new_word

def censor2(text, word):
    list_words = text.split(" ")
    new_list = []
    new_word = ""
    for single_word in list_words:
        temp_word = single_word
        if single_word == word:
            temp_word = "*"*len(single_word)
        new_list.append(temp_word)
    new_word = " ".join(map(str, new_list))
    return new_word

#this one will run with ending space
print(censor("haha fuck you boy ", "fuck"))
#this one will run without ending space
print(censor2("god damn, fuck you ", "fuck"))
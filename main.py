import time

meme_dict = {"CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "Abreviação da palavra 'verdade'",
            "BISCOITAR": "postar algo apenas para chamar a atenção",
            "HATER": "pessoa que está constantemente criticando os outros",
            "VLW": "abreviação da palavra 'valeu'",
            "SIX SEVEN": "... Não posso... te ajudar... com isso...",
            "LARP": "Quando alguém copia outra pessoa, mas muda algum aspecto, como a voz"}

while True:
    time.sleep(1.5)
    word = input("Digite uma palavra moderna que você não entende (escreva toda a palavra em letras maiúsculas):")
    
    if word in meme_dict.keys():
        time.sleep(1.5)
        print(meme_dict[word]) 
        print("")
    else:
        time.sleep(2.5)
        print("A palavra '" + word + "' não está presente no dicionário")
        print("")

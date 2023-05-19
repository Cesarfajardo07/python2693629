diccionarioe={"gato": "cat" ,
            "perro": "dog" ,
            "aguila": "eagle" ,
            "zorro": "fox" ,
            "mono": "monkey" ,
            "vaca": "cow" ,
            "serpiente": "snake" ,
            "caballo": "horse",
            "raton": "mouse",
            "cebra": "zebra"}

words=[input('ingrese animal del diccionario en español: ')]
for word in words:
    if word in diccionarioe:
        print(word, "-->", diccionarioe[word])
    else:
        print(word, 'no esta en el diccionario')


diccionarioi={"cat": "gato" ,
            "dog": "perro" ,
            "eagle": "aguila" ,
            "fox": "zorro" ,
            "monkey": "mono" ,
            "cow": "vaca" ,
            "snake": "serpiente" ,
            "caballo": "horse",
            "mouse": "raton",
            "cebra": "zebra"}

words=[input('ingrese animal del diccionario en ingles: ')]
for word in words:
    if word in diccionarioi:
        print(word, "-->", diccionarioi[word])
    else:
        print(word, 'no esta en el diccionario')

#def opcion (i):
    #return opcion
#opcion= input("ingerese diccionarioi o diccionarioe para selccionar diccionario")
#if opcion =="diccionarioi"
    #print(diccionarioi|)
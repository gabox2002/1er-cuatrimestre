import re

#SPLIT 

# print(re.split(" ", "Hola mundo"))              #['Hola', 'mundo']
# print(re.split("[a-zA-Z]", "hola 1c"))          #['', '', '', '', ' 1', '']
# print(re.split("[0-9]", "hola 125c"))           #['hola ', '', '', 'c']
# print(re.split("[0-9a-zA-Z]", "Hola @125c"))    #['', '', '', '', ' @', '', '', '', '']


#SEARCH   hace una busqueda en la cadena y devuelve dos posibles cosas, un objeto o none si no encuentra incidencia
# print(re.search(" ", "texto"))                     #None  
# print(re.search(" t", "el texto ingresado"))       #<re.Match object; span=(2, 4), match=' '>
#                                                                 #[inclusivo-excluyente]
# print(re.search("[0-9]+", "el texto 123 ingresado"))    #<re.Match object; span=(9, 12), match='123'>

# print(re.search("[0-9]{1}", "el texto 12345 ingresado"))    #{1} limitante <re.Match object; span=(9, 10), match='1'>

# print(re.search(" ","el texto").span())   # tupla que representa la exp regular (2, 3)
# print(re.search(" ","eltexto").span())    #AttributeError: 'NoneType' object has no attribute 'span'

# print(re.search(" ","el texto").span())          #(2, 3)
# print(re.search(" ","el texto").start())            #2
# print(re.search(" ","el texto").end())              #3

# print(re.search("[a-z]","el texto"))                #<re.Match object; span=(0, 1), match='e'>
# print(re.search("[a-z]+","el texto"))               #<re.Match object; span=(0, 2), match='el'>
# print(re.search("[a-z]+","     "))                  #None

#FINDALL   contrapartida del split, busca dentro de la cadena todas las ocurrencias

# texto = "uno 1 dos 25 tres 3 cuatro"

# print(re.findall(" ", texto))        #[' ', ' ', ' ', ' ', ' ', ' ']    la primera la expresion regular y la segunda el texto
# print(re.findall("[0-9]", texto))       #['1', '2', '3']
# print(re.findall("[0-9]+", texto))          #['1', '25', '3']
# print(re.findall("[a-z]", texto))        #['u', 'n', 'o', 'd', 'o', 's', 't', 'r', 'e', 's', 'c', 'u', 'a', 't', 'r', 'o']   
# print(re.findall("[a-z]+", texto))      #['uno', 'dos', 'tres', 'cuatro']
# print(re.findall("[a-z]+", texto)) #una coincidiencia o mas una al lado de la otra ['uno', 'dos', 'tres', 'cuatro']
# print(re.findall("[a-z]{3}", texto))    #['uno', 'dos', 'tre', 'cua', 'tro']
# print(re.findall("[a-z]{4}", texto))     #['tres', 'cuat']
# print(re.findall("[a-z]{6}", texto))        #['cuatro']
# print(re.findall("[a-z]{7}", texto))        #[]   vacio


#SUB

# texto = "abc   ccc  ddd  abc  aaa"

# resultado = re.sub("abc", "", texto)
# print(resultado)                            # ccc ddd  aaa

# resultado = re.sub("abc", "xyz", texto)
# print(resultado)                            #xyz ccc ddd xyz aaa

# resultado = re.sub(r"\s+", "-", texto)      #abc-ccc-ddd-abc-aaa elimina espacio duplicado
# print(resultado) 

texto = "QUEVEDO || BZRP Music Sessions #52"

print(re.split("[||]+ ", texto))            ['QUEVEDO ', 'BZRP Music Sessions #52']
print(re.split(" \|+ ", texto))


#1:05:45 video Gio
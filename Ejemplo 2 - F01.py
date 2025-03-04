#Losrafikis
# Este código imprime los elemetos de la variable "frutas" (manzana, platano y naranja) agregando tambien el metodo .append (pera) al final haciendo lista primero, para despues imprimir los elementos pero esta vez en una lista vertical para mostrar que frutas tiene en ese momento.
# 2025 / 03/ 03 - V. 1. 0. 0 - SE  AGREGO EL ECANBEZADO AL CÓDIGO E INFORMACIÓN DEL EQUIPO   
# 2025 / 03/ 03 - V. 1. 0. 2 - SE AGREGARON COMENTARIOS LA VARIABLE "frutas" Y EN LOS COMANDOS PRINT
# 2025 / 03/ 03 - V. 1. 0. 3 - SE AGREGAN COMENTARIO EN LA LINEA 9, EXPLICANDO EL FUNCIONAMIENTO DEL .append
# 2025 / 03/ 03 - V. 1. 0. 4 - SE AGREGO COMENTARIO EN LA LINEA 18 EXPLICANDO EL FUNCIONAMENTO DE FOR
# TRABAJARON: kevin(snapdragon1971) y cristopher(ivanG0lopez)

frutas = ["manzana", "plátano", "naranja"] #Se crea una variable llamada "frutas" en la cual contiene elementos que referencian 3 frutas que se utilizaran en el codigo.


frutas.append("pera") #Se usa la variable llamada "frutas", y usando el metodo .append con la palabra pera para agregar dicha palabra al final de la lista de frutas.


print("Lista de frutas:", frutas) #Se llama a imprimir una palanbra siendo "Lista de frutas" para despues usar las variables de "frutas" y finalizando con el elemento del metodo .append.


for fruta in frutas: #Se crea el bucle "fruta" el cual usa los elementos de la variable "frutas" mientras va aumenta de 1 en 1 su valor, asi usando el elemento "manzana" despues "plátano" y asi hasta aver impreso toda la lista
    print("Tengo una", fruta) #Se llama a imprimir "Tengo una" junto con el elemento de la variable "frutas" sucesivamente hasta que se acabe la lista con el elemeneto del metodo .append

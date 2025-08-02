frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])
print('oi')
# para imprimir texto grande inteiro
print('''Para fazer o "ç" (cê-cedilha) no teclado americano em Linux,
você pode usar a combinação de teclas "AltGr + , (vírgula)" seguido da letra "c".
Alternativamente, se estiver usando o layout "EUA Internacional (com AltGr como tecla morta)",
você pode pressionar a tecla de aspas simples (') seguida da letra "c".
Para o "Ç" maiúsculo, a combinação é "AltGr + Shift + , (vírgula)" ou,
no caso do layout EUA Internacional, "Shift + ' (aspas simples) + c". 
''')

#conta quantas vees tem o caractere
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
#trocar palavra ou frase
print(frase.replace('Python','Android'))
print(frase)
#str só muda de atribuir
#frase = frase.replace('Python','Android')
#print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('video'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2] [3])

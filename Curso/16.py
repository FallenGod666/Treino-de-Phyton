# Exemplo de uso de strings
text = input('Digite uma frase ou um texto: ')
search = input('Digite algo da frase que vc queira encontrar na propria frase: ')
text.lower()
search.lower()

print(text[::2])
print(text[5::3])
print(text.upper())
print(text.count('s'))
print(len(text))
print(len(text.strip()))
print(text.lower().find(search))

if search in text:
    print('Encontrado')

# Exemplo do print usando texto enorme sem usar varios códigos
print('''\nNessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), upper(), 
lower(), capitalize(), title(), strip(), junção com join().
      ''')
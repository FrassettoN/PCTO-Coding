from random import randint
random_number = randint(0,100)
victory = False

print('É stato generato un numero causale da 1 a 100, riesci a indovinarlo?')

counter = 0
while not victory:
  counter += 1
  user_answer = int(input('Scegli il tuo numero: '))
  if user_answer > random_number:
    print('Numero troppo alto')
  elif user_answer < random_number:
    print('Numero troppo basso')
  else:
    victory = True

print(f'Bravo! Ti sono bastati solo {counter} tentativi!')


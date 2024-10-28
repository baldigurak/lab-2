import random

def guess_the_number():
  """Игра 'Угадай число' с ограничением по диапазону и попыткам."""

  number = random.randint(1, 10)
  attempts = 0
  max_attempts = 3

  print("Добро пожаловать в игру 'Угадай число'!")
  print("Я загадал число от 1 до 10. У вас есть 3 попытки.")

  while attempts < max_attempts:
    try:
      guess = int(input(f"Введите ваше предположение ({attempts + 1}/{max_attempts}): "))
    except ValueError:
      print("Неверный ввод. Пожалуйста, введите целое число.")
      continue

    attempts += 1

    if guess < number:
      print("Загаданное число больше.")
    elif guess > number:
      print("Загаданное число меньше.")
    else:
      print(f"Поздравляю! Вы угадали число {number} за {attempts} попыток.")
      return

  print(f"У вас закончились попытки. Загаданное число было {number}.")

if __name__ == "__main__":
  guess_the_number()

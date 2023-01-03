import requests
import random
import string
import time

replitnames = []

# Проверка подключен ли пользователь к интернету
url = "https://replit.com"
try:
    response = requests.get(url)
    print("Проверка подключения...")
    time.sleep(4)
    print('Вы подключены к интернету, парсер запустится через 4 секунды.')
    pass
except requests.exceptions.ConnectionError:
    input("Вы не подключены к интернету, проверьте соединение и попробуйте перезагрузить программу\nНажмите Enter чтобы закрыть программу")
    exit()    
time.sleep(4)
kolichestvo = input('Количество никнеймов: ')
simvols = input('Количество символов в никнейме: ')
time.sleep(1)
print('Генерация никнеймов была запущена.')
time.sleep(3)

def replit_nicknames_gen(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    replitnames.append(rand_string)
    print(f' СГЕНЕРИРОВАН НИКНЕЙМ | https://replit.com/@{rand_string}')

for i in range(int(kolichestvo)):
	replit_nicknames_gen(int(simvols))

print('Генерация ников завершена. Проверка никнеймов начнется через 3 секунды')
time.sleep(3)
print('Проверка успешно запущена. При обнаружении валидных реплит аккаунтов вы будете оповещены.')
for replitname in replitnames:
    resp = requests.get('https://replit.com/@')
    if resp.status_code in [404]:
        print(f'https://replit.com/@{replitname} | Не валиден')
        pass
    else:
        print(f'https://replit.com/@{replitname} | Валиден')
input()

#pgzero

import random

characters = "#$%&/()=?¡¨*[]_:;'¿´+}{-.,}1234567890abcdefghijklmnñopqrstuvwxyz"

password_lenth = int(input("introduce la longitud de la contraseña:"))

x = ""

for i in range(password_lenth):
 x += random.choice(characters)

print(x)

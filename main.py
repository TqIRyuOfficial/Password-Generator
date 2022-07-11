import string
import secrets
import os



textsize = int(input("何桁のパスワードを生成しますか : "))


def password(size=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    chars += '%&$#()'

    return ''.join(secrets.choice(chars) for x in range(size))


print("パスワードを生成しました")

passwords = password(textsize)

print(passwords)

f = open('password.txt', 'a')
f.write(f"{passwords}\n")
f.close()
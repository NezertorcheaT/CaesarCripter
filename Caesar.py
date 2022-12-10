import string


# это класс
class CaesarCrypter:
    # метод задаия переменных
    def __init__(self):
        # русский алфавит маленький
        self.abc_l = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        # русский алфавит большой
        self.abc_b = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    # приватный статический метод шифрования 1 символа
    @staticmethod
    def __encrypt_symbol(s: str, alf: str, dist=3):
        if len(s) > 1 or len(s) == 0:
            raise ValueError('The entered character has length greater than 1 or equal to 0')
        ii = (alf[0] + alf).find(s)
        if ii != -1:
            return (alf[0] + alf)[ii + dist if ii + dist < len((alf[0] + alf)) else ii + dist - len((alf[0] + alf))]
        else:
            return ''

    # обезопасеный приватный статический метод шифрования 1 символа
    @staticmethod
    def __try_encrypt_symbol(s: str, alf: str, dist=3):
        try:
            return CaesarCrypter.__encrypt_symbol(s, alf, dist=dist)
        except ValueError:
            return CaesarCrypter.__encrypt_symbol(s[0], alf, dist=dist)

    # публичный статический метод шифрования строки
    @staticmethod
    def encrypt(s: str, dist=3):
        s_end = ''
        for i in s:
            if i in string.ascii_lowercase + string.ascii_uppercase + CaesarCrypter().abc_b + CaesarCrypter().abc_l:
                s_end += CaesarCrypter.__encrypt_symbol(i, string.ascii_lowercase, dist=dist) + \
                         CaesarCrypter.__encrypt_symbol(i, string.ascii_uppercase, dist=dist) + \
                         CaesarCrypter.__encrypt_symbol(i, CaesarCrypter().abc_b, dist=dist) + \
                         CaesarCrypter.__encrypt_symbol(i, CaesarCrypter().abc_l, dist=dist)
            else:
                s_end += i
        return s_end

    # публичный статический метод дешифрования строки
    @staticmethod
    def decrypt(s: str, dist=3):
        return CaesarCrypter.encrypt(s, dist=-dist)


# пример работы кода
if __name__ == '__main__':
    s = input()
    se = CaesarCrypter.encrypt(s)
    print(se)
    print(CaesarCrypter.decrypt(se))
    input()

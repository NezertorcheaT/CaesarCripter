import os
import string


class CaesarCrypter:
    def __init__(self):
        self.alphabets: list[str] = ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
                                     string.ascii_lowercase, string.ascii_uppercase]

    @staticmethod
    def __encrypt_symbol(s: str, alf: str, dist=3):
        if len(s) > 1 or len(s) == 0:
            raise ValueError('The entered character has length greater than 1 or equal to 0')
        ii = (alf[0] + alf).find(s)
        if ii != -1:
            return (alf[0] + alf)[ii + dist if ii + dist < len((alf[0] + alf)) else ii + dist - len((alf[0] + alf))]
        else:
            return ''

    @staticmethod
    def __try_encrypt_symbol(s: str, alf: str, dist=3):
        try:
            return CaesarCrypter.__encrypt_symbol(s, alf, dist=dist)
        except ValueError:
            return CaesarCrypter.__encrypt_symbol(s[0], alf, dist=dist)

    @staticmethod
    def encrypt(s: str, dist=3, alphabets: list[str] = None) -> str:
        """
        :param s: string to convert
        :param dist: symbol shift distance
        :param alphabets: list of alphabets, original alphabet is ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        :return: string
        """
        s_end = ''
        for i in s:
            if alphabets is None:
                print(CaesarCrypter().alphabets)
                if i in ''.join(CaesarCrypter().alphabets):
                    s_end += ''.join(
                        list([CaesarCrypter.__encrypt_symbol(i, al, dist=dist) for al in CaesarCrypter().alphabets]))
                else:
                    s_end += i
            else:
                if i in ''.join(alphabets):
                    s_end += ''.join(
                        list([CaesarCrypter.__encrypt_symbol(i, al, dist=dist) for al in alphabets]))
                else:
                    s_end += i
        return s_end

    @staticmethod
    def decrypt(s: str, dist=3, alphabets: list[str] = None) -> str:
        """
        :param s: string to convert
        :param dist: symbol shift distance
        :param alphabets: list of alphabets, original alphabet is ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        :return: string
        """
        return CaesarCrypter.encrypt(s, dist=-dist, alphabets=alphabets)


def cls():
    os.system('cls||clear')


if __name__ == '__main__':
    while True:
        print((i := CaesarCrypter.encrypt(input())), CaesarCrypter.decrypt(i))

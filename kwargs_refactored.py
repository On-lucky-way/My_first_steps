x = ['Слово', "Дело", 5]


def word(*args):
    for arg in args:

        try:
            int(arg)
        except Exception:
            print(args)
        else:
            pass

        return word


word(5)
word("Дело")

word(5, "жизнь", 7, 8)
word("яблоко", "помидор", 'циркулярка', 8)

def first(text):
    if type(text) == str:
        return text.split()[0]
    return False


def average(*numb: float):
    x = len(numb)
    return round(sum(numb) / x, 0)


def pass_check(password):
    low_let = 'abcdefghijklmnopqrstuvwxyz'
    cap_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig = '1234567890'
    punc = '!@"#№$;%^:?&*()_-+=\|}]{["/?.,<>`~'
    cp = lw = dg = False
    if len(password) >= 6:
        for i in password:
            if i in low_let:
                lw = True
            if i in cap_let:
                cp = True
            if i in dig:
                dg = True
            if i in punc:
                return False
    return cp or lw and dg


'''проверка'''
print(first('qwerty rety uil ocx'))
print(average(12.3, 14, 56))
print(pass_check('B5200AB'))




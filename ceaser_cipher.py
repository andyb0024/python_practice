import string
x=input('enter text:\n')
def ceaser(plain_text,shift_num=1):
    letters=string.ascii_lowercase
    mask=letters[shift_num:]+letters[:shift_num]
    transtab=str.maketrans(letters,mask)
    return plain_text.translate(transtab)
print(ceaser(x))
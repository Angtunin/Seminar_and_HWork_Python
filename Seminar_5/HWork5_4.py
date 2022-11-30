"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""
with open('file_encode.txt', 'w') as data:
    data.write('vvvVVVAAAADDDD')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(dec_string):
    enc_string = ''
    count = 1
    char = dec_string[0]
    for i in range(1, len(dec_string)):
        if dec_string[i] == char:
            count += 1
        else:
            enc_string = enc_string + str(count) + char
            char = dec_string[i]
            count = 1
    enc_string = enc_string + str(count) + char
    return enc_string

def rle_decode(enc_string):
    dec_string = ''
    char_amount = ''
    for i in range(len(enc_string)):
        if enc_string[i].isdigit():
            char_amount += enc_string[i]
        else:
            dec_string += enc_string[i] * int(char_amount)
        char_amount = ''
    print(dec_string)
    return dec_string

with open('file_encode.txt', 'r') as file:
    dec_string = file.read()

with open('file_decode.txt', 'w') as file:
    enc_string = rle_encode(dec_string)
    file.write(enc_string)

print('decode: \t' + dec_string)
print('encode: \t' + rle_encode(dec_string))
print(f'c: \t{round(len(dec_string) / len(enc_string), 1)}')

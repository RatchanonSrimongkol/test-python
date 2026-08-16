def character_frequency(*args):
    rvm = ''.join(args)

    krang = {}

    for i in rvm:
        if i in krang:
            krang[i] +=1
        else:
            krang[i] = 1

    return krang

print(character_frequency('ioioio'))
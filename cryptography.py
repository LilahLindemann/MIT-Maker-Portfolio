alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M',\
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def basic_caesar(alph,origin,shift):
    output = ''
    for i in range(0,len(origin)):
        if origin[i] == ' ':
            output += ' '
        else:
            num = alph.index(origin[i])
            nnum = (num + shift) % 26
            output += alph[nnum]
    return output

def decode_basic_caesar(alph,origin,shift):
    output = ''
    for i in range(0,len(origin)):
        if origin[i] == ' ':
            output += ' '
        else:
            num = alph.index(origin[i])
            nnum = (num - shift) % 26
            output += alph[nnum]
    return output

def adv_caesar(alph,origin,oshift,schange):
    output = ''
    shift = oshift
    for i in range(0,len(origin)):
        if origin[i] == ' ':
            output += ' '
        else:
            num = alph.index(origin[i])
            nnum = (num + shift) % 26
            output += alph[nnum]
            shift = (shift + schange) % 26
    return output

def decode_adv_caesar(alph,origin,oshift,schange):
    output = ' '
    shift = oshift
    for i in range(0,len(origin)):
        if origin[i] == ' ':
            output += ' '
        else:
            num = alph.index(origin[i])
            nnum = (num - shift) % 26
            output += alph[nnum]
            shift = (shift + schange) % 26

def key_encipher(alph,origin,key):
    output = ''
    count = 0
    for i in range(0,len(origin)):
        if origin[i] == ' ' or origin[i] == '\'' or origin[i] == '.'\
           or origin[i] == ':':
            output += origin[i]
        else:
            num = alph.index(origin[i])
            keypos = count % len(key)
            shift = alph.index(key[keypos]) + 1
            nnum = (num + shift) % 26
            output += alph[nnum]
            count += 1
    return output

def basic_solutions(alph,text):
    for x in range(0,25):
        print(decode_basic_caesar(alph,text,x) + ' - ' + str(x))

antialph = []
for i in range(0,len(alph)):
    antialph.append(alph[len(alph)-1-i])

def atbash(antialph,text,shift):
    output = ''
    for i in range(0,len(text)):
        if text[i] == ' ':
            output += ' '
        else:
            ashift = (alph.index(text[i])+shift) % 26
            output += antialph[ashift]
    return output

morseKey = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M',\
            '-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}

def pollux_morbit(text, nums={}):
    morse = ''
    for i in range(0,len(text)):
        #print('number = ' + text[i])
        #print('\ttranslation to Morse: ' + nums[text[i]])
        morse += nums[text[i]]
    letter = ''
    output = ''
    for i in range(0, len(morse)):
        if morse[i] == 'x' and i != len(morse) - 1 and morse[i+1] == 'x':
            if letter != '':
                output += morseKey[letter]
                output += ' '
            letter = ''
            i += 1
        elif morse[i] == 'x':
            if letter != '':
                output += morseKey[letter]
            letter = ''
        else:
            letter += morse[i]
    if letter != '':
        output += morseKey[letter]
    return output

nums = {'0':'x','1':'.','2':'.','3':'.','4':'-','5':'-','6':'-','7':'x','8':'x','9':'x'}
text = '120598110122784733744918059466981433939350262961983130455866718756946591628223037761517666963203'          
print(pollux_morbit(text, nums))

nums = {'1':'-.','2':'.-','3':'x-','4':'.x','5':'..','6':'-x','7':'--','8':'xx','9':'x.'}
text = '585596529828545537324165347436473791326949193647354424995642417395453474'          
print(pollux_morbit(text, nums))
    
        

'''for x in range(0,25):
    print(atbash(antialph,'V KOFIRYFH GIVNYOVB',x))'''
##text = input()
##print(basic_caesar(alph,text,3))
##
##text = input()
##for i in range(0,26):
##    print(decode_basic_caesar(alph,text,i))
##text = input()
##for i in range(0,26):
##    print(decode_basic_caesar(alph,text,i))
##text = input()
##for i in range(0,26):
##    print(decode_basic_caesar(alph,text,i))
##text = input()
##for i in range(0,26):
##    print(decode_basic_caesar(alph,text,i))
##text = input()
##for i in range(0,26):
##    print(decode_basic_caesar(alph,text,i))
##text = input()
##for i in range(0,26):
##    print(decode_basic_caesar(alph,text,i))

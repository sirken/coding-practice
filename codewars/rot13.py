from Test import Test, Test as test

'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''

# Using list
def rot13(msg):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    output = ''
    for i in msg:
        if i.isupper():
            output += l[l.index(i.lower())-13].upper()
        else:
            output += l[l.index(i)-13].lower()
    return output

# Using dict
def rot13(msg):
    d = dict(a='n',b='o',c='p',d='q',e='r',f='s',g='t',h='u',i='v',j='w',k='x',l='y',m='z',n='a',o='b',p='c',q='d',r='e',s='f',t='g',u='h',v='i',w='j',x='k',y='l',z='m',A='N',B='O',C='P',D='Q',E='R',F='S',G='T',H='U',I='V',J='W',K='X',L='Y',M='Z',N='A',O='B',P='C',Q='D',R='E',S='F',T='G',U='H',V='I',W='J',X='K',Y='L',Z='M')
    out = ''
    for i in msg:
        if i in d:
            out += d[i]
        else:
            out += i
    return out

# Condensed
def rot13(msg):
    d = dict(a='n',b='o',c='p',d='q',e='r',f='s',g='t',h='u',i='v',j='w',k='x',l='y',m='z',n='a',o='b',p='c',q='d',r='e',s='f',t='g',u='h',v='i',w='j',x='k',y='l',z='m',A='N',B='O',C='P',D='Q',E='R',F='S',G='T',H='U',I='V',J='W',K='X',L='Y',M='Z',N='A',O='B',P='C',Q='D',R='E',S='F',T='G',U='H',V='I',W='J',X='K',Y='L',Z='M')
    return ''.join([d[i] if i in d else i for i in msg])


test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
test.assert_equals(rot13("T!e2st"),"G!r2fg")
test.assert_equals(rot13("Te st"),"Gr fg")

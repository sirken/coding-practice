from Test import Test, Test as test

'''
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
'''

# Breaking up into chunks
def data_reverse(i):
    r = len(i) // 8
    l = []
    for x in range(r, -1, -1):
        l.extend(i[x*8:x*8+8])
    return l

# Simplify
def data_reverse(data):
    l = []
    for x in range(len(data) // 8, -1, -1):
        l.extend(data[x*8:x*8+8])
    return l

# One of the top solutions
def data_reverse(data):
  res = []
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
  return res

data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
test.assert_equals(data_reverse(data1),data2)

#data_reverse(data1)


data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
test.assert_equals(data_reverse(data3),data4)

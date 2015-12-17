from itertools import cycle, product
import string

def crypt(text, key):
    return ''.join(map(lambda x: chr(ord(x[0]) ^ ord(x[1])), zip(text, cycle(key))))

def gen_keys(length=3, keyspace=string.ascii_lowercase):
    for k in product(keyspace, repeat=length):
        yield ''.join(k)

# Do the most used words appear on the text?
most_used_words = ['the', 'be', 'to', 'of', 'and']
def good_decrypt(message):
    m = message.lower()
    for word in most_used_words:
        if m.find(word) == -1:
            return False
    return True

message = ''
with open('p059_cipher.txt') as f:
    data = f.read()
    message = ''.join(map(lambda x: chr(int(x)), data.split(",")))

for key in gen_keys():
    m = crypt(message, key)
    if good_decrypt(m):
        print "Key:", key
        print "Message:", m
        print "Sum:", sum(map(ord, m))
        break

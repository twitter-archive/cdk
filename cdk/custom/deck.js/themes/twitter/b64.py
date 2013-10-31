import sys
import base64

def encode(name):
    fp = open(name)
    data = fp.read(32000); # max-size in data-uri I think
    print base64.b64encode(data)

if __name__ == '__main__':
    encode(sys.argv[-1])

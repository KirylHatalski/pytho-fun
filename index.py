import json, random, array, os
from decimal import *

def generNumber(leng):
    if leng > 16:
        pass
    getcontext().prec = 18
    rnum = Decimal.from_float(random.uniform(0, 1))
    return int(str(rnum)[-leng:])

def arrayMass(weight):
    if weight > 16:
        pass
    elif weight > 8:
        return 'Q'
    elif weight > 4:
        return 'L'
    elif weight > 2:
        return 'I'
    elif weight > 0:
        return 'H'
    else:
        pass

def gener(count, numLeng):
    arr = array.array(arrayMass(numLeng));
    i = 0
    while i <= count:
        arr.append(generNumber(numLeng));
        i+=1
    return arr

def createJson(name, data):
    fname = f"{name}.json"
    with open(fname, 'w') as outfile:
        json.dump(data, outfile)
    pass

def init():
    fileName = input('File name:');
    count = int(input('How many elems:'))
    weight = int(input('How large digits (16 max):'))
    os.makedirs(os.path.dirname('files/%s.json' % fileName), exist_ok=True)
    createJson('files/' + fileName, gener(count, weight).tolist())
    pass

if __name__ == "__main__":
    init()

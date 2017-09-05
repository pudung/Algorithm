
# map function define

def f(x):
    return x+x

def map(f,sequence):
    result = ()
    for a in sequence:
        result += (f(a),)
    return result

sequence = ("apple","banana","peach")

print(map(f,sequence))






'''emulate a container class'''

def traverse(ict_d, key):
    if key:
        l = list(key)
        return traverse(ict_d[l.pop(0)], l)
    else:
        return ict_d

def traverse_gen(node, key):

    key = list(key)
    if key:
        p = key.pop(0)
    
        yield node[p]
        for x in traverse_gen(node[p], key):
            yield x

alist = traverse_gen({"x": {"a": 1, "b": 2}, "y": 3}, ["x", "b"])

for i in alist:
    print(i)


class SpecialDict:
    '''["x"]["y"] == ["x.y"]'''
    def __init__(self):
        self.dictionary = {"x": {"a": 1, "b": 2}, "y": 3}

    def __getitem__(self, key):
        if "." in key:
            key_list = key.split(".")
            return self.__getitem__(key_list)
        else:
            return traverse(self.dictionary, key)



'''using generator'''




adict = SpecialDict()

print(adict["x"]["a"], 'should be 1')
print(adict["x.b"], "should be 2")
print(adict["y"], 'should be 3')
print(adict["x.a"], 'should be 1')


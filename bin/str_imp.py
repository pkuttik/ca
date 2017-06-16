class test(object):
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return "My id is {}".format(self.id)

t =test(1)
print(t)
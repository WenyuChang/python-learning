import pickle


class Cls():
    static_var = 1
    def __init__(self):
        self.instance_var = 2


def dump_to_file():
    ins = Cls()

    f = open('filename', 'wb')
    pickle.dump(ins, f)
    f.close

    f = open('filename', 'rb')
    ins1 = pickle.load(f)
    f.close()


def dump_to_str():
    ins = Cls()
    data = pickle.dumps(ins)
    print data

    ins1 = pickle.loads(data)
    print ins1

if __name__ == '__main__':
    # dump_to_file()

    dump_to_str()
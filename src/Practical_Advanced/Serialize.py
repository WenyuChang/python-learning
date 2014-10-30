'''
Created on Mar 12, 2014

@author: wenychan
'''

class Cls():
    static_var = 1
    def __init__(self):
        self.instance_var = 2
    
if __name__ == '__main__':
    ins = Cls()
    
    import pickle
    f = open('filename', 'wb')
    pickle.dump(ins, f)
    f.close
    
    f = open('filename', 'rb')
    ins1 = pickle.load(f)
    f.close()
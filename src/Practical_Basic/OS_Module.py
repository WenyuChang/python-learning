import os

# Run a command
os.system('dir')


#================================================================

print('==========================================================')
print('os.name:',os.name)
print('os.getcwd:',os.getcwd())
print('os.getcwdb:',os.getcwdb())
print("os.getenv('PATH'):",os.getenv('PATH'))
print("os.getenv('PATH1'):",os.getenv('PATH1','no such env'))
print('os.listdir:',os.listdir())
print('os.curdir:',os.curdir)
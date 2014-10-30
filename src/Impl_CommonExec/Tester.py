__author__ = 'wenychan'

from Command import Command
from LocalExecutor import LocalExec
from RemoteExecutor import RemoteExec

command = Command('echo')
command.add_argument('${text}')
dict = {}
dict['text'] = 'aaaaaaaa'
command.set_substitution_dict(dict)
command1 = Command('ls -a')
command2 = Command('echo')
command2.add_argument('${text}')
dict = {}
dict['text'] = 'bbbbbbbbbbb'
command2.set_substitution_dict(dict)
ins = LocalExec(command)

ins.add_command(command1)
ins.insert_command_at(1, command2)
# ins.show_commands()

ins.add_command("python aaa.py")

print
print

ins2 = LocalExec([command1, command2])
# ins2.show_commands()
print
print

# ins = ins+ins2+ins
# ins.show_commands()

print
print

# ins = ins[2:-1]
# ins.show_commands()

from Modifier import FG, VAR
ins >> FG(timeout=1)

#ins.show_commands()
# result = ins >> VAR()
# print result

# ins = ins+ins2+ins
# ins.show_commands()
#
# ins.insert_command_at(1, [command, command1, command2])
# ins.show_commands()

# result = (ins+ins2+ins)()
# if result is not None:
#     print result[0].stdout
#
# print
#
# result = ins()
# if result is not None:
#     print result[0].stdout
# print
# print '#'*30
# print

# ins = LocalExec('sh aaa')
# with ins.cwd('/home/wenychan'):
#     ins.add_command('sh aaa')
#     result = ins(background=True)
#     if result is not None and len(result)>0:
#         print '#'*10
#         print result
#
#         future = result[0]
#         future.wait()
#         print future
#         print '$'*10, future._stdout
#         print '#'*10, future._stderr


# with ins.cwd('/home/wenychan'):
#     ins.add_command('sh aaa')
#     result = ins(out='out', err='err')
#     if result is not None and len(result)>0:
#         print '#'*10
#         print result
#
#         future = result[0]
#         future.wait()
#         print future
#         print '$'*10, future._stdout
#         print '#'*10, future._stderr


# ins.tail('/opt/tomcat/logs/catalina.out')
# # ins.ls('-al')
# ins.cwd()
# with ins.cwd('/home/wenychan/'):
#     import sys
#     from Modifier import FG, BG
    # ins.ls('-al')
    # ins > (sys.stdout, sys.stderr)
    # print
    # ins > (sys.stdout,)
    # print
    # ins > (None, sys.stderr)
    # print
    # ins()
    # print
    # ins > ('out', 'err')
    # print
    # ins > ('outonly',)
    # print
    # ins > (None, 'erronly')

    # ins >> FG(out=sys.stdout, err=sys.stderr, timeout=100, append=False)
    # print
    # ins >> FG(out=sys.stdout, err=None, append=False)
    # print
    # ins >> FG(out=None, err=sys.stderr)
    # print
    # ins()
    # print
    # ins >> FG(out='out', err='err', append=False)
    # print
    # ins >> FG(out='outonly', err=None, append=False)
    # print
    # ins >> FG(out=None, err='erronly', append=False)

    # result = ins >> BG(timeout=100)
    # print result
    #
    # result = ins >> BG()
    # print result
    # ins.tail('catalina.out')

# print '#'*30

# remote = RemoteExec('10.140.29.49', 'root', password='C!sco20!2')
# remote.add_command('ls -al')
# remote.ls('-al')
# # # remote.tail('/opt/tomcat/logs/catalina.out')
# remote.cwd()
# with remote.cwd('/opt/tomcat/logs/'):
#     remote.cwd()
#     remote.ls('-al')
#     remote(out='/home/wenychan/out1', err='/home/wenychan/err1')
#     remote.tail('catalina.out')
#     remote >> FG()
#     result = remote >> FG(timeout=1)
#     print result
# #
#
# from plumbum import SshMachine
# remote = SshMachine()
# remote.cwd
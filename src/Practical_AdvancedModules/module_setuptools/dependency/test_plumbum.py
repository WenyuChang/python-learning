__author__ = 'wenychan'

from plumbum import local, FG

def testnet():
    ipconfig = local['ipconfig']
    with local.cwd('c:/windows/system32/'):
        ipconfig & FG
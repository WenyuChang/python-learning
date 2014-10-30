__author__ = 'wenychan'

from argparse import RawTextHelpFormatter
import argparse


def func(args):
    pass


def func1(args):
    pass


def parserCreatioin():
    parser = argparse.ArgumentParser(description='CesiumCLI Commands:', formatter_class=RawTextHelpFormatter)
    parser.add_argument('-version', action='version', version='%(prog)s 1.0', help='Version of %(prog)s')
    subparsers = parser.add_subparsers(help='Sub-Command help')

    # commands for crypto
    helpStr = 'This command is for crypto, and is used on local CSA Server.'
    parser_crypto = subparsers.add_parser('crypto', help=helpStr, formatter_class=RawTextHelpFormatter)
    parser_crypto.set_defaults(func=func)

    parser_crypto.add_argument('-hsm', action="store_true", help="For HSM mode")
    group_crypto = parser_crypto.add_mutually_exclusive_group(required=True)

    helpStr = 'Generate certificate signing request and private key.\n'
    helpStr += 'usage: [-hsm] -genreq <destination path>'
    group_crypto.add_argument('-genreq', help=helpStr, nargs=1, metavar='args')

    helpStr = 'Generate PEM files or install signed CSR. \n'
    helpStr += 'usage: -i <cert file> <private key>.\n'
    helpStr += '       -hsm -i <reqSigning cert> <TLSclient cert> <TLSserver cert>'
    group_crypto.add_argument('-i', help=helpStr, nargs='+', metavar='args')

    helpStr = 'set the pin value.\n'
    helpStr += 'usage: -i <pin value>.'
    group_crypto.add_argument('-setpin', help=helpStr, nargs=1, metavar='args')
    group_crypto.add_argument('-showpin', action="store_true", help='Show pin value of current CSA server.')
    group_crypto.add_argument('-getpin', action="store_true", help='Return pin value of current CSA server.')
    group_crypto.add_argument('-initapache', action="store_true", help='Initialize when apache starting.')
    aa = group_crypto.add_argument('-resetpin', action="store_true", help='Reset pin value of current CSA server.')

    # commands for rms
    helpStr = "This command is for activation, and is used on remote managed server."
    parser_rms = subparsers.add_parser('rms', help=helpStr, formatter_class=RawTextHelpFormatter)
    parser_rms.set_defaults(func=func1)

    parser_rms.add_argument('-hsm', action="store_true", help='For HSM mode')

    group_rms = parser_rms.add_mutually_exclusive_group(required=True)

    helpStr = 'Activation remote CSA server.\n'
    helpStr += 'usage: -activate <ManagedServerID> <User>@<Host>:<CLI_PATH> <KeyFile>.\n'
    helpStr += '       -hsm -activate <ManagedServerID> <Host> <Port> <PemFile> <Password>'
    group_rms.add_argument('-activate', help=helpStr, nargs='+', metavar='args')

    helpStr = 'Show pin of remote CSA server.\n'
    helpStr += 'usage: -showpin <User>@<Host>:<CLI_PATH> <KeyFile>.'
    group_rms.add_argument('-showpin', help=helpStr, nargs='+', metavar='args')

    return parser


if __name__ == '__main__':
    parser = parserCreatioin()

    args = parser.parse_args()
    args = parser.parse_known_args(['rms', '-h'])[0]
    print args
    args.func(args)

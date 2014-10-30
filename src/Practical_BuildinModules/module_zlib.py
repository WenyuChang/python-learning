__author__ = 'wenychan'

import zlib


def simple_usage():
    # File:zlib-example-1.py
    MESSAGE = "life of brian"
    compressed_message = zlib.compress(MESSAGE)
    decompressed_message = zlib.decompress(compressed_message)
    print "original:", repr(MESSAGE)
    print "compressed message:", repr(compressed_message)
    print "decompressed message:", repr(decompressed_message)


def zip_files():
    import glob
    for file in glob.glob("c:\*.txt"):
        indata = open(file, "rb").read()
        outdata = zlib.compress(indata, zlib.Z_BEST_COMPRESSION)
        print file, len(indata), "=>", len(outdata),
        print "%d%%" % (len(outdata) * 100 / len(indata))


if __name__ == '__main__':
    zip_files()
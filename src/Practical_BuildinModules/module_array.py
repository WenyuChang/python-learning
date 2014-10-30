__author__ = 'wenychan'

import array


def simple_usage():
    # Type code 	C Type 	Python Type 	Minimum size in bytes
    #     'c' 	char 	character 	1
    #     'b' 	signed char 	int 	1
    #     'B' 	unsigned char 	int 	1
    #     'u' 	Py_UNICODE 	Unicode character 	2 (see note)
    #     'h' 	signed short 	int 	2
    #     'H' 	unsigned short 	int 	2
    #     'i' 	signed int 	int 	2
    #     'I' 	unsigned int 	long 	2
    #     'l' 	signed long 	int 	4
    #     'L' 	unsigned long 	long 	4
    #     'f' 	float 	float 	4
    #     'd' 	double 	float 	8
    arr = array.array('B', range(16))
    print arr
    print arr[0]


def another_usage():
    arr = array.array('b', [1, 2, 3])
    arr.append(6)
    arr.append(8)
    arr.append(9)
    arr.insert(0, -1)

    print arr
    print len(arr)
    print arr.tolist()


if __name__ == '__main__':
    simple_usage()

    another_usage()
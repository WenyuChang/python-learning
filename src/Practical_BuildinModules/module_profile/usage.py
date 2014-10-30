import profile

def func():
        for i in range(1000):
            for j in range(2000):
                pass

def usage0():
    # simple usage
    profile.run('func()')
    # output:
    # ncalls:  for the number of calls,
    # tottime: for the total time spent in the given function
    #          (and excluding time made in calls to sub-functions)
    # percall: is the quotient of tottime divided by ncalls
    # cumtime: is the cumulative time spent in this and all subfunctions
    #          (from invocation till exit). This figure is accurate even for recursive functions.
    # percall: is the quotient of cumtime divided by primitive calls
    # filename:lineno(function): provides the respective data of each function
    #
    # When there are two numbers in the first column (for example 3/1), it means
    # that the function recursed. The second value is the number of primitive calls
    # and the former is the total number of calls. Note that when the function does
    # not recurse, these two values are the same, and only the single figure is printed.

def usage1():
    # print the output to the file
    # simple usage
    profile.run('func()', 'perf_file')

    # using psstats module to output profile
    import pstats
    p = pstats.Stats('perf_file')
    p.strip_dirs().sort_stats(-1).print_stats()

    # print out sorted profile
    p.sort_stats('tottime')
    p.print_stats()

    # print out top calls
    p.sort_stats('tottime')
    p.print_stats(2)  # top 2

def usage2():
    # sort profile result when call profile.run
    profile.run('func()', sort='tottime')
    # Valid Arg 	    Meaning
    # 'calls' 	    call count
    # 'cumulative' 	cumulative time
    # 'cumtime' 	    cumulative time
    # 'file' 	        file name
    # 'filename' 	    file name
    # 'module' 	    file name
    # 'ncalls' 	    call count
    # 'pcalls' 	    primitive call count
    # 'line' 	        line number
    # 'name' 	        function name
    # 'nfl' 	        name/file/line
    # 'stdname' 	    standard name
    # 'time' 	        internal time
    # 'tottime' 	    internal time

def usage3():
    # using the Profile class allows formatting profile results
    # without writing the profile data to a file

    pr = profile.Profile()
    pr.enable()

    print 'aa'

    pr.disable()

if __name__ == '__main__':
    # usage0()

    # usage1()

    # usage2()

    usage3()
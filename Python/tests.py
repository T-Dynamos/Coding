from timeit import default_timer as timer

def Run(function, args : list) -> int:
    start = timer()

    function(args)
    
    end = timer()

    return abs(start - end)
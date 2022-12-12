def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum / len(kwargs)
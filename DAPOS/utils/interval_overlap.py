
def overlap_with(interval, dic):
    for key in dic.keys():
        if max(0, min(interval[1], key[1]) - max(interval[0], key[0])):
            return True
    return False

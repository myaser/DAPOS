from banyan import SortedSet, OverlappingIntervalsUpdator


def overlap(intervals1, intervals2):
    intervals = SortedSet(intervals1,
                          key_type = (int, int),
                          updator=OverlappingIntervalsUpdator)

    results = []
    for other_interval in intervals2:
        # TODO: PROBLEM: if intervals overlap in one point, it's counted here!
        results += intervals.overlap(other_interval)
    return results

def overlap_with(interval, dic):
    for key in dic.keys():
        if max(0, min(interval[1], key[1]) - max(interval[0], key[0])):
            return True
    return False

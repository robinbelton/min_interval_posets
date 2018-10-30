def get_sublevel_sets(births_only_merge_tree,curve,eps):
    '''
    Calculates the sublevel set interval for every minimum in curve that exceeds a threshold.
    :param births_only_merge_tree: merge tree dict with intermediate points removed
    :param curve: dict with times keying function values (Curve.curve or Curve.normalized)
    :param eps: float threshold (noise level) For normalized curves, 0 < eps < 1.
    :return: dict of minima birth times keying lifetime intervals
    '''

    big_enough = [u for u,(s,v) in births_only_merge_tree.items() if not(u!=v and abs(curve[u] - curve[s]) < 2*eps)]
    times = sorted([k for k in curve])
    time_intervals = dict()
    for b in big_enough:
        i = times.index(b)
        k = i
        # the reason why we need 2*eps instead of eps is in the paper Berry et al.
        while k < len(times)-1 and abs(curve[times[k]] - curve[times[i]]) < 2*eps:
            k += 1
        j = i
        # the reason why we need 2*eps instead of eps is in the paper Berry et al.
        while j > 0 and abs(curve[times[j]] - curve[times[i]]) < 2*eps:
            j -= 1
        time_intervals[b] = (times[j],times[k])
    return time_intervals


def minimal_time_ints(births_only_merge_tree,curve,eps):
    '''
    Produce merge tree and remove intervals that overlap by picking deeper min
    (shorter interval). The remaining intervals are the "epsilon minimum intervals."
    :param births_only_merge_tree: merge tree dict with intermediate points removed
    :param curve: dict with times keying function values (Curve.curve or Curve.normalized)
    :param eps: float threshold (noise level) For normalized curves, 0 < eps < 1.
    :return: dict of minima birth times each keying the associated (closed) epsilon-minimum interval
    '''
    ti = get_sublevel_sets(births_only_merge_tree,curve,eps)
    # Choose the earliest of equally deep minima in same component
    vals = [curve[k] for k in births_only_merge_tree]
    if len(set(vals)) != len(vals):
        stack = sorted([w for w in ti],reverse=True)
        for u in stack:
            if any([u != v and curve[u] == curve[v] and ti[u][0] <= ti[v][0] and ti[u][1] >= ti[v][1] for v in ti]):
                ti.pop(u)
    stack = sorted([w for w in ti], reverse=True)
    for u in stack:
        if any([u != v and ti[u][0] <= ti[v][0] and ti[u][1] >= ti[v][1] for v in ti]):
            raise ValueError("Debug: More intervals need to be excluded.")
    return ti


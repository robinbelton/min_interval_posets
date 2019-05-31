from min_interval_posets.curve import Curve
from min_interval_posets.posets import *
import numpy as np


times = [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0, 44.0, 48.0, 52.0, 56.0, 60.0, 64.0, 68.0, 72.0, 76.0, 80.0, 84.0, 88.0, 92.0, 96.0, 100.0, 104.0, 108.0, 112.0, 116.0, 120.0, 124.0, 128.0, 132.0, 136.0, 140.0, 144.0, 148.0, 152.0, 156.0, 160.0, 164.0, 168.0, 172.0, 176.0, 180.0, 184.0, 188.0, 192.0, 196.0]

# data = np.asarray([[2.85, 79.04, 50.87, 32.95, 21.65, 14.52, 10.01, 7.15, 5.35, 4.21, 3.5, 3.05, 2.76, 2.59, 2.48, 2.39, 2.27, 2.16, 2.09, 2.04, 2.01, 2.0, 2.03, 2.11, 2.33, 3.0, 75.06, 48.28, 31.31, 20.61, 13.87, 9.6, 6.89, 5.18, 4.11, 3.43, 3.01, 2.74, 2.57, 2.47, 2.38, 2.25, 2.15, 2.08, 2.03, 2.01, 2.01, 2.03, 2.13, 2.37], [18.0, 434.11, 1431.49, 1579.93, 1570.39, 1519.12, 1474.24, 1443.22, 1423.15, 1410.45, 1402.45, 1397.28, 1392.93, 1383.26, 1340.44, 1199.38, 933.38, 629.04, 400.88, 251.94, 158.03, 99.38, 62.83, 40.08, 25.93, 17.14, 683.52, 1464.79, 1584.2, 1564.95, 1513.09, 1469.85, 1440.33, 1421.31, 1409.29, 1401.72, 1396.77, 1392.28, 1380.88, 1330.05, 1173.99, 895.68, 597.06, 379.39, 238.29, 149.49, 94.05, 59.52, 38.02, 24.65], [2.85, 1044.82, 1938.7, 2066.94, 1996.09, 1639.77, 956.7, 396.65, 140.02, 49.38, 19.46, 9.19, 5.3, 3.64, 2.85, 2.41, 2.0, 1.62, 1.37, 1.21, 1.12, 1.08, 1.09, 1.21, 1.6, 3.27, 1254.03, 1971.96, 2067.5, 1972.97, 1569.92, 874.21, 351.95, 123.32, 43.85, 17.61, 8.52, 5.03, 3.51, 2.78, 2.36, 1.95, 1.59, 1.34, 1.2, 1.11, 1.08, 1.1, 1.24, 1.69], [1.09, 36.92, 123.67, 183.85, 225.59, 254.53, 274.54, 287.31, 273.84, 203.85, 142.1, 98.73, 68.62, 47.73, 33.25, 23.21, 16.24, 11.41, 8.06, 5.73, 4.12, 3.0, 2.23, 1.69, 1.32, 1.06, 49.06, 132.09, 189.7, 229.64, 257.34, 276.47, 288.1, 267.36, 195.4, 136.05, 94.53, 65.7, 45.71, 31.85, 22.23, 15.57, 10.94, 7.73, 5.51, 3.97, 2.9, 2.15, 1.64, 1.28], [0.15, 45.75, 148.2, 155.55, 156.06, 156.1, 156.1, 156.1, 156.1, 156.1, 156.1, 156.05, 155.79, 154.25, 145.76, 111.6, 51.25, 14.2, 3.14, 0.73, 0.26, 0.17, 0.15, 0.15, 0.15, 0.15, 74.53, 150.36, 155.7, 156.08, 156.1, 156.1, 156.1, 156.1, 156.1, 156.09, 156.04, 155.72, 153.81, 143.54, 104.96, 44.93, 11.94, 2.62, 0.63, 0.24, 0.17, 0.15, 0.15, 0.15], [0.52, 2.69, 728.1, 1449.09, 1782.01, 1929.02, 1993.48, 2021.71, 2033.93, 2036.84, 2019.96, 1906.59, 1485.2, 853.35, 408.13, 182.59, 79.99, 34.92, 15.35, 6.89, 3.24, 1.67, 0.99, 0.7, 0.57, 0.52, 13.03, 842.37, 1504.49, 1806.62, 1939.82, 1998.21, 2023.78, 2034.76, 2036.39, 2014.45, 1876.89, 1411.43, 786.49, 371.56, 165.56, 72.45, 31.63, 13.93, 6.28, 2.98, 1.56, 0.94, 0.68, 0.56]])

data=np.array([[0.01103, 1.00000, 0.63435, 0.40174, 0.25506, 0.16251, 0.10397,
        0.06685, 0.04348, 0.02869, 0.01947, 0.01363, 0.00987, 0.00766,
        0.00623, 0.00506, 0.00350, 0.00208, 0.00117, 0.00052, 0.00013,
        0.00000, 0.00039, 0.00143, 0.00428, 0.01298, 0.94834, 0.60073,
        0.38045, 0.24156, 0.15408, 0.09865, 0.06347, 0.04128, 0.02739,
        0.01856, 0.01311, 0.00961, 0.00740, 0.00610, 0.00493, 0.00325,
        0.00195, 0.00104, 0.00039, 0.00013, 0.00013, 0.00039, 0.00169,
        0.00480],
       [0.00055, 0.26608, 0.90255, 0.99728, 0.99119, 0.95847, 0.92983,
        0.91004, 0.89723, 0.88912, 0.88402, 0.88072, 0.87794, 0.87177,
        0.84445, 0.75443, 0.58469, 0.39048, 0.24488, 0.14983, 0.08991,
        0.05248, 0.02916, 0.01464, 0.00561, 0.00000, 0.42524, 0.92380,
        1.00000, 0.98772, 0.95462, 0.92703, 0.90819, 0.89605, 0.88838,
        0.88355, 0.88039, 0.87753, 0.87025, 0.83782, 0.73823, 0.56063,
        0.37007, 0.23117, 0.14112, 0.08446, 0.04908, 0.02704, 0.01332,
        0.00479],
       [0.00086, 0.50510, 0.93767, 0.99973, 0.96544, 0.79301, 0.46245,
        0.19143, 0.06724, 0.02337, 0.00889, 0.00392, 0.00204, 0.00124,
        0.00086, 0.00064, 0.00045, 0.00026, 0.00014, 0.00006, 0.00002,
        0.00000, 0.00000, 0.00006, 0.00025, 0.00106, 0.60634, 0.95377,
        1.00000, 0.95425, 0.75921, 0.42253, 0.16980, 0.05916, 0.02070,
        0.00800, 0.00360, 0.00191, 0.00118, 0.00082, 0.00062, 0.00042,
        0.00025, 0.00013, 0.00006, 0.00001, 0.00000, 0.00001, 0.00008,
        0.00030],
       [0.00010, 0.12493, 0.42715, 0.63681, 0.78223, 0.88305, 0.95276,
        0.99725, 0.95032, 0.70649, 0.49136, 0.34027, 0.23537, 0.16259,
        0.11214, 0.07717, 0.05288, 0.03606, 0.02439, 0.01627, 0.01066,
        0.00676, 0.00408, 0.00219, 0.00091, 0.00000, 0.16722, 0.45649,
        0.65719, 0.79634, 0.89284, 0.95948, 1.00000, 0.92775, 0.67705,
        0.47028, 0.32563, 0.22520, 0.15555, 0.10727, 0.07375, 0.05055,
        0.03442, 0.02324, 0.01550, 0.01014, 0.00641, 0.00380, 0.00202,
        0.00077],
       [0.00000, 0.29240, 0.94934, 0.99647, 0.99974, 1.00000, 1.00000,
        1.00000, 1.00000, 1.00000, 1.00000, 0.99968, 0.99801, 0.98814,
        0.93370, 0.71465, 0.32767, 0.09009, 0.01917, 0.00372, 0.00071,
        0.00013, 0.00000, 0.00000, 0.00000, 0.00000, 0.47695, 0.96319,
        0.99744, 0.99987, 1.00000, 1.00000, 1.00000, 1.00000, 1.00000,
        0.99994, 0.99962, 0.99756, 0.98532, 0.91946, 0.67207, 0.28714,
        0.07560, 0.01584, 0.00308, 0.00058, 0.00013, 0.00000, 0.00000,
        0.00000],
       [0.00000, 0.00107, 0.35730, 0.71137, 0.87486, 0.94705, 0.97871,
        0.99257, 0.99857, 1.00000, 0.99171, 0.93604, 0.72910, 0.41881,
        0.20017, 0.08941, 0.03903, 0.01689, 0.00728, 0.00313, 0.00134,
        0.00056, 0.00023, 0.00009, 0.00002, 0.00000, 0.00614, 0.41342,
        0.73857, 0.88694, 0.95236, 0.98103, 0.99359, 0.99898, 0.99978,
        0.98900, 0.92145, 0.69287, 0.38598, 0.18221, 0.08105, 0.03532,
        0.01528, 0.00659, 0.00283, 0.00121, 0.00051, 0.00021, 0.00008,
        0.00002]])

names = ["A", "B", "C", "D", "E", "F"]
curves = [Curve(data[k, :]/sum(data[k, :]), times, True) for k in range(data.shape[0])]
c = dict(zip(names, curves))


def test1():
    eps = 0.05

    solns = {
        "A" : [((0.0, 4.0), ('A', 'min')),((0.0, 8.0), ('A', 'max')), ((24.0, 104.0), ('A', 'min')),((100.0, 108.0), ('A', 'max')), ((120.0, 196.0), ('A', 'min'))], "B" : [((0.0, 4.0), ('B', 'min')), ((4.0, 32.0), ('B', 'max')), ((76.0, 104.0), ('B', 'min')), ((104.0, 132.0), ('B', 'max')), ((176.0, 196.0), ('B', 'min'))], "C" : [((0.0, 4.0), ('C', 'min')), ((4.0, 20.0), ('C','max')), ((28.0, 104.0), ('C', 'min')), ((104.0, 120.0), ('C', 'max')), ((128.0, 196.0), ('C', 'min'))], "D" : [((0.0, 4.0), ('D', 'min')), ((20.0, 36.0), ('D', 'max')), ((56.0, 104.0), ('D', 'min')), ((120.0, 136.0), ('D', 'max')), ((156.0, 196.0), ('D', 'min'))], "E" : [((0.0, 4.0), ('E', 'min')), ((4.0, 60.0), ('E', 'max')), ((64.0, 104.0), ('E', 'min')), ((104.0, 160.0), ('E','max')), ((164.0, 196.0), ('E', 'min'))], "F" : [((0.0, 8.0), ('F', 'min')), ((16.0, 48.0), ('F', 'max')), ((56.0, 108.0), ('F', 'min')), ((116.0, 148.0), ('F', 'max')), ((156.0, 196.0), ('F', 'min'))]
    }

    for k in ["A","B","C","D","E","F"]:
        assert(get_total_order(k,c[k],eps)[0] == solns[k])

    eps = 0.51

    for k in ["A","B","C","D","E","F"]:
        assert(get_total_order(k,c[k],eps)[0] == [])


def test2():
    eps = 0.05

    edges = set([
        (0,1),(0,2),(0,3),(0,4),(0,6),(0,7),(0,8),(0,9),
        (1,2),(1,3),(1,4),(1,7),(1,8),(1,9),
        (2,3),(2,4),(2,8),(2,9),
        (3,4),(3,9),
        (5,2),(5,3),(5,4),(5,6),(5,7),(5,8),(5,9),
        (6,3),(6,4),(6,7),(6,8),(6,9),
        (7,4),(7,8),(7,9),
        (8,9)
    ])

    ct = {"A" : c["A"], "B" : c["B"]}
    assert(eps_posets(ct, [eps])[0][1][1] == edges)

    eps = 0.1

    solns = {
        "A": [((0.0, 4.0), ('A', 'min')), ((0.0, 8.0), ('A', 'max')), ((16.0, 104.0), ('A', 'min')), ((100.0, 108.0),('A', 'max')),((116.0, 196.0), ('A', 'min'))],
        "B": [((0.0, 4.0), ('B', 'min')), ((4.0, 60.0), ('B', 'max')), ((72.0, 104.0), ('B', 'min')), ((104.0, 160.0), ('B', 'max')), ((172.0, 196.0), ('B', 'min'))]
    }

    for k in ["A","B"]:
        print(get_total_order(k,c[k],eps)[0])
        assert(get_total_order(k,c[k],eps)[0] == solns[k])

    edges1 = eps_posets(ct, [eps])[0][1][1]
    assert(edges1.issubset(edges))

    eps = 0.2

    solns = {
        "A": [((0.0, 4.0), ('A', 'min')), ((0.0, 12.0), ('A', 'max')), ((12.0, 104.0), ('A', 'min')),((100.0, 112.0),('A', 'max')),((108.0, 196.0), ('A', 'min'))],
        "B": [((0.0, 8.0), ('B', 'min')), ((4.0, 64.0), ('B', 'max')), ((64.0, 104.0), ('B', 'min')), ((104.0,164.0), ('B','max')), ((164.0, 196.0), ('B', 'min'))]
    }

    for k in ["A","B"]:
        assert(get_total_order(k,c[k],eps)[0] == solns[k])

    edges2 = eps_posets(ct, [eps])[0][1][1]
    assert(edges2.issubset(edges1))


def test3():
    curve6 = Curve({0:2,1:2,2:2,3:2,4:2,5:2,6:2,7:2})
    curve7 = Curve({0:2,1:2,2:2,3:2,4:2,5:2,6:2})
    eps=0.1

    def part(curve):
        n = curve.normalize()
        r = curve.normalize_reflect()
        merge_tree_mins = tmt.births_only(n)
        merge_tree_maxs = tmt.births_only(r)
        # time_ints_mins = ss.minimal_time_ints(merge_tree_mins,n,eps)
        # time_ints_maxs = ss.minimal_time_ints(merge_tree_maxs,r,eps)
        time_ints_mins = ss.get_sublevel_sets(merge_tree_mins,n,eps)
        time_ints_maxs = ss.get_sublevel_sets(merge_tree_maxs,r,eps)
        labeled_mins = sorted([(v,("name","min")) for _,v in time_ints_mins.items()])
        labeled_maxs = sorted([(v,("name","max")) for _,v in time_ints_maxs.items()])
        # When eps is close to (b-a)/2 for max b and min a, then the intervals can be identical. Annihilate them.
        all_extrema = labeled_mins+labeled_maxs
        nodes = annihilate(sorted(all_extrema))
        return all_extrema,nodes


    all_extrema,nodes = part(curve6)
    assert(len(all_extrema) == 16)
    assert(len(nodes)==0)
    all_extrema,nodes = part(curve7)
    assert(len(all_extrema) == 14)
    assert(len(nodes)==0)
    nodes,edges = get_total_order("name", curve6, eps)
    assert(len(nodes)==0)
    nodes,edges = get_total_order("name", curve7, eps)
    assert(len(nodes)==0)

    posets = eps_posets({"curve6":curve6},[eps])
    assert(posets == [(eps, ([], set()))])


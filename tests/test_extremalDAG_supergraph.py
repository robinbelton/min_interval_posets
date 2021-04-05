from min_interval_posets.curve import Curve
from min_interval_posets.extremal_DAG import get_extremalDAG
from min_interval_posets.supergraph import get_supergraph
import numpy as np

######################
####### TEST 1 #######
######################

def test1():
    c1 = Curve({0:1, 5:10, 10:3})
    c2 = Curve({0:8, 5:3, 10:1})
    curves = {"1":c1, "2":c2}
    DAG1 = get_extremalDAG(curves)
    assert(DAG1 == ([('1', 'min'), ('1', 'max'), ('1', 'min'), ('2', 'max'), ('2', 'min')],
    [(0, 4.5), (1, 4.5), (2, 3.5), (3, 3.5), (4, 3.5)],
    [((0, 1), 4.5),
    ((0, 2), 3.5),
    ((0, 4), 0),
    ((1, 2), 3.5),
    ((1, 4), 0),
    ((3, 1), 0),
    ((3, 2), 0),
    ((3, 4), 3.5)]))

    c1 = Curve({0:1, 5:7, 9:1, 10:2})
    c2 = Curve({0:10, 5:2, 10:0})
    curves = {"1":c1, "2":c2}
    DAG2 = get_extremalDAG(curves)
    assert(DAG2 == ([('1', 'min'),
    ('1', 'max'),
    ('1', 'min'),
    ('1', 'max'),
    ('2', 'max'),
    ('2', 'min')],
    [(0, 3.0), (1, 3.0), (2, 3.0), (3, 0.5), (4, 5.0), (5, 5.0)],
    [((0, 1), 3.0),
    ((0, 2), 3.0),
    ((0, 3), 0.5),
    ((0, 5), 0),
    ((1, 2), 3.0),
    ((1, 3), 0.5),
    ((1, 5), 0),
    ((2, 3), 0.5),
    ((2, 5), 0),
    ((4, 1), 0),
    ((4, 2), 0),
    ((4, 3), 0.5),
    ((4, 5), 5.0)]))

    names = ['1', '2']
    supergraph = get_supergraph(names, DAG1, DAG2)
    assert(supergraph == ([(('1', 'min'), (4.5, 3.0)),
    (('1', 'max'), (4.5, 3.0)),
    (('1', 'min'), (3.5, 3.0)),
    (('1', 'max'), (0, 0.5)),
    (('2', 'max'), (3.5, 5.0)),
    (('2', 'min'), (3.5, 5.0))],
    [((0, 1), (4.5, 3.0)),
    ((0, 2), (3.5, 3.0)),
    ((0, 3), (0, 0.5)),
    ((1, 2), (3.5, 3.0)),
    ((1, 3), (0, 0.5)),
    ((2, 3), (0, 0.5)),
    ((4, 3), (0, 0.5)),
    ((4, 5), (3.5, 5.0))],
    3.9370039370059056))

######################
####### TEST 2 #######
######################

def test2():
    c1 = Curve({0:0, 1:2, 4:5, 5:1, 7:10, 10:7})
    c2 = Curve({0:0, 3:2, 6:4, 10:5})
    curves = {"1":c1, "2":c2}
    DAG1 = get_extremalDAG(curves)
    assert(DAG1 == ([('1', 'min'),
    ('1', 'max'),
    ('1', 'min'),
    ('1', 'max'),
    ('1', 'min'),
    ('2', 'min'),
    ('2', 'max')],
    [(0, 5.0), (1, 2.0), (2, 2.0), (3, 5.0), (4, 1.5), (5, 2.5), (6, 2.5)],
    [((0, 1), 2.0),
    ((0, 2), 2.0),
    ((0, 3), 5.0),
    ((0, 4), 1.5),
    ((0, 6), 1.0),
    ((1, 2), 2.0),
    ((1, 3), 2.0),
    ((1, 4), 1.5),
    ((1, 6), 0.5),
    ((2, 3), 2.0),
    ((2, 4), 1.5),
    ((2, 6), 0),
    ((3, 4), 1.5),
    ((3, 6), 0),
    ((5, 1), 0),
    ((5, 2), 1.0),
    ((5, 3), 1.0),
    ((5, 4), 1.5),
    ((5, 6), 2.5)]))

    c1 = Curve({0:.5, 7:9, 10:6})
    c2 = Curve({0:0, 3:2, 6:4, 10:5})
    curves = {"1":c1, "2":c2}
    DAG2 = get_extremalDAG(curves)
    assert(DAG2 == ([('1', 'min'), ('1', 'max'), ('1', 'min'), ('2', 'min'), ('2', 'max')],
    [(0, 4.25), (1, 4.25), (2, 1.5), (3, 2.5), (4, 2.5)],
    [((0, 1), 4.25),
    ((0, 2), 1.5),
    ((0, 4), 0),
    ((1, 2), 1.5),
    ((1, 4), 0),
    ((3, 1), 0),
    ((3, 2), 1.5),
    ((3, 4), 2.5)]))

    names = ['1', '2']
    supergraph = get_supergraph(names, DAG1, DAG2)
    assert(supergraph == ([(('1', 'min'), (5.0, 4.25)),
    (('1', 'max'), (2.0, 0)),
    (('1', 'min'), (2.0, 0)),
    (('1', 'max'), (5.0, 4.25)),
    (('1', 'min'), (1.5, 1.5)),
    (('2', 'min'), (2.5, 2.5)),
    (('2', 'max'), (2.5, 2.5))],
    [((0, 1), (2.0, 0)),
    ((0, 2), (2.0, 0)),
    ((0, 3), (5.0, 4.25)),
    ((0, 4), (1.5, 1.5)),
    ((0, 6), (1.0, 0)),
    ((1, 2), (2.0, 0)),
    ((1, 3), (2.0, 0)),
    ((1, 4), (1.5, 0)),
    ((1, 6), (0.5, 0)),
    ((2, 3), (2.0, 0)),
    ((2, 4), (1.5, 0)),
    ((3, 4), (1.5, 1.5)),
    ((5, 2), (1.0, 0)),
    ((5, 3), (1.0, 0)),
    ((5, 4), (1.5, 1.5)),
    ((5, 6), (2.5, 2.5))],
    6.118619125260208))

######################
####### TEST 3 #######
######################

def test3():
    c1 = Curve({0:1, 5:10, 10:3})
    c2 = Curve({0:8, 5:3, 10:1})
    c3 = Curve({0:2, 5:9, 10:4})
    curves = {"1":c1, "2":c2, "3":c3}
    DAG1 = get_extremalDAG(curves)
    assert(DAG1 == ([('1', 'min'),
    ('1', 'max'),
    ('1', 'min'),
    ('2', 'max'),
    ('2', 'min'),
    ('3', 'min'),
    ('3', 'max'),
    ('3', 'min')],
    [(0, 4.5),
    (1, 4.5),
    (2, 3.5),
    (3, 3.5),
    (4, 3.5),
    (5, 3.5),
    (6, 3.5),
    (7, 2.5)],
    [((0, 1), 4.5),
    ((0, 2), 3.5),
    ((0, 4), 0),
    ((0, 6), 0),
    ((0, 7), 0),
    ((1, 2), 3.5),
    ((1, 4), 0),
    ((1, 7), 0),
    ((3, 1), 0),
    ((3, 2), 0),
    ((3, 4), 3.5),
    ((3, 6), 0),
    ((3, 7), 0),
    ((5, 1), 0),
    ((5, 2), 0),
    ((5, 4), 0),
    ((5, 6), 3.5),
    ((5, 7), 2.5),
    ((6, 2), 0),
    ((6, 4), 0),
    ((6, 7), 2.5)]))

    c1 = Curve({0:1, 5:7, 9:1, 10:2})
    c2 = Curve({0:10, 5:2, 10:0})
    c3 = Curve({0:2.5, 5:9, 10:4})
    curves = {"1":c1, "2":c2, "3":c3}
    DAG2 = get_extremalDAG(curves)
    assert(DAG2 == ([('1', 'min'),
    ('1', 'max'),
    ('1', 'min'),
    ('1', 'max'),
    ('2', 'max'),
    ('2', 'min'),
    ('3', 'min'),
    ('3', 'max'),
    ('3', 'min')],
    [(0, 3.0),
    (1, 3.0),
    (2, 3.0),
    (3, 0.5),
    (4, 5.0),
    (5, 5.0),
    (6, 3.25),
    (7, 3.25),
    (8, 2.5)],
    [((0, 1), 3.0),
    ((0, 2), 3.0),
    ((0, 3), 0.5),
    ((0, 5), 0),
    ((0, 7), 0),
    ((0, 8), 0),
    ((1, 2), 3.0),
    ((1, 3), 0.5),
    ((1, 5), 0),
    ((1, 8), 0),
    ((2, 3), 0.5),
    ((2, 5), 0),
    ((2, 8), 0),
    ((4, 1), 0),
    ((4, 2), 0),
    ((4, 3), 0.5),
    ((4, 5), 5.0),
    ((4, 7), 0),
    ((4, 8), 0),
    ((6, 1), 0),
    ((6, 2), 0),
    ((6, 3), 0.5),
    ((6, 5), 0),
    ((6, 7), 3.25),
    ((6, 8), 2.5),
    ((7, 2), 0),
    ((7, 3), 0),
    ((7, 5), 0),
    ((7, 8), 2.5)]))

    names = ['1', '2','3']
    supergraph = get_supergraph(names, DAG1, DAG2)
    assert(supergraph == ([(('1', 'min'), (4.5, 3.0)),
    (('1', 'max'), (4.5, 3.0)),
    (('1', 'min'), (3.5, 3.0)),
    (('1', 'max'), (0, 0.5)),
    (('2', 'max'), (3.5, 5.0)),
    (('2', 'min'), (3.5, 5.0)),
    (('3', 'min'), (3.5, 3.25)),
    (('3', 'max'), (3.5, 3.25)),
    (('3', 'min'), (2.5, 2.5))],
    [((0, 1), (4.5, 3.0)),
    ((0, 2), (3.5, 3.0)),
    ((0, 3), (0, 0.5)),
    ((1, 2), (3.5, 3.0)),
    ((1, 3), (0, 0.5)),
    ((2, 3), (0, 0.5)),
    ((4, 3), (0, 0.5)),
    ((4, 5), (3.5, 5.0)),
    ((6, 3), (0, 0.5)),
    ((6, 7), (3.5, 3.25)),
    ((6, 8), (2.5, 2.5)),
    ((7, 8), (2.5, 2.5))],
    3.992179855667828))

######################
####### TEST 4 #######
######################

def test4():
    x = np.arange(0,2*np.pi,0.1)   # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    c1 = Curve({x[i]:y[i] for i in range(len(x))})
    c2 = Curve({x[i]:z[i] for i in range(len(y))})
    curves = {"sine":c1, "cosine":c2}
    DAG1 = get_extremalDAG(curves)
    assert(DAG1 == ([('sine', 'min'),
    ('sine', 'max'),
    ('sine', 'min'),
    ('sine', 'max'),
    ('cosine', 'max'),
    ('cosine', 'min'),
    ('cosine', 'max')],
    [(0, 0.49978680152075255),
    (1, 0.999748430302803),
    (2, 0.999748430302803),
    (3, 0.4584169273733022),
    (4, 0.9995675751366397),
    (5, 0.9995675751366397),
    (6, 0.9978386236482485)],
    [((0, 1), 0.49978680152075255),
    ((0, 2), 0.49978680152075255),
    ((0, 3), 0.4584169273733022),
    ((0, 5), 0.4927248649942301),
    ((0, 6), 0.49978680152075255),
    ((1, 2), 0.999748430302803),
    ((1, 3), 0.4584169273733022),
    ((1, 5), 0.12693419543239254),
    ((1, 6), 0.8250928589434148),
    ((2, 3), 0.4584169273733022),
    ((2, 6), 0.11357938500405684),
    ((4, 1), 0.11757890635775581),
    ((4, 2), 0.8331380106399122),
    ((4, 3), 0.4584169273733022),
    ((4, 5), 0.9995675751366397),
    ((4, 6), 0.9978386236482485),
    ((5, 2), 0.12156038112808631),
    ((5, 3), 0.45653760300917207),
    ((5, 6), 0.9978386236482485)]))

    # Adding small noise to curves
    c1.curve[6.0] = 0
    c2.curve[0.4] = 1
    curves = {"sine":c1, "cosine":c2}
    DAG2 = get_extremalDAG(curves)
    assert(DAG2 == ([('sine', 'min'),
    ('sine', 'max'),
    ('sine', 'min'),
    ('sine', 'max'),
    ('sine', 'min'),
    ('sine', 'max'),
    ('cosine', 'max'),
    ('cosine', 'min'),
    ('cosine', 'max'),
    ('cosine', 'min'),
    ('cosine', 'max')],
    [(0, 0.49978680152075255),
    (1, 0.999748430302803),
    (2, 0.999748430302803),
    (3, 0.4999616287820504),
    (4, 0.09108125213604751),
    (5, 0.0495365507272993),
    (6, 0.9995675751366397),
    (7, 0.02233175543719701),
    (8, 0.02233175543719701),
    (9, 0.9995675751366397),
    (10, 0.9978386236482485)],
    [((0, 1), 0.49978680152075255),
    ((0, 2), 0.49978680152075255),
    ((0, 3), 0.49978680152075255),
    ((0, 4), 0.09108125213604751),
    ((0, 5), 0.0495365507272993),
    ((0, 7), 0.012365044357817823),
    ((0, 8), 0.02233175543719701),
    ((0, 9), 0.4927248649942301),
    ((0, 10), 0.49978680152075255),
    ((1, 2), 0.999748430302803),
    ((1, 3), 0.4999616287820504),
    ((1, 4), 0.09108125213604751),
    ((1, 5), 0.0495365507272993),
    ((1, 9), 0.12693419543239254),
    ((1, 10), 0.8250928589434148),
    ((2, 3), 0.4999616287820504),
    ((2, 4), 0.09108125213604751),
    ((2, 5), 0.0495365507272993),
    ((2, 10), 0.11357938500405684),
    ((3, 4), 0.09108125213604751),
    ((3, 5), 0.0495365507272993),
    ((3, 10), 0),
    ((4, 5), 0.0495365507272993),
    ((4, 10), 0),
    ((6, 1), 0.11757890635775581),
    ((6, 2), 0.8331380106399122),
    ((6, 3), 0.4999616287820504),
    ((6, 4), 0.09108125213604751),
    ((6, 5), 0.0495365507272993),
    ((6, 7), 0.02233175543719701),
    ((6, 8), 0.02233175543719701),
    ((6, 9), 0.9995675751366397),
    ((6, 10), 0.9978386236482485),
    ((7, 1), 0.02233175543719701),
    ((7, 2), 0.02233175543719701),
    ((7, 3), 0.02233175543719701),
    ((7, 4), 0.02233175543719701),
    ((7, 5), 0.02233175543719701),
    ((7, 8), 0.02233175543719701),
    ((7, 9), 0.02233175543719701),
    ((7, 10), 0.02233175543719701),
    ((8, 1), 0.02233175543719701),
    ((8, 2), 0.02233175543719701),
    ((8, 3), 0.02233175543719701),
    ((8, 4), 0.02233175543719701),
    ((8, 5), 0.02233175543719701),
    ((8, 9), 0.02233175543719701),
    ((8, 10), 0.02233175543719701),
    ((9, 2), 0.12156038112808631),
    ((9, 3), 0.49337324340519445),
    ((9, 4), 0.09108125213604751),
    ((9, 5), 0.0495365507272993),
    ((9, 10), 0.9978386236482485)]))
    
    names = ['sine', 'cosine']
    supergraph = get_supergraph(names, DAG1, DAG2)
    assert(supergraph == ([(('sine', 'min'), (0.49978680152075255, 0.49978680152075255)),
    (('sine', 'max'), (0.999748430302803, 0.999748430302803)),
    (('sine', 'min'), (0.999748430302803, 0.999748430302803)),
    (('sine', 'max'), (0.4584169273733022, 0.4999616287820504)),
    (('sine', 'min'), (0, 0.09108125213604751)),
    (('sine', 'max'), (0, 0.0495365507272993)),
    (('cosine', 'max'), (0.9995675751366397, 0.9995675751366397)),
    (('cosine', 'min'), (0, 0.02233175543719701)),
    (('cosine', 'max'), (0, 0.02233175543719701)),
    (('cosine', 'min'), (0.9995675751366397, 0.9995675751366397)),
    (('cosine', 'max'), (0.9978386236482485, 0.9978386236482485))],
    [((0, 1), (0.49978680152075255, 0.49978680152075255)),
    ((0, 2), (0.49978680152075255, 0.49978680152075255)),
    ((0, 3), (0.4584169273733022, 0.49978680152075255)),
    ((0, 4), (0, 0.09108125213604751)),
    ((0, 5), (0, 0.0495365507272993)),
    ((0, 7), (0, 0.012365044357817823)),
    ((0, 8), (0, 0.02233175543719701)),
    ((0, 9), (0.4927248649942301, 0.4927248649942301)),
    ((0, 10), (0.49978680152075255, 0.49978680152075255)),
    ((1, 2), (0.999748430302803, 0.999748430302803)),
    ((1, 3), (0.4584169273733022, 0.4999616287820504)),
    ((1, 4), (0, 0.09108125213604751)),
    ((1, 5), (0, 0.0495365507272993)),
    ((1, 9), (0.12693419543239254, 0.12693419543239254)),
    ((1, 10), (0.8250928589434148, 0.8250928589434148)),
    ((2, 3), (0.4584169273733022, 0.4999616287820504)),
    ((2, 4), (0, 0.09108125213604751)),
    ((2, 5), (0, 0.0495365507272993)),
    ((2, 10), (0.11357938500405684, 0.11357938500405684)),
    ((3, 4), (0, 0.09108125213604751)),
    ((3, 5), (0, 0.0495365507272993)),
    ((4, 5), (0, 0.0495365507272993)),
    ((6, 1), (0.11757890635775581, 0.11757890635775581)),
    ((6, 2), (0.8331380106399122, 0.8331380106399122)),
    ((6, 3), (0.4584169273733022, 0.4999616287820504)),
    ((6, 4), (0, 0.09108125213604751)),
    ((6, 5), (0, 0.0495365507272993)),
    ((6, 7), (0, 0.02233175543719701)),
    ((6, 8), (0, 0.02233175543719701)),
    ((6, 9), (0.9995675751366397, 0.9995675751366397)),
    ((6, 10), (0.9978386236482485, 0.9978386236482485)),
    ((7, 1), (0, 0.02233175543719701)),
    ((7, 2), (0, 0.02233175543719701)),
    ((7, 3), (0, 0.02233175543719701)),
    ((7, 4), (0, 0.02233175543719701)),
    ((7, 5), (0, 0.02233175543719701)),
    ((7, 8), (0, 0.02233175543719701)),
    ((7, 9), (0, 0.02233175543719701)),
    ((7, 10), (0, 0.02233175543719701)),
    ((8, 1), (0, 0.02233175543719701)),
    ((8, 2), (0, 0.02233175543719701)),
    ((8, 3), (0, 0.02233175543719701)),
    ((8, 4), (0, 0.02233175543719701)),
    ((8, 5), (0, 0.02233175543719701)),
    ((8, 9), (0, 0.02233175543719701)),
    ((8, 10), (0, 0.02233175543719701)),
    ((9, 2), (0.12156038112808631, 0.12156038112808631)),
    ((9, 3), (0.45653760300917207, 0.49337324340519445)),
    ((9, 4), (0, 0.09108125213604751)),
    ((9, 5), (0, 0.0495365507272993)),
    ((9, 10), (0.9978386236482485, 0.9978386236482485))],
    0.312731099172106))

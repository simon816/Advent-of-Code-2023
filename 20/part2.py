from collections import namedtuple, defaultdict
from functools import reduce
import math
import queue
import sys

FlipFlop = namedtuple('FlipFlop', 'outputs state')
Conjunction = namedtuple('Conjunction', 'outputs inputs state')

broadcaster = None
modules = {}
input_map = defaultdict(list)

for line in sys.stdin.readlines():
    module, outputs = line.strip().split(' -> ')
    outputs = tuple(outputs.split(', '))
    if module == 'broadcaster':
        broadcaster = outputs
        continue
    elif module[0] == '%':
        name = module[1:]
        modules[name] = FlipFlop(outputs=outputs, state=False)
    elif module[0] == '&':
        name = module[1:]
        modules[name] = Conjunction(outputs=outputs, inputs=None, state=0)
    else:
        assert False
    for out in outputs:
        input_map[out].append(name)

for name, module in sorted(modules.items()):
    if type(module) == Conjunction and name in input_map:
        modules[name] = module._replace(inputs=tuple(input_map[name]))
    print(name, modules[name])

not_gates = input_map[input_map['rx'][0]]
counters = list(input_map[gate][0] for gate in not_gates)

values = []
for start in broadcaster:
    counter = None
    for c in counters:
        if start in modules[c].inputs:
            counter = c
            break
    assert counter is not None
    place = 0
    count_value = 0
    node = start
    while True:
        mod = modules[node]
        assert type(mod) == FlipFlop
        if node in modules[counter].inputs:
            count_value |= 1 << place
            print(counter, node, place)
        outputs = list(mod.outputs)
        if counter in outputs:
            outputs.remove(counter)
        if not outputs:
            break
        assert len(outputs) == 1
        node = outputs[0]
        place += 1
    values.append(count_value)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print(reduce(lcm, values, 1))

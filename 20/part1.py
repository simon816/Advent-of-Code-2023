from collections import namedtuple, defaultdict
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

for name, module in modules.items():
    if type(module) == Conjunction and name in input_map:
        modules[name] = module._replace(inputs=tuple(input_map[name]))

def press():
    low_count = 1 # button starts as 1
    high_count = 0
    pulses = queue.Queue()
    for mod in broadcaster:
        pulses.put((False, mod, None))
    while not pulses.empty():
        high, mod, src = pulses.get()
        if high:
            high_count += 1
        else:
            low_count += 1
        if mod not in modules:
            continue
        module = modules[mod]
        if type(module) == FlipFlop and not high:
            module = module._replace(state=not module.state)
            for out in module.outputs:
                pulses.put((module.state, out, mod))
            modules[mod] = module
        elif type(module) == Conjunction:
            pos = module.inputs.index(src)
            num = len(module.inputs)
            val = 1 << pos
            if high:
                state = module.state | val
            else:
                state = module.state & ~val
            module = module._replace(state=state)
            modules[mod] = module
            send = False if state == (1 << num) - 1 else True
            for out in module.outputs:
                pulses.put((send, out, mod))
    return low_count, high_count

hi = 0
lo = 0
for _ in range(1000):
    l, h = press()
    hi += h
    lo += l

print(hi * lo)

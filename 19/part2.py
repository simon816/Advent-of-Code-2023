import sys
import operator

opp = { '<': '>=', '>': '<=' }

workflows = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        break
    name, rest = line.split('{', 2)
    assert rest[-1] == '}'
    rules = rest[:-1].split(',')
    conditions = []
    negative = []
    terminal = False
    for rule in rules:
        assert not terminal
        if rule.find(':') != -1:
            cond, dest = rule.split(':')
            assert cond[1] in '<>'
            component = cond[0]
            value = int(cond[2:])
            conditions.append(negative + [(component, cond[1], value), dest])
            negative.append((component, opp[cond[1]], value))
        else:
            conditions.append(negative + [rule])
            terminal = True
    workflows[name] = conditions

def get_flattened(workflow):
    flat = []
    for conds in workflows[workflow]:
        dest = conds[-1]
        if dest not in 'RA':
            for dest_conds in get_flattened(dest):
                flat.append(conds[:-1] + dest_conds)
        else:
            flat.append(conds)
    return flat

s = 0
for conds in get_flattened('in'):
    if conds[-1] == 'A':
        min_v = {}
        max_v = {}
        min_v['x'] = min_v['m'] = min_v['a'] = min_v['s'] = 1
        max_v['x'] = max_v['m'] = max_v['a'] = max_v['s'] = 4000
        for (comp, op, val) in conds[:-1]:
            if op == '<':
                max_v[comp] = min(max_v[comp], val - 1)
            elif op == '>':
                min_v[comp] = max(min_v[comp], val + 1)
            elif op == '<=':
                max_v[comp] = min(max_v[comp], val)
            elif op == '>=':
                min_v[comp] = max(min_v[comp], val)
            else:
                assert False
        combinations = 1
        for comp in 'xmas':
            vals = max_v[comp] - (min_v[comp] - 1)
            combinations *= vals
        s += combinations

print(s)

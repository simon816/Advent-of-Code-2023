import sys
import operator

def gen_lambda(cmp, component, value):
    return lambda part: cmp(part[component], value)

workflows = {}
parts = []
read_parts = False
for line in sys.stdin.readlines():
    line = line.strip()
    if read_parts:
        part = {}
        desc = line[1:-1].split(',')
        for comp in desc:
            c, val = comp.split('=')
            part[c] = int(val)
        parts.append(part)
    else:
        if not line:
            read_parts = True
            continue
        name, rest = line.split('{', 2)
        assert rest[-1] == '}'
        rules = rest[:-1].split(',')
        funcs = []
        for rule in rules:
            if rule.find(':') != -1:
                cond, dest = rule.split(':')
                assert cond[1] in '<>'
                component = cond[0]
                cmp = operator.lt if cond[1] == '<' else operator.gt
                value = int(cond[2:])
                test = gen_lambda(cmp, component, value)
            else:
                test = lambda part: True
                dest = rule
            funcs.append((test, dest))
        workflows[name] = funcs

tot = 0
for part in parts:
    workflow = 'in'
    while True:
        new_workflow = None
        for fn, dest in workflows[workflow]:
            if fn(part):
                new_workflow = dest
                break
        assert new_workflow is not None
        if new_workflow == 'R':
            break
        if new_workflow == 'A':
            tot += sum(part.values())
            break
        workflow = new_workflow

print(tot)

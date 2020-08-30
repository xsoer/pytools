import json

def tree_data():
    with open('add.json') as f:
        data = json.loads(f.read())
    tree = []
    gen_tree(tree, 0, data)
    
    with open('地址.json', 'w') as f:
        f.write(json.dumps(tree, ensure_ascii=False))


def gen_tree(tree, i, data):
    for d in data:
        if d['pid'] == i:
            child = gen_child(d['id'], data)
            d['child'] = child
            for c in child:
                gen_tree(c['child'], c['id'], data)
            tree.append(d)
            
    
def gen_child(i, data):
    child = []
    for d in data:
        if d['pid'] == i:
            d['child'] = []
            child.append(d)
    return child

tree_data()
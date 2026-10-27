import io, re, json
s = io.open('index.html', encoding='utf-8').read()
# 去掉注释行（粗略：整行 // 或 /* */ 里的中文不算）
lits = set()
for m in re.finditer(r"'([^'\n]*[\u4e00-\u9fa5][^'\n]*)'", s):
    lits.add(m.group(1))
for m in re.finditer(r'"([^"\n]*[\u4e00-\u9fa5][^"\n]*)"', s):
    lits.add(m.group(1))
# HTML 文本节点
for m in re.finditer(r'>([^<>]*[\u4e00-\u9fa5][^<>]*)<', s):
    lits.add(m.group(1).strip())
print('unique:', len(lits))
for x in sorted(lits):
    print(repr(x))

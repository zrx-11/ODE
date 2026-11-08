#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把四批章节内容插入骨架，生成最终单文件 HTML"""
import sys, pathlib

BASE = pathlib.Path(__file__).parent
ROOT = BASE.parent

def load(name):
    # 执行对应模块文件拿到 CH_x 变量
    ns = {}
    code = (BASE / name).read_text(encoding='utf-8')
    exec(compile(code, name, 'exec'), ns)
    for k in ns:
        if k.startswith('CH_'):
            return ns[k]
    raise KeyError(f'no CH_ in {name}')

chapters = ''.join(load(f'chapters_{c}.py') for c in 'abcde')

html_path = ROOT / 'index.html'
html = html_path.read_text(encoding='utf-8')
if '<!-- REST_CHAPTERS -->' not in html:
    # 锚点已被替换（非首次运行）——重新跑骨架脚本恢复锚点
    import subprocess
    subprocess.run([sys.executable, str(BASE / 'build_skeleton.py')], check=True)
    html = html_path.read_text(encoding='utf-8')
assert '<!-- REST_CHAPTERS -->' in html, 'anchor missing'
html = html.replace('<!-- REST_CHAPTERS -->', chapters)

out = ROOT / 'index.html'
out.write_text(html, encoding='utf-8')
print('最终文件大小:', round(len(html)/1024), 'KB')
print('章节数量:', html.count('<section class="chapter"'))

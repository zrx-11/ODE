#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建《常微分方程 · 从零推导》单文件 HTML 骨架"""
import base64, pathlib, re

BASE = pathlib.Path(__file__).parent        # src/
ROOT = BASE.parent                          # 仓库根
VENDOR = ROOT / 'assets' / 'vendor'

# ===== 读取 KaTeX 资源 =====
katex_css = (VENDOR / 'katex.min.css').read_text(encoding='utf-8')
katex_js = (VENDOR / 'katex.min.js').read_text(encoding='utf-8')
auto_render_js = (VENDOR / 'auto-render.min.js').read_text(encoding='utf-8')

# ===== 字体 base64 内联 =====
def inline_fonts(css):
    for m in re.finditer(r'url\((["\' ]*)(fonts/[^)"\']+\.woff2)\1\)', css):
        name = m.group(2)
        font_path = VENDOR / name
        if font_path.exists():
            b64 = base64.b64encode(font_path.read_bytes()).decode('ascii')
            css = css.replace(m.group(0), f'url(data:font/woff2;base64,{b64})')
    return css

katex_css = inline_fonts(katex_css)

# ===== 章节定义 =====
CHAPTERS = [
    ("intro",        "课程概览"),
    ("foundation",   "数学地基：从变化率到微积分"),
    ("ode-basic",    "认识微分方程"),
    ("separable",    "变量分离法"),
    ("linear",       "一阶线性方程与常数变易法"),
    ("exact",        "恰当方程与积分因子"),
    ("implicit",     "一阶隐式方程与参数表示"),
    ("existence",    "存在唯一性定理与逐步逼近"),
    ("extension",    "解的延拓与初值依赖性"),
    ("singular",     "奇解"),
    ("numeric",      "数值解"),
    ("summary",      "知识图谱与自测"),
]

nav_items = "\n".join(
    f'  <a class="nav-item{" active" if i == 0 else ""}" data-target="{cid}">{title}</a>'
    for i, (cid, title) in enumerate(CHAPTERS)
)

chapter_ids = [cid for cid, _ in CHAPTERS]
chapter_order_js = "[" + ", ".join(f"'{c}'" for c in chapter_ids) + "]"
chapter_titles_js = "{" + ", ".join(f"'{cid}': '{title}'" for cid, title in CHAPTERS) + "}"

css = """
:root{--bg:#0f1117;--bg2:#161922;--bg3:#1e2230;--card:#1a1e2a;--text:#e4e6ed;--text2:#9ba1b3;--text3:#6b7185;--border:#2a2f42;--accent:#7c5bff;--accent2:#4e9cff;--green:#3ecf8e;--yellow:#f5c451;--red:#ff6b6b}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:"Noto Sans SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;line-height:1.75;overflow-x:hidden;overflow-wrap:break-word;word-break:break-word}
.layout{display:flex;min-height:100vh}
/* ===== 顶部常驻导航栏（移动端）===== */
.topbar-fixed{display:none}
.topbar-menu{display:flex;align-items:center;gap:6px;background:var(--bg3);border:1px solid var(--border);color:var(--text);padding:7px 12px;border-radius:8px;cursor:pointer;font-size:13px}
.topbar-fixed{display:flex;align-items:center;justify-content:space-between;position:fixed;top:0;left:0;right:0;height:52px;padding:0 12px;background:rgba(22,25,34,.97);border-bottom:1px solid var(--border);z-index:95}
.topbar-chapter{font-size:14px;font-weight:600;color:var(--text);max-width:46%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.topbar-arrows{display:flex;gap:8px}
.topbar-arrow{display:flex;align-items:center;justify-content:center;width:38px;height:38px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;color:var(--text);cursor:pointer;font-size:20px;line-height:1;user-select:none}
.topbar-arrow:hover{border-color:var(--accent);color:var(--accent)}
.topbar-arrow.disabled{opacity:.28;pointer-events:none}
/* ===== 进度条 ===== */
.progress-bar{position:fixed;top:52px;left:0;height:3px;background:var(--accent);z-index:96;width:0;transition:width .1s}
/* ===== 侧边栏 ===== */
.sidebar{width:260px;max-width:82vw;flex-shrink:0;background:var(--bg2);border-right:1px solid var(--border);position:fixed;top:0;left:0;bottom:0;overflow-y:auto;overflow-x:hidden;padding:24px 0;z-index:100;transition:transform .3s}
.sidebar-title{font-size:15px;font-weight:700;padding:0 20px 16px;color:var(--text)}
.nav-item{display:block;padding:9px 20px;font-size:13.5px;color:var(--text2);text-decoration:none;border-left:3px solid transparent}
.nav-item:hover{background:var(--bg3);color:var(--text)}
.nav-item.active{color:var(--accent);border-left-color:var(--accent);background:rgba(124,91,255,.08)}
/* ===== 遮罩 ===== */
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:99;display:none}
.overlay.show{display:block}
/* ===== 主内容 ===== */
.main{flex:1;margin-left:260px;padding:40px 48px 80px;max-width:960px}
.chapter{max-width:100%}
h2{font-size:24px;margin-bottom:8px;color:var(--text)}
h2 .num{display:inline-block;background:var(--accent);color:#fff;border-radius:8px;padding:1px 10px;margin-right:10px;font-size:18px}
.lead{color:var(--text2);font-size:15px;margin-bottom:24px}
h3{font-size:18px;margin:28px 0 10px;color:var(--text);border-left:4px solid var(--accent);padding-left:10px}
h4{font-size:15px;margin:18px 0 8px;color:var(--accent2)}
p{margin:10px 0}
b,strong{color:var(--text)}
/* ===== 提示框 ===== */
.callout{border-radius:10px;padding:14px 16px;margin:14px 0;font-size:14px}
.callout-tip{background:rgba(62,207,142,.08);border:1px solid rgba(62,207,142,.35)}
.callout-key{background:rgba(124,91,255,.08);border:1px solid rgba(124,91,255,.4)}
.callout-warn{background:rgba(245,196,81,.08);border:1px solid rgba(245,196,81,.4)}
.callout-title{font-weight:700;margin-bottom:6px;font-size:14px}
.callout-tip .callout-title{color:var(--green)}
.callout-key .callout-title{color:var(--accent)}
.callout-warn .callout-title{color:var(--yellow)}
/* ===== 推导折叠 ===== */
.derive-steps{margin:14px 0}
.derive-step{border:1px solid var(--border);border-radius:10px;margin-bottom:10px;overflow:hidden}
.derive-step-header{padding:12px 16px;background:var(--bg2);cursor:pointer;display:flex;align-items:center;gap:10px;font-size:14px}
.derive-step-header:hover{background:var(--bg3)}
.derive-step-num{display:inline-flex;align-items:center;justify-content:center;min-width:26px;height:26px;border-radius:6px;background:var(--bg3);color:var(--accent);font-size:12.5px;font-weight:700;padding:0 6px}
.derive-step-title{flex:1}
.derive-step-arrow{color:var(--text3);transition:transform .3s;font-size:12px}
.derive-step.open .derive-step-arrow{transform:rotate(90deg)}
.derive-step-body{padding:0 18px;max-height:0;overflow:hidden;transition:max-height .4s ease,padding .3s}
.derive-step.open .derive-step-body{padding:16px 18px 20px;max-height:8000px}
/* ===== 公式 ===== */
.formula{background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:12px 16px;margin:12px 0;overflow-x:auto;font-size:15px;max-width:100%}
.formula-left{text-align:left}
.katex-display{margin:6px 0;overflow-x:auto;overflow-y:hidden}
/* ===== 表格 ===== */
.table-wrap{overflow-x:auto;max-width:100%;margin:14px 0}
table{width:100%;border-collapse:collapse;font-size:13.5px;min-width:340px}
th{background:var(--bg3);padding:8px 10px;text-align:left;color:var(--text)}
td{padding:8px 10px;border-bottom:1px solid var(--border);color:var(--text2)}
/* ===== 知识树 ===== */
.knowledge-tree{margin:18px 0}
.kt-level{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0;align-items:center}
.kt-label{display:inline-block;background:var(--bg3);border:1px solid var(--border);border-radius:6px;padding:3px 10px;font-size:12.5px;color:var(--text2)}
.kt-label.root{color:var(--green);border-color:rgba(62,207,142,.4)}
.kt-label.base{color:var(--yellow);border-color:rgba(245,196,81,.4)}
.kt-label.tool{color:var(--accent2);border-color:rgba(78,156,255,.4)}
.kt-node{display:inline-block;background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:5px 12px;font-size:13px;cursor:pointer;color:var(--text);text-decoration:none;transition:border-color .2s}
.kt-node:hover{border-color:var(--accent);color:var(--accent)}
.kt-node.main{color:var(--accent);border-color:rgba(124,91,255,.5)}
.kt-node.root{color:var(--green);border-color:rgba(62,207,142,.5)}
.kt-node.base{color:var(--yellow);border-color:rgba(245,196,81,.5)}
.kt-node.tool{color:var(--accent2);border-color:rgba(78,156,255,.5)}
/* ===== 导航 ===== */
.breadcrumb{font-size:13px;color:var(--text3);margin:20px 0 4px}
.breadcrumb a{color:var(--accent);text-decoration:none}
.breadcrumb .sep{margin:0 6px}
.breadcrumb .current{color:var(--text2)}
.chapter-nav{display:flex;justify-content:space-between;gap:12px;margin-top:36px;padding-top:24px;border-top:1px solid var(--border)}
.chapter-nav a{display:flex;flex-direction:column;padding:16px 20px;background:var(--card);border:1px solid var(--accent);border-radius:12px;color:var(--text2);max-width:46%;transition:all .2s;text-decoration:none}
.chapter-nav a:hover{border-color:var(--accent);background:rgba(124,91,255,.10);color:var(--text)}
.chapter-nav .nav-label{font-size:13px;font-weight:700;color:var(--accent);margin-bottom:6px;letter-spacing:.5px}
.chapter-nav .nav-title{font-size:15px;font-weight:600;color:var(--text)}
.chapter-nav .nav-next{text-align:right;margin-left:auto}
/* ===== 顶栏按钮 ===== */
.topbar-actions{margin:16px 0}
.topbar-btn{background:var(--bg3);border:1px solid var(--border);color:var(--text);padding:8px 16px;border-radius:8px;cursor:pointer;font-size:13.5px}
.topbar-btn:hover{border-color:var(--accent)}
/* ===== 返回顶部 ===== */
.back-top{position:fixed;bottom:24px;right:20px;width:44px;height:44px;border-radius:50%;background:var(--bg3);border:1px solid var(--border);color:var(--text);cursor:pointer;display:none;align-items:center;justify-content:center;font-size:18px;z-index:90}
.back-top.show{display:flex}
/* ===== 思考题 ===== */
.qa-item{border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin:12px 0}
.qa-q{font-weight:700;margin-bottom:8px;color:var(--yellow)}
.qa-a{color:var(--text2);font-size:14px}
/* ===== 移动端 ===== */
@media(max-width:768px){
  .sidebar{transform:translateX(-100%);display:none}
  .sidebar.open{transform:translateX(0);display:block}
  .main{margin-left:0;padding:76px 12px 60px;max-width:100%;width:100%}
  .derive-step-header{padding:10px 12px;font-size:13px}
  .derive-step-body{padding:0 12px;max-width:100%}
  .derive-step.open .derive-step-body{padding:10px 12px 14px}
  .chapter-nav a{padding:12px 14px}
  .chapter-nav .nav-title{font-size:13.5px}
  .callout{padding:12px}
  .formula{font-size:13.5px;padding:10px}
}
@media(min-width:769px){
  .topbar-fixed,.progress-bar{display:none}
}
@media print{.topbar-fixed,.progress-bar,.back-top{display:none}}
"""

js = """
// ===== 章节切换 =====
const chapterTitles = """ + chapter_titles_js + """;
const chapterOrder = """ + chapter_order_js + """;
const chapters = document.querySelectorAll('.chapter');
const navItems = document.querySelectorAll('.nav-item');
let currentChapter = chapterOrder[0];

function renderBreadcrumb(id){
  const idx = chapterOrder.indexOf(id);
  const prev = idx > 0 ? chapterOrder[idx-1] : null;
  const next = idx < chapterOrder.length-1 ? chapterOrder[idx+1] : null;
  const chapterEl = document.getElementById(id);
  const bc = chapterEl ? chapterEl.querySelector('.breadcrumb') : null;
  if (bc) bc.innerHTML = '<a href="#" onclick="showChapter(\\'intro\\');return false">首页</a><span class="sep">/</span><span class="current">'+chapterTitles[id]+'</span>';
  const navBox = chapterEl ? chapterEl.querySelector('.chapter-nav') : null;
  if (navBox) navBox.innerHTML =
    (prev ? '<a href="#" onclick="showChapter(\\''+prev+'\\');return false"><span class="nav-label">← 上一章</span><span class="nav-title">'+chapterTitles[prev]+'</span></a>' : '<span></span>') +
    (next ? '<a class="nav-next" href="#" onclick="showChapter(\\''+next+'\\');return false"><span class="nav-label">下一章 →</span><span class="nav-title">'+chapterTitles[next]+'</span></a>' : '');
}

function showChapter(id){
  chapters.forEach(c => c.style.display = c.id === id ? 'block' : 'none');
  navItems.forEach(n => n.classList.toggle('active', n.dataset.target === id));
  currentChapter = id;
  renderBreadcrumb(id);
  updateTopbar(id);
  window.scrollTo({top:0,behavior:'smooth'});
  closeSidebar();
  function renderCurrentChapter(retries){
    if (window.renderMathInElement) {
      try {
        const el = document.getElementById(id);
        if (el) renderMathInElement(el, {
          delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],
          throwOnError:false
        });
      } catch(e){}
    } else if (retries > 0) {
      setTimeout(() => renderCurrentChapter(retries - 1), 200);
    }
  }
  renderCurrentChapter(10);
}

navItems.forEach(n => n.addEventListener('click', e => { e.preventDefault(); showChapter(n.dataset.target); }));
// ===== 知识树节点跳转 =====
document.querySelectorAll('.kt-node[data-goto]').forEach(n => {
  n.addEventListener('click', e => { e.preventDefault(); showChapter(n.dataset.goto); });
});
// ===== 折叠推导 =====
document.addEventListener('click', e => {
  const h = e.target.closest('.derive-step-header');
  if (h) { h.parentElement.classList.toggle('open'); }
});
// ===== 展开全部 =====
function toggleAllDerivations(){
  const steps = document.querySelectorAll('.chapter:not([style*="none"]) .derive-step');
  const allOpen = [...steps].every(s => s.classList.contains('open'));
  steps.forEach(s => s.classList.toggle('open', !allOpen));
}
// ===== 移动端菜单 =====
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');
function openSidebar(){sidebar.classList.add('open');overlay.classList.add('show')}
function closeSidebar(){sidebar.classList.remove('open');overlay.classList.remove('show')}
overlay.addEventListener('click', closeSidebar);
const menuToggle = document.getElementById('menuToggle');
if (menuToggle) menuToggle.addEventListener('click', openSidebar);
// ===== 顶部固定导航栏 =====
function updateTopbar(id){
  const idx = chapterOrder.indexOf(id);
  const t = document.getElementById('topbarChapter');
  if (t) t.textContent = chapterTitles[id];
  const prev = document.getElementById('topbarPrev');
  const next = document.getElementById('topbarNext');
  if (prev) {
    if (idx > 0) { prev.classList.remove('disabled'); prev.onclick = function(){ showChapter(chapterOrder[idx-1]); }; }
    else { prev.classList.add('disabled'); prev.onclick = null; }
  }
  if (next) {
    if (idx >= 0 && idx < chapterOrder.length-1) { next.classList.remove('disabled'); next.onclick = function(){ showChapter(chapterOrder[idx+1]); }; }
    else { next.classList.add('disabled'); next.onclick = null; }
  }
}
// 页面加载即渲染导航
renderBreadcrumb('intro');
updateTopbar('intro');
// ===== 进度条与返回顶部 =====
const progressBar = document.getElementById('progressBar');
const backTop = document.getElementById('backTop');
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const p = h.scrollTop / (h.scrollHeight - h.clientHeight) * 100;
  progressBar.style.width = p + '%';
  backTop.classList.toggle('show', h.scrollTop > 400);
});
backTop.addEventListener('click', () => window.scrollTo({top:0,behavior:'smooth'}));
// ===== KaTeX 全量渲染（含隐藏章节）=====
function tryRenderKatex(retries){
  if (window.renderMathInElement) {
    try {
      document.querySelectorAll('.chapter').forEach(ch => {
        renderMathInElement(ch, {
          delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],
          throwOnError:false
        });
      });
    } catch(e){}
  } else if (retries > 0) {
    setTimeout(() => tryRenderKatex(retries - 1), 200);
  }
}
tryRenderKatex(20);
setTimeout(() => tryRenderKatex(10), 500);
setTimeout(() => tryRenderKatex(5), 1500);
"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%237c5bff'/%3E%3Ctext x='16' y='23' font-size='18' font-family='Georgia,serif' fill='white' text-anchor='middle'%3E%E2%88%AB%3C/text%3E%3C/svg%3E">
<title>常微分方程 · 从零推导交互式学习</title>
<style>{katex_css}
{css}</style>
</head>
<body>
<div class="topbar-fixed" id="topbarFixed">
  <button class="topbar-menu" id="menuToggle">
    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    目录
  </button>
  <span class="topbar-chapter" id="topbarChapter">课程概览</span>
  <div class="topbar-arrows">
    <span class="topbar-arrow" id="topbarPrev" role="button" tabindex="0" title="上一章">‹</span>
    <span class="topbar-arrow" id="topbarNext" role="button" tabindex="0" title="下一章">›</span>
  </div>
</div>
<div class="progress-bar" id="progressBar"></div>
<div class="layout">
<aside class="sidebar" id="sidebar">
  <div class="sidebar-title">常微分方程 · 从零推导</div>
{nav_items}
</aside>
<div class="overlay" id="overlay"></div>
<main class="main" id="mainContent">
<!-- REST_CHAPTERS -->
</main>
</div>
<button class="back-top" id="backTop">↑</button>
<script>{katex_js}</script>
<script>{auto_render_js}</script>
<script>{js}</script>
</body>
</html>
"""

(ROOT / 'index.html').write_text(html, encoding='utf-8')
print('骨架生成:', len(html), 'bytes')

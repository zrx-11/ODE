# 常微分方程 · 从零推导

把杭电《常微分方程》前三章的九个课件重写成一份能直接打开学习的长页面。起点是初中数学，终点是能判断一个一阶方程属于哪一类、能自己推出解法、能说清存在唯一性定理为什么需要那几个条件。

页面是一个单文件 HTML，公式字体、KaTeX 全部内联，没有外部请求。仓库根目录放 `index.html`，打开 GitHub Pages 就能看。

## 页面上有什么

十二个章节，侧边栏常驻目录，手机顶部有常驻导航条（目录、章名、前后箭头），每章结尾有上一章/下一章按钮。

每章固定结构：绿色直觉框（生活类比）、黄色前置知识框、可折叠的推导步骤、编号公式、算例、真/假对照表、三到五道带答案的思考题。

| # | 章节 | 对应课件 |
|---|------|----------|
| 0 | 课程概览 | 1-1 绪论 |
| 1 | 数学地基：从变化率到微积分 | 自补前置 |
| 2 | 认识微分方程 | 1-1 |
| 3 | 变量分离法 | 2-1 |
| 4 | 一阶线性方程与常数变易法 | 2-2 |
| 5 | 恰当方程与积分因子 | 2-3 |
| 6 | 一阶隐式方程与参数表示 | 2-4 |
| 7 | 存在唯一性定理与逐步逼近 | 3-1 |
| 8 | 解的延拓与初值依赖性 | 3-2 |
| 9 | 奇解 | 3-3 |
| 10 | 数值解 | 3-4 |
| 11 | 知识图谱与自测 | 汇总 |

第 1 章是自己加的。课件默认你已经会导数、微分、积分、偏导，真用的时候这些地方一旦有缺口后面每章都会卡住，所以单独铺了一层，共 15 节。

## 目录

```
.
├── index.html              成品，GitHub Pages 入口
├── README.md
├── .nojekyll               关掉 Jekyll 处理，避免文件名和路径被改写
├── .gitignore
├── src/
│   ├── build_skeleton.py   生成骨架（CSS/JS/导航）
│   ├── chapters_a.py       第 0-1 章
│   ├── chapters_b.py       第 2-3 章
│   ├── chapters_c.py       第 4-5 章
│   ├── chapters_d.py       第 6-7 章
│   ├── chapters_e.py       第 8-11 章
│   ├── chapters_e2.py      第 10-11 章旧稿，已合并，不参与构建
│   └── insert_chapters.py  把章节填进骨架，输出 index.html
├── assets/vendor/
│   ├── katex.min.css
│   ├── katex.min.js
│   ├── auto-render.min.js
│   └── fonts/              20 个 woff2，构建时转 base64 写进 HTML
└── sources/                九个课件的 PyMuPDF 提取文本（默认不入库）
```

## 本地看

直接双击 `index.html` 就行，`file://` 下可用。

要看和线上一致的效果，起个本地服务：

```bash
python3 -m http.server 8000
# 打开 http://localhost:8000/
```

## 部署到 GitHub Pages

**整个仓库当站点（推荐）**

```bash
git init
git add .
git commit -m "常微分方程从零推导"
git branch -M main
git remote add origin git@github.com:<你的用户名>/<仓库名>.git
git push -u origin main
```

推完去仓库 Settings → Pages → Build and deployment，Source 选 `Deploy from a branch`，Branch 选 `main`，目录选 `/ (root)`，保存。一两分钟后访问：

```
https://<你的用户名>.github.io/<仓库名>/
```

仓库名如果是 `<用户名>.github.io`，地址就是 `https://<用户名>.github.io/`。

`index.html` 里没有任何绝对路径，页面内部也不请求任何文件，放在子路径下同样能正常显示，不会出现公式变成源码的情况。

**已经有仓库，只想加一个页面**

不需要复制整个仓库，成品就一个文件：

```bash
mkdir -p docs
cp index.html docs/
```

Pages 的目录改选 `/docs`，访问 `https://<用户名>.github.io/<仓库名>/`。源码目录留着不影响，Pages 只发布 `docs/`。

**`.nojekyll` 的作用**

根目录那个空文件用来跳过 Jekyll。没有它，GitHub 会跑一遍 Jekyll 构建，遇到下划线开头的文件或特殊路径可能报错。内容全是静态文件时加上最省事。

**更新内容**

改 `src/chapters_*.py` 里的文字，然后：

```bash
python3 src/insert_chapters.py
```

会重新生成 `index.html`，提交推送即可。脚本发现骨架里没有 `<!-- REST_CHAPTERS -->` 锚点时会自动重跑 `build_skeleton.py` 再合并，所以重复执行是安全的，不会叠加章节。

## 几个实现细节

**KaTeX 全内联。** CSS、JS、auto-render 都写进 HTML。20 个 woff2 转 base64 塞进 `@font-face`，产物因此多 300 多 KB。用 CDN 的话，国内网络或断网时公式会直接显示成 `$y'=f(x,y)$` 这样的源码。

**公式里的 `<` 一律写成 `&lt;`。** `$x_0<x_1$` 这种写法浏览器会把 `<x` 当成标签开头，DOM 被拆坏，KaTeX 匹配不到，页面上只剩半截 `$x_0`。所有含小于号的位置都做了转义。

**章节 id、导航 data-target、章节顺序数组三处对齐。** 渲染面包屑和上下章按钮时用章节内的 `querySelector` 查找 `.breadcrumb` / `.chapter-nav`，不用 `getElementById`，避免多章节撞 id 只命中第一章。

**折叠推导默认收起。** 每步的代数过程折叠起来，点标题展开，嵌套的也能点开。

## 交付前跑过的检查

静态扫描：217 个公式块、140 个折叠步骤，公式里没有裸写的 `<`。

浏览器端（Chromium，390×844，走本地 HTTP 服务模拟 Pages）：

- 十二个章节全部渲染，KaTeX 元素数 8 到 478，与各章公式密度对得上
- 没有残留的裸 `$` 文本节点
- 每章 `scrollWidth == clientWidth`，整页也没有横向溢出
- 每章的 `.breadcrumb` 和 `.chapter-nav` 都有内容
- 没有失败请求，控制台无 error

交互测了四条：点折叠头能展开、手机顶栏目录能打开抽屉、抽屉里点章节能切过去、顶栏 `›` 和章末「下一章」都能切换。

## 已知边界

- **只到课件第三章。** 课件停在 3-4 数值解，第五章线性微分方程组没有展开，只在第 11 章指了下一步要补的前置（线性代数）。
- **习题详解没用上。** 《常微分方程（第四版）习题详解》129 页，OCR 出来的公式符号错位（`y` 被识别成「归」「夕」），照抄会教错。页面里的 37 道思考题是按课件例题自拟的，答案都验算过。
- **`sources/` 里的提取文本有损。** 积分上下限被拆行，`∂M/∂y` 会断成两行，只能用来核对章节结构和定理编号。正文里的公式是按上下文重建的。
- **`sources/` 默认不进仓库。** 课件原文版权归课程组，`.gitignore` 里已经排除。自己本地重建时留着就行，公开仓库建议不要提交。
- **行内 `\dfrac` 会撑高行距。** 少数句子里的行内公式用了 `\dfrac`，窄屏上那一行高度会变大。不影响正确性。
- **字体 fallback 指向不存在的 woff/ttf。** KaTeX 的 `@font-face` 里 woff2 已经内联，后面的 woff/ttf 是原 CSS 留下的备用链，浏览器优先用 woff2，不会去请求它们（验证时无失败请求）。

## 版权

课件内容与例题的版权属于杭州电子科技大学课程组。本仓库的整理、推导补全与页面代码可以自行取用，如果要对外分发，建议补一个 LICENSE 文件说明授权范围。

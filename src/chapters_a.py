#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 0、1 章：课程概览 + 数学地基"""

CH_A = r'''
<!-- ========== 第 0 章：课程概览 ========== -->
<section class="chapter" id="intro">
<div class="breadcrumb"></div>
<h2><span class="num">0</span>课程概览</h2>
<p class="lead">这门课研究一件事：已知一个量"变化得多快"，怎么把它本身求出来。全程从初二数学出发，缺的工具在第 1 章补齐。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：从"速度表"倒推"走到了哪"</div>
你开车时速度表一直在跳。如果只知道每一刻的速度，能不能还原出你走了多远？可以，把每一小段时间的速度乘以时间，累加起来。反过来说，如果题目告诉你"速度等于当前位置的某个函数"，要你求位置随时间的表达式，这就是微分方程。整门课都在干这件事。
</div>

<h3>本课要解决的问题</h3>
<p>现实里的规律通常写成"变化率与当前状态的关系"。人口越多增长越快，写成 $\dfrac{dN}{dt}=rN$；物体越热降温越快，写成 $\dfrac{dT}{dt}=-k(T-T_{\text{环境}})$。这类含导数的关系式叫微分方程。解它，就是找一个函数，使得把这个函数代进去以后等式成立。</p>
<p>课件覆盖三块内容：第一章讲什么叫微分方程；第二章讲一阶方程的五种初等解法（分离变量、线性方程、恰当方程、隐式方程）；第三章讲解到底存不存在、唯不唯一、怎么用数值方法算。</p>

<h3>知识树：这一路要爬的台阶</h3>
<div class="knowledge-tree">
  <div class="kt-level"><span class="kt-label root">根系</span>
    <a class="kt-node root" data-goto="foundation">四则运算</a>
    <a class="kt-node root" data-goto="foundation">大于小于</a>
    <a class="kt-node root" data-goto="foundation">等号</a>
    <a class="kt-node root" data-goto="foundation">绝对值</a>
    <a class="kt-node root" data-goto="foundation">函数</a>
  </div>
  <div class="kt-level"><span class="kt-label base">数学工具</span>
    <a class="kt-node base" data-goto="foundation">导数</a>
    <a class="kt-node base" data-goto="foundation">微分</a>
    <a class="kt-node base" data-goto="foundation">不定积分</a>
    <a class="kt-node base" data-goto="foundation">定积分</a>
    <a class="kt-node base" data-goto="foundation">偏导与全微分</a>
    <a class="kt-node base" data-goto="foundation">不等式</a>
    <a class="kt-node base" data-goto="foundation">数列极限</a>
  </div>
  <div class="kt-level"><span class="kt-label tool">概念层</span>
    <a class="kt-node tool" data-goto="ode-basic">阶·线性·解</a>
    <a class="kt-node tool" data-goto="ode-basic">通解·特解</a>
    <a class="kt-node tool" data-goto="ode-basic">方向场</a>
    <a class="kt-node tool" data-goto="ode-basic">初值问题</a>
  </div>
  <div class="kt-level"><span class="kt-label tool">解法层</span>
    <a class="kt-node tool" data-goto="separable">分离变量</a>
    <a class="kt-node tool" data-goto="linear">常数变易</a>
    <a class="kt-node tool" data-goto="exact">恰当方程·积分因子</a>
    <a class="kt-node tool" data-goto="implicit">参数表示</a>
  </div>
  <div class="kt-level"><span class="kt-label tool">理论层</span>
    <a class="kt-node main" data-goto="existence">Lipschitz·Picard</a>
    <a class="kt-node main" data-goto="extension">延拓·初值依赖</a>
    <a class="kt-node main" data-goto="singular">奇解·包络</a>
  </div>
  <div class="kt-level"><span class="kt-label base">计算层</span>
    <a class="kt-node base" data-goto="numeric">Euler 法</a>
    <a class="kt-node base" data-goto="numeric">误差阶</a>
  </div>
</div>

<h3>学习路径</h3>
<div class="table-wrap">
<table>
<thead><tr><th style="width:12%">章</th><th style="width:42%">内容</th><th>对应课件</th></tr></thead>
<tbody>
<tr><td>1</td><td>数学地基：导数、微分、积分、偏导、不等式、极限</td><td>初中到大学一年级</td></tr>
<tr><td>2</td><td>认识微分方程：阶、线性、解、通解、方向场</td><td>chapter1-1 绪论</td></tr>
<tr><td>3</td><td>变量分离法：分离变量、齐次方程、$ax+by+c$ 型</td><td>chapter2-1</td></tr>
<tr><td>4</td><td>一阶线性方程、常数变易法、伯努利方程</td><td>chapter2-2</td></tr>
<tr><td>5</td><td>恰当方程、积分因子</td><td>chapter2-3</td></tr>
<tr><td>6</td><td>一阶隐式方程、参数表示</td><td>chapter2-4</td></tr>
<tr><td>7</td><td>存在唯一性定理、Picard 逐步逼近</td><td>chapter3-1</td></tr>
<tr><td>8</td><td>解的延拓、解对初值的连续性与可微性</td><td>chapter3-2</td></tr>
<tr><td>9</td><td>奇解、包络、$p$-判别式与 $c$-判别式</td><td>chapter3-3</td></tr>
<tr><td>10</td><td>数值解：Euler、后退 Euler、梯形、改进 Euler</td><td>chapter3-4</td></tr>
<tr><td>11</td><td>知识图谱、解题决策树、自测题</td><td>全部</td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<div class="callout-title">读法建议</div>
第 1 章看起来像"补课"，但它决定后面能不能读懂。如果某一节你已经会，直接跳过；如果第 1 章没看就跳到第 3 章，遇到 $\dfrac{dy}{dx}$ 的除法、$\displaystyle\int$ 的积分、$|y_1-y_2|$ 的绝对值时会断链。第 1 章每一节都标了"后面用在哪"。
</div>

<div class="chapter-nav"></div>
</section>

<!-- ========== 第 1 章：数学地基 ========== -->
<section class="chapter" id="foundation" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">1</span>数学地基：从变化率到微积分</h2>
<p class="lead">这一章把后面要用的工具从初二知识重建一遍：函数、导数、微分、积分、偏导、绝对值、极限。每个工具都给定义、直观、完整推导和一个数字例子。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：整章就三句话</div>
导数回答"现在变化多快"，积分回答"把这些变化累加起来是多少"，微积分基本定理说这两件事互为逆运算。微分方程就是把"变化多快"和"现在是多少"绑在一起写的等式。
</div>

<h3>1.1 函数与二元函数</h3>
<p>函数就是一个对应规则：给一个输入 $x$，按规则算出一个输出 $y$，记作 $y=f(x)$。初二学的正比例 $y=kx$、反比例 $y=\frac{k}{x}$、一次函数 $y=kx+b$、二次函数 $y=ax^2+bx+c$ 都是函数。</p>
<p>本课需要一种更宽的函数：<strong>二元函数</strong> $u=f(x,y)$。输入不是一个数，而是一对有序的数 $(x,y)$，输出一个数。可以想成平面上每个点上都插了一面小旗，旗上写着一个数，$f(x,y)$ 就是这个点的旗上的数。</p>
<div class="formula">$$u=x^2y+3y^2 \quad\Rightarrow\quad u(2,1)=2^2\cdot1+3\cdot1^2=7$$</div>
<p>后面第 5 章会出现 $M(x,y)\,dx+N(x,y)\,dy$，其中 $M,N$ 都是二元函数；第 7 章会出现 $f(x,y)$，右端同时依赖横坐标和纵坐标。</p>
<div class="callout callout-warn"><div class="callout-title">后面用在哪</div>第 5 章恰当方程的 $M,N$；第 7 章存在唯一性定理右端函数 $f(x,y)$。</div>

<h3>1.2 平均速度与瞬时速度：极限的由来</h3>
<p>一辆车 2 小时走了 120 公里，平均速度 $120/2=60$ 公里每小时。但仪表盘显示的是<strong>某一瞬间</strong>的速度，它不等于平均速度。</p>
<p>怎么算瞬时速度？取一个很短的时间段。测 $t$ 到 $t+\Delta t$ 之间走过的距离 $\Delta s$，平均速度是 $\dfrac{\Delta s}{\Delta t}$。时间段越短，这个平均值越接近那一瞬间的真实速度。</p>
<div class="table-wrap">
<table>
<thead><tr><th>时间段长度 $\Delta t$（秒）</th><th>$\Delta s/\Delta t$（米每秒）</th></tr></thead>
<tbody>
<tr><td>1</td><td>2.1</td></tr>
<tr><td>0.1</td><td>2.01</td></tr>
<tr><td>0.01</td><td>2.001</td></tr>
<tr><td>0.001</td><td>2.0001</td></tr>
</tbody>
</table>
</div>
<p>数字越来越靠近 2，但永远不是 2。我们说 $\Delta t\to0$ 时平均速度的<strong>极限</strong>是 2，记作 $\displaystyle\lim_{\Delta t\to0}\frac{\Delta s}{\Delta t}=2$。极限是"无限靠近的那个目标值"，不是"代入 $\Delta t=0$"（代入会得到 0/0，没有意义）。</p>
<div class="callout callout-tip"><div class="callout-title">极限的白话读法</div>$x\to a$ 读作"$x$ 无限靠近 $a$"，$\displaystyle\lim_{x\to a}g(x)=L$ 读作"当 $x$ 无限靠近 $a$ 时，$g(x)$ 无限靠近 $L$"。它描述的是一个<strong>过程的结果</strong>，不是某一步的取值。</div>

<h3>1.3 导数：定义、数值表、几何意义</h3>
<p><strong>定义。</strong>函数 $y=f(x)$ 在 $x$ 处的导数定义为</p>
<div class="formula">$$f'(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$$</div>
<p>分子是"函数值改变了多少"，分母是"自变量改变了多少"，两者相除是"平均变化率"，再取 $\Delta x\to0$ 的极限，得到"瞬时变化率"。记号还有 $\dfrac{dy}{dx}$、$y'$、$\dfrac{df}{dx}$，都指同一个东西。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">用定义求 $f(x)=x^2$ 在 $x=2$ 处的导数</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>第一步，写出差商：</p>
<div class="formula">$$\frac{f(2+\Delta x)-f(2)}{\Delta x}=\frac{(2+\Delta x)^2-4}{\Delta x}$$</div>
<p>第二步，展开分子。$(2+\Delta x)^2=4+4\Delta x+(\Delta x)^2$，所以</p>
<div class="formula">$$\frac{4+4\Delta x+(\Delta x)^2-4}{\Delta x}=\frac{4\Delta x+(\Delta x)^2}{\Delta x}$$</div>
<p>第三步，约掉 $\Delta x$（此时 $\Delta x\ne0$，可以约）：</p>
<div class="formula">$$=4+\Delta x$$</div>
<p>第四步，令 $\Delta x\to0$：</p>
<div class="formula">$$f'(2)=\lim_{\Delta x\to0}(4+\Delta x)=4$$</div>
<p>数字验证：$\Delta x=0.1$ 时差商 $4.1$，$\Delta x=0.01$ 时 $4.01$，$\Delta x=0.001$ 时 $4.001$，确实逼近 4。</p>
</div></div>
</div>

<p><strong>几何意义。</strong>$f'(x)$ 是曲线 $y=f(x)$ 在点 $(x,f(x))$ 处切线的斜率。割线斜率为 $\dfrac{f(x+\Delta x)-f(x)}{\Delta x}$，让 $\Delta x\to0$ 时割线转成切线。这也是后面"方向场"的根据：微分方程 $\dfrac{dy}{dx}=f(x,y)$ 在每一点规定了曲线该往哪个方向走。</p>
<div class="callout callout-warn"><div class="callout-title">后面用在哪</div>第 2 章方向场、第 7 章 Lipschitz 条件（用导数有界）、第 10 章 Taylor 展开估误差，全都以导数为基础。</div>

<h3>1.4 导数的计算规则</h3>
<p>用定义一个个算太慢。下面把常用规则推出来，之后直接查表。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">常数的导数等于 0</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\frac{c-c}{\Delta x}=0 \;\Rightarrow\; (c)'=0$$</div>
<p>常数不变，变化率当然是 0。</p>
</div></div>

<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">$(x^n)'=nx^{n-1}$（以 $n=2,3$ 验证）</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$n=2$ 时已算过：$f'(x)=\displaystyle\lim_{\Delta x\to0}\frac{(x+\Delta x)^2-x^2}{\Delta x}=\lim\frac{2x\Delta x+(\Delta x)^2}{\Delta x}=2x$。</p>
<p>$n=3$ 时用展开 $(x+\Delta x)^3=x^3+3x^2\Delta x+3x(\Delta x)^2+(\Delta x)^3$：</p>
<div class="formula">$$\frac{3x^2\Delta x+3x(\Delta x)^2+(\Delta x)^3}{\Delta x}=3x^2+3x\Delta x+(\Delta x)^2 \;\to\; 3x^2$$</div>
<p>规律是：幂次拿到前面当系数，指数减一。$n$ 可以是负数和分数，规则一样成立。</p>
</div></div>

<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">乘积法则 $(uv)'=u'v+uv'$ 的完整推导</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>要算 $u(x)v(x)$ 的变化率。分子是</p>
<div class="formula">$$u(x+\Delta x)v(x+\Delta x)-u(x)v(x)$$</div>
<p>技巧：在中间加上再减去一项 $u(x+\Delta x)v(x)$，等式不变：</p>
<div class="formula">$$=u(x+\Delta x)v(x+\Delta x)-u(x+\Delta x)v(x)+u(x+\Delta x)v(x)-u(x)v(x)$$</div>
<p>前两项提出 $u(x+\Delta x)$，后两项提出 $v(x)$：</p>
<div class="formula">$$=u(x+\Delta x)\big[v(x+\Delta x)-v(x)\big]+v(x)\big[u(x+\Delta x)-u(x)\big]$$</div>
<p>两边除以 $\Delta x$，再令 $\Delta x\to0$。第一项里 $u(x+\Delta x)\to u(x)$（函数连续），$\dfrac{v(x+\Delta x)-v(x)}{\Delta x}\to v'(x)$；第二项直接得到 $v(x)u'(x)$。所以</p>
<div class="formula">$$(uv)'=uv'+vu'$$</div>
<p>这个"加一项减一项"的技巧很常用，记住它的动机：把"两样东西同时变"拆成"先只让 $v$ 变，再只让 $u$ 变"。</p>
</div></div>

<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">商的法则、常数倍法则、和差法则</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>常数倍：$(cu)'=cu'$，因为常数可以提出极限。</p>
<p>和差：$(u\pm v)'=u'\pm v'$，逐项求导。</p>
<p>商：$\left(\dfrac{u}{v}\right)'=\dfrac{u'v-uv'}{v^2}$，$v\ne0$。由乘积法则作用于 $u=v\cdot\dfrac{u}{v}$ 推出：$u'=v'\dfrac{u}{v}+v\left(\dfrac{u}{v}\right)'$，解出右边的导数即可。</p>
</div></div>

<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">⑤</span><span class="derive-step-title">链式法则 $\dfrac{d}{dx}f(g(x))=f'(g(x))\,g'(x)$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>含义：外层函数变化率乘内层函数变化率。直观像两级传动：齿轮 A 带动 B，B 带动 C，A 转 1 圈 C 转 $2\times3=6$ 圈，是两级倍率相乘。</p>
<p>例：$y=(3x+1)^5$。设 $g=3x+1$，外层 $f(g)=g^5$。$f'(g)=5g^4$，$g'(x)=3$，所以</p>
<div class="formula">$$y'=5(3x+1)^4\cdot3=15(3x+1)^4$$</div>
<p>验证思路：把 $(3x+1)^5$ 展开求导也能得到同样结果，但计算量大得多。</p>
</div></div>
</div>

<h3>1.5 常用导数表</h3>
<div class="table-wrap">
<table>
<thead><tr><th>函数</th><th>导数</th><th>说明</th></tr></thead>
<tbody>
<tr><td>$c$（常数）</td><td>0</td><td>不变</td></tr>
<tr><td>$x^n$</td><td>$nx^{n-1}$</td><td>幂次提前</td></tr>
<tr><td>$e^x$</td><td>$e^x$</td><td>变化率等于自身，这是 $e$ 的定义性质</td></tr>
<tr><td>$\ln x$</td><td>$\dfrac{1}{x}$</td><td>$x>0$</td></tr>
<tr><td>$\sin x$</td><td>$\cos x$</td><td>后面证</td></tr>
<tr><td>$\cos x$</td><td>$-\sin x$</td><td>后面证</td></tr>
<tr><td>$\tan x$</td><td>$\dfrac{1}{\cos^2x}$</td><td>由 $\tan=\frac{\sin}{\cos}$ 用商法则</td></tr>
<tr><td>$\arcsin x$</td><td>$\dfrac{1}{\sqrt{1-x^2}}$</td><td>反函数求导，$|x|&lt;1$</td></tr>
<tr><td>$\arctan x$</td><td>$\dfrac{1}{1+x^2}$</td><td>反函数求导</td></tr>
</tbody>
</table>
</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">补</span><span class="derive-step-title">$\tan x$ 的导数用商法则算一遍</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$(\tan x)'=\left(\frac{\sin x}{\cos x}\right)'=\frac{\cos x\cdot\cos x-\sin x\cdot(-\sin x)}{\cos^2x}=\frac{\cos^2x+\sin^2x}{\cos^2x}=\frac{1}{\cos^2x}$$</div>
<p>最后一步用了 $\sin^2x+\cos^2x=1$（勾股定理在单位圆上的形式）。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">补</span><span class="derive-step-title">$\arctan x$ 的导数怎么来的</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $y=\arctan x$，意思是 $x=\tan y$，且 $y$ 在 $\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$ 内。两边对 $x$ 求导（右边用链式法则，$y$ 是 $x$ 的函数）：</p>
<div class="formula">$$1=\frac{1}{\cos^2y}\cdot\frac{dy}{dx} \;\Rightarrow\; \frac{dy}{dx}=\cos^2y$$</div>
<p>再用 $\cos^2y=\dfrac{1}{1+\tan^2y}=\dfrac{1}{1+x^2}$，得 $\dfrac{dy}{dx}=\dfrac{1}{1+x^2}$。</p>
</div></div>
</div>
<div class="callout callout-warn"><div class="callout-title">后面用在哪</div>第 3 章分离变量要积分 $\frac{1}{y}$ 和 $\frac{1}{1+y^2}$；第 4 章要积分 $\frac{1}{x+1}$；第 5 章积分因子要算 $e^{\int P}$；第 10 章误差估计要 $y''$。</div>

<h3>1.6 微分：把"变化多快"翻译成"变化多少"</h3>
<p>导数给的是变化率。如果自变量改变一点点 $dx$，函数值大约改变多少？答案是</p>
<div class="formula">$$dy=f'(x)\,dx$$</div>
<p>这叫<strong>微分</strong>。$dx$ 是自变量的微小改变，$dy$ 是对应的函数值改变的<strong>线性近似</strong>。严格地说 $dy$ 和真实改变量 $f(x+dx)-f(x)$ 差一个比 $dx$ 更高阶的小量，但当 $dx$ 很小时这个差可以忽略。</p>
<div class="formula">$$f(x+dx)\approx f(x)+f'(x)\,dx$$</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">用微分估算 $\sqrt{4.01}$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>取 $f(x)=\sqrt{x}$，$x=4$，$dx=0.01$。$f'(x)=\dfrac{1}{2\sqrt x}$，$f'(4)=\dfrac{1}{4}$。</p>
<div class="formula">$$\sqrt{4.01}\approx\sqrt4+\frac14\cdot0.01=2+0.0025=2.0025$$</div>
<p>真实值约 $2.002498$，误差在 $10^{-6}$ 量级。</p>
</div></div>
</div>
<div class="callout callout-key"><div class="callout-title">关键：为什么 $\dfrac{dy}{dx}$ 可以当分数用</div>在第 3 章会把 $\dfrac{dy}{dx}=f(x)\varphi(y)$ 改写成 $\dfrac{dy}{\varphi(y)}=f(x)\,dx$，看起来像"把 $dx$ 乘过去"。合法的原因是：两边都是微分。原式乘以 $dx$ 得 $dy=f(x)\varphi(y)\,dx$，再除以 $\varphi(y)$ 得 $\dfrac{dy}{\varphi(y)}=f(x)\,dx$。这正是两个微分相等，而不是"导数这个整体可以拆"。理解这一点，后面所有"分离变量"的合法性都清楚了。
</div>

<h3>1.7 不定积分：导数的逆运算</h3>
<p>已知一个函数的导数，反推它本身，叫<strong>求不定积分</strong>，记作 $\displaystyle\int f(x)\,dx=F(x)+C$，其中 $F'(x)=f(x)$，$C$ 是任意常数。</p>
<p>为什么必须带 $C$？因为常数求导是 0。$x^2$、$x^2+1$、$x^2-5$ 的导数都是 $2x$，所以只凭导数无法区分它们，只能写成"$x^2$ 加上某个常数"。</p>
<div class="callout callout-tip"><div class="callout-title">生活直觉</div>导数像速度表，原函数像里程表。同一段路程，里程表可以任意设定零点，所以还原出来的"里程"永远差一个常数。这个常数后面由初值条件定出来。</div>
<div class="table-wrap">
<table>
<thead><tr><th>$\displaystyle\int f(x)dx$</th><th>结果</th><th>验证（对结果求导）</th></tr></thead>
<tbody>
<tr><td>$\displaystyle\int x^n dx$</td><td>$\dfrac{x^{n+1}}{n+1}+C$（$n\ne-1$）</td><td>$\dfrac{(n+1)x^n}{n+1}=x^n$</td></tr>
<tr><td>$\displaystyle\int \frac{1}{x}dx$</td><td>$\ln|x|+C$</td><td>$x>0$ 时为 $\frac1x$；$x&lt;0$ 时 $(\ln(-x))'=\frac{1}{-x}\cdot(-1)=\frac1x$</td></tr>
<tr><td>$\displaystyle\int e^x dx$</td><td>$e^x+C$</td><td>$(e^x)'=e^x$</td></tr>
<tr><td>$\displaystyle\int \cos x\,dx$</td><td>$\sin x+C$</td><td>$(\sin x)'=\cos x$</td></tr>
<tr><td>$\displaystyle\int \sin x\,dx$</td><td>$-\cos x+C$</td><td>$(-\cos x)'=\sin x$</td></tr>
<tr><td>$\displaystyle\int \frac{1}{1+x^2}dx$</td><td>$\arctan x+C$</td><td>$(\arctan x)'=\frac{1}{1+x^2}$</td></tr>
<tr><td>$\displaystyle\int \frac{1}{\sqrt{1-x^2}}dx$</td><td>$\arcsin x+C$</td><td>$(\arcsin x)'=\frac{1}{\sqrt{1-x^2}}$</td></tr>
</tbody>
</table>
</div>
<p>注意 $\ln|x|$ 的绝对值：$x&lt;0$ 时 $\frac1x$ 也有原函数，绝对值保证两种情况都覆盖。这个细节在第 3、4 章解方程时会决定答案里有没有绝对值。</p>

<h3>1.8 换元积分与分部积分</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">换元法：$\displaystyle\int 2x\cos(x^2)dx$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>观察：$2x$ 正好是 $x^2$ 的导数。设 $u=x^2$，则 $du=2x\,dx$，原式变成</p>
<div class="formula">$$\int \cos u\,du=\sin u+C=\sin(x^2)+C$$</div>
<p>反向验证：$(\sin(x^2))'=\cos(x^2)\cdot2x$，对上了。换元法的本质是把链式法则反过来用。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">分部积分：$\displaystyle\int x e^x dx$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>从乘积求导公式出发：$(uv)'=u'v+uv'$。两边积分：</p>
<div class="formula">$$uv=\int u'v\,dx+\int uv'\,dx \;\Rightarrow\; \int uv'\,dx=uv-\int u'v\,dx$$</div>
<p>写成更常用的形式 $\displaystyle\int u\,dv=uv-\int v\,du$。</p>
<p>用这个算：取 $u=x$，$dv=e^x dx$，则 $du=dx$，$v=e^x$。</p>
<div class="formula">$$\int xe^x dx=xe^x-\int e^x dx=xe^x-e^x+C$$</div>
<p>验证：$(xe^x-e^x)'=e^x+xe^x-e^x=xe^x$。</p>
<p>选 $u$ 的经验：选"求导会变简单"的那部分。$x$ 求导变 1，$e^x$ 积分不变，所以让 $x$ 当 $u$。</p>
</div></div>
</div>
<div class="callout callout-warn"><div class="callout-title">后面用在哪</div>第 4 章解 $\int Q(x)e^{-\int P}dx$；第 5 章 $\int P(x)dx$；第 10 章 Taylor 展开。</div>

<h3>1.9 定积分与牛顿-莱布尼茨公式</h3>
<p><strong>定积分</strong> $\displaystyle\int_a^b f(x)\,dx$ 表示曲线 $y=f(x)$ 与 $x$ 轴之间、从 $a$ 到 $b$ 的面积（$x$ 轴上方算正，下方算负）。</p>
<p>严格做法：把 $[a,b]$ 平均切成 $n$ 份，每份宽 $\Delta x=\dfrac{b-a}{n}$，第 $i$ 份上用某个点的函数值当高，得到矩形面积之和（黎曼和）</p>
<div class="formula">$$S_n=\sum_{i=1}^n f(\xi_i)\Delta x$$</div>
<p>当 $n\to\infty$（也就是 $\Delta x\to0$）时，这个和的极限就是定积分。$\Sigma$（西格玛）是求和记号，$\displaystyle\sum_{i=1}^n$ 表示"把 $i$ 从 1 到 $n$ 挨个代进去再加起来"。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">用矩形和算 $\displaystyle\int_0^1 x^2 dx$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把 $[0,1]$ 均分 $n$ 份，取右端点，$\Delta x=\frac1n$，$\xi_i=\frac in$：</p>
<div class="formula">$$S_n=\sum_{i=1}^n\left(\frac in\right)^2\frac1n=\frac{1}{n^3}\sum_{i=1}^n i^2=\frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}$$</div>
<p>（最后用了平方和公式。）化简：</p>
<div class="formula">$$S_n=\frac{(n+1)(2n+1)}{6n^2}=\frac{2n^2+3n+1}{6n^2}\;\to\;\frac{2}{6}=\frac13$$</div>
<p>所以 $\displaystyle\int_0^1x^2dx=\frac13$。用公式验证：$\left[\frac{x^3}{3}\right]_0^1=\frac13$，一致。</p>
<p>注意 $n=10$ 时 $S_{10}=\frac{2\cdot100+30+1}{600}=\frac{231}{600}=0.385$，已经很接近 $0.333$，但还差一点。极限是"越来越近的目标"，不是某个有限 $n$ 的值。</p>
</div></div>
</div>
<p><strong>牛顿-莱布尼茨公式</strong>（微积分基本定理）：如果 $F'(x)=f(x)$，则</p>
<div class="formula">$$\int_a^b f(x)\,dx=F(b)-F(a)$$</div>
<p>它把"算面积"这件慢事变成了"找原函数再代端点"这件快事。这也是"积分和求导互逆"的确切含义。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">为什么面积函数求导等于被积函数</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $S(x)=\displaystyle\int_a^x f(t)dt$ 是从 $a$ 到 $x$ 的面积。让 $x$ 增加一点点 $\Delta x$，面积增加的是窄条，宽 $\Delta x$，高约为 $f(x)$：</p>
<div class="formula">$$S(x+\Delta x)-S(x)\approx f(x)\Delta x \;\Rightarrow\; \frac{S(x+\Delta x)-S(x)}{\Delta x}\approx f(x)$$</div>
<p>令 $\Delta x\to0$，得 $S'(x)=f(x)$。所以 $S$ 就是 $f$ 的一个原函数，$S(b)-S(a)$ 就是从 $a$ 到 $b$ 的总面积，等于 $F(b)-F(a)$。</p>
<p>这个结论在第 7 章的命题 1（微分方程等价于积分方程）里是核心工具。</p>
</div></div>
</div>

<h3>1.10 变上限积分：积分里带未知函数</h3>
<p>第 7 章会出现 $\displaystyle\varphi(x)=y_0+\int_{x_0}^x f(\xi,\varphi(\xi))\,d\xi$。这里积分号里面含有未知函数 $\varphi$，积分上限是变量 $x$。对它求导，有</p>
<div class="formula">$$\frac{d}{dx}\int_{x_0}^x g(\xi)\,d\xi=g(x)$$</div>
<p>把 $g$ 换成 $g(\xi)=f(\xi,\varphi(\xi))$，求导得 $f(x,\varphi(x))$。这条性质让"积分方程的解"自动满足微分方程，是命题 1 的另一半。</p>
<div class="callout callout-warn"><div class="callout-title">后面用在哪</div>第 7 章命题 1、命题 4；第 8 章解的可微性。</div>

<h3>1.11 偏导数：只让一个变量动</h3>
<p>二元函数 $u=f(x,y)$ 有两个输入。想知道"只改 $x$、$y$ 不动"时 $u$ 的变化率，叫对 $x$ 的<strong>偏导数</strong>，记作 $\dfrac{\partial u}{\partial x}$ 或 $f_x$。算的时候把 $y$ 当常数，按一元函数求导。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$u=x^2y+3y^2$ 的两个偏导</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>对 $x$ 求偏导：$3y^2$ 里没有 $x$，当常数，导数为 0；$x^2y$ 里 $y$ 当常数，导数为 $2xy$。</p>
<div class="formula">$$\frac{\partial u}{\partial x}=2xy$$</div>
<p>对 $y$ 求偏导：$x^2y$ 对 $y$ 导数是 $x^2$；$3y^2$ 对 $y$ 导数是 $6y$。</p>
<div class="formula">$$f_y=x^2+6y$$</div>
<p>数字验证：在 $(2,1)$ 处 $f_x=4$，$f_y=4+6=10$。让 $x$ 从 2 变到 2.01（$dx=0.01$），$u$ 约增加 $4\cdot0.01=0.04$；让 $y$ 从 1 变到 1.01，$u$ 约增加 $10\cdot0.01=0.1$。</p>
</div></div>
</div>
<div class="callout callout-tip"><div class="callout-title">符号怎么读</div>$\partial$ 读作"偏"（round d）。它和 $d$ 的区别是：$d$ 表示所有变量都在动（全微分），$\partial$ 表示只有一个变量在动。</div>

<h3>1.12 全微分：两个方向的变化加起来</h3>
<p>如果 $x$ 和 $y$ 同时改变 $dx$、$dy$，函数 $u$ 大约改变</p>
<div class="formula">$$du=\frac{\partial u}{\partial x}dx+\frac{\partial u}{\partial y}dy$$</div>
<p>这叫<strong>全微分</strong>。直观：在平面上走一小步（横向 $dx$，纵向 $dy$），高度的变化等于"横向坡度×横向距离"加上"纵向坡度×纵向距离"。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$u=x^2y$ 的全微分</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$du=2xy\,dx+x^2\,dy$$</div>
<p>数字验证：在 $(2,1)$ 处，取 $dx=0.01,dy=0.01$，则 $du\approx 2\cdot2\cdot1\cdot0.01+4\cdot0.01=0.04+0.04=0.08$。真实改变：$u(2.01,1.01)-u(2,1)=4.0401\cdot1.01-4=4.080501-4=0.080501$，与 0.08 相差 0.0005，是高阶小量。</p>
</div></div>
</div>
<div class="callout callout-key"><div class="callout-title">这是第 5 章的钥匙</div>第 5 章恰当方程要求 $M(x,y)dx+N(x,y)dy$ 恰好等于某个 $u$ 的全微分，也就是要找出 $u$ 使 $u_x=M$、$u_y=N$。判定条件 $\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial x}$ 来自"混合偏导相等"（$u_{xy}=u_{yx}$）。</div>

<h3>1.13 绝对值与不等式：第 7 章的语言</h3>
<p>$|a|$ 是 $a$ 到 0 的距离，$|a|=\begin{cases}a,&a\ge0\\-a,&a&lt;0\end{cases}$。$|a-b|$ 是数轴上 $a$ 与 $b$ 的距离。</p>
<p>三条要用的性质：</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">三角不等式 $|a+b|\le|a|+|b|$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>分情况验证。$a,b$ 同号时 $|a+b|=|a|+|b|$，取等。$a,b$ 异号时，比如 $a=3,b=-5$：$|a+b|=|-2|=2$，$|a|+|b|=8$，左边小。一般情形下"和的绝对值不超过绝对值的和"，直观上：两个人往不同方向走，合起来的位移不会超过各自路程之和。</p>
<p>推论：$|a-b|\le|a-c|+|c-b|$（把 $a-b$ 写成 $(a-c)+(c-b)$）。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">$|ab|=|a||b|$ 与 $\left|\dfrac{a}{b}\right|=\dfrac{|a|}{|b|}$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>符号只管"正负"，不管"大小"。相乘时符号相乘，大小相乘，绝对值就是大小相乘。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">$|a|\le L$ 等价于 $-L\le a\le L$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>离 0 不超过 $L$，就是落在 $-L$ 到 $L$ 之间。这个等价关系在第 7 章的每一次误差估计里都会用到：要证 $|X|\le b$，就去证 $-b\le X\le b$。</p>
</div></div>
</div>
<div class="callout callout-warn"><div class="callout-title">后面用在哪</div>第 7 章 Lipschitz 条件 $|f(x,y_1)-f(x,y_2)|\le L|y_1-y_2|$；命题 2、3、5 的每一步误差估计；第 10 章截断误差递推。</div>

<h3>1.14 数列极限、一致收敛、阶乘与 $e$</h3>
<p>第 7 章的证明靠一个函数序列 $\varphi_0,\varphi_1,\varphi_2,\dots$ 不断逼近真正的解。这里先把"序列收敛"讲清楚。</p>
<p><strong>数列</strong>是一串数 $a_1,a_2,a_3,\dots$。<strong>收敛到 $A$</strong> 的意思是：只要要求"离 $A$ 有多近"，总能找到一个下标 $N$，之后所有的 $a_n$ 都离 $A$ 不超过这个距离。写作 $\displaystyle\lim_{n\to\infty}a_n=A$。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$a_n=\dfrac{1}{n}$ 收敛到 0</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>要求 $|a_n-0|\le0.01$，解 $\frac1n\le0.01$ 得 $n\ge100$。所以从第 100 项起，全部落在 $0.01$ 以内。要求更近就取更大的 $N$。这就是"无限靠近"的确切意思。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">概念</span><span class="derive-step-title">一致收敛：所有点同时靠近</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>如果函数序列 $\varphi_n(x)$ 在区间 $I$ 上每一点都收敛到一个值 $\varphi(x)$，而且"对每个点要求的 $N$ 可以统一选择一个"，就叫<strong>一致收敛</strong>。</p>
<p>直观区别：逐点收敛是"每一处都会到，但不同地方快慢不一样"；一致收敛是"整段一起到，最快的点和最慢的点同时进入误差范围"。</p>
<p>为什么要一致收敛？因为只有一致收敛，才能把极限搬到积分号里面：$\displaystyle\lim_{n\to\infty}\int f(\xi,\varphi_n(\xi))d\xi=\int \lim_{n\to\infty}f(\xi,\varphi_n(\xi))d\xi$。第 7 章命题 4 靠这个。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">工具</span><span class="derive-step-title">阶乘与 $e^x$ 的级数：用来证明序列收敛</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>阶乘 $n!=1\cdot2\cdot3\cdots n$。从 $n+1$ 到 $2n$ 一共 $n$ 个数，每个都小于 $2n$，大于 1，于是</p>
<div class="formula">$$n!\;\le\;(2n)^n$$</div>
<p>指数函数有级数展开</p>
<div class="formula">$$e^{x}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots=\sum_{n=0}^\infty\frac{x^n}{n!}$$</div>
<p>级数就是"无穷多项相加"。这个级数在任意 $x$ 处都收敛，因为 $n!$ 增长得比 $x^n$ 快得多。第 7 章命题 3 用这个级数当"比较标准"，证明 $\sum \frac{(L|x-x_0|)^n}{n!}$ 收敛，从而 $\varphi_n$ 一致收敛。</p>
</div></div>
</div>

<h3>1.15 指数与对数</h3>
<p>$e$ 是一个常数，约等于 $2.71828$。它的来源：连续复利。年利率 100%，一年结算 2 次得 $(1+\frac12)^2=2.25$；结算 12 次得 $(1+\frac1{12})^{12}\approx2.613$；结算 $n$ 次得 $(1+\frac1n)^n$；$n\to\infty$ 时极限就是 $e$。含义是"利息不停地生利息"，增长倍数的上界是 $e$。</p>
<p>$\ln x$ 是 $e^x$ 的反函数：$e^{\ln x}=x$，$\ln e^x=x$。它满足三条运算律：</p>
<div class="formula">$$\ln(ab)=\ln a+\ln b,\quad \ln\frac ab=\ln a-\ln b,\quad \ln(a^k)=k\ln a$$</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">$\ln(ab)=\ln a+\ln b$ 怎么来的</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $A=\ln a$，$B=\ln b$，则 $a=e^A$，$b=e^B$。相乘：$ab=e^Ae^B=e^{A+B}$（指数相加，因为 $e^{A+B}=e^Ae^B$）。两边取 $\ln$：$\ln(ab)=A+B=\ln a+\ln b$。</p>
<p>第 3 章解 $\dfrac{dy}{dx}=P(x)y$ 时得到 $\ln|y|=\int P(x)dx+C$，再取指数得 $|y|=e^{\int P+C}=e^C e^{\int P}$，这里就用了"对数把乘积变加法"的性质。</p>
</div></div>
</div>
<div class="callout callout-warn"><div class="callout-title">后面用在哪</div>第 3 章分离变量后取指数；第 4 章常数变易的指数形式 $\mu=e^{\int P}$；第 5 章积分因子 $e^{\int\psi(x)dx}$。</div>

<h3>1.16 三角函数与反三角函数</h3>
<p>直角三角形里，$\sin\theta=\dfrac{\text{对边}}{\text{斜边}}$，$\cos\theta=\dfrac{\text{邻边}}{\text{斜边}}$，$\tan\theta=\dfrac{\text{对边}}{\text{邻边}}=\dfrac{\sin\theta}{\cos\theta}$。</p>
<p>弧度制：把"长度等于半径的弧"所对的圆心角叫 1 弧度。$180^\circ=\pi$ 弧度，所以 $30^\circ=\frac\pi6$，$45^\circ=\frac\pi4$，$90^\circ=\frac\pi2$。微积分里所有三角公式默认弧度制，否则 $(\sin x)'=\cos x$ 不成立。</p>
<p>反函数：$\arcsin x$ 表示"正弦值等于 $x$ 的那个角"，值域 $\left[-\frac\pi2,\frac\pi2\right]$；$\arctan x$ 表示"正切值等于 $x$ 的那个角"，值域 $\left(-\frac\pi2,\frac\pi2\right)$。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">第 3 章要用：$\tan u=0$ 时 $u$ 是多少</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$\tan u=\dfrac{\sin u}{\cos u}$。分数为 0 当且仅当分子为 0 且分母不为 0，所以 $\sin u=0$，即 $u=k\pi$（$k$ 为整数）。这一点在 chapter2-1 的例子里用来判断"$\tan u=0$ 也是解"，从而在通解中允许 $c=0$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\arcsin\frac12=\frac\pi6$，$\arctan1=\frac\pi4$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$\sin\frac\pi6=\frac12$，且 $\frac\pi6$ 在 $\arcsin$ 的值域内，所以 $\arcsin\frac12=\frac\pi6$。$\tan\frac\pi4=1$，所以 $\arctan1=\frac\pi4$。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">地基小结：一张对照表</div>
工具 → 一句话 → 用在哪：导数（瞬时变化率）→ 方向场与 Lipschitz；微分（变化量≈斜率×步长）→ 分离变量的合法性；不定积分（求导的逆运算）→ 所有解方程步骤；定积分与变上限积分（累加、对上限求导）→ 积分方程与误差估计；偏导与全微分（单个方向变化、各方向相加）→ 恰当方程判定与隐式方程参数化；绝对值不等式（距离的上界）→ 唯一性证明；数列极限与一致收敛（序列整体靠近目标）→ Picard 逼近。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">用定义求 $f(x)=x^3$ 在 $x=1$ 处的导数。<br>答：$\frac{(1+\Delta x)^3-1}{\Delta x}=\frac{3\Delta x+3(\Delta x)^2+(\Delta x)^3}{\Delta x}=3+3\Delta x+(\Delta x)^2\to3$。所以 $f'(1)=3$，与公式 $3x^2|_{x=1}=3$ 一致。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">为什么 $\displaystyle\int\frac{1}{x}dx=\ln|x|+C$ 而不是 $\ln x+C$？<br>答：$x&lt;0$ 时 $\ln x$ 没有定义，但 $\frac1x$ 有原函数。$(\ln|x|)'=\frac1x$ 对 $x\ne0$ 都成立，绝对值把两种情况都覆盖了。</div></div>
<div class="qa-item"><div class="qa-q">思考题 3</div><div class="qa-a">$|a+b|\le|a|+|b|$ 什么时候取等号？<br>答：$a,b$ 同号（或有一个为 0）时取等。例如 $a=2,b=3$：$|5|=5=|2|+|3|$。</div></div>

<div class="chapter-nav"></div>
</section>
'''

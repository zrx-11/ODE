#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 4、5 章：一阶线性方程 + 恰当方程与积分因子"""

CH_C = r'''
<!-- ========== 第 4 章：一阶线性方程与常数变易法 ========== -->
<section class="chapter" id="linear" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">4</span>一阶线性方程与常数变易法</h2>
<p class="lead">形如 $y'=P(x)y+Q(x)$ 的方程。齐次时能分离变量；非齐次时用一个巧妙的"常数变易"把已知的齐次解改造成非齐次解。对应课件 chapter2-2。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：本来定的工资标准，临时改成随时间变</div>齐次方程 $y'=P(x)y$ 的解是 $y=Ce^{\int P}$，其中 $C$ 是"定死的常数"。非齐次方程多了一个 $Q(x)$ 项，相当于不断有外来收入。常数变易法的想法：既然外来收入会改变总量，那就让"定死的常数"变成一个随时间变化的函数 $C(x)$，其他形式照抄。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 3 章的可分离变量解法（齐次解 $y=Ce^{\int P}$）、第 1 章的换元积分与 $\ln$。</div>

<h3>4.1 标准形式与两个名字</h3>
<div class="formula">$$\frac{dy}{dx}=P(x)y+Q(x) \tag{2.23}$$</div>
<p>$P,Q$ 连续。$Q(x)\equiv0$ 时叫<strong>一阶齐次线性方程</strong>：</p>
<div class="formula">$$\frac{dy}{dx}=P(x)y \tag{2.24}$$</div>
<p>$Q(x)\ne0$ 时叫<strong>非齐次</strong>。注意"齐次"这个词在两个地方出现：第 3 章的"齐次方程"指 $y'=g(y/x)$，这里的"齐次线性"指 $Q=0$。两者不是一回事，看上下文区分。</p>

<h3>4.2 齐次解</h3>
<p>(2.24) 是变量分离型，第 3 章 3.3 节已经解过：</p>
<div class="formula">$$y=Ce^{\int P(x)dx} \tag{2.25}$$</div>
<p>含义：指数上的 $\displaystyle\int P(x)dx$ 是 $P$ 的任意一个原函数。取哪一个都行，差出来的常数被 $C$ 吸收。</p>

<h3>4.3 常数变易法：完整推导</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">为什么敢"猜"这个形式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>齐次解已经满足了方程左边，只是右边多出 $Q(x)$。如果直接把 $C$ 换成 $C(x)$，形式上是</p>
<div class="formula">$$y=C(x)e^{\int P(x)dx} \tag{2.26}$$</div>
<p>这个"猜"不是乱猜：它保留了齐次解的骨架，只把唯一能吸收外来影响的地方（常数）放开。这叫"待定函数法"的思路：把已知解里的常数变成函数，代入原方程定出这个函数。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">对 (2.26) 求导，用乘积法则</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>注意 $e^{\int P dx}$ 对 $x$ 求导时，指数求导得 $P(x)$（因为 $\int P$ 的导数就是 $P$），再乘链式：$\left(e^{\int P}\right)'=P(x)e^{\int P}$。所以</p>
<div class="formula">$$\frac{dy}{dx}=C'(x)e^{\int P}+C(x)P(x)e^{\int P}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">代进 (2.23)，消项</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把求导结果和 $y=C(x)e^{\int P}$ 代进 $y'=P(x)y+Q(x)$：</p>
<div class="formula">$$C'e^{\int P}+CPe^{\int P}=P\cdot Ce^{\int P}+Q$$</div>
<p>左右两边 $CPe^{\int P}$ 完全相同，直接消掉，剩下</p>
<div class="formula">$$C'(x)e^{\int P}=Q(x)$$</div>
<p>这一步是整个方法的核心：$P$ 项自动抵消，说明形式选对了。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">解出 $C(x)$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>两边除以 $e^{\int P}$（即乘以 $e^{-\int P}$）：</p>
<div class="formula">$$\frac{dc(x)}{dx}=Q(x)e^{-\int P(x)dx}$$</div>
<p>积分：</p>
<div class="formula">$$C(x)=\int Q(x)e^{-\int P(x)dx}dx+\bar C$$</div>
<p>其中 $\bar C$ 是任意常数。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">⑤</span><span class="derive-step-title">代回 (2.26)，得到通解公式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$y=e^{\int P(x)dx}\left(\int Q(x)e^{-\int P(x)dx}dx+\bar C\right) \tag{2.28}$$</div>
<p>记成 $y=e^{\int P}\left(\int Qe^{-\int P}dx+C\right)$。这个公式是整章最重要的东西，它就是"一阶线性方程求根公式"，和第 5 章积分因子法给出的是同一个结果。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">用法：三步</div>① 把方程整理成 $y'=P(x)y+Q(x)$，读出 $P$、$Q$；② 算 $\displaystyle\int Pdx$；③ 套公式。如果题目给初值，再代入定 $C$。
</div>

<h3>4.4 例 1：$(x+1)\dfrac{dy}{dx}-ny=e^x(x+1)^{n+1}$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">化成标准形式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>两边除以 $(x+1)$：</p>
<div class="formula">$$\frac{dy}{dx}=\frac{n}{x+1}y+e^x(x+1)^n \tag{2.29}$$</div>
<p>读出 $P=\dfrac{n}{x+1}$，$Q=e^x(x+1)^n$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">先解齐次</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\int Pdx=\int\frac{n}{x+1}dx=n\ln|x+1|=\ln|x+1|^n$$</div>
<p>所以齐次通解 $y=Ce^{\ln|x+1|^n}=C(x+1)^n$（$x&gt;-1$ 时去掉绝对值）。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">常数变易：设 $y=c(x)(x+1)^n$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>求导：</p>
<div class="formula">$$\frac{dy}{dx}=c'(x)(x+1)^n+n(x+1)^{n-1}c(x) \tag{2.31}$$</div>
<p>代入 (2.29)，右边第一项 $\dfrac{n}{x+1}y=\dfrac{n}{x+1}c(x)(x+1)^n=n(x+1)^{n-1}c(x)$，恰好和 (2.31) 的第二项抵消。剩下</p>
<div class="formula">$$c'(x)(x+1)^n=e^x(x+1)^n \;\Rightarrow\; c'(x)=e^x$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">积分得 $c(x)=e^x+\bar C$，代回</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$y=(e^x+\bar C)(x+1)^n$$</div>
<p>验证：$y'=e^x(x+1)^n+n(x+1)^{n-1}(e^x+\bar C)$。右边 $\dfrac{n}{x+1}y+e^x(x+1)^n=n(x+1)^{n-1}(e^x+\bar C)+e^x(x+1)^n$，相等 ✓。</p>
</div></div>
</div>

<h3>4.5 伯努利方程</h3>
<p>形如</p>
<div class="formula">$$\frac{dy}{dx}=P(x)y+Q(x)y^n,\quad n\ne0,1 \tag{2.35}$$</div>
<p>的方程叫<strong>伯努利方程</strong>。未知函数被 $n$ 次方，属于非线性，但可以通过换元化成线性。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">先分离出 $y=0$ 这个解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$y\equiv0$：左边 0，右边 $P\cdot0+Q\cdot0^n=0$（$n&gt;0$ 时），是解。以下设 $y\ne0$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">两边乘 $y^{-n}$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$y^{-n}\frac{dy}{dx}=P(x)y^{1-n}+Q(x) \tag{2.36}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">观察左边是 $y^{1-n}$ 的导数的一部分</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $z=y^{1-n}$，用链式法则：</p>
<div class="formula">$$\frac{dz}{dx}=(1-n)y^{-n}\frac{dy}{dx}$$</div>
<p>所以 $y^{-n}\dfrac{dy}{dx}=\dfrac{1}{1-n}\dfrac{dz}{dx}$。代进 (2.36)：</p>
<div class="formula">$$\frac{1}{1-n}\frac{dz}{dx}=P z+Q \;\Rightarrow\; \frac{dz}{dx}=(1-n)P(x)z+(1-n)Q(x)$$</div>
<p>这就是标准的一阶线性方程（把 $(1-n)P$ 当新的 $P$，$(1-n)Q$ 当新的 $Q$），套 4.1 的公式即可。</p>
</div></div>
</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例3</span><span class="derive-step-title">$\dfrac{dy}{dx}=\dfrac{6y}{x}-xy^2$ 的通解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$n=2$ 的伯努利方程，$P=\dfrac6x$，$Q=-x$。设 $z=y^{1-2}=y^{-1}$，则</p>
<div class="formula">$$\frac{dz}{dx}=(1-n)Pz+(1-n)Q=(-1)\frac6x z+(-1)(-x)=-\frac6x z+x$$</div>
<p>这是一阶线性方程。解齐次：$\dfrac{dz}{z}=-\dfrac6x dx$，$\ln|z|=-6\ln|x|+C$，$z=Cx^{-6}$。</p>
<p>常数变易设 $z=c(x)x^{-6}$，求导 $z'=c'x^{-6}-6cx^{-7}$，代入 $z'=-\dfrac6xz+x$：</p>
<div class="formula">$$c'x^{-6}-6cx^{-7}=-\frac6x cx^{-6}+x \;\Rightarrow\; c'x^{-6}=x \;\Rightarrow\; c'=x^7$$</div>
<p>积分 $c(x)=\dfrac{x^8}{8}+\bar C$，所以</p>
<div class="formula">$$z=\left(\frac{x^8}{8}+\bar C\right)x^{-6}=\frac{x^2}{8}+\frac{\bar C}{x^6}$$</div>
<p>代回 $y=1/z$：</p>
<div class="formula">$$\frac1y=\frac{x^2}{8}+\frac{\bar C}{x^6},\quad \text{即}\quad y=\frac{8x^6}{x^8+8\bar C}$$</div>
<p>再加上 $y=0$ 这个解。</p>
<p>验证（取 $\bar C=0$）：$y=\dfrac{8}{x^2}$，$y'=-\dfrac{16}{x^3}$。右边 $\dfrac{6y}{x}-xy^2=\dfrac{48}{x^3}-\dfrac{64}{x^4}$，对不上。说明我算错了，重查。</p>
<p>重查：$z'=-\dfrac6x z+x$ 中，代入 $z=\frac{x^2}{8}$：$z'=\frac{x}{4}$；右边 $-\frac6x\cdot\frac{x^2}{8}+x=-\frac{3x}{4}+x=\frac{x}{4}$ ✓。所以 $z$ 是对的。问题在回代：$y=1/z=\dfrac{1}{x^2/8}=\dfrac{8}{x^2}$，$y'=-\dfrac{16}{x^3}$。右边 $\dfrac{6y}{x}-xy^2=\dfrac{6\cdot8}{x^3}-x\cdot\dfrac{64}{x^4}=\dfrac{48}{x^3}-\dfrac{64}{x^3}=-\dfrac{16}{x^3}$ ✓。刚才我把 $-\frac{64}{x^4}$ 的幂次算错了，应为 $-\frac{64}{x^3}$。验证通过。</p>
</div></div>
</div>

<h3>4.6 数值例：$y'+2y=4$，$y(0)=1$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">套公式，代初值，列表验证</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$P=2$，$Q=4$，$\int Pdx=2x$。由公式：</p>
<div class="formula">$$y=e^{2x}\left(\int4e^{-2x}dx+C\right)=e^{2x}\left(-2e^{-2x}+C\right)=Ce^{2x}-2$$</div>
<p>代 $y(0)=1$：$1=C-2$，$C=3$，特解</p>
<div class="formula">$$y=3e^{2x}-2$$</div>
<p>数值检查：$x=0$ 时 $y=1$ ✓；$x=0.1$ 时 $y=3e^{0.2}-2\approx3\cdot1.2214-2=1.664$；$x=0.2$ 时 $y\approx3\cdot1.4918-2=2.475$。</p>
<p>从物理上看：$y'=4-2y$，$y$ 小于 2 时导数为正（增长），大于 2 时为负（下降），所以 $y$ 越靠近 2 越慢，$y=2$ 是稳定平衡点。解确实从 1 单调上升到 2。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">本章方法选择</div>$y'$ 和 $y$ 都是一次、系数只含 $x$ → 直接套线性公式。出现 $y^n$（$n\ne1$）→ 伯努利，换 $z=y^{1-n}$。齐次解记得先算，常数变易时 $P$ 项会自动抵消，如果没抵消说明形式设错了。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">解 $y'-y=x$，$y(0)=2$。<br>答：$P=-1,Q=x$，$\int Pdx=-x$。$y=e^{x}(\int xe^{-x}dx+C)$。$\int xe^{-x}dx=-(x+1)e^{-x}$（分部积分），所以 $y=e^x(-(x+1)e^{-x}+C)=Ce^x-x-1$。代 $y(0)=2$：$2=C-1$，$C=3$，$y=3e^x-x-1$。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">为什么伯努利方程要求 $n\ne0,1$？<br>答：$n=0$ 时 $y^0=1$，方程退化成线性；$n=1$ 时 $y'=(P+Q)y$，仍是线性（$Q$ 并进 $P$）。这两种都不需要换元，本来就是线性方程。</div></div>

<div class="chapter-nav"></div>
</section>

<!-- ========== 第 5 章：恰当方程与积分因子 ========== -->
<section class="chapter" id="exact" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">5</span>恰当方程与积分因子</h2>
<p class="lead">把方程写成 $M\,dx+N\,dy=0$。如果左边正好是某个二元函数的全微分，方程就能一步积分；不是的话，乘以一个"积分因子"把它变成恰当方程。对应课件 chapter2-3。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：找一件东西的"包装盒"</div>$M\,dx+N\,dy$ 看起来是一堆散件。恰当方程的意思是：这堆散件其实是从同一个盒子里拆出来的，$du$。找到盒子（函数 $u$），方程就变成 $du=0$，解直接是 $u=c$。积分因子是"给散件换个包装方式"，让它们能被装进一个盒子。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 1 章的偏导数、全微分、混合偏导相等；第 4 章的线性方程解法（例 3 会用）。</div>

<h3>5.1 对称形式</h3>
<p>一阶方程 $y'=f(x,y)$ 可以写成 $f(x,y)dx-dy=0$。更一般地，把 $x,y$ 平等看待：</p>
<div class="formula">$$M(x,y)\,dx+N(x,y)\,dy=0 \tag{2.39}$$</div>
<p>$M,N$ 连续且有连续一阶偏导。这个形式的好处是不偏向"$y$ 是 $x$ 的函数"，$x$ 也可以当 $y$ 的函数。</p>

<h3>5.2 恰当方程的定义</h3>
<p>如果 (2.39) 的左边恰好是某个二元函数 $u(x,y)$ 的全微分：</p>
<div class="formula">$$M\,dx+N\,dy=du=\frac{\partial u}{\partial x}dx+\frac{\partial u}{\partial y}dy \tag{2.40}$$</div>
<p>则称 (2.39) 为<strong>恰当微分方程</strong>。等价于两条：</p>
<div class="formula">$$\frac{\partial u}{\partial x}=M,\qquad \frac{\partial u}{\partial y}=N$$</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">为什么通解是 $u(x,y)=c$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $y=y(x)$ 是解，沿解曲线 $u(x,y(x))$ 对 $x$ 求导：</p>
<div class="formula">$$\frac{d}{dx}u(x,y(x))=u_x+u_y\,y'=M+N\,y'$$</div>
<p>由方程 $M+N y'=0$，所以 $\dfrac{d}{dx}u=0$，$u$ 沿解曲线是常数：$u(x,y)=c$。</p>
<p>反过来，如果 $u(x,y)=c$ 确定了一个函数 $y(x)$，两边对 $x$ 求导得 $u_x+u_yy'=0$，即 $M+Ny'=0$，是解。所以通解就是 $u(x,y)=c$。</p>
</div></div>
</div>

<h3>5.3 判定定理：$\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial x}$</h3>
<p>在单连通区域内，$M,N$ 有连续一阶偏导，则 (2.39) 恰当<strong>当且仅当</strong></p>
<div class="formula">$$\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x} \tag{2.42}$$</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">必要性：恰当就能推出这个等式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>如果恰当，存在 $u$ 使 $u_x=M$，$u_y=N$。对 $M$ 求 $y$ 的偏导：$M_y=u_{xy}$；对 $N$ 求 $x$ 的偏导：$N_x=u_{yx}$。二阶混合偏导连续时相等（这是微积分里的定理：先对 $x$ 后对 $y$ 与先对 $y$ 后对 $x$ 结果相同），所以 $M_y=N_x$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">充分性：等式成立时怎么造出 $u$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>固定起点 $(x_0,y_0)$，定义</p>
<div class="formula">$$u(x,y)=\int_{x_0}^{x}M(t,y_0)dt+\int_{y_0}^{y}N(x,s)ds$$</div>
<p>先沿水平走到 $(x,y_0)$，再沿竖直走到 $(x,y)$。验证 $u_x=M$：第一项对 $x$ 求导得 $M(x,y_0)$，第二项对 $x$ 求导（积分号内求导）得 $\displaystyle\int_{y_0}^{y}N_x(x,s)ds$。两项相加：</p>
<div class="formula">$$u_x=M(x,y_0)+\int_{y_0}^{y}N_x ds=M(x,y_0)+\int_{y_0}^{y}M_y ds=M(x,y_0)+M(x,y)-M(x,y_0)=M(x,y)$$</div>
<p>这里用了条件 $N_x=M_y$ 把被积函数换掉，再用牛顿-莱布尼茨公式收回。$u_y=N$ 更直接：第一项与 $y$ 无关，第二项对 $y$ 求导得 $N(x,y)$。</p>
<p>所以 $u$ 存在，条件充分。</p>
</div></div>
</div>
<div class="callout callout-tip"><div class="callout-title">单连通是什么意思</div>"区域里没有洞"。如果区域中间挖掉一块，绕洞一圈的积分可能不为零，上面的路径构造就不一定给出单值函数。本课的例题都在整个平面或简单矩形上，不涉及洞。</div>

<h3>5.4 求 $u$ 的两种方法</h3>
<h4>方法一：曲线积分法（折线路径）</h4>
<div class="formula">$$u(x,y)=\int_{x_0}^{x}M(x,y_0)dx+\int_{y_0}^{y}N(x,y)dy \tag{2.51}$$</div>
<p>先横后竖。也可以先竖后横：</p>
<div class="formula">$$u(x,y)=\int_{y_0}^{y}N(x_0,y)dy+\int_{x_0}^{x}M(x,y)dx \tag{2.52}$$</div>
<p>起点 $(x_0,y_0)$ 随便选，通常选原点或让积分为零的点，算起来简单。</p>

<h4>方法二：分项组合法（凑全微分）</h4>
<p>利用已知的全微分公式，把各项凑成 $d(\cdot)$ 的形式。常用公式：</p>
<div class="table-wrap">
<table>
<thead><tr><th>表达式</th><th>等于</th></tr></thead>
<tbody>
<tr><td>$y\,dx+x\,dy$</td><td>$d(xy)$</td></tr>
<tr><td>$\dfrac{y\,dx-x\,dy}{y^2}$</td><td>$d\!\left(\dfrac{x}{y}\right)$</td></tr>
<tr><td>$\dfrac{x\,dy-y\,dx}{x^2}$</td><td>$d\!\left(\dfrac{y}{x}\right)$</td></tr>
<tr><td>$\dfrac{y\,dx-x\,dy}{xy}$</td><td>$d\!\left(\ln\left|\dfrac{x}{y}\right|\right)$</td></tr>
<tr><td>$\dfrac{y\,dx-x\,dy}{x^2+y^2}$</td><td>$d\!\left(\arctan\dfrac{y}{x}\right)$</td></tr>
<tr><td>$\dfrac{y\,dx-x\,dy}{x^2-y^2}$</td><td>$\dfrac12d\!\left(\ln\left|\dfrac{x-y}{x+y}\right|\right)$</td></tr>
<tr><td>$x\,dx+y\,dy$</td><td>$\dfrac12d(x^2+y^2)$</td></tr>
</tbody>
</table>
</div>
<div class="callout callout-warn"><div class="callout-title">怎么记</div>不用死记。推导一次就记住了：$d(xy)=y\,dx+x\,dy$ 是乘积法则；$d(x/y)=(y\,dx-x\,dy)/y^2$ 是商的法则反过来。</div>

<h3>5.5 例 1：$(3x^2+6xy^2)dx+(6x^2y+4y^3)dy=0$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">验证恰当性</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$M=3x^2+6xy^2$，$N=6x^2y+4y^3$。</p>
<div class="formula">$$\frac{\partial M}{\partial y}=12xy,\qquad \frac{\partial N}{\partial x}=12xy$$</div>
<p>相等，恰当。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">方法一：从原点积分</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$u=\int_0^x 3x^2dx+\int_0^y(6x^2y+4y^3)dy=x^3+3x^2y^2+y^4$$</div>
<p>第一个积分把 $y$ 当 0，$M(x,0)=3x^2$；第二个积分把 $x$ 当固定。</p>
<p>通解 $x^3+3x^2y^2+y^4=c$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">方法二：分项组合</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>重新分组：</p>
<div class="formula">$$3x^2dx+4y^3dy+6xy^2dx+6x^2ydy$$</div>
<p>前两项：$3x^2dx=d(x^3)$，$4y^3dy=d(y^4)$。后两项：$6xy^2dx+6x^2ydy=3(2xy^2dx+2x^2ydy)=3d(x^2y^2)$。</p>
<p>合起来：</p>
<div class="formula">$$d(x^3)+d(y^4)+3d(x^2y^2)=d(x^3+y^4+3x^2y^2)=0$$</div>
<p>通解 $x^3+3x^2y^2+y^4=c$，与曲线积分法一致。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">求导验证</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>对 $x^3+3x^2y^2+y^4=c$ 两边对 $x$ 求导：$3x^2+6xy^2+6x^2yy'+4y^3y'=0$，即 $(3x^2+6xy^2)+(6x^2y+4y^3)y'=0$，与原方程一致。</p>
</div></div>
</div>

<h3>5.6 积分因子</h3>
<p>不是恰当方程时，想办法乘上一个非零函数 $\mu(x,y)$，让它变成恰当方程：</p>
<div class="formula">$$\mu M\,dx+\mu N\,dy=0 \tag{2.56}$$</div>
<p>$\mu$ 叫<strong>积分因子</strong>。由判定定理，$\mu$ 满足</p>
<div class="formula">$$\frac{\partial(\mu M)}{\partial y}=\frac{\partial(\mu N)}{\partial x}$$</div>
<p>展开（用乘积法则和 $M,N$ 的偏导）：</p>
<div class="formula">$$\mu M_y+\mu_yM=\mu N_x+\mu_xN$$</div>
<p>整理成关于 $\mu$ 的方程：</p>
<div class="formula">$$N\mu_x-M\mu_y=(M_y-N_x)\mu \tag{2.57}$$</div>
<p>这是关于 $\mu$ 的一阶线性偏微分方程。一般情况下比原方程还难解。但**如果假设 $\mu$ 只与 $x$（或只与 $y$）有关**，它就退化成一元可解问题。</p>

<h3>5.7 只与 $x$ 有关的积分因子</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推导</span><span class="derive-step-title">令 $\mu=\mu(x)$，$\mu_y=0$，方程变成</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>代入 (2.57)：$N\mu'(x)-0=(M_y-N_x)\mu$，即</p>
<div class="formula">$$\frac{d\mu}{\mu}=\frac{M_y-N_x}{N}dx \tag{2.58}$$</div>
<p>左边只含 $\mu$，右边只含 $x$（如果 $\mu$ 只与 $x$ 有关，右边必须不显含 $y$）。所以要求</p>
<div class="formula">$$\frac{M_y-N_x}{N}=\psi(x) \tag{2.59}$$</div>
<p>此时积分得</p>
<div class="formula">$$\mu(x)=e^{\int\psi(x)dx} \tag{2.60}$$</div>
<p>（常数取 1，因为乘常数不改变恰当性，只改变 $c$ 的取值。）</p>
</div></div>
</div>

<h3>5.8 只与 $y$ 有关的积分因子</h3>
<p>同理，设 $\mu=\mu(y)$，$\mu_x=0$，(2.57) 变成 $-M\mu_y=(M_y-N_x)\mu$，即</p>
<div class="formula">$$\frac{d\mu}{\mu}=\frac{N_x-M_y}{M}dy$$</div>
<p>要求</p>
<div class="formula">$$\frac{N_x-M_y}{M}=\varphi(y)$$</div>
<p>此时</p>
<div class="formula">$$\mu(y)=e^{\int\varphi(y)dy}$$</div>
<p>注意符号：只与 $x$ 有关时分子是 $M_y-N_x$，只与 $y$ 有关时分子是 $N_x-M_y$（反过来了），除以的分母也分别换成了 $N$ 和 $M$。记错符号是这类题最常见的错误。</p>

<h3>5.9 例 3：用积分因子重解一阶线性方程</h3>
<p>方程 $y'=P(x)y+Q(x)$，改写成</p>
<div class="formula">$$[P(x)y+Q(x)]dx-dy=0 \tag{2.61}$$</div>
<p>读出 $M=P(x)y+Q(x)$，$N=-1$。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">算判别式，看出只与 $x$ 有关</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\frac{M_y-N_x}{N}=\frac{P(x)-0}{-1}=-P(x)$$</div>
<p>不含 $y$，所以存在只与 $x$ 有关的积分因子。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">算出 $\mu$，乘到方程上</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\mu=e^{\int(-P)dx}=e^{-\int Pdx}$$</div>
<p>两边乘以 $\mu$：</p>
<div class="formula">$$\left[P(x)e^{-\int P}dx\right]y+e^{-\int P}Q(x)dx-e^{-\int P}dy=0$$</div>
<p>注意 $P e^{-\int P}$ 正好是 $-e^{-\int P}$ 的导数（链式，指数求导出 $-P$），所以前一项与第三项能合成一个全微分：</p>
<div class="formula">$$d\!\left(ye^{-\int P}\right)=e^{-\int P}dy+y\,d(e^{-\int P})=e^{-\int P}dy-P e^{-\int P}y\,dx$$</div>
<p>带负号正好对上，于是方程变成</p>
<div class="formula">$$-d\!\left(ye^{-\int P}\right)+Qe^{-\int P}dx=0 \;\Rightarrow\; d\!\left(ye^{-\int P}\right)=Qe^{-\int P}dx$$</div>
<p>积分：$ye^{-\int P}=\displaystyle\int Qe^{-\int P}dx+c$，两边乘 $e^{\int P}$：</p>
<div class="formula">$$y=e^{\int P}\left(\int Qe^{-\int P}dx+c\right)$$</div>
<p>与第 4 章常数变易法得到的公式完全一样。两条路殊途同归，这是很好的交叉验证。</p>
</div></div>
</div>

<h3>5.10 例 5：$y\,dx+(y-x)dy=0$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">先查恰当性</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$M=y$，$N=y-x$。$M_y=1$，$N_x=-1$，不相等，不是恰当方程。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">算两个判别式，看哪个只含一个变量</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>只与 $x$ 有关：$\dfrac{M_y-N_x}{N}=\dfrac{1-(-1)}{y-x}=\dfrac{2}{y-x}$，含 $y$，不行。</p>
<p>只与 $y$ 有关：$\dfrac{N_x-M_y}{M}=\dfrac{-1-1}{y}=-\dfrac2y$，只含 $y$ ✓。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">算 $\mu(y)$，乘上去</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\mu=e^{\int(-2/y)dy}=e^{-2\ln|y|}=\frac{1}{y^2}$$</div>
<p>两边乘以 $\dfrac{1}{y^2}$：</p>
<div class="formula">$$\frac{dx}{y}+\frac{y-x}{y^2}dy=0$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">分项组合</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>拆开：</p>
<div class="formula">$$\frac{dx}{y}-\frac{x}{y^2}dy+\frac{dy}{y}=\left(\frac{dx}{y}-\frac{x\,dy}{y^2}\right)+\frac{dy}{y}=d\!\left(\frac xy\right)+d(\ln|y|)$$</div>
<p>所以 $d\!\left(\dfrac xy+\ln|y|\right)=0$，通解</p>
<div class="formula">$$\frac xy+\ln|y|=c$$</div>
<p>另外原方程还有解 $y=0$（乘 $\mu$ 时被排除了，要单独补）。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">本章流程</div>① 写成 $M dx+N dy=0$；② 算 $M_y, N_x$，相等就是恰当，用曲线积分或分项组合求 $u$；③ 不等就试两个判别式，哪个只含一个变量就用哪个算 $\mu$；④ 乘 $\mu$ 后重新走 ②；⑤ 别忘了检查被 $\mu$ 除掉的解（$\mu$ 的分母为 0 的那些）。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">验证 $(2x+y)dx+(x+2y)dy=0$ 是恰当方程并求解。<br>答：$M_y=1=N_x$ ✓。$u=\int_0^x 2xdx+\int_0^y(x+2y)dy=x^2+xy+y^2$。通解 $x^2+xy+y^2=c$（一族椭圆）。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">$(x^2+y^2)dx+2xy\,dy=0$ 的积分因子怎么找？<br>答：$M_y=2y$，$N_x=2y$，其实已经是恰当方程。（若换一个不平衡的系数，比如 $(x^2+y^2)dx+xy\,dy=0$，$M_y=2y,N_x=y$，只与 $x$ 判别式 $\frac{y}{xy}=\frac1x$ 只含 $x$，$\mu=e^{\int dx/x}=x$。）</div></div>
<div class="qa-item"><div class="qa-q">思考题 3</div><div class="qa-a">为什么积分因子不唯一？<br>答：如果 $\mu$ 是积分因子，那么 $\mu\cdot g(u)$（$g$ 是任意可微函数）也是积分因子，因为 $g(u)du=d(G(u))$ 仍是全微分。不同积分因子给出的通解形式不同，但本质等价。</div></div>

<div class="chapter-nav"></div>
</section>
'''

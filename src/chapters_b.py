#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 2、3 章：认识微分方程 + 变量分离法"""

CH_B = r'''
<!-- ========== 第 2 章：认识微分方程 ========== -->
<section class="chapter" id="ode-basic" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">2</span>认识微分方程</h2>
<p class="lead">这一章建立概念：什么叫微分方程，阶是什么，线性是什么意思，解和通解怎么区分，方向场怎么看。对应课件 chapter1-1。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：一句话的长度</div>普通方程是"一个数等于多少"，比如 $x+2=5$，答案是 $x=3$。微分方程是"一个函数的变化率等于多少"，答案是<strong>一整条曲线</strong>，不是一个数。所以解微分方程得到的是一族函数，不是单个值。
</div>

<h3>2.1 定义：含导数的等式</h3>
<p>含未知函数及其导数的方程，叫<strong>微分方程</strong>。未知函数只有一个自变量时叫<strong>常微分方程</strong>（ordinary differential equation，ODE）；有两个以上自变量、出现偏导数时叫<strong>偏微分方程</strong>（PDE）。本课只讲常微分方程。</p>
<div class="formula">$$\frac{dy}{dx}=2x,\qquad y''+y=0,\qquad \frac{dy}{dx}=x+y^2$$</div>
<p>第一条：什么函数的导数是 $2x$？$y=x^2+C$，$C$ 任意。<br>第二条：什么函数求两次导等于自己的相反数？$y=\sin x$ 和 $y=\cos x$ 都行，一般解是 $y=C_1\sin x+C_2\cos x$。<br>第三条：$y'$ 同时依赖 $x$ 和 $y$，解不出初等函数，这正说明后面需要理论（存在性）和数值方法。</p>

<h3>2.2 怎么从现实里写出微分方程</h3>
<p>四步：设出要研究的量；写出它"变化多快"与"现在是多少"的关系；把关系写成含导数的等式；补一个初始条件。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">模型①</span><span class="derive-step-title">人口增长（Malthus 模型）</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>假设增长率正比于当前人口：单位时间增加的量 $=r\times$ 当前人口。写成</p>
<div class="formula">$$\frac{dN}{dt}=rN$$</div>
<p>$r$ 是增长率常数。解出来是 $N=N_0e^{rt}$，指数增长。这个模型只在资源充足时成立，人口大了就不准。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">模型②</span><span class="derive-step-title">Logistic 模型（加一个上限）</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>资源有限，环境最多容纳 $K$。人口接近 $K$ 时增长率下降，写成</p>
<div class="formula">$$\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)$$</div>
<p>$N$ 小时括号接近 1，像 Malthus；$N$ 接近 $K$ 时括号接近 0，增长停住。解是 S 形曲线。这个方程属于第 3 章的变量分离型。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">模型③</span><span class="derive-step-title">牛顿冷却</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>物体温度 $T$ 与环境温度 $T_0$ 差得越多，降温越快：</p>
<div class="formula">$$\frac{dT}{dt}=-k(T-T_0)$$</div>
<p>这是一个一阶线性方程（第 4 章），解是 $T=T_0+(T_{\text{初}}-T_0)e^{-kt}$，指数趋近环境温度。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">模型④</span><span class="derive-step-title">洛伦茨方程：确定性里的混沌</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>三个变量互相影响，写成方程组：</p>
<div class="formula">$$\frac{dx}{dt}=\sigma(y-x),\quad \frac{dy}{dt}=x(\rho-z)-y,\quad \frac{dz}{dt}=xy-\beta z$$</div>
<p>它描述大气对流。初值差万分之一，过一段时间两条轨道就完全分开，这叫<strong>混沌</strong>。这说明"解存在且唯一"不等于"能长期预测"，第 7 章的存在唯一性定理保证短期内的确定性，长期预测还要看初值敏感度。</p>
</div></div>
</div>

<h3>2.3 阶</h3>
<p>方程里出现的<strong>最高阶导数</strong>的阶数，就是方程的阶。一阶方程（只含 $y'$）是一阶，含 $y''$ 是二阶。本课主要讲一阶方程，第 1 章绪论提了一句二阶的例子。</p>
<div class="formula">$$\underbrace{\frac{dy}{dx}=2x}_{\text{一阶}},\qquad \underbrace{y''+y=0}_{\text{二阶}}$$</div>

<h3>2.4 线性与非线性</h3>
<p>把方程整理成"未知函数及其各阶导数都在分子上、都是一次、系数只依赖于自变量"的形式，叫<strong>线性方程</strong>。否则叫非线性。</p>
<div class="callout callout-tip"><div class="callout-title">判断口诀</div>看到 $y^2$、$y'y$、$\sin y$、$e^y$、$\sqrt{y}$，只要未知函数本身被平方、被开方、放进三角函数或指数、或两个未知函数相乘，就是非线性。看到 $y$、$y'$、$y''$ 单独出现、前面系数只含 $x$，就是线性。
</div>
<div class="table-wrap">
<table>
<thead><tr><th>方程</th><th>阶</th><th>线性？</th><th>理由</th></tr></thead>
<tbody>
<tr><td>$y'=4x^2$</td><td>1</td><td>线性</td><td>$y'$ 一次，系数 $4x^2$ 只含 $x$</td></tr>
<tr><td>$y''+12xy=0$</td><td>2</td><td>线性</td><td>系数 $12x$ 只含 $x$</td></tr>
<tr><td>$(y')^3+3xy'-3y=0$</td><td>1</td><td>非线性</td><td>$y'$ 被三次方</td></tr>
<tr><td>$y'+y^2=\sin x$</td><td>1</td><td>非线性</td><td>$y$ 被平方</td></tr>
<tr><td>$y'=\cos y+2x$</td><td>1</td><td>非线性</td><td>$y$ 在余弦里</td></tr>
<tr><td>$y'=\dfrac{y}{x}+\tan\dfrac{y}{x}$</td><td>1</td><td>非线性</td><td>$y$ 在正切里</td></tr>
</tbody>
</table>
</div>

<h3>2.5 解、隐式解</h3>
<p>把函数 $y=\varphi(x)$ 代进方程，两边恒等成立，就叫方程的<strong>解</strong>。验证方法只有一个：求导，代入，看两边是否相等。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">验证 $y=C e^{3x}$ 是 $y'-3y=0$ 的解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>求导：$y'=3Ce^{3x}$。代入左边：$y'-3y=3Ce^{3x}-3Ce^{3x}=0$，右边也是 0。恒等成立。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">验证 $x^2+y^2=C$ 是 $y'=-\dfrac{x}{y}$ 的解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>这是<strong>隐式解</strong>：$y$ 没有解出来，而是写成一个含 $y$ 的等式。验证时两边对 $x$ 求导（$y$ 是 $x$ 的函数，用链式法则）：</p>
<div class="formula">$$2x+2y\cdot y'=0 \;\Rightarrow\; y'=-\frac{x}{y}$$</div>
<p>正好是原方程。隐式解和显式解是同一件事的两种写法，显式解就是能写成 $y=\varphi(x)$ 的那种。</p>
</div></div>
</div>

<h3>2.6 通解、特解、初值问题</h3>
<p>解里带一个任意常数 $C$，叫<strong>通解</strong>：它代表了方程的全部解（一阶方程的通解带一个任意常数，二阶带两个）。指定一个初始条件把 $C$ 定下来，得到的叫<strong>特解</strong>。</p>
<div class="formula">$$\frac{dy}{dx}=2x \;\Rightarrow\; y=x^2+C \;(通解) \;\xrightarrow{\;y(1)=4\;}\; y=x^2+3 \;(特解)$$</div>
<p>带初始条件的方程叫<strong>初值问题</strong>：</p>
<div class="formula">$$\begin{cases}\dfrac{dy}{dx}=f(x,y)\\[4pt] y(x_0)=y_0\end{cases}$$</div>
<p>解初值问题的步骤：先求通解，再代入 $(x_0,y_0)$ 定常数。后面第 7 章会问：这个初值问题<strong>一定有解吗</strong>？如果有，<strong>只有一个解吗</strong>？</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$y'=3y$，$y(0)=2$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>通解 $y=Ce^{3x}$。代入 $x=0$：$2=Ce^{0}=C$，所以 $C=2$，特解 $y=2e^{3x}$。</p>
<p>验证：$y(0)=2$ ✓；$y'=6e^{3x}=3\cdot2e^{3x}=3y$ ✓。</p>
</div></div>
</div>

<h3>2.7 积分曲线、方向场、等斜线</h3>
<p>每一个解 $y=\varphi(x)$ 在平面上画出来是一条曲线，叫<strong>积分曲线</strong>。通解带一个参数，所以是一族曲线，彼此不相交（因为唯一性，第 7 章会证明）。</p>
<p>把方程 $y'=f(x,y)$ 看成"平面上每一点给出一个斜率"。在每一点画一小段斜率为 $f(x,y)$ 的短线，得到<strong>方向场</strong>。积分曲线就是"处处顺着小短线走"的曲线。</p>
<div class="callout callout-tip"><div class="callout-title">生活直觉</div>方向场像一片草地，每根草都倒了某个角度。你从某点出发，眼睛盯着最近的草不断往前接，走出来的轨迹就是积分曲线。初值不同，出发点不同，走出的轨迹不同，但都不交叉。</div>
<p><strong>等斜线</strong>是"斜率相同的所有点连成的线"，即 $f(x,y)=k$。画出若干条等斜线，再顺着它们的方向画短线，方向场就出来了。手工画方向场常用这个方法。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$y'=x+y$ 的等斜线</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>令 $x+y=k$，得到一族平行直线 $y=-x+k$。在每条这样的直线上，所有点的斜率都等于 $k$。$k=0$ 那条（$y=-x$）上斜率全是 0，曲线在这里水平；$k=1$ 那条上斜率全是 1；$k=-1$ 那条上斜率全是 $-1$。</p>
</div></div>
</div>

<h3>2.8 微分方程组与驻定</h3>
<p>多个未知函数互相耦合，写成方程组</p>
<div class="formula">$$\frac{dy_i}{dx}=f_i(x,y_1,y_2,\dots,y_n),\quad i=1,\dots,n$$</div>
<p>如果右端不显含 $x$，即 $f_i=f_i(y_1,\dots,y_n)$，叫<strong>驻定</strong>（自治）方程组；否则叫<strong>非驻定</strong>。驻定系统的方向场在平面上不随 $x$ 平移改变，画一次就够用，是动力系统研究的主要对象。</p>
<div class="callout callout-warn"><div class="callout-title">为什么讲这个</div>课件第一章把"微分方程组 + 驻定/非驻定/动力系统"作为背景介绍。后面 9 个章节全部针对单个一阶方程，方程组只在概念上交代，不展开解法。</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">判断 $y''+3y'+2y=e^x$ 的阶与线性性。<br>答：最高阶是 $y''$，二阶；$y''$、$y'$、$y$ 都是一次，系数是常数，$e^x$ 只含 $x$，所以是二阶线性非齐次方程。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">$y'=\sqrt{y}$ 在 $y=0$ 附近有什么问题？<br>答：$\sqrt y$ 在 $y=0$ 处导数无穷大，不满足 Lipschitz 条件。这类方程初值 $(0,0)$ 的解不唯一：$y=0$ 是解，$y=\frac{x^2}{4}$（$x\ge0$）也是解。这为第 7 章"为什么需要 Lipschitz 条件"埋下伏笔。</div></div>

<div class="chapter-nav"></div>
</section>

<!-- ========== 第 3 章：变量分离法 ========== -->
<section class="chapter" id="separable" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">3</span>变量分离法</h2>
<p class="lead">最基础的一类解法：把 $x$ 和 $y$ 分开，各自积分。对应课件 chapter2-1。学完还能处理两类变形：齐次方程和 $ax+by+c$ 型。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：把两种东西分装</div>方程 $\dfrac{dy}{dx}=f(x)\varphi(y)$ 右边是一个"只含 $x$ 的东西"乘一个"只含 $y$ 的东西"。就像把混在一起的两种豆子分到两个碗里：$y$ 相关的移到左边和 $dy$ 一起，$x$ 相关的留在右边和 $dx$ 一起，然后各自积分。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 1 章的微分（$dy=y'dx$）、不定积分表、$\ln|x|$、链式法则。</div>

<h3>3.1 形式与解法</h3>
<p>形如</p>
<div class="formula">$$\frac{dy}{dx}=f(x)\varphi(y) \tag{2.1}$$</div>
<p>的方程，其中 $f,\varphi$ 连续，叫<strong>可分离变量的微分方程</strong>。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">第一步：把 $dx$ 乘过去，得到两个微分相等</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>原式两边乘以 $dx$：</p>
<div class="formula">$$dy=f(x)\varphi(y)\,dx$$</div>
<p>这一步合法，因为 $\dfrac{dy}{dx}$ 是"微分 $dy$ 除以微分 $dx$"的商，$\dfrac{dy}{dx}=f(x)\varphi(y)$ 两边乘以 $dx$ 就是两个微分相等。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">第二步：除以 $\varphi(y)$，变量就分开了</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $\varphi(y)\ne0$，两边除以 $\varphi(y)$：</p>
<div class="formula">$$\frac{dy}{\varphi(y)}=f(x)\,dx$$</div>
<p>左边只含 $y$，右边只含 $x$。这正是"分装"完成。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">第三步：两边各自积分</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\int\frac{dy}{\varphi(y)}=\int f(x)\,dx+C \tag{2.2}$$</div>
<p>两个不定积分各自都带常数，移到一边只留一个 $C$ 就够了。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">第四步：写成隐式关系 $\Phi(y,x,C)=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>(2.2) 左边积分出来是 $y$ 的函数，右边是 $x$ 的函数加常数，整理成</p>
<div class="formula">$$\Phi(y,x,C)=0$$</div>
<p>这就是通解的隐式形式。能不能解出 $y$ 要看具体方程，解得出就写显式解，解不出就保留隐式。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">⑤</span><span class="derive-step-title">验证：对 (2.2) 两边微分，能回到原方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>对 $\displaystyle\int\frac{dy}{\varphi(y)}=\int f(x)dx+C$ 两边求微分（左边对 $y$，右边对 $x$，用链式法则把 $y$ 看成 $x$ 的函数）：</p>
<div class="formula">$$\frac{1}{\varphi(y)}\,dy=f(x)\,dx \;\Rightarrow\; \frac{dy}{dx}=f(x)\varphi(y)$$</div>
<p>回到原方程，说明 (2.2) 确定的隐函数确实满足 (2.1)。这一步是"解的正确性"证明，不是走形式。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">丢解问题：$\varphi(y)=0$ 的情形</div>第二步除以 $\varphi(y)$ 时假设了 $\varphi(y)\ne0$。如果 $\varphi(y_0)=0$，那么 $y\equiv y_0$ 是常函数，$y'=0$，右边 $f(x)\varphi(y_0)=0$，所以 $y=y_0$ 也是解，但它可能在通解里取不到（当 $C$ 取某些值时才能得到）。检查办法：解完以后看 $\varphi(y)=0$ 的根是不是解，是就单独写上。
</div>

<h3>3.2 例：$\dfrac{dy}{dx}=-\dfrac{x}{y}$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">分离、积分、整理</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>分离：两边乘 $dx$，乘 $y$：</p>
<div class="formula">$$y\,dy=-x\,dx$$</div>
<p>积分：</p>
<div class="formula">$$\frac{y^2}{2}=-\frac{x^2}{2}+C_1 \;\Rightarrow\; x^2+y^2=2C_1$$</div>
<p>记 $C=2C_1$（$C\ge0$ 才有实曲线），得通解</p>
<div class="formula">$$x^2+y^2=C$$</div>
<p>这是一族以原点为圆心的同心圆。显式解：$y=\pm\sqrt{C-x^2}$。</p>
<p>检查丢解：$\varphi(y)=y$，$\varphi(0)=0$，$y=0$ 是解吗？代入原方程：左边 $y'=0$，右边 $-x/0$，右边没有定义，所以 $y=0$ 不是解（原方程在 $y=0$ 处无意义）。无需补。</p>
</div></div>
</div>

<h3>3.3 例：$\dfrac{dy}{dx}=P(x)y$</h3>
<p>这是最重要的一类，第 4 章的线性齐次方程就是它。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">$y\ne0$ 时分离，$y=0$ 单独检查</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$y\ne0$ 时：</p>
<div class="formula">$$\frac{dy}{y}=P(x)\,dx \;\Rightarrow\; \ln|y|=\int P(x)dx+\bar C$$</div>
<p>两边取指数：$|y|=e^{\bar C}e^{\int P(x)dx}$。去掉绝对值，符号吸收进常数：</p>
<div class="formula">$$y=\pm e^{\bar C}e^{\int P(x)dx}=C e^{\int P(x)dx},\quad C=\pm e^{\bar C}\ne0$$</div>
<p>再检查 $y=0$：代入 $y'=P(x)y$，左边 0，右边 $P(x)\cdot0=0$，是解。它对应 $C=0$。所以通解可以写成</p>
<div class="formula">$$y=C e^{\int P(x)dx},\quad C\text{ 为任意常数}$$</div>
<p>这个结果第 4 章会反复用到，记住它的形状："指数上是一个积分"。</p>
</div></div>
</div>

<h3>3.4 可化为分离变量的类型（一）：齐次方程</h3>
<p>形如</p>
<div class="formula">$$\frac{dy}{dx}=g\!\left(\frac{y}{x}\right) \tag{2.5}$$</div>
<p>的方程叫<strong>齐次方程</strong>。右边不是 $x$ 和 $y$ 各自独立，而是只依赖它们的比值 $y/x$。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">变量变换 $u=\dfrac{y}{x}$，即 $y=ux$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$u$ 是新未知函数（$u$ 是 $x$ 的函数）。对 $y=ux$ 两边求导，用乘积法则：</p>
<div class="formula">$$\frac{dy}{dx}=x\frac{du}{dx}+u \tag{2.7}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">代入 (2.5) 并整理</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把 (2.7) 代进 $y'=g(y/x)=g(u)$：</p>
<div class="formula">$$x\frac{du}{dx}+u=g(u) \;\Rightarrow\; \frac{du}{dx}=\frac{g(u)-u}{x} \tag{2.8}$$</div>
<p>右边是"只含 $u$ 的部分"除以 $x$，属于可分离型：$\dfrac{du}{g(u)-u}=\dfrac{dx}{x}$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">分离积分，再把 $u=y/x$ 代回</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\int\frac{du}{g(u)-u}=\int\frac{dx}{x}+C=\ln|x|+C$$</div>
<p>积分完得到 $u$ 与 $x$ 的关系，把 $u=\dfrac{y}{x}$ 代回，就是原方程的通解。</p>
</div></div>
</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\dfrac{dy}{dx}=\dfrac{y}{x}+\tan\dfrac{y}{x}$（课件例题）</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>这是 $g(u)=u+\tan u$ 型。设 $u=y/x$，(2.8) 给出</p>
<div class="formula">$$\frac{du}{dx}=\frac{\tan u}{x} \tag{2.9}$$</div>
<p>当 $\tan u\ne0$ 时分离：</p>
<div class="formula">$$\cot u\,du=\frac{dx}{x}$$</div>
<p>积分。$\cot u=\dfrac{\cos u}{\sin u}$，分子正好是分母的导数，换元 $v=\sin u$，$dv=\cos u\,du$：</p>
<div class="formula">$$\int\frac{\cos u}{\sin u}du=\ln|\sin u|=\ln|x|+\bar C$$</div>
<p>整理：$\ln|\sin u|-\ln|x|=\bar C$，即 $\ln\left|\dfrac{\sin u}{x}\right|=\bar C$，取指数：</p>
<div class="formula">$$\sin u=cx,\quad c=\pm e^{\bar C}$$</div>
<p>另一方面 $\tan u=0$ 时 $\sin u=0$，对应 $c=0$，所以允许 $c=0$ 后通解统一为</p>
<div class="formula">$$\sin\frac{y}{x}=cx$$</div>
<p>注意原方程在 $\tan u$ 无定义（$u=\frac\pi2+k\pi$）的地方要排除，这些是"解曲线不能穿过"的竖直线。</p>
</div></div>
</div>

<h3>3.5 可化为分离变量的类型（二）：$\dfrac{dy}{dx}=f(ax+by+c)$</h3>
<p>右边只依赖线性组合 $ax+by+c$（$a\ne0$，$b\ne0$）。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">设 $u=ax+by+c$，对 $x$ 求导</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\frac{du}{dx}=a+b\frac{dy}{dx} \tag{2.15}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">代入原方程，得到可分离方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把 $\dfrac{dy}{dx}=f(u)$ 代进 (2.15)：</p>
<div class="formula">$$\frac{du}{dx}=a+bf(u)$$</div>
<p>这是"只含 $u$"等于常数，属于可分离型：$\dfrac{du}{a+bf(u)}=dx$。积分后把 $u=ax+by+c$ 代回。</p>
</div></div>
</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">数值例</span><span class="derive-step-title">$\dfrac{dy}{dx}=2x+y$，初值 $y(0)=1$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>这里 $u=2x+y$（$a=2,b=1,c=0$），$\dfrac{du}{dx}=2+\dfrac{dy}{dx}=2+u$。</p>
<div class="formula">$$\frac{du}{2+u}=dx \;\Rightarrow\; \ln|2+u|=x+C \;\Rightarrow\; 2+u=Ke^{x}$$</div>
<p>代回 $u=2x+y$：$2+2x+y=Ke^x$，即</p>
<div class="formula">$$y=Ke^x-2x-2$$</div>
<p>代入初值 $y(0)=1$：$1=K-2$，$K=3$。特解 $y=3e^x-2x-2$。</p>
<p>验证：$y'=3e^x-2$。右边 $2x+y=2x+3e^x-2x-2=3e^x-2$ ✓。$y(0)=3-2=1$ ✓。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">本章解题流程</div>
看到 $\dfrac{dy}{dx}=$ 一坨东西：先看能不能写成"$x$ 的函数乘 $y$ 的函数"（直接分离）；再看右边是否只依赖 $y/x$（齐次，换 $u=y/x$）；再看是否只依赖 $ax+by+c$（换 $u=ax+by+c$）。三条都不符，进入第 4、5、6 章。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">解 $\dfrac{dy}{dx}=e^{x+y}$。<br>答：$e^{x+y}=e^x e^y$，可分离。$\dfrac{dy}{e^y}=e^x dx \Rightarrow -e^{-y}=e^x+C \Rightarrow e^x+e^{-y}=C'$（$C'=-C$）。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">解 $\dfrac{dy}{dx}=\dfrac{x+y}{x-y}$。<br>答：分子分母同除 $x$，右边 $=\dfrac{1+y/x}{1-y/x}=g(y/x)$，齐次型。设 $u=y/x$，得 $\dfrac{du}{dx}=\dfrac{1+u^2}{x(1-u)}$，分离 $\dfrac{1-u}{1+u^2}du=\dfrac{dx}{x}$，积分 $\arctan u-\frac12\ln(1+u^2)=\ln|x|+C$。代回 $u=y/x$。</div></div>
<div class="qa-item"><div class="qa-q">思考题 3</div><div class="qa-a">为什么分离变量时只在一侧留一个常数 $C$？<br>答：两侧各自积分各带一个常数 $C_1,C_2$，相减得到 $C_1-C_2$，仍是一个任意常数，记作 $C$ 即可。留两个不增加信息。</div></div>

<div class="chapter-nav"></div>
</section>
'''

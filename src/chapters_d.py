#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 6、7 章：一阶隐式方程 + 存在唯一性定理"""

CH_D = r'''
<!-- ========== 第 6 章：一阶隐式方程与参数表示 ========== -->
<section class="chapter" id="implicit" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">6</span>一阶隐式方程与参数表示</h2>
<p class="lead">方程没有把 $y'$ 解出来，写成 $F(x,y,y')=0$。分四种类型处理，核心手法是"令 $p=y'$ 当参数，再对另一变量求导，把方程降成可解的形式"。对应课件 chapter2-4。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：解不出 $y'$，那就把 $y'$ 当"第三个变量"</div>显式方程 $y'=f(x,y)$ 能直接读出斜率。隐式方程里 $y'$ 被包在立方、乘积、平方里，解不出来。换个思路：把 $y'$ 命名为 $p$，于是方程变成关于 $x,y,p$ 的关系。再利用"$p$ 就是导数"这条信息，对某个变量求导，得到新的关系式，往往就能解出参数形式的解。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 1 章的全微分、链式法则；第 3 章的分离变量；第 5 章的恰当方程（有些隐式方程可以用 $p$ 的恰当形式处理）。</div>

<h3>6.1 四种类型总览</h3>
<div class="formula">$$F(x,y,y')=0$$</div>
<div class="table-wrap">
<table>
<thead><tr><th>类型</th><th>形式</th><th>处理</th></tr></thead>
<tbody>
<tr><td>(1)</td><td>$y=f(x,y')$，即 $y$ 解出来了</td><td>令 $p=y'$，对 $x$ 求导</td></tr>
<tr><td>(2)</td><td>$x=f(y,y')$，即 $x$ 解出来了</td><td>令 $p=y'$，对 $y$ 求导</td></tr>
<tr><td>(3)</td><td>$F(x,y')=0$，不含 $y$</td><td>在 $xp$ 平面参数化</td></tr>
<tr><td>(4)</td><td>$F(y,y')=0$，不含 $x$</td><td>在 $yp$ 平面参数化</td></tr>
</tbody>
</table>
</div>

<h3>6.2 类型 (1)：$y=f(x,y')$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">令 $p=y'$，把方程写成 $y=f(x,p)$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$y=f(x,p) \tag{2.63}$$</div>
<p>此时 $y$ 被表示为 $x$ 和 $p$ 的函数。但 $p$ 本身也是 $x$ 的函数，所以这是恒等式，可以两边对 $x$ 求导。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">两边对 $x$ 求导，得到关于 $p$ 的方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>左边 $y$ 对 $x$ 求导就是 $p$。右边对 $x$ 求导时 $p$ 是 $x$ 的函数，用链式法则：</p>
<div class="formula">$$p=\frac{\partial f}{\partial x}+\frac{\partial f}{\partial p}\cdot\frac{dp}{dx} \tag{2.64}$$</div>
<p>这是关于 $x$ 和 $p$ 的一阶方程（$p$ 当未知函数）。解出 $p$ 与 $x$ 的关系后，代回 (2.63) 就得到 $y$。</p>
<p>关键：这一步把"$y$ 的方程"变成了"$p$ 的方程"，降了一阶。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">(2.64) 的三种结果，对应三种写法</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p><strong>情形 a：</strong>解出 $p=\varphi(x,c)$。直接代入 $y=f(x,p)$：</p>
<div class="formula">$$y=f(x,\varphi(x,c))$$</div>
<p>得到显式通解。</p>
<p><strong>情形 b：</strong>解出 $x=\psi(p,c)$。此时 $y=f(\psi(p,c),p)$，得到参数形式的解：</p>
<div class="formula">$$\begin{cases}x=\psi(p,c)\\ y=f(\psi(p,c),p)\end{cases}$$</div>
<p>$p$ 当参数，$c$ 是任意常数。</p>
<p><strong>情形 c：</strong>得到隐式关系 $\Phi(x,p,c)=0$。此时</p>
<div class="formula">$$\begin{cases}\Phi(x,p,c)=0\\ y=f(x,p)\end{cases}$$</div>
<p>联立消 $p$ 就得到 $x,y$ 的关系。</p>
</div></div>
</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例1</span><span class="derive-step-title">$(y')^3+2xy'-y=0$（课件例题）</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>先把 $y$ 解出来：$y=p^3+2xp$，其中 $p=y'$。属于类型 (1)。</p>
<p>两边对 $x$ 求导。左边 $y'=p$；右边 $p^3$ 对 $x$ 求导是 $3p^2\dfrac{dp}{dx}$，$2xp$ 用乘积法则得 $2p+2x\dfrac{dp}{dx}$：</p>
<div class="formula">$$p=3p^2\frac{dp}{dx}+2p+2x\frac{dp}{dx}$$</div>
<p>移项，把 $2p$ 移过来：</p>
<div class="formula">$$p-2p=3p^2\frac{dp}{dx}+2x\frac{dp}{dx} \;\Rightarrow\; -p=(3p^2+2x)\frac{dp}{dx}$$</div>
<p>写成微分形式：$3p^2dp+2xdp+p\,dx=0$。这个式子不是恰当方程。课件给的处理是：$p\ne0$ 时两边乘以 $p$：</p>
<div class="formula">$$3p^3dp+2px\,dp+p^2dx=0$$</div>
<p>现在验证恰当性：$M=p^2$，$N=3p^3+2px$（把 $p$ 当"另一个变量"）。$M_p=2p$，$N_x=2p$，相等 ✓，是恰当方程。</p>
<p>求 $u$：$\displaystyle u=\int_0^p 3p^3dp+\int_0^x p^2dx=\frac34p^4+p^2x$（先对 $p$ 积分时 $x=0$，$N$ 中的 $2px$ 项消失；再对 $x$ 积分，$M=p^2$ 与 $x$ 无关）。</p>
<p>所以 $\dfrac34p^4+xp^2=c$，解出 $x$：</p>
<div class="formula">$$x=\frac{c-\frac34p^4}{p^2}$$</div>
<p>代入 $y=p^3+2xp$：</p>
<div class="formula">$$y=p^3+2p\cdot\frac{c-\frac34p^4}{p^2}=p^3+\frac{2c}{p}-\frac32p^3=\frac{2c}{p}-\frac12p^3$$</div>
<p>参数形式通解：</p>
<div class="formula">$$\begin{cases}x=\dfrac{c}{p^2}-\dfrac34p^2\\[6pt] y=\dfrac{2c}{p}-\dfrac12p^3\end{cases}$$</div>
<p>另外 $p=0$（即 $y'=0$）时，原方程给 $-y=0$，即 $y=0$，这是一条直线解（$y\equiv0$，$y'=0$，代入原方程 $0+0-0=0$ ✓）。</p>
</div></div>
</div>

<h3>6.3 类型 (2)：$x=f(y,y')$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">令 $p=y'$，写成 $x=f(y,p)$，对 $y$ 求导</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>此时 $x$ 被表示成 $y$ 和 $p$ 的函数。对 $y$ 求导。注意 $\dfrac{dx}{dy}=\dfrac{1}{y'}=\dfrac1p$（这就是"把 $x$ 看成 $y$ 的函数"的含义）。因此</p>
<div class="formula">$$\frac1p=\frac{\partial f}{\partial y}+\frac{\partial f}{\partial p}\cdot\frac{dp}{dy} \tag{2.67}$$</div>
<p>这是关于 $y$ 和 $p$ 的一阶方程，解出 $p$ 与 $y$ 的关系，再代回 $x=f(y,p)$。</p>
</div></div>
</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例3</span><span class="derive-step-title">$y=(y')^2-x(y')+\dfrac{x^2}{2}$ 的两种解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>这个方程同时含 $x$ 和 $y$，但 $y$ 能解出来：$y=p^2-xp+\dfrac{x^2}{2}$，属类型 (1)。</p>
<p>两边对 $x$ 求导。左边 $p$；右边 $p^2\to 2p\dfrac{dp}{dx}$，$-xp\to -p-x\dfrac{dp}{dx}$，$\dfrac{x^2}{2}\to x$：</p>
<div class="formula">$$p=2p\frac{dp}{dx}-p-x\frac{dp}{dx}+x$$</div>
<p>把右边的 $-p$ 移到左边：$2p=2p\dfrac{dp}{dx}-x\dfrac{dp}{dx}+x=(2p-x)\dfrac{dp}{dx}+x$。再移项：</p>
<div class="formula">$$2p-x=(2p-x)\frac{dp}{dx} \;\Rightarrow\; (2p-x)\left(\frac{dp}{dx}-1\right)=0$$</div>
<p>两个因子，给出两条路。</p>
<p><strong>路一：</strong>$\dfrac{dp}{dx}=1$，即 $p=x+c$。代回 $y=p^2-xp+\dfrac{x^2}{2}$：</p>
<div class="formula">$$y=(x+c)^2-x(x+c)+\frac{x^2}{2}=x^2+2cx+c^2-x^2-cx+\frac{x^2}{2}=\frac{x^2}{2}+cx+c^2$$</div>
<p>这是通解（含一个常数 $c$）。</p>
<p><strong>路二：</strong>$2p-x=0$，即 $p=\dfrac x2$。代回：$y=\dfrac{x^2}{4}-\dfrac{x^2}{2}+\dfrac{x^2}{2}=\dfrac{x^2}{4}$。这是一个不含任意常数的解。</p>
<p>它和通解什么关系？取通解里的 $c$，求它与 $y=\dfrac{x^2}{4}$ 的交点：解 $\dfrac{x^2}{2}+cx+c^2=\dfrac{x^2}{4}$，即 $\dfrac{x^2}{4}+cx+c^2=0$，判别式 $c^2-4\cdot\dfrac14\cdot c^2=c^2-c^2=0$，只有一个交点，且在该点两曲线相切（因为它是二重根）。所以 $y=\dfrac{x^2}{4}$ 与通解族的<strong>每一条</strong>都相切，这就是第 9 章的"奇解"，也是通解族的包络。</p>
</div></div>
</div>

<h3>6.4 类型 (3)：$F(x,y')=0$，不含 $y$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">把方程看成 $x$-$p$ 平面上的一条曲线，参数化</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>令 $p=y'$，方程变成 $F(x,p)=0$，这是 $x$-$p$ 平面里的一条曲线。设它可以用参数 $t$ 表示：</p>
<div class="formula">$$x=\varphi(t),\qquad p=\psi(t) \tag{2.70}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">用 $dy=p\,dx$ 求 $y$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把 $p=\psi(t)$、$dx=\varphi'(t)dt$ 代进 $dy=p\,dx$：</p>
<div class="formula">$$dy=\psi(t)\varphi'(t)\,dt$$</div>
<p>积分：</p>
<div class="formula">$$y=\int\psi(t)\varphi'(t)\,dt+c$$</div>
<p>于是参数形式的通解：</p>
<div class="formula">$$\begin{cases}x=\varphi(t)\\ y=\int\psi(t)\varphi'(t)dt+c\end{cases}$$</div>
</div></div>
</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$(y')^2-x=0$，即 $x=p^2$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>取 $p=t$，$x=t^2$。$dy=p\,dx=t\cdot2t\,dt=2t^2dt$，积分 $y=\dfrac{2t^3}{3}+c$。</p>
<p>参数通解 $\begin{cases}x=t^2\\y=\frac{2t^3}{3}+c\end{cases}$。消 $t$：$t=\pm\sqrt x$，$y=\pm\dfrac{2}{3}x^{3/2}+c$。这正是 $y'=\pm\sqrt x$ 的两族解。</p>
</div></div>
</div>

<h3>6.5 类型 (4)：$F(y,y')=0$，不含 $x$</h3>
<p>令 $p=y'$，方程变成 $F(y,p)=0$，在 $y$-$p$ 平面上参数化：$y=\varphi(t)$，$p=\psi(t)$。</p>
<p>这次用 $dx=\dfrac{dy}{p}$：</p>
<div class="formula">$$dx=\frac{\varphi'(t)}{\psi(t)}dt \;\Rightarrow\; x=\int\frac{\varphi'(t)}{\psi(t)}dt+c$$</div>
<p>参数通解：$\begin{cases}y=\varphi(t)\\ x=\int\frac{\varphi'(t)}{\psi(t)}dt+c\end{cases}$。</p>

<h3>6.6 克莱罗方程：一个包含参数解的特例</h3>
<p>形如</p>
<div class="formula">$$y=xp+f(p),\quad p=y'$$</div>
<p>的方程叫<strong>克莱罗方程</strong>。两边对 $x$ 求导：</p>
<div class="formula">$$p=p+x\frac{dp}{dx}+f'(p)\frac{dp}{dx} \;\Rightarrow\; 0=\left(x+f'(p)\right)\frac{dp}{dx}$$</div>
<p>两条路：$\dfrac{dp}{dx}=0$ 给 $p=c$，代回得<strong>直线族</strong> $y=cx+f(c)$；$x+f'(p)=0$ 给一条<strong>包络</strong>，参数式 $\begin{cases}x=-f'(p)\\ y=-pf'(p)+f(p)\end{cases}$，它是奇解。</p>
<p>结构上和上一节例 3 完全一样：通解是直线族，奇解是它们的包络。</p>

<div class="callout callout-key"><div class="callout-title">本章统一手法</div>令 $p=y'$。方程里哪一变量能解出来，就对另一个变量求导（$y$ 解出来 → 对 $x$ 求导；$x$ 解出来 → 对 $y$ 求导）。两个都解不出来，就把 $F=0$ 当曲线参数化，用 $dy=p\,dx$ 或 $dx=dy/p$ 积出另一个变量。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">解 $y=(y')^2$。<br>答：类型 (1)，$y=p^2$。求导 $p=2p\dfrac{dp}{dx}$。$p\ne0$ 时 $\dfrac{dp}{dx}=\dfrac12$，$p=\dfrac x2+c$，$y=\left(\dfrac x2+c\right)^2$。$p=0$ 时 $y=0$，是一条退化解。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">为什么类型 (2) 里对 $y$ 求导出现 $\dfrac1p$？<br>答：$x$ 当 $y$ 的函数时，$\dfrac{dx}{dy}=\dfrac{1}{dy/dx}=\dfrac1p$。这正是反函数求导法则。</div></div>

<div class="chapter-nav"></div>
</section>

<!-- ========== 第 7 章：存在唯一性定理 ========== -->
<section class="chapter" id="existence" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">7</span>存在唯一性定理与逐步逼近</h2>
<p class="lead">前面五章都在"假设解存在"的前提下求解。这一章回答两个问题：解一定存在吗？存在的话唯一吗？答案要用 Picard 逐步逼近来构造。对应课件 chapter3-1。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：修桥</div>要证明"从 A 到 B 有唯一一条路"，一个办法是自己造一条出来。Picard 的办法是：先站在 A，按地形给的坡度迈一小步，得到一个粗糙的路线；再拿这条路线重走一遍，修正每一步；反复迭代，路线越来越贴近真实地形。最后证明这个迭代序列会收敛到一条路，且只有一条。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 1 章的绝对值不等式、数列极限与一致收敛、变上限积分求导、阶乘与 $e^x$ 级数。</div>

<h3>7.1 为什么需要这个定理</h3>
<p>看两个反面例子。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">反例①</span><span class="derive-step-title">解不唯一</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>方程 $\dfrac{dy}{dx}=\sqrt{y}$，初值 $y(0)=0$。两个解都满足：</p>
<div class="formula">$$y_1\equiv0,\qquad y_2=\begin{cases}0,& x\le0\\ \dfrac{x^2}{4},& x&gt;0\end{cases}$$</div>
<p>验证 $y_2$：$x&gt;0$ 时 $y_2'=\dfrac x2$，$\sqrt{y_2}=\sqrt{\dfrac{x^2}{4}}=\dfrac x2$ ✓；$x\le0$ 时两边都是 0 ✓；在 $x=0$ 处左右导数都是 0，可导。所以 $y_2$ 也是解。</p>
<p>原因：$\sqrt y$ 在 $y=0$ 处变化太剧烈，斜率对 $y$ 的变化没有上界。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">反例②</span><span class="derive-step-title">解只在小区间存在</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>方程 $\dfrac{dy}{dx}=y^2$，初值 $y(0)=1$。分离变量解得 $y=\dfrac{1}{1-x}$。这个解只在 $x&lt;1$ 有定义，$x\to1^-$ 时 $y\to+\infty$。</p>
<p>方程本身处处光滑，但解"跑出无穷"了。所以"存在"必须说清<strong>在哪个区间上存在</strong>。</p>
</div></div>
</div>

<h3>7.2 Lipschitz 条件</h3>
<p>设 $f(x,y)$ 在矩形域</p>
<div class="formula">$$R:\quad |x-x_0|\le a,\quad |y-y_0|\le b \tag{3.2}$$</div>
<p>上有定义。如果存在常数 $L&gt;0$，使得对 $R$ 内任意两点 $(x,y_1)$、$(x,y_2)$ 都有</p>
<div class="formula">$$|f(x,y_1)-f(x,y_2)|\le L|y_1-y_2| \tag{3.3}$$</div>
<p>就说 $f$ 在 $R$ 上关于 $y$ 满足 <strong>Lipschitz 条件</strong>，$L$ 叫 Lipschitz 常数。</p>
<div class="callout callout-tip"><div class="callout-title">白话解释</div>"纵坐标改变 $|y_1-y_2|$，函数值的改变被同一个倍数 $L$ 控制住"。也就是斜率在 $y$ 方向上不会无限陡。$\sqrt y$ 在 $y=0$ 附近违反这一条：$y_1=0,y_2=\epsilon$ 时 $|\sqrt\epsilon-0|/\epsilon=1/\sqrt\epsilon\to\infty$。</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">检验</span><span class="derive-step-title">$f(x,y)=x+y^2$ 在 $|y|\le1$ 上满足 Lipschitz</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$|(x+y_1^2)-(x+y_2^2)|=|y_1^2-y_2^2|=|y_1+y_2|\cdot|y_1-y_2|\le2|y_1-y_2|$$</div>
<p>取 $L=2$。（$|y_1+y_2|\le|y_1|+|y_2|\le 2$。）</p>
<p>注意：在更大的范围里 $L$ 要变大。$|y|\le10$ 时 $L=20$。这说明 $L$ 和区域有关。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">检验</span><span class="derive-step-title">$f(x,y)=x^2+y$ 对 $y$ 满足 Lipschitz，$L=1$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$|(x^2+y_1)-(x^2+y_2)|=|y_1-y_2|$，取 $L=1$ 即可。这种叫"对 $y$ 是线性的"，Lipschitz 常数就是 $y$ 的系数绝对值。</p>
</div></div>
</div>

<h3>7.3 存在唯一性定理（Picard 定理）</h3>
<div class="callout callout-key"><div class="callout-title">定理 3.1</div>设 $f(x,y)$ 在矩形 $R:|x-x_0|\le a,\ |y-y_0|\le b$ 上连续，且关于 $y$ 满足 Lipschitz 条件，则初值问题 $\dfrac{dy}{dx}=f(x,y),\ y(x_0)=y_0$ 在区间 $|x-x_0|\le h$ 上存在唯一解，其中<div class="formula">$$h=\min\left(a,\ \frac{b}{M}\right),\qquad M=\max_{(x,y)\in R}|f(x,y)|$$</div>
</div>
<p>读法：$M$ 是区域内斜率的最大绝对值。$b/M$ 的意思是"以最大斜率往上冲，多久会冲出矩形的上边界"。$h$ 取 $a$ 和 $b/M$ 中较小的那个，保证解曲线既不出左右边界，也不出上下边界。</p>

<h3>7.4 证明的骨架</h3>
<p>五步，每步一个命题：</p>
<div class="table-wrap">
<table>
<thead><tr><th>命题</th><th>内容</th><th>作用</th></tr></thead>
<tbody>
<tr><td>1</td><td>微分方程等价于积分方程</td><td>把"求导"变成"求积分"，好做迭代</td></tr>
<tr><td>2</td><td>迭代序列 $\varphi_n$ 有定义、连续、落在 $R$ 内</td><td>保证每一步都合法</td></tr>
<tr><td>3</td><td>$\{\varphi_n\}$ 一致收敛</td><td>极限存在</td></tr>
<tr><td>4</td><td>极限是解</td><td>构造出了解（存在性）</td></tr>
<tr><td>5</td><td>解唯一</td><td>唯一性</td></tr>
</tbody>
</table>
</div>

<h3>7.5 命题 1：微分方程 ↔ 积分方程</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">正向</span><span class="derive-step-title">解微分方程就能得到积分方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $y=\varphi(x)$ 是初值问题的解。从 $x_0$ 到 $x$ 积分：</p>
<div class="formula">$$\int_{x_0}^{x}\varphi'(\xi)\,d\xi=\int_{x_0}^{x}f(\xi,\varphi(\xi))\,d\xi$$</div>
<p>左边由牛顿-莱布尼茨公式等于 $\varphi(x)-\varphi(x_0)=\varphi(x)-y_0$。移项：</p>
<div class="formula">$$y=\varphi(x)=y_0+\int_{x_0}^{x}f(\xi,\varphi(\xi))\,d\xi \tag{3.5}$$</div>
</div></div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">反向</span><span class="derive-step-title">积分方程的解就是微分方程的解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $\varphi$ 连续且满足 (3.5)。代 $x=x_0$，积分上下限相同，右边 $\int_{x_0}^{x_0}=0$，得 $\varphi(x_0)=y_0$ ✓。</p>
<p>两边对 $x$ 求导。右边用第 1 章的"变上限积分求导"：</p>
<div class="formula">$$\varphi'(x)=\frac{d}{dx}\int_{x_0}^{x}f(\xi,\varphi(\xi))d\xi=f(x,\varphi(x))$$</div>
<p>所以 $\varphi$ 满足微分方程 ✓。</p>
<p>结论：解微分方程与解积分方程是同一件事。这个转换是关键，因为积分方程可以做迭代（把未知函数 $\varphi$ 代进右边的积分号，得到新的函数）。</p>
</div></div>
</div>

<h3>7.6 命题 2：Picard 迭代序列</h3>
<p>取初始猜测 $\varphi_0(x)=y_0$（常数函数，就是初值），定义</p>
<div class="formula">$$\varphi_n(x)=y_0+\int_{x_0}^{x}f(\xi,\varphi_{n-1}(\xi))\,d\xi \tag{3.4}$$</div>
<p>直观：拿上一条粗略曲线当"参考轨迹"，沿它的斜率重新积出一条更准的曲线。重复下去。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">$\varphi_n$ 有定义、连续，且 $|\varphi_n(x)-y_0|\le b$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>用数学归纳法。</p>
<p><strong>基础：</strong>$n=0$ 时 $\varphi_0\equiv y_0$，$|\varphi_0-y_0|=0\le b$ ✓。</p>
<p><strong>归纳：</strong>设 $\varphi_{n-1}$ 连续且 $|\varphi_{n-1}(x)-y_0|\le b$（也就是落在 $R$ 的 $y$ 范围内，$f(\xi,\varphi_{n-1}(\xi))$ 有定义）。连续函数的复合与积分都连续，所以 $\varphi_n$ 连续。</p>
<p>估计大小：</p>
<div class="formula">$$|\varphi_n(x)-y_0|\le\left|\int_{x_0}^x\big|f(\xi,\varphi_{n-1}(\xi))\big|d\xi\right|\le M|x-x_0|\le Mh\le b$$</div>
<p>最后一步 $Mh\le b$ 由 $h\le b/M$ 推出（这就是 $h$ 取 $\min(a,b/M)$ 的作用）。</p>
<p>所以每一步都在 $R$ 内，$f$ 始终有定义，迭代可以一直做下去。</p>
<p>注意积分上限是 $x$，$x$ 可以在 $x_0$ 左边，此时 $\displaystyle\int_{x_0}^x$ 为负，但加绝对值后有 $\left|\int_{x_0}^x\right|\le M|x-x_0|$，仍然成立。</p>
</div></div>
</div>

<h3>7.7 命题 3：一致收敛</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">先估相邻两项之差</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>算 $\varphi_1-\varphi_0$：</p>
<div class="formula">$$|\varphi_1(x)-\varphi_0(x)|=\left|\int_{x_0}^x f(\xi,y_0)d\xi\right|\le M|x-x_0|$$</div>
<p>算 $\varphi_2-\varphi_1$：用 Lipschitz 条件</p>
<div class="formula">$$|\varphi_2(x)-\varphi_1(x)|\le\left|\int_{x_0}^x L|\varphi_1(\xi)-\varphi_0(\xi)|d\xi\right|\le L\int_{x_0}^{x}M|\xi-x_0|d\xi=\frac{ML}{2}|x-x_0|^2$$</div>
<p>（$\int_0^t s\,ds=t^2/2$。）继续用归纳：</p>
<div class="formula">$$|\varphi_n(x)-\varphi_{n-1}(x)|\le\frac{ML^{n-1}}{n!}|x-x_0|^n \tag{3.9}$$</div>
<p>归纳步：如果 $n-1$ 时成立，则</p>
<div class="formula">$$|\varphi_n-\varphi_{n-1}|\le L\int\left|\varphi_{n-1}-\varphi_{n-2}\right|\le L\int\frac{ML^{n-2}}{(n-1)!}|\xi-x_0|^{n-1}d\xi=\frac{ML^{n-1}}{n!}|x-x_0|^n$$</div>
<p>（$\int_0^t s^{n-1}ds=t^n/n$。）</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">把 $\varphi_n$ 写成级数，用比较法证收敛</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$\varphi_n=\varphi_0+(\varphi_1-\varphi_0)+\cdots+(\varphi_n-\varphi_{n-1})$。对绝对值取上界：</p>
<div class="formula">$$|\varphi_n(x)-\varphi_0(x)|\le\sum_{k=1}^n\frac{ML^{k-1}}{k!}|x-x_0|^k$$</div>
<p>右边是一个正项级数的部分和，它收敛，因为</p>
<div class="formula">$$\sum_{k=1}^\infty\frac{ML^{k-1}h^k}{k!}=\frac{M}{L}\left(e^{Lh}-1\right)&lt;\infty$$</div>
<p>（用了第 1 章的 $e^x=\sum x^n/n!$。）所以对每个固定的 $x$，$\varphi_n(x)$ 是柯西列，必然收敛，极限记作 $\varphi(x)$。</p>
<p>而且收敛是<strong>一致的</strong>：上面的级数上界与 $x$ 无关（只与 $h$ 有关），所以对 $|x-x_0|\le h$ 上所有 $x$，$n$ 足够大时误差同时小于给定值。这一点对命题 4 至关重要。</p>
</div></div>
</div>

<h3>7.8 命题 4：极限函数是解</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">把极限搬进积分号</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>对 (3.4) 两边取 $n\to\infty$：</p>
<div class="formula">$$\lim_{n\to\infty}\varphi_n(x)=y_0+\lim_{n\to\infty}\int_{x_0}^{x}f(\xi,\varphi_{n-1}(\xi))d\xi$$</div>
<p>左边是 $\varphi(x)$。右边要把极限搬进积分号，需要两件事：</p>
<p>① $f$ 在紧区域 $R$ 上连续，因此<strong>一致连续</strong>。含义：只要两点足够近，函数值就足够近，且这个"足够近"对区域内所有点统一。</p>
<p>② $\varphi_{n-1}$ 一致收敛于 $\varphi$，所以 $\varphi_{n-1}(\xi)$ 与 $\varphi(\xi)$ 的差可以一致地小。</p>
<p>合起来：$|f(\xi,\varphi_{n-1}(\xi))-f(\xi,\varphi(\xi))|$ 可以一致地小，于是积分之差也被控制住。所以</p>
<div class="formula">$$\varphi(x)=y_0+\int_{x_0}^{x}f(\xi,\varphi(\xi))d\xi$$</div>
<p>由命题 1 的反向部分，$\varphi$ 是初值问题的解。存在性证完。</p>
</div></div>
</div>

<h3>7.9 命题 5：唯一性</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">设两个解，作差</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $\varphi,\psi$ 都是解。两者都满足积分方程，相减：</p>
<div class="formula">$$\varphi(x)-\psi(x)=\int_{x_0}^{x}\left[f(\xi,\varphi(\xi))-f(\xi,\psi(\xi))\right]d\xi$$</div>
<p>取绝对值，用 Lipschitz 条件：</p>
<div class="formula">$$|\varphi(x)-\psi(x)|\le L\left|\int_{x_0}^x|\varphi(\xi)-\psi(\xi)|d\xi\right|$$</div>
</div></div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">Gronwall 不等式：从"积分不超过自己"推到"必须是 0"</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设非负连续函数 $u(x)$ 满足</p>
<div class="formula">$$u(x)\le K+L\left|\int_{x_0}^{x}u(\xi)d\xi\right|$$</div>
<p>则 $u(x)\le K e^{L|x-x_0|}$。</p>
<p>这里取 $K=0$，得到 $u(x)\le0$。但 $u$ 非负，所以 $u(x)=0$。</p>
<p>推一下为什么 $K=0$ 时一定是 0（不依赖 Gronwall 的一般形式，直接看这个特例）：设 $U(x)=\displaystyle\int_{x_0}^x u$（$x&gt;x_0$ 时），则 $U'=u\le LU$，即 $U'-LU\le0$。两边乘 $e^{-L(x-x_0)}$：$\left(Ue^{-L(x-x_0)}\right)'\le0$，所以 $Ue^{-L(x-x_0)}$ 单调不增，在 $x_0$ 处等于 0，故 $U\le0$。又 $U\ge0$（$u\ge0$ 且积分上限增），所以 $U\equiv0$，$u=U'=0$。$x&lt;x_0$ 同理。</p>
<p>于是 $\varphi-\psi\equiv0$，两解相同。唯一性证完。</p>
</div></div>
</div>
<div class="callout callout-key"><div class="callout-title">Gronwall 的一般形式（记住形状）</div>若 $u(x)\le K+\displaystyle\int_{x_0}^{x}u(\xi)g(\xi)d\xi$（$g\ge0$），则 $u(x)\le Ke^{\int_{x_0}^x g}$。它的用途：任何"误差被自己的积分控制住"的场合，误差都会指数增长但有上界。第 8 章初值依赖、第 10 章误差估计都用它。
</div>

<h3>7.10 $h$ 的几何意义</h3>
<p>解曲线在矩形内，斜率绝对值不超过 $M$。从 $(x_0,y_0)$ 出发往右走，最多走 $b/M$ 就会碰到 $y=y_0+b$ 或 $y=y_0-b$ 的上/下边界；往左走同理。左右边界距离是 $a$。所以能保证的安全区间是 $\min(a,b/M)$。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">同一个方程，矩形放大 $h$ 反而变小</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>方程 $y'=x^2+y^2$，初值 $(0,0)$。</p>
<p>矩形 $R_1:[-1,1]\times[-1,1]$：$M=\max(x^2+y^2)=2$，$h=\min(1,1/2)=1/2$。</p>
<p>矩形 $R_2:[-2,2]\times[-2,2]$：$M=8$，$h=\min(2,2/8)=1/4$。</p>
<p>区域变大了，$M$ 变大，$b/M$ 变小，保证的区间反而短。这不是定理错了，而是"在这块更大的区域里，斜率可能更陡，所以能保证的路程更短"。要得到更长的区间，应该用第 8 章的延拓：从 $1/2$ 的端点再造一个小矩形继续走。</p>
</div></div>
</div>

<h3>7.11 怎么检验 Lipschitz：用偏导</h3>
<p>直接用定义检验很麻烦。有一个充分条件：如果 $\dfrac{\partial f}{\partial y}$ 在 $R$ 上连续，则由中值定理，存在 $\theta\in(0,1)$ 使</p>
<div class="formula">$$f(x,y_1)-f(x,y_2)=\frac{\partial f}{\partial y}\left(x,\ y_2+\theta(y_1-y_2)\right)(y_1-y_2)$$</div>
<p>取绝对值，用 $\left|\dfrac{\partial f}{\partial y}\right|\le L$：</p>
<div class="formula">$$|f(x,y_1)-f(x,y_2)|\le L|y_1-y_2|$$</div>
<p>所以"偏导有界"就能推出 Lipschitz。实务中都用这一条，很少直接用定义。</p>
<div class="callout callout-warn"><div class="callout-title">注意方向</div>偏导有界是充分条件，不是必要条件。$f(x,y)=|y|$ 在 $y=0$ 处偏导不存在，但满足 Lipschitz（$L=1$）。所以不能用"偏导不存在"来判断"不满足 Lipschitz"。</div>

<h3>7.12 隐式方程的存在唯一性</h3>
<p>对 $F(x,y,y')=0$，不能直接套上面的定理。需要三个条件：</p>
<div class="formula">$$F(x,y,p)\ \text{在}\ (x_0,y_0,p_0)\ \text{的邻域内连续，且有连续偏导}\ F_x,F_y,F_p$$</div>
<div class="formula">$$F(x_0,y_0,p_0)=0\quad(\text{初值点满足方程})$$</div>
<div class="formula">$$F_p(x_0,y_0,p_0)\ne0$$</div>
<p>在这三个条件下，方程在 $x_0$ 附近能唯一确定一个函数 $y=y(x)$，满足 $y(x_0)=y_0$、$y'(x_0)=p_0$。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">$F_p\ne0$ 为什么保证能解出 $y'$，以及 $\dfrac{\partial f}{\partial y}$ 的公式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$F(x,y,p)=0$ 在 $(x_0,y_0,p_0)$ 附近，若 $F_p\ne0$，由隐函数存在定理可以把 $p$ 解成 $(x,y)$ 的函数 $p=f(x,y)$，并且</p>
<div class="formula">$$f_x=-\frac{F_x}{F_p},\qquad f_y=-\frac{F_y}{F_p}$$</div>
<p>（隐函数求导：$F(x,y,f(x,y))=0$ 两边对 $y$ 求导，$F_y+F_p f_y=0$，解出 $f_y=-F_y/F_p$。）</p>
<p>于是原方程局部化成了显式方程 $y'=f(x,y)$，可以套定理。而 $f_y$ 是否连续、是否有界，取决于 $F_y,F_p$ 的性质。这就是第 9 章判断奇解的根据：<strong>唯一性失效的地方必须有 $F_p=0$</strong>。</p>
</div></div>
</div>

<h3>7.13 算例：Picard 迭代手算三次</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\dfrac{dy}{dx}=x+y^2$，$y(0)=0$ 的前三次近似</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$\varphi_0=0$。</p>
<p>$\varphi_1(x)=\displaystyle\int_0^x\left(\xi+0^2\right)d\xi=\frac{x^2}{2}$。</p>
<p>$\varphi_2(x)=\displaystyle\int_0^x\left(\xi+\frac{\xi^4}{4}\right)d\xi=\frac{x^2}{2}+\frac{x^5}{20}$。</p>
<p>$\varphi_3(x)=\displaystyle\int_0^x\left[\xi+\left(\frac{\xi^2}{2}+\frac{\xi^5}{20}\right)^2\right]d\xi$。展开平方：$\dfrac{\xi^4}{4}+\dfrac{\xi^7}{20}+\dfrac{\xi^{10}}{400}$。积分：</p>
<div class="formula">$$\varphi_3(x)=\frac{x^2}{2}+\frac{x^5}{20}+\frac{x^8}{160}+\frac{x^{11}}{4400}$$</div>
<p>（和课件复习题给的结果一致。）</p>
<p>数值检查：$x=0.5$ 时 $\varphi_3=0.125+0.5^5/20+0.5^8/160+0.5^{11}/4400=0.125+0.0015625+0.0000244+0.0000001\approx0.1266$。真解可以用第 10 章的 Euler 法粗估：$h=0.1$ 时几步之后约 0.13，量级对得上。</p>
<p>注意这三项是逐次增加的（每多一项，近似更精确），这正是 Picard 序列单调逼近的样子。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">本章要点</div>① Lipschitz 条件 = 斜率对 $y$ 有上界；② 定理给的是<strong>局部</strong>存在唯一（$|x-x_0|\le h$，$h=\min(a,b/M)$）；③ 证明靠 Picard 迭代 + 一致收敛 + Gronwall；④ 偏导有界 → Lipschitz → 唯一；⑤ 隐式方程需要 $F_p\ne0$。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">$f(x,y)=\sqrt{|y|}$ 在 $y=0$ 附近满足 Lipschitz 吗？<br>答：不满足。取 $y_1=0$，$y_2=\epsilon$，则 $|\sqrt\epsilon-0|/\epsilon=1/\sqrt\epsilon\to\infty$。所以 $y'=\sqrt{|y|},y(0)=0$ 的解不唯一。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">为什么 $h$ 不能取 $a$ 和 $b/M$ 中较大的？<br>答：取较大值就保证不了解曲线不冲出上下边界。$b/M$ 是"以最大斜率冲刺，冲出 $y$ 方向边界所需的距离"，超过它就可能在 $R$ 内找不到 $f$ 的定义。</div></div>
<div class="qa-item"><div class="qa-q">思考题 3</div><div class="qa-a">Picard 迭代为什么不直接取极限，而要证一致收敛？<br>答：极限要能搬进积分号（$\lim\int=\int\lim$），这一步需要一致收敛。只是逐点收敛不够。</div></div>

<div class="chapter-nav"></div>
</section>
'''

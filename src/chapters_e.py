CH_E = r"""
<!-- ========== 第 8 章：解的延拓与初值依赖性 ========== -->
<section class="chapter" id="extension" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">8</span>解的延拓与初值依赖性</h2>
<p class="lead">第 7 章只在 $|x-x_0|\le h$ 的小区间上保证了存在唯一。这一章把解往两边接出去，直到接不动为止；再讨论初值稍有偏差时解会怎么变。对应课件 chapter3-2。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：接力赛</div>第 7 章给的是一段"能保证的跑道"。到了段末，把那里当新起点，再造一小段能保证的跑道，接上去。一段一段接，直到撞墙（跑出区域或跑到无穷）为止。这条接起来的最长跑道叫"饱和解"，撞墙的位置就是最大存在区间的端点。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 7 章的定理、$h=\min(a,b/M)$、Gronwall 不等式。</div>

<h3>8.1 局部解的局限</h3>
<p>第 7 章的 $h$ 依赖矩形 $R$ 的大小。区域放大，$M$ 变大，$h$ 反而变小（见 7.10 节的例子）。所以定理给的区间往往很短，实际解却可能延伸到很远。例：$y'=x^2+y^2$ 的解在 $\mathbb{R}$ 上其实存在，但定理只保证 $|x|\le1/4$。</p>

<h3>8.2 延拓怎么做</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">在右端点取新起点</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>第 7 章解出 $\varphi$ 在 $[x_0-h,x_0+h]$ 上。取 $x_1=x_0+h$，$y_1=\varphi(x_1)$。以 $(x_1,y_1)$ 为中心重新作一个小矩形 $R_1$，其中 $f$ 仍有定义、连续、满足局部 Lipschitz。再套定理，得到在 $[x_1-h_1,x_1+h_1]$ 上的解 $\varphi_1$。</p>
<p>因为 $R_1$ 与 $R$ 有重叠，重叠区域内两个解都满足同一个初值问题，由唯一性它们相等。所以可以拼起来：</p>
<div class="formula">$$\Phi(x)=\begin{cases}\varphi(x),& x\in[x_0-h,x_1]\\ \varphi_1(x),& x\in[x_1,x_1+h_1]\end{cases}$$</div>
<p>定义域延长到 $[x_0-h,\ x_0+h+h_1]$。左端同理向左接。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">一直接下去，得到饱和解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>重复这个过程。定义域不断扩大的解叫<strong>延拓</strong>；不能再延拓的解叫<strong>饱和解</strong>（极大延拓解）。一个饱和解的定义区间叫<strong>最大存在区间</strong>，记作 $(\alpha,\beta)$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">最大存在区间必是开区间</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>假设最大存在区间是闭的 $[\alpha,\beta]$ 且 $\beta&lt;\infty$。那么在 $\beta$ 处解有值 $\varphi(\beta)$。以 $(\beta,\varphi(\beta))$ 为中心再作小矩形，定理又给一段向右的延拓，与"已到最大"矛盾。</p>
<p>所以右端点不能取到，区间是开的：$(\alpha,\beta)$。端点处解要么跑到无穷，要么跑到区域边界，$x$ 不能取到端点。</p>
</div></div>
</div>

<h3>8.3 延拓定理</h3>
<div class="callout callout-key"><div class="callout-title">定理 3.2（延拓定理）</div>设 $f(x,y)$ 在有界区域 $G$ 内连续，且关于 $y$ 满足局部 Lipschitz 条件（每一点附近都有一个 $L$，不必全局统一）。则过 $G$ 内任一点 $(x_0,y_0)$ 的解可以延拓到任意接近 $G$ 的边界。如果只能延拓到 $[x_0,d)$（$d$ 有限），那么当 $x\to d^-$ 时，点 $(x,\varphi(x))$ 趋于 $G$ 的边界。
</div>
<p>"局部 Lipschitz"是比第 7 章更弱的条件：每个点附近有一个 Lipschitz 常数，不同点可以不同。因为延拓是一小段一小段做的，每段只需要本段的 Lipschitz 条件，所以局部版就够。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推论</span><span class="derive-step-title">区域无界时的两种结局</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>若 $G$ 无界（比如整个条带或整个平面），则解或者可以延拓到 $[x_0,+\infty)$，或者只能到 $[x_0,d)$，且 $x\to d^-$ 时 $y=\varphi(x)$ 无界、或趋于 $G$ 的边界。</p>
<p>举例：$y'=y^2$ 的解 $y=1/(1-x)$ 只能到 $d=1$，此时 $y\to+\infty$，属于"无界"这一种。$y'=y$ 的解 $y=e^x$ 可以到 $+\infty$，属于第一种。</p>
</div></div>
</div>

<h3>8.4 例：$\dfrac{dy}{dx}=\dfrac{y^2-1}{2}$ 的两个初值</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">先求通解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>分离变量：$\dfrac{2dy}{y^2-1}=dx$。左边拆成部分分式：$\dfrac{2}{y^2-1}=\dfrac{1}{y-1}-\dfrac{1}{y+1}$。积分：</p>
<div class="formula">$$\ln|y-1|-\ln|y+1|=x+C \;\Rightarrow\; \left|\frac{y-1}{y+1}\right|=Ke^{x}$$</div>
<p>去掉绝对值：$\dfrac{y-1}{y+1}=Ce^x$（$C$ 可正可负）。解出 $y$：</p>
<div class="formula">$$y-1=C e^x(y+1)\;\Rightarrow\; y(1-Ce^x)=1+Ce^x\;\Rightarrow\; y=\frac{1+Ce^x}{1-Ce^x}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">过 $(0,0)$ 的解：$C=-1$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$0=\dfrac{1+C}{1-C}$ 得 $C=-1$。代入：</p>
<div class="formula">$$y=\frac{1-e^x}{1+e^x}$$</div>
<p>分母 $1+e^x$ 恒正，不会为零。分子分母都有限。所以解在 $(-\infty,+\infty)$ 上都有定义。</p>
<p>数值感觉：$x\to+\infty$ 时 $y\to-1$；$x\to-\infty$ 时 $y\to1$。解从 $1$ 单调下降穿到 $-1$，两端分别贴着 $y=\pm1$（这两个是平衡解，$y'=0$）。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">过 $(\ln2,-3)$ 的解：存在区间 $(0,+\infty)$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>代入：$-3=\dfrac{1+Ce^{\ln2}}{1-Ce^{\ln2}}=\dfrac{1+2C}{1-2C}$。解方程：$-3+6C=1+2C$，$4C=4$，$C=1$。所以</p>
<div class="formula">$$y=\frac{1+e^x}{1-e^x}$$</div>
<p>分母 $1-e^x$ 在 $x=0$ 处为零。初值点在 $x=\ln2&gt;0$，解只能在 $x&gt;0$ 这一侧：区间 $(0,+\infty)$。当 $x\to0^+$ 时 $y\to-\infty$（分母从负侧趋于 0），跑到无穷，符合"只能延拓到 $d=0$ 且 $y$ 无界"。</p>
<p>注意这个解不能跨过 $x=0$ 接到 $x&lt;0$ 那一支，因为 $x=0$ 处解没定义。</p>
</div></div>
</div>

<h3>8.5 解对初值的连续性</h3>
<p>把解写成依赖初值的形式：$y=\varphi(x,x_0,y_0)$。也就是同一个方程，初值不同给出不同的解曲线。</p>
<div class="callout callout-key"><div class="callout-title">定理 3.3（连续性）</div>若 $f(x,y)$ 在区域 $G$ 内连续且关于 $y$ 满足局部 Lipschitz 条件，则解 $\varphi(x,x_0,y_0)$ 作为 $(x,x_0,y_0)$ 的函数是连续的。
</div>
<p>含义：初值只移动一点点，解整条曲线也只移动一点点（在有限的 $x$ 范围内）。这是数值计算可行的根据——数值方法引入的微小初值误差不会突然放大成灾难。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">估</span><span class="derive-step-title">误差的 Gronwall 估计</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $\varphi,\psi$ 是同一方程、初值相差 $\delta$ 的两个解。作差并积分：</p>
<div class="formula">$$|\varphi(x)-\psi(x)|\le\delta+L\left|\int_{x_0}^{x}|\varphi-\psi|d\xi\right|$$</div>
<p>由 Gronwall：</p>
<div class="formula">$$|\varphi(x)-\psi(x)|\le\delta\,e^{L|x-x_0|}$$</div>
<p>所以误差最多按指数增长，系数是 $L$ 和区间长度。区间短、$L$ 小，误差就小。这也解释了为什么"长期预测"很难：$e^{L|x-x_0|}$ 会变大。</p>
</div></div>
</div>

<h3>8.6 解对初值的可微性</h3>
<div class="callout callout-key"><div class="callout-title">定理 3.4（可微性）</div>若 $f$ 与 $\dfrac{\partial f}{\partial y}$ 在 $G$ 内都连续，则解 $\varphi(x,x_0,y_0)$ 对 $x_0,y_0$ 有连续偏导数，且<div class="formula">$$\frac{\partial\varphi}{\partial y_0}=\exp\left(\int_{x_0}^{x}\frac{\partial f}{\partial y}\left(\xi,\varphi(\xi,x_0,y_0)\right)d\xi\right)$$</div><div class="formula">$$\frac{\partial\varphi}{\partial x_0}=-f(x_0,y_0)\cdot\exp\left(\int_{x_0}^{x}\frac{\partial f}{\partial y}d\xi\right)$$</div>
</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">$\dfrac{\partial\varphi}{\partial y_0}$ 怎么来的</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>记 $v=\dfrac{\partial\varphi}{\partial y_0}$。对积分方程 $y=y_0+\displaystyle\int_{x_0}^xf(\xi,y)d\xi$ 两边对 $y_0$ 求偏导（把 $y$ 当 $y_0$ 的函数，链式法则）：</p>
<div class="formula">$$v=1+\int_{x_0}^{x}f_y(\xi,\varphi)\cdot v\,d\xi$$</div>
<p>这是关于 $v$ 的线性积分方程。对 $x$ 求导得 $\dfrac{dv}{dx}=f_y(x,\varphi)v$，$v(x_0)=1$（在 $x=x_0$ 处右边积分为 0）。解这个一阶线性方程：</p>
<div class="formula">$$v=\exp\left(\int_{x_0}^{x}f_y d\xi\right)$$</div>
<p>指数上的 $\displaystyle\int f_y$ 是"沿解曲线累计的斜率敏感度"。$f_y$ 越大，初值误差放大越快。</p>
<p>$\dfrac{\partial\varphi}{\partial x_0}$ 的公式用同一个 $v$ 乘上 $-f(x_0,y_0)$，来源是"改变起点相当于同时改变初值和时间"，两个效应叠加。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">本章要点</div>① 延拓靠"端点接力"，重叠区域由唯一性保证拼接合法；② 最大存在区间是开区间，端点处解跑向无穷或边界；③ 无界区域上解要么到 $+\infty$ 要么在有限处爆掉；④ 初值微变，解微变，误差按 $e^{L|x-x_0|}$ 增长；⑤ 可微时，$\partial\varphi/\partial y_0=e^{\int f_y}$。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">$y'=\dfrac{1}{1-x^2}$，$y(0)=0$ 的最大存在区间是什么？<br>答：解 $y=\dfrac12\ln\dfrac{1+x}{1-x}$（积分 $\frac{1}{1-x^2}=\frac12(\frac{1}{1+x}+\frac{1}{1-x})$）。在 $x=\pm1$ 处对数发散，所以区间是 $(-1,1)$。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">为什么最大存在区间不能是半开 $[\alpha,\beta)$？<br>答：左端点如果取到，那里解有值，可以向左再延拓一小段，说明不是最大。所以两端都取不到。</div></div>

<div class="chapter-nav"></div>
</section>

<!-- ========== 第 9 章：奇解 ========== -->
<section class="chapter" id="singular" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">9</span>奇解</h2>
<p class="lead">有些方程除了通解之外，还有一条"额外"的解，它在每一点上都与通解族里某条曲线相切，这条曲线叫奇解，也叫通解族的包络。这一章讲怎么找它。对应课件 chapter3-3。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：两条曲线相切</div>一堆同心圆（通解族），外面再套一个和它们都相切的大圆？不行，同心圆没有公共切线族。真正会出现包络的是"直线族"：一族斜率不同的直线，它们的边界常常围出一条曲线，每条直线都和这条曲线相切。这条曲线就是包络，对应"奇解"。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 6 章例 3（$y=x^2/4$ 的出现）；第 7 章隐式存在唯一性定理（$F_p\ne0$ 保证唯一）。</div>

<h3>9.1 包络的定义</h3>
<p>单参数曲线族 $\Phi(x,y;c)=0$（$c$ 是参数）的<strong>包络</strong>是这样一条曲线：</p>
<p>① 它不属于这个族（不是某个 $c$ 对应的那条）；② 它上面每一点，族中至少有一条曲线经过该点，且在该点与包络<strong>相切</strong>。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">圆族 $(x-c)^2+y^2=R^2$ 的包络是 $y=\pm R$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>固定 $R$，让圆心在 $x$ 轴上移动，得到一族半径相同的圆。所有圆都被夹在 $y=R$ 和 $y=-R$ 两条平行线之间。</p>
<p>取 $y=R$ 上任一点 $(x_0,R)$。族中哪个圆经过它？要求 $(x_0-c)^2+R^2=R^2$，即 $c=x_0$。正好有一个圆，圆心在 $(x_0,0)$，它在 $(x_0,R)$ 处的切线是水平的（圆的最上端），与直线 $y=R$ 平行。所以 $y=R$ 与每一点处的那个圆相切。</p>
<p>同理 $y=-R$。</p>
<p>$y=R$ 不是族中任何一条曲线（它是直线，族里全是圆），满足条件 ①；每点有族中曲线相切，满足 ②。所以是包络。</p>
</div></div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">反例</span><span class="derive-step-title">同心圆族、平行直线族没有包络</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>同心圆族 $x^2+y^2=r^2$：任意一条曲线（圆）都整条包在另一条里，没有公共切线。平行直线族 $y=x+c$：互不相交，没有切点。都无包络。</p>
</div></div>
</div>

<h3>9.2 $c$-判别式：包络一定满足的方程</h3>
<div class="callout callout-key"><div class="callout-title">结论</div>包络一定包含在由<div class="formula">$$\Phi(x,y,c)=0,\qquad \Phi_c(x,y,c)=0 \tag{3.20}$$</div>消去 $c$ 所得的曲线里。这条曲线叫 <strong>$c$-判别曲线</strong>。
</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推导</span><span class="derive-step-title">为什么对 $c$ 求偏导等于 0</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设包络的参数方程是 $L:\ x=\varphi(t),\ y=\psi(t)$。$L$ 上每一点 $(x,y)$ 对应族中一条曲线，其参数记作 $c=c(t)$。所以沿 $L$ 恒有</p>
<div class="formula">$$\Phi(\varphi(t),\psi(t),c(t))\equiv0$$</div>
<p>两边对 $t$ 求导，用链式法则：</p>
<div class="formula">$$\frac{\partial\Phi}{\partial x}\varphi'(t)+\frac{\partial\Phi}{\partial y}\psi'(t)+\frac{\partial\Phi}{\partial c}c'(t)=0 \tag{A}$$</div>
<p>另一方面，包络与族曲线在这一点相切，意思是它们的切线方向相同。族曲线在该点的法向量是 $\left(\dfrac{\partial\Phi}{\partial x},\dfrac{\partial\Phi}{\partial y}\right)$，切向量与它垂直，所以</p>
<div class="formula">$$\frac{\partial\Phi}{\partial x}\varphi'(t)+\frac{\partial\Phi}{\partial y}\psi'(t)=0 \tag{B}$$</div>
<p>（切向量 $(\varphi',\psi')$ 与法向量 $(Φ_x,Φ_y)$ 的内积为 0。）</p>
<p>(A) 减 (B)，剩下</p>
<div class="formula">$$\frac{\partial\Phi}{\partial c}c'(t)=0$$</div>
<p>只要包络不是"$c$ 恒为常数"的退化情形（那样 $L$ 就是族中一条曲线，不叫包络），必有 $c'(t)\ne0$，于是 $\Phi_c=0$。</p>
<p>所以包络上的点同时满足 $\Phi=0$ 和 $\Phi_c=0$。</p>
</div></div>
</div>
<p><strong>注意方向：</strong>包络 ⊂ $c$-判别曲线，不是相等。$c$-判别曲线里可能混有"非包络"的东西（比如族曲线的重点、自交点轨迹），必须逐条检验。</p>

<h3>9.3 例：直线族 $x\cos\alpha+y\sin\alpha-p=0$ 的包络</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">对参数 $\alpha$ 求偏导</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>族：$x\cos\alpha+y\sin\alpha-p=0$（$p&gt;0$ 固定，$\alpha$ 是参数，表示法向量方向）。</p>
<p>对 $\alpha$ 求偏导：</p>
<div class="formula">$$-x\sin\alpha+y\cos\alpha=0 \tag{3.22}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">两式平方相加，消掉 $\alpha$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>由原式移项：$x\cos\alpha+y\sin\alpha=p$，两边平方：</p>
<div class="formula">$$x^2\cos^2\alpha+y^2\sin^2\alpha+2xy\cos\alpha\sin\alpha=p^2 \tag{3.23}$$</div>
<p>由 (3.22) 平方：$x^2\sin^2\alpha+y^2\cos^2\alpha-2xy\cos\alpha\sin\alpha=0 \tag{3.24}$</p>
<p>(3.23)+(3.24)：交叉项 $2xy\cos\alpha\sin\alpha$ 一正一负抵消，$\cos^2+\sin^2=1$：</p>
<div class="formula">$$x^2(\cos^2\alpha+\sin^2\alpha)+y^2(\sin^2\alpha+\cos^2\alpha)=p^2 \;\Rightarrow\; x^2+y^2=p^2 \tag{3.25}$$</div>
<p>得到半径为 $p$ 的圆。这就是包络：一族与原点距离为 $p$ 的直线（所有切线），包络是圆。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">检验它确实是包络</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>圆上取一点 $(p\cos\theta,p\sin\theta)$。它到直线 $x\cos\alpha+y\sin\alpha=p$ 的距离是 $p\cos\theta\cos\alpha+p\sin\theta\sin\alpha-p=p\cos(\theta-\alpha)-p$。令 $\alpha=\theta$ 时距离为 0，说明这条直线经过该点。且该直线的法向量是 $(\cos\theta,\sin\theta)$，正是圆的径向，所以直线是圆的切线。每点都对上，确认是包络。</p>
</div></div>
</div>

<h3>9.4 奇解的定义</h3>
<div class="callout callout-key"><div class="callout-title">定义</div>方程的一个解，如果它上面<strong>每一点</strong>都至少还有方程的另一个解经过，即每一点的唯一性都不成立，就叫<strong>奇解</strong>。
</div>
<p>"每一点唯一性都不成立"是关键。普通解上也可能有个别点唯一性失效（比如解曲线与另一条解曲线相交的点），但不会"处处失效"。奇解要求整条解上都这样。</p>

<h3>9.5 通解包络 ↔ 奇解</h3>
<div class="callout callout-key"><div class="callout-title">定理</div>如果通解族有包络，包络一定是奇解；反之，奇解一定是通解族的包络。
</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">包络 → 奇解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>包络上每点与族中一条曲线相切。相切意味着在这点附近，包络与那条族曲线有相同的切线、相同的一阶导数。而族曲线是方程的解，所以包络在该点的 $y'$ 与族曲线的 $y'$ 相同，代进方程也成立。</p>
<p>又包络本身不在族中，是一条独立的解。所以经过包络上每一点，至少有两条解（包络自己 + 相切的那条族曲线），唯一性处处失效，是奇解。</p>
</div></div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">奇解 → 包络</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>奇解上每点 $(x_0,y_0)$ 还有另一条解 $\psi$ 经过，且在该点 $y'$ 相同（都满足同一个方程）。所以两条曲线在该点相切。</p>
<p>只要证明"经过每点的另一条解可以选成通解族里的曲线"，就说明奇解是通解族的包络。这一步需要通解的稠密性（在给定初值附近通解能取到任意接近的解），一般教材作为已知结论使用，本课不展开。</p>
</div></div>
</div>

<h3>9.6 $p$-判别式：奇解必须满足 $F_p=0$</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">从隐式存在唯一性定理来</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>方程 $F(x,y,p)=0$（$p=y'$）。第 7 章说过：若 $F_p\ne0$，则能局部解出唯一的 $p=f(x,y)$，再套 Picard 定理，得到唯一的解。</p>
<p>所以"唯一性失效"的地方必须有 $F_p=0$。奇解处处唯一性失效，所以奇解上处处 $F_p=0$。</p>
<p>加上奇解本身满足 $F=0$，得到：奇解包含在</p>
<div class="formula">$$F(x,y,p)=0,\qquad F_p(x,y,p)=0 \tag{3.31}$$</div>
<p>消去 $p$ 所得的曲线里。这条曲线叫 <strong>$p$-判别曲线</strong>。</p>
</div></div>
</div>

<h3>9.7 例：$(y')^2+y^2-1=0$ 的两条奇解</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">$p$-判别法</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$F=p^2+y^2-1$。$F_p=2p$。令 $F_p=0$ 得 $p=0$，代回 $F=0$：$0+y^2-1=0$，$y=\pm1$。</p>
<p>候选曲线是两条水平直线 $y=1$ 和 $y=-1$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">验证它们是解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$y=1$：$y'=0$，代进方程 $0+1-1=0$ ✓。$y=-1$ 同理 ✓。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">求通解，验证相切</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>原方程 $y'=\pm\sqrt{1-y^2}$。分离变量：$\dfrac{dy}{\sqrt{1-y^2}}=\pm dx$，积分 $\arcsin y=\pm x+c$，即</p>
<div class="formula">$$y=\sin(x+c)$$</div>
<p>这是一族振幅为 1 的正弦曲线。它们的最高点是 $y=1$，最低点 $y=-1$，在这些点上切线水平，正好与 $y=\pm1$ 相切。</p>
<p>每一点 $(x,1)$ 都在某条正弦曲线的峰上：取 $c$ 使 $x+c=\frac\pi2+2k\pi$ 即可。所以 $y=1$ 与族中曲线处处相切，是包络，也是奇解。$y=-1$ 同理。</p>
</div></div>
</div>

<h3>9.8 判别曲线不是解的两种情况</h3>
<p>$p$-判别曲线或 $c$-判别曲线只是"候选"，必须检验两件事：它是不是解；它上面的唯一性是否真的失效。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例①</span><span class="derive-step-title">候选曲线根本不是解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$(y')^2+y^2+1=0$ 没有实函数解（左边恒 $\ge1$）。$p$-判别：$2p=0\Rightarrow p=0$，代回得 $y^2+1=0$，无实点。候选集为空，自然没有奇解。</p>
</div></div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例②</span><span class="derive-step-title">候选曲线是解，但不是奇解（是"结点"轨迹）</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$y=xp-p^2$（这是 $y=xy'-y'^2$）。$F=xp-p^2-y=0$，$F_p=x-2p=0\Rightarrow p=x/2$，代回：$y=\dfrac{x^2}{2}-\dfrac{x^2}{4}=\dfrac{x^2}{4}$。这是第 6 章的例 3，确实是奇解（与通解每条相切）。</p>
<p>但换成 $x=p^2$ 情形（即 $(y')^2-x=0$）：$p$-判别给 $2p=0\Rightarrow p=0$，$x=0$，即 $y$ 轴。它不满足原方程（$x=0$ 时 $p$ 只能取 0，但 $x=0$ 是竖直线，不能写成 $y(x)$），所以不是解。</p>
<p>结论：判别完必须代回原方程验证，再看唯一性。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">找奇解的两条路</div>① <strong>$p$-判别法</strong>：由 $F(x,y,p)=0$ 与 $F_p=0$ 消 $p$ 得候选曲线，检验是否为解、是否处处唯一性失效。② <strong>$c$-判别法</strong>：先求通解 $\Phi(x,y,c)=0$，再由 $\Phi=0$ 与 $\Phi_c=0$ 消 $c$ 得候选曲线，同样检验。两条路得到的结果应当一致。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">求 $y=xp+p^2$ 的奇解。<br>答：$F=xp+p^2-y=0$，$F_p=x+2p=0\Rightarrow p=-x/2$，代回 $y=-\dfrac{x^2}{2}+\dfrac{x^2}{4}=-\dfrac{x^2}{4}$。验证：它是解（$y'=-\frac x2$，右边 $x(-\frac x2)+\frac{x^2}{4}=-\frac{x^2}{2}+\frac{x^2}{4}=-\frac{x^2}{4}$ ✓），且通解为直线族 $y=cx+c^2$，与抛物线 $y=-x^2/4$ 相切于一点（判别式为零）。是奇解。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">为什么 $c$-判别曲线可能包含非包络的曲线？<br>答：推导中用了"$c'(t)\ne0$"这个条件。如果族曲线本身有奇点（比如所有曲线都经过一个固定点），在该点可能 $c'=0$，得到的是轨迹而不是包络。另外 $c$-判别也可能给出族的自交线，那不是包络。所以必须检验相切性。</div></div>

<div class="chapter-nav"></div>
</section>

<!-- ========== 第 10 章：数值解 ========== -->
<section class="chapter" id="numeric" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">10</span>数值解</h2>
<p class="lead">大多数方程解不出初等函数。这一章讲怎么用计算机一步步逼近解，以及误差有多大。对应课件 chapter3-4。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：沿方向场一小步一小步走</div>知道起点和每点的方向（斜率），就以当前位置为起点，沿当前斜率走一小步；到新位置重新读斜率，再走一步。步长越小，折线越贴近真实曲线。这就是 Euler 法的全部内容。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 1 章的 Taylor 展开；第 7 章的 Gronwall 不等式；第 2 章的方向场。</div>

<h3>10.1 为什么需要数值解</h3>
<p>第 3-6 章的五种解法只覆盖"能分离、能凑全微分、能换元"的一小类方程。像 $y'=e^{-x^2}$、$y'=\sin(xy)$ 这类，解存在（第 7 章保证了），但写不成初等函数。这时只能算数值。</p>

<h3>10.2 离散化与 Euler 公式</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">取一串节点，步长 $h$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>在区间上取节点 $x_0&lt;x_1&lt;x_2&lt;\cdots&lt;x_n&lt;x_{n+1}&lt;\cdots$，通常等步长 $h=x_{i+1}-x_i$。记 $y_i\approx y(x_i)$：$y_i$ 是数值近似，$y(x_i)$ 是真解在该点的值。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">把微分方程写成积分形式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>从 $x_n$ 积到 $x_{n+1}$：</p>
<div class="formula">$$y(x_{n+1})=y(x_n)+\int_{x_n}^{x_{n+1}}f(x,y(x))\,dx$$</div>
<p>这一步是恒等变形（牛顿-莱布尼茨公式）。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">用左矩形近似积分</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>积分是曲线下的面积。用"宽 $h$、高 $f(x_n,y(x_n))$"的矩形代替，面积 $h f(x_n,y(x_n))$。代进去，把真解换成数值解：</p>
<div class="formula">$$y_{n+1}=y_n+h f(x_n,y_n) \tag{Euler}$$</div>
<p>这就是 <strong>Euler 公式</strong>（显式 Euler、向前 Euler）。</p>
</div></div>
</div>
<div class="callout callout-tip"><div class="callout-title">几何读法</div>从 $(x_n,y_n)$ 出发，以该点方向场给的斜率 $f(x_n,y_n)$ 画一段长为 $h$ 的直线，终点就是 $(x_{n+1},y_{n+1})$。一步步连起来是一条折线。</div>

<h3>10.3 单步截断误差</h3>
<p>一步走完后，真实解和数值解差多少（假设这一步开始时两者完全相等）？这叫<strong>局部截断误差</strong>。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">真解 Taylor 展开，与 Euler 公式对比</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>真解在 $x_n$ 处展开（$h=x_{n+1}-x_n$）：</p>
<div class="formula">$$y(x_{n+1})=y(x_n)+hy'(x_n)+\frac{h^2}{2}y''(x_n)+\frac{h^3}{6}y'''(x_n)+\cdots$$</div>
<p>Euler 公式用的 $f(x_n,y_n)$ 当 $y_n=y(x_n)$ 时就是 $y'(x_n)$。所以两者之差是</p>
<div class="formula">$$R(x_n,h)=y(x_{n+1})-y(x_n)-hf(x_n,y(x_n))=\frac{h^2}{2}y''(x_n)+O(h^3)$$</div>
<p>首项 $h^2$ 量级，记作 $R=O(h^2)$。这说"局部误差是 $h$ 的二阶小量"，等价地说"Euler 法是 1 阶方法"。</p>
<p>数值感觉：$h=0.1$ 时 $h^2/2=0.005$，若 $y''\approx1$，一步就偏 0.005；$h$ 减半到 0.05，一步偏 0.00125，缩小 4 倍。</p>
</div></div>
</div>

<h3>10.4 整体截断误差：阶数掉一阶</h3>
<div class="callout callout-key"><div class="callout-title">定理 3.5</div>若单步法有 $p+1$ 阶局部截断误差（$R=O(h^{p+1})$），$f$ 关于 $y$ 满足 Lipschitz 条件（常数 $L$），且初值精确，则在有限区间 $[x_0,T]$ 上整体误差<div class="formula">$$y(x_n)-y_n=O(h^p)$$</div>局部 $p+1$ 阶，整体只有 $p$ 阶。
</div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">误差递推，再用 Gronwall 的离散版</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>记 $\varepsilon_n=y(x_n)-y_n$。把真解与数值解都写成积分形式，相减：</p>
<div class="formula">$$\varepsilon_{n+1}=\varepsilon_n+\int_{x_n}^{x_{n+1}}\left[f(x,y(x))-f(x_n,y_n)\right]dx+R(x_n,h)$$</div>
<p>拆开被积函数，插入一项 $f(x_n,y(x_n))$：</p>
<div class="formula">$$f(x,y(x))-f(x_n,y_n)=\underbrace{f(x,y(x))-f(x_n,y(x_n))}_{\text{积分内随 }x\text{ 变化}}+\underbrace{f(x_n,y(x_n))-f(x_n,y_n)}_{\text{起点误差}}$$</div>
<p>第一项对 $x$ 积分是 $O(h^2)$（$f$ 连续，随 $x$ 变化有限），记 $M_1h^2$；第二项用 Lipschitz $\le L\varepsilon_n$，乘区间长 $h$ 得 $Lh\varepsilon_n$。</p>
<div class="formula">$$|\varepsilon_{n+1}|\le(1+Lh)|\varepsilon_n|+Mh^{p+1}$$</div>
<p>反复代入展开：</p>
<div class="formula">$$|\varepsilon_n|\le(1+Lh)^n\varepsilon_0+Mh^{p+1}\left[1+(1+Lh)+\cdots+(1+Lh)^{n-1}\right]$$</div>
<p>等比求和：$\displaystyle\sum_{k=0}^{n-1}(1+Lh)^k=\frac{(1+Lh)^n-1}{Lh}$。又 $(1+Lh)^n\le e^{Lnh}\le e^{LT}$（$nh\le T$）。所以</p>
<div class="formula">$$|\varepsilon_n|\le e^{LT}\varepsilon_0+\frac{M}{L}\left(e^{LT}-1\right)h^p$$</div>
<p>$\varepsilon_0=0$，剩下 $O(h^p)$。证完。</p>
<p>证明形状与第 7 章唯一性完全一样：误差被自己的积分控制住 → Gronwall → 有界。区别只在离散版用 $(1+Lh)$ 代替 $e^{Lh}$。</p>
</div></div>
</div>
<div class="callout callout-warn"><div class="callout-title">实践含义</div>1 阶方法（Euler）误差 $O(h)$。要把误差减到 1/10，步长要减到 1/10，计算量增 10 倍。这就是实际计算要用高阶方法的原因。</div>

<h3>10.5 三种改进</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">后退 Euler：用右矩形</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>用右端点的函数值代替左端点：</p>
<div class="formula">$$y_{n+1}=y_n+hf(x_{n+1},y_{n+1})$$</div>
<p>右边含 $y_{n+1}$，是<strong>隐式</strong>公式，每一步要解方程（通常迭代）。局部误差仍是 $O(h^2)$，但稳定性更好。</p>
<p>稳定性直观：$y'=-100y$（急剧衰减）。显式 Euler 取 $h=0.1$ 时 $y_{n+1}=y_n(1-10)=-9y_n$，符号乱跳、绝对值放大，数值解发散；后退 Euler 是 $y_{n+1}=y_n/(1+10)\approx0.09y_n$，正确衰减。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">梯形公式：左右平均</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>用梯形面积代替矩形：</p>
<div class="formula">$$y_{n+1}=y_n+\frac h2\left[f(x_n,y_n)+f(x_{n+1},y_{n+1})\right]$$</div>
<p>局部误差 $O(h^3)$。也是隐式。</p>
<p>阶数提高的来源：左矩形误差 $-\frac{h^2}{2}y''$，右矩形误差 $+\frac{h^2}{2}y''$，一正一负，平均后 $h^2$ 项抵消，剩 $h^3$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">改进 Euler：预测—校正，显式且 $O(h^3)$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>梯形公式隐式，解起来麻烦。办法：先用 Euler 公式算"预测值"$\bar y_{n+1}$，再用它代替梯形公式里的 $y_{n+1}$：</p>
<div class="formula">$$\bar y_{n+1}=y_n+hf(x_n,y_n)\quad(\text{预测})$$</div>
<div class="formula">$$y_{n+1}=y_n+\frac h2\left[f(x_n,y_n)+f(x_{n+1},\bar y_{n+1})\right]\quad(\text{校正})$$</div>
<p>合并写成</p>
<div class="formula">$$y_{n+1}=y_n+\frac h2\left[f(x_n,y_n)+f\left(x_n+h,\ y_n+hf(x_n,y_n)\right)\right]$$</div>
<p>它是显式的，局部误差 $O(h^3)$，与梯形同阶。代价是每步算两次 $f$。</p>
<p>为什么预测的误差不降低阶数：$\bar y_{n+1}-y(x_{n+1})=O(h^2)$，代进 $f$ 后由 Lipschitz 引起的误差是 $L\cdot O(h^2)$，乘 $\frac h2$ 得 $O(h^3)$，与主项同阶。</p>
</div></div>
</div>

<h3>10.6 数值例：$y'=y-\dfrac{2x}{y}$，$y(0)=1$</h3>
<p>有解析解 $y=\sqrt{1+2x}$。验证：$y'=\dfrac{1}{\sqrt{1+2x}}=\dfrac{1}{y}$；右边 $y-\dfrac{2x}{y}=\dfrac{y^2-2x}{y}=\dfrac{1+2x-2x}{y}=\dfrac1y$ ✓。可以精确对比误差。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">手算</span><span class="derive-step-title">Euler 法，$h=0.1$，算三步</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$f(x,y)=y-\dfrac{2x}{y}$。</p>
<p>第 1 步：$x_0=0,y_0=1$，$f=1$，$y_1=1+0.1\cdot1=1.1$。</p>
<p>第 2 步：$x_1=0.1$，$f=1.1-\dfrac{0.2}{1.1}=1.1-0.1818=0.9182$，$y_2=1.1+0.09182=1.19182$。</p>
<p>第 3 步：$x_2=0.2$，$f=1.19182-\dfrac{0.4}{1.19182}=1.19182-0.33562=0.85620$，$y_3=1.19182+0.08562=1.27744$。</p>
<p>精确值：$y(0.1)=\sqrt{1.2}=1.09545$，$y(0.2)=\sqrt{1.4}=1.18322$，$y(0.3)=\sqrt{1.6}=1.26491$。</p>
<p>误差：$+0.00455$、$+0.00860$、$+0.01253$，单调累积。Euler 总是沿起点斜率走，而真解斜率在下降，所以数值解偏高。</p>
</div></div>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">手算</span><span class="derive-step-title">改进 Euler，$h=0.1$，算两步</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>第 1 步：预测 $\bar y_1=1.1$；$f(0.1,1.1)=1.1-\dfrac{0.2}{1.1}=0.91818$；校正</p>
<div class="formula">$$y_1=1+\frac{0.1}{2}(1+0.91818)=1+0.09591=1.09591$$</div>
<p>误差 $+0.00046$，比 Euler 的 $0.00455$ 小约 10 倍。</p>
<p>第 2 步：$f(0.1,1.09591)=1.09591-0.18250=0.91341$；预测 $\bar y_2=1.09591+0.09134=1.18725$；$f(0.2,1.18725)=1.18725-0.33691=0.85034$；校正</p>
<div class="formula">$$y_2=1.09591+\frac{0.1}{2}(0.91341+0.85034)=1.09591+0.08819=1.18410$$</div>
<p>误差 $+0.00088$，同样小一个量级。</p>
</div></div>
</div>
<div class="table-wrap">
<table>
<thead><tr><th>$x$</th><th>精确 $\sqrt{1+2x}$</th><th>Euler $h=0.1$</th><th>误差</th><th>改进 Euler</th><th>误差</th></tr></thead>
<tbody>
<tr><td>0.1</td><td>1.09545</td><td>1.10000</td><td>+0.00455</td><td>1.09591</td><td>+0.00046</td></tr>
<tr><td>0.2</td><td>1.18322</td><td>1.19182</td><td>+0.00860</td><td>1.18410</td><td>+0.00088</td></tr>
<tr><td>0.3</td><td>1.26491</td><td>1.27744</td><td>+0.01253</td><td>—</td><td>—</td></tr>
<tr><td>0.5</td><td>1.41421</td><td>1.43514</td><td>+0.02093</td><td>—</td><td>—</td></tr>
</tbody>
</table>
</div>
<p>规律：Euler 误差随 $x$ 近似线性增大（整体 $O(h)$），改进 Euler 小一个量级（整体 $O(h^2)$）。$h$ 减半，Euler 误差约减半，改进 Euler 约减到 1/4。</p>

<div class="callout callout-key"><div class="callout-title">四种方法一句话</div>Euler：左矩形，显式，整体 $O(h)$；后退 Euler：右矩形，隐式，$O(h)$，稳定；梯形：左右平均，隐式，$O(h^2)$；改进 Euler：预测—校正，显式，$O(h^2)$。局部误差都比整体误差高一阶。
</div>

<div class="qa-item"><div class="qa-q">思考题 1</div><div class="qa-a">$y'=-y$，$y(0)=1$，取 $h=1$ 用 Euler 法算一步，结果合理吗？<br>答：$y_1=1+1\cdot(-1)=0$，精确值 $e^{-1}=0.3679$，误差 0.37。原因：$h=1$ 太大，"斜率沿步长不变"的假设失效（真解斜率从 $-1$ 变到 $-0.37$）。减小 $h$ 可改善。</div></div>
<div class="qa-item"><div class="qa-q">思考题 2</div><div class="qa-a">为什么隐式方法稳定性更好？<br>答：显式 Euler 的放大因子是 $1+h\lambda$（$\lambda=f_y$）。$h\lambda$ 很大且为负时绝对值大于 1，误差放大。隐式 Euler 是 $1/(1-h\lambda)$，$h\lambda\to-\infty$ 时趋于 0，误差衰减。</div></div>
<div class="qa-item"><div class="qa-q">思考题 3</div><div class="qa-a">局部 $O(h^3)$ 的方法，整体为什么是 $O(h^2)$？<br>答：一共走 $T/h$ 步，每步 $O(h^3)$，累加 $O(h^3)\cdot T/h=O(h^2)$。阶数掉一阶是"步数随 $h$ 变小而增加"造成的。</div></div>

<div class="chapter-nav"></div>
</section>

<!-- ========== 第 11 章：知识图谱与自测 ========== -->
<section class="chapter" id="summary" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">11</span>知识图谱与自测</h2>
<p class="lead">把十章内容连成一张图，给出拿到方程时的判断顺序，最后用十道题检验。</p>

<h3>11.1 一条完整的依赖链</h3>
<div class="knowledge-tree">
  <div class="kt-level"><span class="kt-label root">根</span>
    <span class="kt-node root">四则运算</span>
    <span class="kt-node root">不等式</span>
    <span class="kt-node root">函数</span>
  </div>
  <div class="kt-level"><span class="kt-label base">工具</span>
    <span class="kt-node base">导数</span>
    <span class="kt-node base">微分 $dy=y'dx$</span>
    <span class="kt-node base">积分</span>
    <span class="kt-node base">偏导与全微分</span>
    <span class="kt-node base">极限与一致收敛</span>
  </div>
  <div class="kt-level"><span class="kt-label tool">一阶方程</span>
    <span class="kt-node tool" data-goto="separable">分离变量</span>
    <span class="kt-node tool" data-goto="linear">线性方程</span>
    <span class="kt-node tool" data-goto="exact">恰当方程</span>
    <span class="kt-node tool" data-goto="implicit">隐式与参数</span>
  </div>
  <div class="kt-level"><span class="kt-label main">理论</span>
    <span class="kt-node main" data-goto="existence">Lipschitz 与 Picard</span>
    <span class="kt-node main" data-goto="extension">延拓与初值依赖</span>
    <span class="kt-node main" data-goto="singular">奇解与包络</span>
  </div>
  <div class="kt-level"><span class="kt-label base">计算</span>
    <span class="kt-node base" data-goto="numeric">Euler 法</span>
    <span class="kt-node base" data-goto="numeric">误差阶</span>
  </div>
</div>
<p>连线关系一句话：导数定义"斜率"，微分把斜率翻译成"小步长下的位移"，积分是它的逆运算。于是 $y'=f(x,y)$ 可以改写成"$dy=f(x,y)dx$"（分离变量），或"沿曲线的 $f dx-dy$ 之和为 0"（恰当方程）。全部解法的合法性来自"微分形式"这个视角。理论层把"解存在唯一"钉死，计算层在没有解析解时给出近似。</p>

<h3>11.2 解题决策树</h3>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">Q1</span><span class="derive-step-title">$y'$ 能单独解出来吗？</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>能 → 进 Q2。不能（$y'$ 被包在幂、积、三角函数里）→ 第 6 章四种类型：$y$ 能解出来就对 $x$ 求导，$x$ 能解出来就对 $y$ 求导，都不行就参数化。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">Q2</span><span class="derive-step-title">右边能写成 $f(x)\varphi(y)$ 吗？</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>能 → 分离变量（第 3 章）。检查 $\varphi(y)=0$ 的根是否丢解。不能 → Q3。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">Q3</span><span class="derive-step-title">是 $g(y/x)$ 或 $f(ax+by+c)$ 吗？</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>是 → 换元 $u=y/x$ 或 $u=ax+by+c$，化成可分离（第 3 章 3.4、3.5 节）。不是 → Q4。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">Q4</span><span class="derive-step-title">是 $y'=P(x)y+Q(x)$ 吗？</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>是 → 套公式 $y=e^{\int P}\left(\int Qe^{-\int P}+C\right)$（第 4 章）。</p>
<p>是 $P(x)y+Q(x)y^n$（$n\ne0,1$）→ 伯努利，换 $z=y^{1-n}$，化成线性。</p>
<p>都不是 → Q5。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">Q5</span><span class="derive-step-title">写成 $M dx+N dy=0$ 后，$M_y=N_x$ 吗？</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>相等 → 恰当方程，求 $u$ 得 $u=c$（第 5 章）。</p>
<p>不等 → 算 $\dfrac{M_y-N_x}{N}$ 与 $\dfrac{N_x-M_y}{M}$，哪个不含另一个变量就用哪个求 $\mu$，乘上后再走一遍。</p>
<p>两个都含另一个变量 → 可能需要 $\mu(xy)$、$\mu(x\pm y)$ 型的积分因子，本课不展开，或者直接用第 10 章的数值方法。</p>
</div></div>
</div>
<p>解完别忘：① 检查丢解（被除掉的因子为 0 的常数解）；② 代回原方程验证；③ 有初值就定常数；④ 想更精确或没有解析解，用第 10 章方法。</p>

<h3>11.3 自测十题</h3>
<div class="qa-item"><div class="qa-q">1. 判断 $y'=\dfrac{y^2}{x^2+1}$ 的类型，说出首选解法。</div><div class="qa-a">可分离：$\dfrac{dy}{y^2}=\dfrac{dx}{x^2+1}$，积分得 $-\dfrac1y=\arctan x+C$。另外 $y=0$ 是解。</div></div>
<div class="qa-item"><div class="qa-q">2. 解 $y'-2xy=x$。</div><div class="qa-a">线性，$P=-2x,Q=x$。$\int P=-x^2$，$y=e^{x^2}\left(\int xe^{-x^2}dx+C\right)=e^{x^2}\left(-\frac12e^{-x^2}+C\right)=Ce^{x^2}-\frac12$。</div></div>
<div class="qa-item"><div class="qa-q">3. 解 $y'=\dfrac{x+y}{x}$。</div><div class="qa-a">$=1+\dfrac yx$，齐次型。设 $u=y/x$，$u'=\dfrac{1+u-u}{x}=\dfrac1x$，$u=\ln|x|+C$，$y=x(\ln|x|+C)$。</div></div>
<div class="qa-item"><div class="qa-q">4. 解 $(2xy+y^2)dx+(x^2+2xy)dy=0$。</div><div class="qa-a">$M_y=2x+2y=N_x$，恰当。$u=\int_0^x 0\,dx+\int_0^y(x^2+2xy)dy=x^2y+xy^2$。通解 $x^2y+xy^2=c$，即 $xy(x+y)=c$。</div></div>
<div class="qa-item"><div class="qa-q">5. 解 $y=xp+p^2$，指出奇解。</div><div class="qa-a">对 $x$ 求导：$p=p+xp'+2pp'$，即 $(x+2p)p'=0$。$p'=0$ 给 $p=c$，通解 $y=cx+c^2$（直线族）。$x+2p=0$ 给 $p=-x/2$，$y=-\dfrac{x^2}{2}+\dfrac{x^2}{4}=-\dfrac{x^2}{4}$，与每条直线相切，是奇解。</div></div>
<div class="qa-item"><div class="qa-q">6. $y'=\sqrt{y}$，$y(0)=0$ 的解唯一吗？为什么？</div><div class="qa-a">不唯一。$y\equiv0$ 与 $y=x^2/4$（$x\ge0$）都是解。$\sqrt y$ 在 $y=0$ 处不满足 Lipschitz 条件，Picard 定理不适用。</div></div>
<div class="qa-item"><div class="qa-q">7. 说出 $h=\min(a,b/M)$ 里每个量的含义。</div><div class="qa-a">$a$：矩形左右半宽；$b$：上下半高；$M$：矩形内 $|f|$ 的最大值，即最大斜率。$b/M$ 是以最大斜率冲出上下边界所需的横向距离。取小者保证解曲线留在矩形内。</div></div>
<div class="qa-item"><div class="qa-q">8. $y'=y^2$，$y(0)=1$ 的最大存在区间？</div><div class="qa-a">$y=\dfrac{1}{1-x}$，分母在 $x=1$ 为零，区间 $(-\infty,1)$。$x\to1^-$ 时 $y\to+\infty$，属于"只能延拓到有限点且解无界"。</div></div>
<div class="qa-item"><div class="qa-q">9. Euler 法的局部截断误差与整体误差各是什么阶？为什么不同？</div><div class="qa-a">局部 $O(h^2)$，整体 $O(h)$。步数 $T/h$，每步 $O(h^2)$，累加得 $O(h)$。</div></div>
<div class="qa-item"><div class="qa-q">10. 为什么"包络一定是奇解"？</div><div class="qa-a">包络上每点与族中一条曲线相切，切线相同则 $y'$ 相同，代进方程也成立，所以包络本身是解；每点都有一条族曲线经过并相切，该点至少两个解，唯一性处处失效，符合奇解定义。</div></div>

<h3>11.4 常见错误清单</h3>
<div class="table-wrap">
<table>
<thead><tr><th>错误</th><th>后果</th><th>正确做法</th></tr></thead>
<tbody>
<tr><td>分离变量除以 $\varphi(y)$ 不检查零点</td><td>丢常数解</td><td>解完看 $\varphi(y)=0$ 的根是否也是解</td></tr>
<tr><td>$\ln|y|$ 写成 $\ln y$</td><td>$y&lt;0$ 的解丢掉</td><td>保留绝对值，后面用 $\pm$ 吸收</td></tr>
<tr><td>积分因子符号记反</td><td>$\mu$ 算错，仍不恰当</td><td>只与 $x$ 有关：分子 $M_y-N_x$、分母 $N$；只与 $y$ 有关：分子 $N_x-M_y$、分母 $M$</td></tr>
<tr><td>伯努利换元漏掉系数 $1/(1-n)$</td><td>方程系数错</td><td>$z'=(1-n)y^{-n}y'$，两边除以 $(1-n)$</td></tr>
<tr><td>隐式方程对 $y$ 求导写 $\dfrac{dx}{dy}=p$</td><td>应为 $1/p$，全错</td><td>$\dfrac{dx}{dy}=1/p$</td></tr>
<tr><td>把 $p$-判别曲线直接当奇解</td><td>可能不是解</td><td>代回原方程验证，再检验相切性</td></tr>
<tr><td>Euler 法步长过大</td><td>误差巨大甚至发散</td><td>减小 $h$，或换改进 Euler</td></tr>
<tr><td>忘记验证解</td><td>算错不自知</td><td>代回原方程，看两边是否恒等</td></tr>
</tbody>
</table>
</div>

<div class="callout callout-key"><div class="callout-title">学到这里，你应该能</div>① 判断一个一阶方程属于哪一类并选出解法；② 独立完成分离变量、常数变易、积分因子的全部推导，不靠查公式；③ 说清"为什么需要 Lipschitz 条件"、"为什么 $h$ 取 $\min(a,b/M)$"、"为什么局部误差高一阶整体掉一阶"；④ 在没有解析解时用 Euler 法算并估误差；⑤ 认出奇解并说明它与通解族的关系。
</div>

<div class="qa-item"><div class="qa-q">下一步学什么</div><div class="qa-a">本课只覆盖一阶方程 + 存在唯一性理论。往后是：高阶线性方程（特征方程、常数变易法推广）、线性微分方程组（矩阵指数）、幂级数解法、稳定性理论（相平面、Lyapunov 函数）。课件第五章"线性微分方程组"是下一个台阶，前置是线性代数（矩阵、特征值）。</div></div>

<div class="chapter-nav"></div>
</section>
"""

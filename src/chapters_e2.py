#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 10、11 章：数值解 + 知识图谱与自测"""

CH_E2 = r"""
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
<div class="formula">$$y_{n+1}=y_n+hf(x_{n+1},y_{n+1}) \tag{后退 Euler}$$</div>
<p>右边含 $y_{n+1}$，是<strong>隐式</strong>公式，每一步要解方程（通常迭代）。局部误差仍是 $O(h^2)$，但稳定性更好。</p>
<p>稳定性直观：$y'=-100y$（急剧衰减）。显式 Euler 取 $h=0.1$ 时 $y_{n+1}=y_n(1-10)=-9y_n$，符号乱跳、绝对值放大，数值解发散；后退 Euler 是 $y_{n+1}=y_n/(1+10)\approx0.09y_n$，正确衰减。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">梯形公式：左右平均</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>用梯形面积代替矩形：</p>
<div class="formula">$$y_{n+1}=y_n+\frac h2\left[f(x_n,y_n)+f(x_{n+1},y_{n+1})\right] \tag{梯形}$$</div>
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

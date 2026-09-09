#!/usr/bin/env python3
def M(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat"><table>{b}</table></span>'
def V(c): return M([[x] for x in c])
def PW(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat pw"><table>{b}</table></span>'
def F(n,d): return f'<span class="f"><span class="n">{n}</span><span class="d">{d}</span></span>'
sp="&#8722;"; inf="&#8734;"; pi="&#960;"; th="&#952;"; ph="&#966;"; sq="&#8730;"; INT="&#8747;"
ARR="&#8594;"; inv="<i>L</i><sup>&minus;1</sup>"; tau="&#964;"; sg="&#963;"; lm="&#955;"

CSS="""
@page{size:A4;margin:14mm 13mm}
*{box-sizing:border-box}
body{font-family:"DejaVu Serif",Georgia,serif;font-size:10.3pt;line-height:1.55;color:#14161b;margin:0}
h1{font-size:22pt;margin:0 0 4px}
.sub{font-size:11pt;color:#4a5361;margin-bottom:16px}

/* ---- per-unit colour themes ---- */
.uw{--ac:#1d2433;--lt:#eef1f6;--md:#c9d2e4}
.u1{--ac:#1b4ed8;--lt:#eef2ff;--md:#c3d0fb}
.u2{--ac:#0c7268;--lt:#e9faf6;--md:#b3e6dc}
.u3{--ac:#6b26c9;--lt:#f4eefe;--md:#d9c6f7}
.u4{--ac:#b0560a;--lt:#fff3e6;--md:#f7d3ab}
.u5{--ac:#b8123f;--lt:#fdecf1;--md:#f7c0cf}

.banner{background:var(--ac);color:#fff;border-radius:6px;padding:16px 20px;margin:0 0 6px}
.banner .t{font-size:20pt;font-weight:700;line-height:1.2}
.banner .a{font-size:12pt;margin-top:6px;opacity:.95}
.bmeta{background:var(--lt);border:1.5px solid var(--md);border-radius:5px;padding:10px 16px;margin:0 0 14px;font-size:10pt}
.bmeta b{color:var(--ac)}

.secwrap{margin:26px 0 0;page-break-inside:avoid;page-break-after:avoid}
.secwrap:first-child{margin-top:0}
.sec{background:var(--ac);color:#fff;padding:9px 15px;border-radius:4px;margin:0 0 4px;font-size:14pt;font-weight:700}
.sec .sl{display:inline-block;background:rgba(255,255,255,.22);border-radius:3px;padding:1px 9px;margin-right:10px;font-size:12pt}
.secmeta{font-size:9.8pt;color:var(--ac);margin:0 0 16px;font-weight:600}
.lbl{font-size:9.5pt;font-weight:700;letter-spacing:.7px;color:var(--ac);margin:20px 0 5px;text-transform:uppercase}

.qbox{border:2px solid var(--ac);border-radius:5px;padding:12px 16px;margin:0;background:var(--lt)}
.fbox{background:#fff8e8;border-left:5px solid #b8842a;border-radius:0 4px 4px 0;padding:11px 16px;margin:0}
.fbox ul{margin:5px 0 0 18px;padding:0}.fbox li{margin:6px 0}
.why{background:#f7f8fa;border-left:5px solid var(--ac);border-radius:0 4px 4px 0;padding:11px 16px;margin:0}
.steps{counter-reset:st;margin:0;padding:0;list-style:none}
.steps>li{counter-increment:st;position:relative;padding:0 0 0 34px;margin:0 0 15px}
.steps>li::before{content:counter(st);position:absolute;left:0;top:1px;width:23px;height:23px;
  background:var(--ac);color:#fff;border-radius:50%;text-align:center;font-size:10pt;line-height:23px;font-weight:700}
.steps>li b.t{display:block;color:var(--ac);margin-bottom:2px}
.eq{margin:8px 0 8px 4px}
.chk{background:#f0faf4;border:1.6px solid #0d7a45;border-radius:5px;padding:11px 16px;margin:0}
.chk b{color:#0d5c34}
.warn{background:#fdf4f4;border-left:5px solid #a04545;border-radius:0 4px 4px 0;padding:11px 16px;margin:0}
.warn b{color:#8a2f2f}
.warn ul{margin:5px 0 0 18px;padding:0}.warn li{margin:5px 0}

table.t{width:100%;border-collapse:collapse;font-size:10pt;margin:6px 0}
table.t th{background:var(--ac);color:#fff;text-align:left;padding:5px 9px;font-size:9.5pt}
table.t td{border-bottom:1px solid #d5dae1;padding:5px 9px}
table.t tr:nth-child(even) td{background:var(--lt)}
table.idx{width:100%;border-collapse:collapse;font-size:9.8pt;margin:6px 0}
table.idx th{background:#1d2433;color:#fff;text-align:left;padding:6px 9px;font-size:9.3pt}
table.idx td{border-bottom:1px solid #d5dae1;padding:5px 9px}
td.c1{background:#eef2ff;font-weight:700;color:#1b4ed8}
td.c2{background:#e9faf6;font-weight:700;color:#0c7268}
td.c3{background:#f4eefe;font-weight:700;color:#6b26c9}
td.c4{background:#fff3e6;font-weight:700;color:#b0560a}
td.c5{background:#fdecf1;font-weight:700;color:#b8123f}
.c{text-align:center}
.mk{display:inline-block;background:var(--ac);color:#fff;border-radius:10px;padding:0 8px;font-size:9pt;font-weight:700}

.mat{display:inline-block;vertical-align:middle;position:relative;padding:2px 7px;margin:0 2px}
.mat::before,.mat::after{content:"";position:absolute;top:0;bottom:0;width:4px;border:1.1px solid #14161b}
.mat::before{left:0;border-right:none}.mat::after{right:0;border-left:none}
.mat.pw::after{display:none}.mat.pw td{text-align:left;padding-right:9px!important}
.mat table{border-collapse:collapse}
.mat td{padding:0 4px!important;text-align:center;font-size:.9em;line-height:1.22;border:none!important;background:transparent!important}
.f{display:inline-block;vertical-align:-.45em;text-align:center;margin:0 3px}
.f .n{display:block;border-bottom:1.1px solid #14161b;padding:0 4px}
.f .d{display:block;padding:0 4px}
.alt{background:#f6f2fb;border-left:5px solid #6b26c9;border-radius:0 4px 4px 0;padding:11px 16px;margin:0}
.alt b{color:#5218a8}
.alt ul{margin:5px 0 0 18px;padding:0}.alt li{margin:6px 0}
.warn,.chk,.fbox,.qbox,.why,.alt{page-break-inside:avoid}
.steps>li{page-break-inside:avoid}
.lbl{page-break-after:avoid}
.sec,.secmeta,.banner{page-break-after:avoid}
table.t{page-break-inside:avoid}
.brk{page-break-before:always}
.avoid{page-break-inside:avoid}
"""
H=[]; w=H.append

def sec(n, title, meta):
    w(f'<div class="secwrap"><div class="sec"><span class="sl">{n}</span>{title}</div>'
      f'<div class="secmeta">{meta}</div></div>')

def banner(u, name, answer, meta):
    w(f'<div class="brk"></div><div class="banner"><div class="t">UNIT {u} &mdash; {name}</div>'
      f'<div class="a">{answer}</div></div><div class="bmeta">{meta}</div>')

def openu(cls): w(f'<div class="uw {cls}">')
def closeu(): w('</div>')
def blk(label, cls, html):
    w(f'<div class="lbl">{label}</div><div class="{cls}">{html}</div>')
def steps(items):
    w('<div class="lbl">Solution &mdash; every step</div><ol class="steps">')
    for t,body in items: w(f'<li><b class="t">{t}</b>{body}</li>')
    w('</ol>')

# ================= COVER + FORMULA SHEET =================
w('<div class="uw">')
w(f"""<h1>24CS31 &mdash; Worked Solutions</h1>
<div class="sub">Every question on your 3-hour plan, solved in full. Read the method, then cover the page and
reproduce it. Each answer below has been checked numerically.</div>

<div class="lbl">Laplace transforms you must know by heart</div>
<table class="t">
<tr><th style="width:33%"><i>f</i>(<i>t</i>)</th><th style="width:33%"><i>F</i>(<i>s</i>) = <i>L</i>{{<i>f</i>}}</th><th>Note</th></tr>
<tr><td>1</td><td>1/<i>s</i></td><td></td></tr>
<tr><td><i>t<sup>n</sup></i></td><td><i>n</i>! / <i>s</i><sup><i>n</i>+1</sup></td><td><i>t</i> &rarr; 1/<i>s</i><sup>2</sup>, &nbsp;<i>t</i><sup>2</sup> &rarr; 2/<i>s</i><sup>3</sup></td></tr>
<tr><td><i>e<sup>at</sup></i></td><td>1/(<i>s</i>&minus;<i>a</i>)</td><td></td></tr>
<tr><td>sin&nbsp;<i>at</i></td><td><i>a</i>/(<i>s</i><sup>2</sup>+<i>a</i><sup>2</sup>)</td><td></td></tr>
<tr><td>cos&nbsp;<i>at</i></td><td><i>s</i>/(<i>s</i><sup>2</sup>+<i>a</i><sup>2</sup>)</td><td></td></tr>
<tr><td>sinh&nbsp;<i>at</i></td><td><i>a</i>/(<i>s</i><sup>2</sup>&minus;<i>a</i><sup>2</sup>)</td><td></td></tr>
<tr><td>cosh&nbsp;<i>at</i></td><td><i>s</i>/(<i>s</i><sup>2</sup>&minus;<i>a</i><sup>2</sup>)</td><td></td></tr>
</table>

<div class="lbl">The properties &mdash; these are what the questions actually test</div>
<table class="t">
<tr><th style="width:32%">Name</th><th style="width:38%">Rule</th><th>When you use it</th></tr>
<tr><td><b>Definition</b></td><td><i>L</i>{{<i>f</i>}} = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></td><td>every proof starts here</td></tr>
<tr><td><b>First shifting</b></td><td><i>L</i>{{<i>e<sup>at</sup>f</i>(<i>t</i>)}} = <i>F</i>(<i>s</i>&minus;<i>a</i>)</td><td>an <i>e<sup>at</sup></i> multiplying anything</td></tr>
<tr><td><b>Second shifting</b></td><td><i>L</i>{{<i>g</i>(<i>t</i>&minus;<i>a</i>)<i>u</i>(<i>t</i>&minus;<i>a</i>)}} = <i>e</i><sup>&minus;<i>as</i></sup><i>G</i>(<i>s</i>)</td><td>Heaviside / piecewise questions</td></tr>
<tr><td><b>Multiply by <i>t<sup>n</sup></i></b></td><td><i>L</i>{{<i>t<sup>n</sup>f</i>}} = (&minus;1)<sup><i>n</i></sup>{F('<i>d<sup>n</sup>F</i>','<i>ds<sup>n</sup></i>')}</td><td>Q1c proof, and <i>L</i>{{<i>t</i>&thinsp;sin&nbsp;<i>at</i>}} type</td></tr>
<tr><td><b>Divide by <i>t</i></b></td><td><i>L</i>{{<i>f</i>/<i>t</i>}} = {INT}<sub>s</sub><sup>{inf}</sup><i>F</i>(<i>u</i>)&thinsp;<i>du</i></td><td>anything over <i>t</i></td></tr>
<tr><td><b>Derivative</b></td><td><i>L</i>{{<i>y</i>&prime;}} = <i>sY</i> &minus; <i>y</i>(0)<br><i>L</i>{{<i>y</i>&Prime;}} = <i>s</i><sup>2</sup><i>Y</i> &minus; <i>s y</i>(0) &minus; <i>y</i>&prime;(0)</td><td><b>every ODE question</b></td></tr>
<tr><td><b>Integral</b></td><td><i>L</i>{{{INT}<sub>0</sub><sup><i>t</i></sup><i>f</i>(<i>u</i>)<i>du</i>}} = <i>F</i>(<i>s</i>)/<i>s</i></td><td>an integral inside the transform</td></tr>
<tr><td><b>Periodic</b></td><td><i>L</i>{{<i>f</i>}} = {F('1','1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>')}{INT}<sub>0</sub><sup><i>T</i></sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)<i>dt</i></td><td>period-<i>T</i> functions</td></tr>
<tr><td><b>Inverse of <i>F</i>&prime;</b></td><td>{inv}{{<i>F</i>&prime;(<i>s</i>)}} = &minus;<i>t f</i>(<i>t</i>)</td><td>inverse of a log or tan<sup>&minus;1</sup></td></tr>
</table>

<div class="lbl">Linear algebra formulas</div>
<table class="t">
<tr><th style="width:32%">Name</th><th style="width:38%">Rule</th><th>Where</th></tr>
<tr><td><b>Linear map test</b></td><td><i>T</i>(<b>u</b>+<b>v</b>) = <i>T</i>(<b>u</b>)+<i>T</i>(<b>v</b>) &nbsp;and&nbsp; <i>T</i>(<i>k</i><b>u</b>) = <i>kT</i>(<b>u</b>)</td><td>Q5b</td></tr>
<tr><td><b>Rank&ndash;nullity</b></td><td>rank + nullity = number of <b>columns</b></td><td>Q6c, Q7</td></tr>
<tr><td><b>Normal equations</b></td><td><i>A</i><sup>T</sup><i>A</i>&#770;<b>x</b> = <i>A</i><sup>T</sup><b>b</b></td><td>least squares, Q8b</td></tr>
<tr><td><b>Orthogonal diagonalization</b></td><td><i>P</i><sup>T</sup><i>AP</i> = <i>D</i>, columns of <i>P</i> = unit eigenvectors</td><td>Q10c</td></tr>
<tr><td><b>SVD</b></td><td><i>A</i> = <i>U</i>&Sigma;<i>V</i><sup>T</sup>, &nbsp;{sg}<sub><i>i</i></sub> = {sq}{lm}<sub><i>i</i></sub> of <i>A</i><sup>T</sup><i>A</i>, &nbsp;<b>u</b><sub><i>i</i></sub> = <i>A</i><b>v</b><sub><i>i</i></sub>/{sg}<sub><i>i</i></sub></td><td>Q9c</td></tr>
<tr><td><b>Conjugate transpose</b></td><td><i>A</i><sup>*</sup> = transpose, then flip the sign of every <i>i</i></td><td>Q10a, Q10b</td></tr>
<tr><td><b>Hermitian / Unitary</b></td><td><i>A</i><sup>*</sup> = <i>A</i> &nbsp;/&nbsp; <i>A</i><sup>*</sup><i>A</i> = <i>I</i></td><td>Q10b</td></tr>
<tr><td><b>Positive definite</b></td><td>ALL leading principal minors &gt; 0 (Sylvester)</td><td>Q10a</td></tr>
<tr><td><b>Rotation matrix</b></td><td>{M(['cos&#952;',sp+'sin&#952;']) if False else M([['cos&#952;',sp+'sin&#952;'],['sin&#952;','cos&#952;']])}, &nbsp;reflect in <i>x</i>: {M([['1','0'],['0',sp+'1']])}</td><td>Q5c, Q6a</td></tr>
</table>""")

def _s1():
    # ================= 1. UNITARY / HERMITIAN =================
    sec("V.2","Unitary and Hermitian check","Unit V &middot; Q10b &middot; 5 marks &middot; 8 minutes to learn")
    blk("The question","qbox",
     f"<b>(a)</b> Determine whether &nbsp;<i>A</i> = {M([['0','<i>i</i>'],[sp+'<i>i</i>','0']])}&nbsp; is unitary.<br><br>"
     f"<b>(b)</b> Determine whether &nbsp;<i>A</i> = {M([['3','7'+sp+'4<i>i</i>',sp+'2+5<i>i</i>'],['7+4<i>i</i>',sp+'2','3+<i>i</i>'],[sp+'2'+sp+'5<i>i</i>','3'+sp+'<i>i</i>','4']])}&nbsp; is Hermitian.")
    blk("Could it appear another way?","alt",
     """<b>The property-check block appeared in all four papers, always as a pair.</b>
    <ul><li><b>Unitary, 2&times;2 with <i>i</i>s</b> &mdash; Mar&nbsp;24 (solved here), and Jun&nbsp;23 used
    &frac12;[[1+<i>i</i>, 1&minus;<i>i</i>], [1&minus;<i>i</i>, 1+<i>i</i>]]. That one is also unitary &mdash; the &frac12; matters,
    so keep it outside the matrix and remember it squares to &frac14;.</li>
    <li><b>Hermitian, the 3&times;3 solved here</b> &mdash; Apr&nbsp;23 and Sep&nbsp;23. Answer: yes.</li>
    <li><b>Hermitian, [[0, 2+<i>i</i>, 1], [2&minus;<i>i</i>, <i>i</i>, 0], [1, 0, 1]]</b> &mdash; Jun&nbsp;23.
    <b>Answer: NO</b> &mdash; the diagonal entry <i>i</i> is not real. <b>Be ready for a &ldquo;no&rdquo;</b>, and give
    that reason.</li></ul>
    <b>Also possible in this slot:</b> check whether a matrix is <b>skew-Hermitian</b> (<i>A</i><sup>*</sup> = &minus;<i>A</i>)
    or <b>orthogonal</b> (<i>A</i><sup>T</sup><i>A</i> = <i>I</i>, the real case). Identical work.""")
    blk("Formulas you need","fbox",
     "<ul><li><b>Conjugate transpose</b> <i>A</i><sup>*</sup>: transpose the matrix, then change the sign of every <i>i</i>. "
     "(Written <i>A</i><sup>*</sup>, <i>A</i><sup>H</sup> or <i>A</i><sup>&dagger;</sup>.)</li>"
     "<li><b>Hermitian</b> means <i>A</i><sup>*</sup> = <i>A</i></li>"
     "<li><b>Unitary</b> means <i>A</i><sup>*</sup><i>A</i> = <i>I</i></li>"
     "<li>Remember <i>i</i><sup>2</sup> = &minus;1, so &minus;<i>i</i><sup>2</sup> = +1</li></ul>")
    blk("Why this works","why",
     "A Hermitian matrix is the complex version of a symmetric matrix. For a real matrix, symmetric means "
     "<i>a<sub>ij</sub></i> = <i>a<sub>ji</sub></i>. For a complex matrix the right generalisation is "
     "<i>a<sub>ij</sub></i> = conjugate of <i>a<sub>ji</sub></i> &mdash; and that forces the diagonal to be real, "
     "because a number equal to its own conjugate has no imaginary part. A unitary matrix is the complex version of an "
     "orthogonal matrix: its columns are unit vectors that are perpendicular to each other, which is exactly what "
     "<i>A</i><sup>*</sup><i>A</i> = <i>I</i> says.")
    steps([
     ("Part (a) &mdash; write down the transpose.",
      f'<div class="eq"><i>A</i> = {M([["0","<i>i</i>"],[sp+"<i>i</i>","0"]])} &nbsp;&nbsp;&rarr;&nbsp;&nbsp; '
      f'<i>A</i><sup>T</sup> = {M([["0",sp+"<i>i</i>"],["<i>i</i>","0"]])}</div>'
      "Swap rows and columns: the entry at position (1,2) moves to (2,1) and vice-versa."),
     ("Conjugate it &mdash; flip the sign of every <i>i</i>.",
      f'<div class="eq"><i>A</i><sup>*</sup> = {M([["0","<i>i</i>"],[sp+"<i>i</i>","0"]])}</div>'
      "Notice this is the same as the original <i>A</i>. So this matrix happens to be <b>Hermitian as well</b> &mdash; "
      "worth one line in your answer, it costs nothing."),
     ("Multiply <i>A</i><sup>*</sup><i>A</i>, entry by entry.",
      f'<div class="eq"><i>A</i><sup>*</sup><i>A</i> = {M([["0","<i>i</i>"],[sp+"<i>i</i>","0"]])}{M([["0","<i>i</i>"],[sp+"<i>i</i>","0"]])}</div>'
      "Row 1 &times; column 1: &nbsp;(0)(0) + (<i>i</i>)(&minus;<i>i</i>) = &minus;<i>i</i><sup>2</sup> = <b>1</b><br>"
      "Row 1 &times; column 2: &nbsp;(0)(<i>i</i>) + (<i>i</i>)(0) = <b>0</b><br>"
      "Row 2 &times; column 1: &nbsp;(&minus;<i>i</i>)(0) + (0)(&minus;<i>i</i>) = <b>0</b><br>"
      "Row 2 &times; column 2: &nbsp;(&minus;<i>i</i>)(<i>i</i>) + (0)(0) = &minus;<i>i</i><sup>2</sup> = <b>1</b>"),
     ("State the conclusion.",
      f'<div class="eq"><i>A</i><sup>*</sup><i>A</i> = {M([["1","0"],["0","1"]])} = <i>I</i></div>'
      "<b>Therefore <i>A</i> is unitary.</b> (And Hermitian.)"),
     ("Part (b) &mdash; compare each entry with the conjugate of its mirror image.",
      "You do not need to write out the whole conjugate transpose. Just check the three off-diagonal pairs and the diagonal:<br><br>"
      "&bull;&nbsp; <i>a</i><sub>12</sub> = 7&minus;4<i>i</i> &nbsp;and&nbsp; conjugate of <i>a</i><sub>21</sub> = conj(7+4<i>i</i>) = 7&minus;4<i>i</i> &nbsp;&#10003;<br>"
      "&bull;&nbsp; <i>a</i><sub>13</sub> = &minus;2+5<i>i</i> &nbsp;and&nbsp; conj(<i>a</i><sub>31</sub>) = conj(&minus;2&minus;5<i>i</i>) = &minus;2+5<i>i</i> &nbsp;&#10003;<br>"
      "&bull;&nbsp; <i>a</i><sub>23</sub> = 3+<i>i</i> &nbsp;and&nbsp; conj(<i>a</i><sub>32</sub>) = conj(3&minus;<i>i</i>) = 3+<i>i</i> &nbsp;&#10003;<br>"
      "&bull;&nbsp; Diagonal 3, &minus;2, 4 &mdash; all real &nbsp;&#10003;"),
     ("Conclude.","Every entry satisfies <i>a<sub>ij</sub></i> = conj(<i>a<sub>ji</sub></i>) and the diagonal is real, "
      "so <i>A</i><sup>*</sup> = <i>A</i>. <b>Therefore <i>A</i> is Hermitian.</b>")])
    blk("Check your answer","chk",
     "<b>Both answers are YES.</b> If you get &ldquo;no&rdquo; for either, you have almost certainly forgotten to "
     "conjugate, or conjugated without transposing. Do the two operations in either order &mdash; the result is the same "
     "&mdash; but you must do <b>both</b>.")
    blk("Watch out","warn",
     "<ul><li>Transposing alone is not enough. <i>A</i><sup>T</sup> &ne; <i>A</i><sup>*</sup> when there are complex entries.</li>"
     "<li>A Hermitian matrix must have a <b>real diagonal</b>. If you spot a diagonal entry with an <i>i</i> in it, "
     "the answer is no and you can stop there.</li>"
     "<li>Show the multiplication for the unitary part. Writing only &ldquo;<i>A</i><sup>*</sup><i>A</i> = <i>I</i>, so unitary&rdquo; "
     "will not get full marks.</li></ul>")

def _s2():
    # ================= 2. PROVE T IS LINEAR =================
    sec("III.2","Prove <i>T</i> is linear, and find images","Unit III &middot; Q5b &middot; 7 marks &middot; 12 minutes")
    blk("The question","qbox",
     f"<b>(a)</b> Prove that <i>T</i>&thinsp;:&thinsp;<i>R</i><sup>2</sup> {ARR} <i>R</i><sup>3</sup> given by "
     f"<i>T</i>(<i>x</i>,&thinsp;<i>y</i>) = (3<i>x</i>+<i>y</i>,&nbsp; 2<i>y</i>,&nbsp; <i>x</i>&minus;<i>y</i>) is linear. "
     f"Find the images of (1,&thinsp;2) and (2,&thinsp;&minus;5).<br><br>"
     f"<b>(b)</b> Show that <i>T</i>&thinsp;:&thinsp;<i>P</i><sub>2</sub> {ARR} <i>P</i><sub>2</sub> given by "
     f"<i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup> + <i>c</i> is linear. "
     f"Find the image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1.")
    blk("Could it appear another way?","alt",
     """<b>The transformation changes every paper; the proof does not.</b>
    <ul><li><i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>), images of (1,2) and (2,&minus;5)
    &mdash; Apr&nbsp;23 and Sep&nbsp;23</li>
    <li><i>T</i>(<i>x</i>,<i>y</i>) = (2<i>x</i>, <i>x</i>+<i>y</i>), images of (1,2) and (&minus;1,&minus;4) &mdash; Jun&nbsp;23</li>
    <li><i>T</i>&thinsp;:&thinsp;<i>P</i><sub>2</sub>&rarr;<i>P</i><sub>2</sub>, the polynomial version &mdash; Mar&nbsp;24</li></ul>
    <b>Watch for the trap version.</b> If the map contains a constant, a square or a product &mdash; for instance
    <i>T</i>(<i>x</i>,<i>y</i>) = (<i>x</i>+1, <i>y</i>) or (<i>x</i><sup>2</sup>, <i>y</i>) &mdash; it is <b>not</b> linear, and the
    answer is to produce a counter-example. The quickest one is <i>T</i>(<b>0</b>) &ne; <b>0</b>.""")
    blk("Formulas you need","fbox",
     "<b>A map <i>T</i> is linear if and only if BOTH of these hold for all vectors and all scalars:</b>"
     "<ul><li><b>Additivity:</b> &nbsp;<i>T</i>(<b>u</b> + <b>v</b>) = <i>T</i>(<b>u</b>) + <i>T</i>(<b>v</b>)</li>"
     "<li><b>Homogeneity:</b> &nbsp;<i>T</i>(<i>k</i><b>u</b>) = <i>k</i>&thinsp;<i>T</i>(<b>u</b>)</li></ul>")
    blk("Why this works","why",
     "&ldquo;Linear&rdquo; means the map does not care whether you combine first and transform, or transform first and "
     "combine. The two conditions say exactly that for the two ways of combining vectors: adding them, and scaling them. "
     "The proof is always the same shape &mdash; take two <b>general</b> vectors with subscripts, work out the left side, "
     "work out the right side, and show the two expressions are identical. <b>Do not use numbers</b>; a check with specific "
     "vectors proves nothing.")
    steps([
     ("Set up general vectors.",
      "Let &nbsp;<b>u</b> = (<i>x</i><sub>1</sub>, <i>y</i><sub>1</sub>) &nbsp;and&nbsp; <b>v</b> = (<i>x</i><sub>2</sub>, <i>y</i><sub>2</sub>), "
      "and let <i>k</i> be any scalar. Everything follows from these."),
     ("Additivity &mdash; work out the left-hand side.",
      "First add the vectors: &nbsp;<b>u</b> + <b>v</b> = (<i>x</i><sub>1</sub>+<i>x</i><sub>2</sub>, &nbsp;<i>y</i><sub>1</sub>+<i>y</i><sub>2</sub>)<br><br>"
      "Now apply <i>T</i> to that, using the given rule:"
      '<div class="eq"><i>T</i>(<b>u</b>+<b>v</b>) = ( 3(<i>x</i><sub>1</sub>+<i>x</i><sub>2</sub>) + (<i>y</i><sub>1</sub>+<i>y</i><sub>2</sub>), '
      '&nbsp; 2(<i>y</i><sub>1</sub>+<i>y</i><sub>2</sub>), &nbsp; (<i>x</i><sub>1</sub>+<i>x</i><sub>2</sub>) &minus; (<i>y</i><sub>1</sub>+<i>y</i><sub>2</sub>) )</div>'),
     ("Work out the right-hand side.",
      '<div class="eq"><i>T</i>(<b>u</b>) + <i>T</i>(<b>v</b>) = (3<i>x</i><sub>1</sub>+<i>y</i><sub>1</sub>, &nbsp;2<i>y</i><sub>1</sub>, &nbsp;<i>x</i><sub>1</sub>&minus;<i>y</i><sub>1</sub>) '
      '+ (3<i>x</i><sub>2</sub>+<i>y</i><sub>2</sub>, &nbsp;2<i>y</i><sub>2</sub>, &nbsp;<i>x</i><sub>2</sub>&minus;<i>y</i><sub>2</sub>)</div>'
      "Add componentwise:"
      '<div class="eq">= ( (3<i>x</i><sub>1</sub>+<i>y</i><sub>1</sub>) + (3<i>x</i><sub>2</sub>+<i>y</i><sub>2</sub>), '
      '&nbsp; 2<i>y</i><sub>1</sub>+2<i>y</i><sub>2</sub>, &nbsp; (<i>x</i><sub>1</sub>&minus;<i>y</i><sub>1</sub>) + (<i>x</i><sub>2</sub>&minus;<i>y</i><sub>2</sub>) )</div>'
      "Expand the brackets in step 2 and you get exactly this. <b>So additivity holds.</b>"),
     ("Homogeneity.",
      "Scale first: &nbsp;<i>k</i><b>u</b> = (<i>kx</i><sub>1</sub>, <i>ky</i><sub>1</sub>). Then transform:"
      '<div class="eq"><i>T</i>(<i>k</i><b>u</b>) = (3<i>kx</i><sub>1</sub>+<i>ky</i><sub>1</sub>, &nbsp;2<i>ky</i><sub>1</sub>, &nbsp;<i>kx</i><sub>1</sub>&minus;<i>ky</i><sub>1</sub>)</div>'
      "Take the common factor <i>k</i> out of every component:"
      '<div class="eq">= <i>k</i>(3<i>x</i><sub>1</sub>+<i>y</i><sub>1</sub>, &nbsp;2<i>y</i><sub>1</sub>, &nbsp;<i>x</i><sub>1</sub>&minus;<i>y</i><sub>1</sub>) = <i>k</i>&thinsp;<i>T</i>(<b>u</b>)</div>'
      "<b>So homogeneity holds. Both conditions hold, therefore <i>T</i> is linear.</b>"),
     ("Find the images &mdash; just substitute.",
      '<div class="eq"><i>T</i>(1,&thinsp;2) = (3(1)+2, &nbsp;2(2), &nbsp;1&minus;2) = <b>(5,&nbsp;4,&nbsp;&minus;1)</b></div>'
      '<div class="eq"><i>T</i>(2,&thinsp;&minus;5) = (3(2)+(&minus;5), &nbsp;2(&minus;5), &nbsp;2&minus;(&minus;5)) = <b>(1,&nbsp;&minus;10,&nbsp;7)</b></div>'
      "Be careful with the double negative in the last component: 2 &minus; (&minus;5) = 2 + 5 = 7."),
     ("Part (b) &mdash; the polynomial version is the same proof.",
      "Let &nbsp;<i>p</i> = <i>a</i><sub>1</sub><i>x</i><sup>2</sup>+<i>b</i><sub>1</sub><i>x</i>+<i>c</i><sub>1</sub> &nbsp;and&nbsp; "
      "<i>q</i> = <i>a</i><sub>2</sub><i>x</i><sup>2</sup>+<i>b</i><sub>2</sub><i>x</i>+<i>c</i><sub>2</sub>.<br><br>"
      "<i>p</i> + <i>q</i> has coefficients <i>a</i><sub>1</sub>+<i>a</i><sub>2</sub>, <i>b</i><sub>1</sub>+<i>b</i><sub>2</sub>, <i>c</i><sub>1</sub>+<i>c</i><sub>2</sub>, so"
      '<div class="eq"><i>T</i>(<i>p</i>+<i>q</i>) = [(<i>a</i><sub>1</sub>+<i>a</i><sub>2</sub>) + (<i>b</i><sub>1</sub>+<i>b</i><sub>2</sub>)]<i>x</i><sup>2</sup> + (<i>c</i><sub>1</sub>+<i>c</i><sub>2</sub>)</div>'
      "Regroup as [(<i>a</i><sub>1</sub>+<i>b</i><sub>1</sub>) + (<i>a</i><sub>2</sub>+<i>b</i><sub>2</sub>)]<i>x</i><sup>2</sup> + <i>c</i><sub>1</sub> + <i>c</i><sub>2</sub> = "
      "<i>T</i>(<i>p</i>) + <i>T</i>(<i>q</i>). &nbsp;&#10003;<br><br>"
      "Similarly <i>T</i>(<i>kp</i>) = (<i>ka</i><sub>1</sub>+<i>kb</i><sub>1</sub>)<i>x</i><sup>2</sup> + <i>kc</i><sub>1</sub> = <i>k T</i>(<i>p</i>). &nbsp;&#10003;"),
     ("The image.",
      "For 5<i>x</i><sup>2</sup>+6<i>x</i>+1 read off <i>a</i> = 5, <i>b</i> = 6, <i>c</i> = 1:"
      '<div class="eq"><i>T</i>(5<i>x</i><sup>2</sup>+6<i>x</i>+1) = (5+6)<i>x</i><sup>2</sup> + 1 = <b>11<i>x</i><sup>2</sup> + 1</b></div>')])
    blk("Check your answer","chk",
     "<b>(5, 4, &minus;1)</b> &nbsp;&middot;&nbsp; <b>(1, &minus;10, 7)</b> &nbsp;&middot;&nbsp; <b>11<i>x</i><sup>2</sup> + 1</b><br>"
     "A quick sanity check that works for any linear map: <i>T</i>(<b>0</b>) must be <b>0</b>. Here "
     "<i>T</i>(0,0) = (0,0,0) &#10003;. If a map sends <b>0</b> to something non-zero, it is <b>not</b> linear and you can say so immediately.")
    blk("Watch out","warn",
     "<ul><li><b>Do not verify with numbers.</b> Showing <i>T</i>(1,2)+<i>T</i>(3,4) = <i>T</i>(4,6) proves nothing. "
     "You must use general subscripted vectors.</li>"
     "<li>Prove <b>both</b> conditions. Each is worth marks; showing only additivity typically loses two or three.</li>"
     "<li>Write the final line explicitly: &ldquo;Since both conditions are satisfied, <i>T</i> is linear.&rdquo;</li></ul>")

def _s3():
    # ================= 3. LEAST SQUARES =================
    sec("IV.1","Least-squares solution of <i>Ax</i> = <i>b</i>","Unit IV &middot; Q8b &middot; 10 marks &middot; 20 minutes")
    blk("The question","qbox",
     f"Find the least-squares solution of <i>AX</i> = <b>b</b>, where<br><br>"
     f"<i>A</i> = {M([['1','3','5'],['1','1','0'],['1','1','2'],['1','3','3']])} &nbsp;&nbsp;and&nbsp;&nbsp; "
     f"<b>b</b> = {V(['3','5','7',sp+'3'])}")
    blk("Could it appear another way?","alt",
     """<b>Least squares appeared in all four papers, with four different matrices.</b> The method &mdash;
    <i>A</i><sup>T</sup><i>A</i>&#770;<b>x</b> = <i>A</i><sup>T</sup><b>b</b> &mdash; never changes.
    <ul><li><i>A</i> = 4&times;3 as solved here, <b>b</b> = (3, 5, 7, &minus;3) &mdash; Jun&nbsp;23 and Mar&nbsp;24</li>
    <li>A <b>6&times;4 block-design matrix</b> of 0s and 1s with <b>b</b> = (&minus;3, &minus;1, 0, 2, 5, 1) &mdash; Apr&nbsp;23.
    Bigger, but the columns are mostly zeros so the dot products are quick.</li>
    <li><i>A</i> = 3&times;2 [[4,0],[0,2],[1,1]], <b>b</b> = (2, 0, 11) &mdash; Sep&nbsp;23. Only a 2&times;2 system to solve.</li></ul>
    <b>The related question:</b> some papers ask for the <b>least-squares line of best fit</b> through given data points.
    Same method &mdash; build <i>A</i> with a column of 1s and a column of <i>x</i>-values, and <b>b</b> from the <i>y</i>-values.""")
    blk("Formulas you need","fbox",
     f"<b>The normal equations:</b> &nbsp;&nbsp;<i>A</i><sup>T</sup><i>A</i>&#770;<b>x</b> = <i>A</i><sup>T</sup><b>b</b>"
     f"<br><br>That is the entire method. Build the two pieces, then solve a small square system.")
    blk("Why this works","why",
     "<i>Ax</i> = <b>b</b> has four equations but only three unknowns, so in general there is <b>no exact solution</b> &mdash; "
     "<b>b</b> does not lie in the column space of <i>A</i>. The best you can do is find the &#770;<b>x</b> that makes "
     "<i>A</i>&#770;<b>x</b> as close to <b>b</b> as possible. Geometrically, <i>A</i>&#770;<b>x</b> is the projection of "
     "<b>b</b> onto the column space, so the error <b>b</b> &minus; <i>A</i>&#770;<b>x</b> must be perpendicular to every "
     "column of <i>A</i>. Writing &ldquo;perpendicular to every column&rdquo; in symbols gives "
     "<i>A</i><sup>T</sup>(<b>b</b> &minus; <i>A</i>&#770;<b>x</b>) = <b>0</b>, which rearranges to the normal equations. "
     "<b>That one sentence is worth writing in your answer.</b>")
    steps([
     ("Write down <i>A</i><sup>T</sup>.",
      f'<div class="eq"><i>A</i><sup>T</sup> = {M([["1","1","1","1"],["3","1","1","3"],["5","0","2","3"]])}</div>'
      "The rows of <i>A</i><sup>T</sup> are the columns of <i>A</i>."),
     ("Build <i>A</i><sup>T</sup><i>A</i>. It is 3&times;3 and symmetric, so you only need six numbers.",
      "Each entry is a dot product of two <b>columns</b> of <i>A</i>. Call the columns "
      "<b>c</b><sub>1</sub> = (1,1,1,1), <b>c</b><sub>2</sub> = (3,1,1,3), <b>c</b><sub>3</sub> = (5,0,2,3).<br><br>"
      "<b>c</b><sub>1</sub>&middot;<b>c</b><sub>1</sub> = 1+1+1+1 = <b>4</b><br>"
      "<b>c</b><sub>1</sub>&middot;<b>c</b><sub>2</sub> = 3+1+1+3 = <b>8</b><br>"
      "<b>c</b><sub>1</sub>&middot;<b>c</b><sub>3</sub> = 5+0+2+3 = <b>10</b><br>"
      "<b>c</b><sub>2</sub>&middot;<b>c</b><sub>2</sub> = 9+1+1+9 = <b>20</b><br>"
      "<b>c</b><sub>2</sub>&middot;<b>c</b><sub>3</sub> = 15+0+2+9 = <b>26</b><br>"
      "<b>c</b><sub>3</sub>&middot;<b>c</b><sub>3</sub> = 25+0+4+9 = <b>38</b>"
      f'<div class="eq"><i>A</i><sup>T</sup><i>A</i> = {M([["4","8","10"],["8","20","26"],["10","26","38"]])}</div>'
      "<b>The symmetry is a free check</b> &mdash; if your matrix is not symmetric, you have made an arithmetic slip."),
     ("Build <i>A</i><sup>T</sup><b>b</b>. Three dot products of the columns with <b>b</b>.",
      "<b>c</b><sub>1</sub>&middot;<b>b</b> = 3 + 5 + 7 &minus; 3 = <b>12</b><br>"
      "<b>c</b><sub>2</sub>&middot;<b>b</b> = 3(3) + 1(5) + 1(7) + 3(&minus;3) = 9 + 5 + 7 &minus; 9 = <b>12</b><br>"
      "<b>c</b><sub>3</sub>&middot;<b>b</b> = 5(3) + 0(5) + 2(7) + 3(&minus;3) = 15 + 0 + 14 &minus; 9 = <b>20</b>"
      f'<div class="eq"><i>A</i><sup>T</sup><b>b</b> = {V(["12","12","20"])}</div>'),
     ("Write out the system.",
      '<div class="eq">4<i>x</i> + 8<i>y</i> + 10<i>z</i> = 12 &nbsp;&nbsp;&hellip;(1)<br>'
      '8<i>x</i> + 20<i>y</i> + 26<i>z</i> = 12 &nbsp;&hellip;(2)<br>'
      '10<i>x</i> + 26<i>y</i> + 38<i>z</i> = 20 &nbsp;&hellip;(3)</div>'),
     ("Eliminate <i>x</i>.",
      "(2) &minus; 2&times;(1): &nbsp; (20&minus;16)<i>y</i> + (26&minus;20)<i>z</i> = 12 &minus; 24"
      '<div class="eq">4<i>y</i> + 6<i>z</i> = &minus;12 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; 2<i>y</i> + 3<i>z</i> = &minus;6 &nbsp;&hellip;(4)</div>'
      "(3) &minus; 2.5&times;(1): &nbsp; (26&minus;20)<i>y</i> + (38&minus;25)<i>z</i> = 20 &minus; 30"
      '<div class="eq">6<i>y</i> + 13<i>z</i> = &minus;10 &nbsp;&hellip;(5)</div>'),
     ("Eliminate <i>y</i> and solve.",
      "(5) &minus; 3&times;(4): &nbsp; 13<i>z</i> &minus; 9<i>z</i> = &minus;10 &minus; (&minus;18)"
      '<div class="eq">4<i>z</i> = 8 &nbsp;&nbsp;&rarr;&nbsp;&nbsp; <b><i>z</i> = 2</b></div>'
      "Put <i>z</i> = 2 into (4): &nbsp;2<i>y</i> + 6 = &minus;6 &nbsp;&rarr;&nbsp; 2<i>y</i> = &minus;12 &nbsp;&rarr;&nbsp; <b><i>y</i> = &minus;6</b><br><br>"
      "Put both into (1): &nbsp;4<i>x</i> &minus; 48 + 20 = 12 &nbsp;&rarr;&nbsp; 4<i>x</i> = 40 &nbsp;&rarr;&nbsp; <b><i>x</i> = 10</b>"),
     ("State the answer.",
      f'<div class="eq">&#770;<b>x</b> = {V(["10",sp+"6","2"])}</div>')])
    blk("Check your answer","chk",
     f"<b>&#770;<b>x</b> = (10, &minus;6, 2).</b> Here is a check that takes thirty seconds and confirms all ten marks.<br><br>"
     f"Compute <i>A</i>&#770;<b>x</b> = (2, 4, 8, &minus;2). The error is<br>"
     f'<div class="eq"><b>r</b> = <b>b</b> &minus; <i>A</i>&#770;<b>x</b> = (3,5,7,&minus;3) &minus; (2,4,8,&minus;2) = (1, 1, &minus;1, &minus;1)</div>'
     f"Now dot <b>r</b> with each column of <i>A</i>:<br>"
     f"&bull;&nbsp; <b>r</b>&middot;<b>c</b><sub>1</sub> = 1+1&minus;1&minus;1 = 0 &nbsp;&#10003;<br>"
     f"&bull;&nbsp; <b>r</b>&middot;<b>c</b><sub>2</sub> = 3+1&minus;1&minus;3 = 0 &nbsp;&#10003;<br>"
     f"&bull;&nbsp; <b>r</b>&middot;<b>c</b><sub>3</sub> = 5+0&minus;2&minus;3 = 0 &nbsp;&#10003;<br><br>"
     f"All three are zero, so the error really is perpendicular to the column space. <b>That is the definition of the "
     f"least-squares solution, so the answer is right.</b> Writing this check earns marks on its own.")
    blk("Watch out","warn",
     "<ul><li>Do <b>not</b> try to solve <i>Ax</i> = <b>b</b> directly. It is inconsistent &mdash; four equations, three "
     "unknowns. If you row-reduce the augmented matrix you will get a contradiction and panic.</li>"
     "<li><i>A</i><sup>T</sup><i>A</i> must come out symmetric. Use that as a checkpoint before going further.</li>"
     "<li>Keep the signs on <b>b</b>. The last entry is &minus;3, and it is easy to drop the minus in the dot products.</li></ul>")

def _s4():
    # ================= 4. t^n PROOF =================
    sec("I.3","Prove the <i>t<sup>n</sup></i>-multiplication rule","Unit I &middot; Q1c or Q2b &middot; 7 marks &middot; 15 minutes")
    blk("The question","qbox",
     f"If <i>L</i>{{<i>f</i>(<i>t</i>)}} = <i>F</i>(<i>s</i>), prove that<br>"
     f'<div class="eq"><i>L</i>{{<i>t<sup>n</sup>f</i>(<i>t</i>)}} = (&minus;1)<sup><i>n</i></sup> '
     f'{F("<i>d<sup>n</sup></i>","<i>ds<sup>n</sup></i>")}{{<i>F</i>(<i>s</i>)}}</div>'
     f"where <i>n</i> is a positive integer.<br><br>"
     f"<b>This has been set word-for-word in all four past papers.</b>")
    blk("Could it appear another way?","alt",
     """<b>This proof is always word-for-word identical.</b> But the examiner keeps a small stock of Unit&nbsp;I proofs
    and rotates them, so the <i>other</i> question may carry one of these instead:
    <ul><li><b><i>L</i>{<i>f</i>(<i>t</i>)/<i>t</i>} = &int;<sub><i>s</i></sub><sup>&infin;</sup><i>F</i>(<i>u</i>)&thinsp;<i>du</i></b>
    (Jun&nbsp;23 Q2b, 7 m). Proof: write the right side as a double integral, <b>swap the order of integration</b>,
    do the <i>u</i>-integral to get <i>e</i><sup>&minus;<i>st</i></sup>/<i>t</i>, and you are left with <i>L</i>{<i>f</i>/<i>t</i>}.</li>
    <li><b><i>L</i>{(sinh&nbsp;<i>at</i>)<i>f</i>(<i>t</i>)} = &frac12;[<i>F</i>(<i>s</i>&minus;<i>a</i>) &minus; <i>F</i>(<i>s</i>+<i>a</i>)]</b>
    (Sep&nbsp;23 Q2b, 7 m). Proof: sinh&nbsp;<i>at</i> = &frac12;(<i>e<sup>at</sup></i> &minus; <i>e</i><sup>&minus;<i>at</i></sup>),
    then apply the <b>first shifting theorem</b> to each term. Three lines.</li>
    <li>Both are often followed by &ldquo;hence find&rdquo; a specific transform &mdash; e.g. <i>L</i>{sin&nbsp;4<i>t</i>/<i>t</i>}
    or <i>L</i>[<i>t</i><sup>8</sup>&thinsp;sinh&nbsp;2<i>t</i>]. Just substitute into the formula you have just proved.</li></ul>""")
    blk("Formulas you need","fbox",
     f"<ul><li><b>Definition:</b> &nbsp;<i>F</i>(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></li>"
     f"<li><b>Differentiation under the integral sign</b> (Leibniz&rsquo;s rule): you may move "
     f"{F('<i>d</i>','<i>ds</i>')} inside the integral, where it becomes a partial derivative "
     f"{F('&#8706;','&#8706;<i>s</i>')}.</li>"
     f"<li>{F('&#8706;','&#8706;<i>s</i>')}(<i>e</i><sup>&minus;<i>st</i></sup>) = &minus;<i>t e</i><sup>&minus;<i>st</i></sup> "
     f"&mdash; note <i>t</i> is a constant as far as <i>s</i> is concerned.</li></ul>")
    blk("Why this works","why",
     "The whole proof rests on one observation: inside the Laplace integral, differentiating with respect to <i>s</i> "
     "pulls down a factor of <b>&minus;<i>t</i></b>. So each differentiation multiplies the function by &minus;<i>t</i>. "
     "Do it <i>n</i> times and you have multiplied by (&minus;<i>t</i>)<sup><i>n</i></sup> = (&minus;1)<sup><i>n</i></sup><i>t<sup>n</sup></i>, "
     "which is exactly the statement, rearranged. Everything else is bookkeeping. "
     "<b>Write it as a proper induction</b> &mdash; that is what the seven marks are for.")
    steps([
     ("Start from the definition.",
      f'<div class="eq"><i>F</i>(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></div>'
      "Every proof in this unit starts on this line. Write it down first, always."),
     ("Differentiate both sides with respect to <i>s</i> and move the derivative inside.",
      f'<div class="eq">{F("<i>dF</i>","<i>ds</i>")} = {F("<i>d</i>","<i>ds</i>")}{INT}<sub>0</sub><sup>{inf}</sup>'
      f'<i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i> = {INT}<sub>0</sub><sup>{inf}</sup>'
      f'{F("&#8706;","&#8706;<i>s</i>")}\[e<sup>&minus;<i>st</i></sup>\]<i>f</i>(<i>t</i>)&thinsp;<i>dt</i></div>'
      "This step is Leibniz&rsquo;s rule. <b>Say the name</b> &mdash; examiners look for it."),
     ("Do the inner differentiation.",
      f'<div class="eq">{F("&#8706;","&#8706;<i>s</i>")}(<i>e</i><sup>&minus;<i>st</i></sup>) = &minus;<i>t e</i><sup>&minus;<i>st</i></sup></div>'
      "so"
      f'<div class="eq">{F("<i>dF</i>","<i>ds</i>")} = {INT}<sub>0</sub><sup>{inf}</sup>(&minus;<i>t</i>)<i>e</i><sup>&minus;<i>st</i></sup>'
      f'<i>f</i>(<i>t</i>)&thinsp;<i>dt</i> = &minus;{INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup>'
      f'\[t f(t)\]&thinsp;<i>dt</i></div>'),
     ("Recognise the integral on the right &mdash; it <i>is</i> a Laplace transform.",
      f'<div class="eq">{F("<i>dF</i>","<i>ds</i>")} = &minus;<i>L</i>{{<i>t f</i>(<i>t</i>)}} '
      f'&nbsp;&nbsp;&rarr;&nbsp;&nbsp; <i>L</i>{{<i>t f</i>(<i>t</i>)}} = &minus;{F("<i>dF</i>","<i>ds</i>")} '
      f'= (&minus;1)<sup>1</sup>{F("<i>d</i><sup>1</sup><i>F</i>","<i>ds</i><sup>1</sup>")}</div>'
      "<b>This is the result for <i>n</i> = 1 &mdash; the base case of the induction.</b>"),
     ("Assume the result holds for some <i>n</i>.",
      "Inductive hypothesis: suppose that for a particular positive integer <i>n</i>,"
      f'<div class="eq"><i>L</i>{{<i>t<sup>n</sup>f</i>(<i>t</i>)}} = {INT}<sub>0</sub><sup>{inf}</sup>'
      f'<i>e</i><sup>&minus;<i>st</i></sup><i>t<sup>n</sup>f</i>(<i>t</i>)&thinsp;<i>dt</i> = (&minus;1)<sup><i>n</i></sup>'
      f'{F("<i>d<sup>n</sup>F</i>","<i>ds<sup>n</sup></i>")}</div>'),
     ("Differentiate the hypothesis once more.",
      "<b>Left side</b> &mdash; same trick as before, another factor of (&minus;<i>t</i>) comes down:"
      f'<div class="eq">{F("<i>d</i>","<i>ds</i>")}{INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup>'
      f'<i>t<sup>n</sup>f</i>(<i>t</i>)<i>dt</i> = &minus;{INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup>'
      f'<i>t</i><sup><i>n</i>+1</sup><i>f</i>(<i>t</i>)<i>dt</i> = &minus;<i>L</i>{{<i>t</i><sup><i>n</i>+1</sup><i>f</i>(<i>t</i>)}}</div>'
      "<b>Right side:</b>"
      f'<div class="eq">{F("<i>d</i>","<i>ds</i>")}\[(&minus;1)<sup><i>n</i></sup>'
      f'{F("<i>d<sup>n</sup>F</i>","<i>ds<sup>n</sup></i>")}\] = (&minus;1)<sup><i>n</i></sup>'
      f'{F("<i>d</i><sup><i>n</i>+1</sup><i>F</i>","<i>ds</i><sup><i>n</i>+1</sup>")}</div>'),
     ("Equate and tidy.",
      f'<div class="eq">&minus;<i>L</i>{{<i>t</i><sup><i>n</i>+1</sup><i>f</i>(<i>t</i>)}} = (&minus;1)<sup><i>n</i></sup>'
      f'{F("<i>d</i><sup><i>n</i>+1</sup><i>F</i>","<i>ds</i><sup><i>n</i>+1</sup>")}</div>'
      "Multiply both sides by &minus;1:"
      f'<div class="eq"><i>L</i>{{<i>t</i><sup><i>n</i>+1</sup><i>f</i>(<i>t</i>)}} = (&minus;1)<sup><i>n</i>+1</sup>'
      f'{F("<i>d</i><sup><i>n</i>+1</sup><i>F</i>","<i>ds</i><sup><i>n</i>+1</sup>")}</div>'
      "<b>This is exactly the statement with <i>n</i> replaced by <i>n</i>+1.</b>"),
     ("Conclude.",
      "The result holds for <i>n</i> = 1, and whenever it holds for <i>n</i> it also holds for <i>n</i>+1. "
      "<b>By the principle of mathematical induction it holds for every positive integer <i>n</i>.</b> &nbsp;&#8718;")])
    blk("Check your answer","chk",
     f"Test the formula on something you know. Take <i>f</i>(<i>t</i>) = 1, so <i>F</i>(<i>s</i>) = 1/<i>s</i>.<br>"
     f"The rule with <i>n</i> = 2 predicts <i>L</i>{{<i>t</i><sup>2</sup>}} = (&minus;1)<sup>2</sup>"
     f'{F("<i>d</i><sup>2</sup>","<i>ds</i><sup>2</sup>")}(1/<i>s</i>) = {F("2","<i>s</i><sup>3</sup>")}, '
     f"and the standard table also gives <i>L</i>{{<i>t</i><sup>2</sup>}} = 2!/<i>s</i><sup>3</sup> = 2/<i>s</i><sup>3</sup>. &nbsp;&#10003;")
    blk("Watch out","warn",
     f"<ul><li><b>Do not just do the <i>n</i> = 1 case and write &ldquo;similarly&rdquo;.</b> The marks are for the induction. "
     f"State the hypothesis, do the step, state the conclusion.</li>"
     f"<li>Name Leibniz&rsquo;s rule when you move the derivative inside the integral.</li>"
     f"<li>Keep track of the sign. It is (&minus;1)<sup><i>n</i></sup>, not (&minus;1). Each differentiation contributes "
     f"one factor of &minus;1.</li></ul>")

def _s5():
    # ================= 5. HEAVISIDE =================
    sec("II.2","Piecewise function via Heaviside, then its Laplace transform","Unit II &middot; Q3c &middot; 7 marks &middot; 20 minutes")
    blk("The question","qbox",
     "Express &nbsp;<i>f</i>(<i>t</i>) = "+PW([["<i>t</i><sup>2</sup>,","0 &lt; <i>t</i> &lt; 2"],["4<i>t</i>,","2 &lt; <i>t</i> &lt; 4"],["8,","<i>t</i> &gt; 4"]])
     +"&nbsp; in terms of the Heaviside function, and hence find its Laplace transform.")
    blk("Could it appear another way?","alt",
     """<b>The method never changes &mdash; only the pieces do.</b> All four papers set this, with these functions:
    <ul><li><i>t</i><sup>2</sup> / 4<i>t</i> / 8 on (0,2), (2,4), (4,&infin;) &mdash; Apr&nbsp;23 and Mar&nbsp;24, the version solved here</li>
    <li>cos&nbsp;<i>t</i> / cos&nbsp;2<i>t</i> / cos&nbsp;3<i>t</i> on (0,&pi;), (&pi;,2&pi;), (2&pi;,&infin;) &mdash; Jun&nbsp;23.
    Rewriting is easier than it looks: cos(&tau;+&pi;) = &minus;cos&nbsp;&tau;.</li>
    <li>1 / <i>t</i> / <i>t</i><sup>2</sup> on (0,1], (1,2], (2,&infin;) &mdash; Sep&nbsp;23</li></ul>
    <b>Also watch for the reverse question:</b> some papers give you the Heaviside expression and ask for the
    <i>inverse</i> transform, or ask you to sketch <i>f</i>(<i>t</i>). Same skills.""")
    blk("Formulas you need","fbox",
     f"<ul><li><b>The unit step:</b> <i>u</i>(<i>t</i>&minus;<i>a</i>) = 0 for <i>t</i> &lt; <i>a</i>, and 1 for <i>t</i> &ge; <i>a</i>. "
     f"It is a switch that turns on at <i>t</i> = <i>a</i>.</li>"
     f"<li><b>Second shifting theorem:</b> &nbsp;<i>L</i>{{<i>g</i>(<i>t</i>&minus;<i>a</i>)&thinsp;<i>u</i>(<i>t</i>&minus;<i>a</i>)}} "
     f"= <i>e</i><sup>&minus;<i>as</i></sup><i>G</i>(<i>s</i>) &nbsp;where <i>G</i>(<i>s</i>) = <i>L</i>{{<i>g</i>(<i>t</i>)}}</li>"
     f"<li><i>L</i>{{1}} = 1/<i>s</i>, &nbsp;<i>L</i>{{<i>t</i>}} = 1/<i>s</i><sup>2</sup>, &nbsp;<i>L</i>{{<i>t</i><sup>2</sup>}} = 2/<i>s</i><sup>3</sup></li></ul>")
    blk("Why this works","why",
     "Think of the function as switching. It starts as <i>t</i><sup>2</sup>. At <i>t</i> = 2 it must <b>stop</b> being "
     "<i>t</i><sup>2</sup> and <b>start</b> being 4<i>t</i>. You achieve that by adding the difference "
     "(4<i>t</i> &minus; <i>t</i><sup>2</sup>) switched on at <i>t</i> = 2. At <i>t</i> = 4 you add the next difference, "
     "(8 &minus; 4<i>t</i>), switched on at <i>t</i> = 4. Each new piece cancels the old one and installs the new one.<br><br>"
     "<b>The one trap:</b> the second shifting theorem only applies when the thing multiplying <i>u</i>(<i>t</i>&minus;<i>a</i>) "
     "is written as a function of (<i>t</i> &minus; <i>a</i>), not of <i>t</i>. So there is always a rewriting step, and "
     "that is where most marks are lost.")
    steps([
     ("Write the function as a sum of switches.",
      "General pattern: &nbsp;<i>f</i> = (first piece) + (second &minus; first)<i>u</i>(<i>t</i>&minus;<i>a</i><sub>1</sub>) + "
      "(third &minus; second)<i>u</i>(<i>t</i>&minus;<i>a</i><sub>2</sub>) + &hellip;"
      '<div class="eq"><i>f</i>(<i>t</i>) = <i>t</i><sup>2</sup> + (4<i>t</i> &minus; <i>t</i><sup>2</sup>)<i>u</i>(<i>t</i>&minus;2) '
      '+ (8 &minus; 4<i>t</i>)<i>u</i>(<i>t</i>&minus;4)</div>'
      "<b>Sanity check.</b> For <i>t</i> between 0 and 2 both switches are off, so <i>f</i> = <i>t</i><sup>2</sup> &#10003;. "
      "For <i>t</i> between 2 and 4 the first switch is on: <i>f</i> = <i>t</i><sup>2</sup> + 4<i>t</i> &minus; <i>t</i><sup>2</sup> = 4<i>t</i> &#10003;. "
      "For <i>t</i> &gt; 4 both are on: <i>f</i> = 4<i>t</i> + 8 &minus; 4<i>t</i> = 8 &#10003;."),
     ("Transform the first term.",
      '<div class="eq"><i>L</i>{<i>t</i><sup>2</sup>} = 2/<i>s</i><sup>3</sup></div>'
      "No switch on this one, so no shifting is needed."),
     ("Rewrite the second bracket in terms of (<i>t</i> &minus; 2).",
      f"Substitute <i>t</i> = {tau} + 2 (so {tau} = <i>t</i> &minus; 2):"
      f'<div class="eq">4<i>t</i> &minus; <i>t</i><sup>2</sup> = 4({tau}+2) &minus; ({tau}+2)<sup>2</sup></div>'
      f'<div class="eq">= 4{tau} + 8 &minus; ({tau}<sup>2</sup> + 4{tau} + 4) = 4{tau} + 8 &minus; {tau}<sup>2</sup> &minus; 4{tau} &minus; 4 '
      f'= <b>4 &minus; {tau}<sup>2</sup></b></div>'
      f"So the term is <i>g</i>(<i>t</i>&minus;2)<i>u</i>(<i>t</i>&minus;2) with <i>g</i>({tau}) = 4 &minus; {tau}<sup>2</sup>."),
     ("Transform it.",
      f'<div class="eq"><i>G</i>(<i>s</i>) = <i>L</i>{{4 &minus; {tau}<sup>2</sup>}} = {F("4","<i>s</i>")} &minus; {F("2","<i>s</i><sup>3</sup>")}</div>'
      "Apply the second shifting theorem &mdash; multiply by <i>e</i><sup>&minus;2<i>s</i></sup>:"
      f'<div class="eq"><i>e</i><sup>&minus;2<i>s</i></sup>\({F("4","<i>s</i>")} &minus; {F("2","<i>s</i><sup>3</sup>")}\)</div>'),
     ("Rewrite the third bracket in terms of (<i>t</i> &minus; 4).",
      f"Substitute <i>t</i> = {tau} + 4:"
      f'<div class="eq">8 &minus; 4<i>t</i> = 8 &minus; 4({tau}+4) = 8 &minus; 4{tau} &minus; 16 = <b>&minus;8 &minus; 4{tau}</b></div>'
      f"So <i>g</i>({tau}) = &minus;8 &minus; 4{tau}."),
     ("Transform it.",
      f'<div class="eq"><i>G</i>(<i>s</i>) = &minus;{F("8","<i>s</i>")} &minus; {F("4","<i>s</i><sup>2</sup>")}</div>'
      "Multiply by <i>e</i><sup>&minus;4<i>s</i></sup>:"
      f'<div class="eq"><i>e</i><sup>&minus;4<i>s</i></sup>\(&minus;{F("8","<i>s</i>")} &minus; {F("4","<i>s</i><sup>2</sup>")}\)</div>'),
     ("Add the three pieces.",
      f'<div class="eq"><b><i>L</i>{{<i>f</i>(<i>t</i>)}} = {F("2","<i>s</i><sup>3</sup>")} '
      f'+ <i>e</i><sup>&minus;2<i>s</i></sup>\({F("4","<i>s</i>")} &minus; {F("2","<i>s</i><sup>3</sup>")}\) '
      f'+ <i>e</i><sup>&minus;4<i>s</i></sup>\(&minus;{F("8","<i>s</i>")} &minus; {F("4","<i>s</i><sup>2</sup>")}\)</b></div>')])
    blk("Check your answer","chk",
     "Two quick checks.<br><br>"
     "<b>1. The switch check in step 1.</b> Put a value of <i>t</i> in each interval into your Heaviside expression and "
     "confirm you get back the original piece. If that works, the hard half is right.<br><br>"
     "<b>2. Every exponential must match its switch.</b> The term switched on at <i>t</i> = 2 carries "
     "<i>e</i><sup>&minus;2<i>s</i></sup>; the one at <i>t</i> = 4 carries <i>e</i><sup>&minus;4<i>s</i></sup>. "
     "If an exponent does not match its switch point, you have mixed up a term.")
    blk("Watch out","warn",
     f"<ul><li><b>The rewriting step is compulsory.</b> Writing <i>L</i>{{(4<i>t</i>&minus;<i>t</i><sup>2</sup>)<i>u</i>(<i>t</i>&minus;2)}} "
     f"= <i>e</i><sup>&minus;2<i>s</i></sup>&thinsp;<i>L</i>{{4<i>t</i>&minus;<i>t</i><sup>2</sup>}} is <b>wrong</b> and will "
     f"cost you most of the marks. You must convert to a function of {tau} = <i>t</i>&minus;2 first.</li>"
     f"<li>Use <b>differences</b>, not the pieces themselves: it is (4<i>t</i> &minus; <i>t</i><sup>2</sup>), not 4<i>t</i>.</li>"
     f"<li>Expand ({tau}+2)<sup>2</sup> carefully &mdash; it is {tau}<sup>2</sup> + 4{tau} + 4, and the 4{tau} is what cancels.</li></ul>")

def _s6():
    # ================= 6. sin sqrt t =================
    sec("I.2",f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show the cos&nbsp;{sq}<i>t</i> result","Unit I &middot; Q1b &middot; 4 marks &middot; 12 minutes")
    blk("The question","qbox",
     f"Given &nbsp;<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = {F(f'{sq}{pi}','2<i>s</i><sup>3/2</sup>')}<i>e</i><sup>&minus;1/4<i>s</i></sup>, "
     f"&nbsp;show that<br>"
     f'<div class="eq"><i>L</i>{{{F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")}}} = {F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")}'
     f'<i>e</i><sup>&minus;1/4<i>s</i></sup></div>')
    blk("Could it appear another way?","alt",
     """<b>The sin&nbsp;&radic;<i>t</i> family has been set three different ways. All four papers had one of them.</b>
    <ul><li><b>Given the result, derive the other</b> (Jun&nbsp;23 Q1c, Mar&nbsp;24 Q1b, 4&ndash;7 m) &mdash; the version solved here.</li>
    <li><b>&ldquo;Find <i>L</i>{sin&nbsp;&radic;<i>t</i>}&rdquo;</b> (Apr&nbsp;23 Q2a, 6 m) &mdash; you must derive it from scratch. Expand
    sin&nbsp;&radic;<i>t</i> as a power series &radic;<i>t</i> &minus; <i>t</i><sup>3/2</sup>/3! + <i>t</i><sup>5/2</sup>/5! &minus; &hellip;,
    transform term by term using <i>L</i>{<i>t</i><sup><i>n</i></sup>} = &Gamma;(<i>n</i>+1)/<i>s</i><sup><i>n</i>+1</sup>,
    and recognise the resulting series as (&radic;&pi;/2<i>s</i><sup>3/2</sup>)<i>e</i><sup>&minus;1/4<i>s</i></sup>.</li>
    <li><b>&ldquo;Show that <i>L</i>{sin&nbsp;&radic;<i>t</i>} = &hellip;&rdquo;</b> (Sep&nbsp;23 Q2a, 6 m) &mdash; same as above, but the
    target is printed, so you can work towards it.</li></ul>
    <b>If the derivation version appears and you have not prepared it, answer the other question in the unit.</b>""")
    blk("Formulas you need","fbox",
     "<ul><li><b>Transform of a derivative:</b> &nbsp;<i>L</i>{<i>f</i>&prime;(<i>t</i>)} = <i>s F</i>(<i>s</i>) &minus; <i>f</i>(0)</li>"
     f"<li><b>Chain rule:</b> &nbsp;{F('<i>d</i>','<i>dt</i>')}(sin&nbsp;{sq}<i>t</i>) = cos&nbsp;{sq}<i>t</i> &times; "
     f"{F('<i>d</i>','<i>dt</i>')}({sq}<i>t</i>)</li>"
     f"<li>{F('<i>d</i>','<i>dt</i>')}({sq}<i>t</i>) = {F('1',f'2{sq}<i>t</i>')}</li></ul>")
    blk("Why this works","why",
     f"You are given a transform and asked for a different one. The trick is to spot that the <b>function you want is "
     f"just a multiple of the derivative of the function you were given</b>. Differentiating sin&nbsp;{sq}<i>t</i> produces "
     f"cos&nbsp;{sq}<i>t</i> over 2{sq}<i>t</i> &mdash; almost exactly the target, off by a factor of 2. So instead of "
     f"integrating anything, you use the derivative rule, which turns the problem into one multiplication by <i>s</i>.")
    steps([
     ("Name the function and note its value at zero.",
      f"Let &nbsp;<i>f</i>(<i>t</i>) = sin&nbsp;{sq}<i>t</i>. &nbsp;Then <i>F</i>(<i>s</i>) = "
      f"{F(f'{sq}{pi}','2<i>s</i><sup>3/2</sup>')}<i>e</i><sup>&minus;1/4<i>s</i></sup> is what you were given.<br><br>"
      f"<b><i>f</i>(0) = sin&nbsp;0 = 0.</b> Note this now &mdash; it is what makes the next step clean."),
     ("Differentiate <i>f</i> using the chain rule.",
      f'<div class="eq"><i>f</i>&prime;(<i>t</i>) = cos&nbsp;{sq}<i>t</i> &times; {F("1",f"2{sq}<i>t</i>")} '
      f'= {F(f"cos&nbsp;{sq}<i>t</i>",f"2{sq}<i>t</i>")}</div>'),
     ("Spot the relationship to the target.",
      f'<div class="eq">{F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")} = 2 &times; {F(f"cos&nbsp;{sq}<i>t</i>",f"2{sq}<i>t</i>")} '
      f'= 2&thinsp;<i>f</i>&prime;(<i>t</i>)</div>'
      "<b>The function you want is exactly twice the derivative.</b> That is the whole idea of the question."),
     ("Take the Laplace transform of both sides.",
      f'<div class="eq"><i>L</i>{{{F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")}}} = 2&thinsp;<i>L</i>{{<i>f</i>&prime;(<i>t</i>)}}</div>'
      "Apply the derivative rule <i>L</i>{<i>f</i>&prime;} = <i>sF</i>(<i>s</i>) &minus; <i>f</i>(0):"
      f'<div class="eq">= 2[<i>s F</i>(<i>s</i>) &minus; <i>f</i>(0)] = 2<i>s F</i>(<i>s</i>) &minus; 0 = 2<i>s F</i>(<i>s</i>)</div>'),
     ("Substitute the given transform and simplify.",
      f'<div class="eq">= 2<i>s</i> &times; {F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")}<i>e</i><sup>&minus;1/4<i>s</i></sup></div>'
      "The 2 cancels the 2, and <i>s</i> &divide; <i>s</i><sup>3/2</sup> = <i>s</i><sup>1&minus;3/2</sup> = <i>s</i><sup>&minus;1/2</sup>:"
      f'<div class="eq">= {F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")}<i>e</i><sup>&minus;1/4<i>s</i></sup> &nbsp;&nbsp;&#8718;</div>')])
    blk("Check your answer","chk",
     f"The exponential factor <i>e</i><sup>&minus;1/4<i>s</i></sup> is untouched throughout &mdash; it should appear "
     f"unchanged in your final line. Only the power of <i>s</i> and the constant change. "
     f"If your exponential has moved, you have differentiated the wrong thing.<br><br>"
     f"The index arithmetic: <i>s</i><sup>1</sup> &divide; <i>s</i><sup>3/2</sup> = <i>s</i><sup>&minus;1/2</sup> = "
     f"1/{sq}<i>s</i> = 1/<i>s</i><sup>1/2</sup>. &nbsp;&#10003;")
    blk("Watch out","warn",
     f"<ul><li><b>Do not try to derive <i>L</i>{{sin&nbsp;{sq}<i>t</i>}} from scratch.</b> It is <i>given</i>. Deriving it "
     f"needs a series expansion and will eat your whole exam.</li>"
     f"<li>You must state <i>f</i>(0) = 0. If you leave the &minus;<i>f</i>(0) term dangling you lose a mark, even though it is zero.</li>"
     f"<li>The factor is <b>2</b>, not &frac12;. Differentiating gives a 2 in the <i>denominator</i>, so you multiply by 2 to remove it.</li></ul>")

def _s8():
    # ================= 8. ODEs =================
    sec("II.3","Solving ODEs and systems of ODEs by Laplace transforms","Unit II &middot; Q3d or Q4d &middot; 7 marks &middot; 22 minutes")
    blk("The question","qbox",
     f"<b>(a) A system.</b> &nbsp;{F('<i>dx</i>','<i>dt</i>')} &minus; 2<i>y</i> = cos&nbsp;2<i>t</i>, &nbsp;&nbsp;"
     f"{F('<i>dy</i>','<i>dt</i>')} + 2<i>x</i> = sin&nbsp;2<i>t</i>, &nbsp;given <i>x</i>(0) = 1, <i>y</i>(0) = 0.<br><br>"
     f"<b>(b) A single ODE.</b> &nbsp;<i>y</i>&Prime; + 4<i>y</i>&prime; + 3<i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup>, "
     f"&nbsp;given <i>y</i>(0) = 0, <i>y</i>&prime;(0) = 0.<br><br>"
     f"<b>(c) A circuit.</b> &nbsp;A voltage <i>Ee</i><sup>&minus;<i>at</i></sup> is applied at <i>t</i> = 0 to a circuit of "
     f"inductance <i>L</i> and resistance <i>R</i>. Show the current is "
     f"{F('<i>E</i>','<i>R</i> &minus; <i>aL</i>')}(<i>e</i><sup>&minus;<i>at</i></sup> &minus; <i>e</i><sup>&minus;<i>Rt/L</i></sup>).")
    blk("Could it appear another way?","alt",
     """<b>Six different versions have appeared. Every one uses the identical method.</b>
    <ul><li><b>Simultaneous, cos/sin forcing</b> &mdash; Mar&nbsp;24 Q4d, solved here.</li>
    <li><b>The &ldquo;particle on a plane curve&rdquo; version</b> &mdash; Apr&nbsp;23 Q3c and Jun&nbsp;23 Q4c.
    Same system, but it then asks you to <b>eliminate <i>t</i></b> from <i>x</i>(<i>t</i>) and <i>y</i>(<i>t</i>) to show the
    path is 4<i>x</i><sup>2</sup> + 4<i>xy</i> + 5<i>y</i><sup>2</sup> = 4. Solve as usual, then substitute into the
    quadratic and use sin<sup>2</sup> + cos<sup>2</sup> = 1.</li>
    <li><b><i>y</i>&Prime; + 4<i>y</i>&prime; + 3<i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup></b> with
    <i>y</i>(0) = <i>y</i>&prime;(0) = 0 (Jun&nbsp;23) <b>or</b> <i>y</i>(0) = <i>y</i>&prime;(0) = 1 (Sep&nbsp;23).
    Only the initial conditions change &mdash; but they change the whole partial-fraction stage, so do both.</li>
    <li><b>Third order:</b> <i>y</i>&#8244; + 2<i>y</i>&Prime; &minus; <i>y</i>&prime; &minus; 2<i>y</i> = 0 with
    <i>y</i>(0)=0, <i>y</i>&prime;(0)=0, <i>y</i>&Prime;(0)=6 (Apr&nbsp;23). You need
    <i>L</i>{<i>y</i>&#8244;} = <i>s</i><sup>3</sup><i>Y</i> &minus; <i>s</i><sup>2</sup><i>y</i>(0) &minus; <i>sy</i>&prime;(0) &minus; <i>y</i>&Prime;(0).</li>
    <li><b>Another system:</b> <i>dx</i>/<i>dt</i> &minus; <i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup>,
    <i>dy</i>/<i>dt</i> + <i>x</i> = sin&nbsp;<i>t</i> (Sep&nbsp;23).</li>
    <li><b>The circuit</b> &mdash; Mar&nbsp;24 Q3d, solved here as part (c).</li></ul>""")
    blk("Formulas you need","fbox",
     f"<ul><li><i>L</i>{{<i>y</i>&prime;}} = <i>sY</i> &minus; <i>y</i>(0)</li>"
     f"<li><i>L</i>{{<i>y</i>&Prime;}} = <i>s</i><sup>2</sup><i>Y</i> &minus; <i>s y</i>(0) &minus; <i>y</i>&prime;(0)</li>"
     f"<li><i>L</i>{{cos&nbsp;<i>at</i>}} = <i>s</i>/(<i>s</i><sup>2</sup>+<i>a</i><sup>2</sup>), &nbsp;"
     f"<i>L</i>{{sin&nbsp;<i>at</i>}} = <i>a</i>/(<i>s</i><sup>2</sup>+<i>a</i><sup>2</sup>)</li>"
     f"<li><i>L</i>{{<i>e</i><sup>&minus;<i>at</i></sup>}} = 1/(<i>s</i>+<i>a</i>), &nbsp;"
     f"<i>L</i>{{<i>t e</i><sup>&minus;<i>at</i></sup>}} = 1/(<i>s</i>+<i>a</i>)<sup>2</sup></li></ul>")
    blk("Why this works","why",
     "A differential equation is hard because it mixes a function with its derivatives. The Laplace transform converts "
     "derivatives into <b>multiplication by <i>s</i></b>, which turns the whole differential equation into an ordinary "
     "algebraic one. You solve the algebra for <i>Y</i>(<i>s</i>), then transform back. The initial conditions are not an "
     "afterthought &mdash; they enter automatically at the transform step, which is why this method is often faster than "
     "the classical one.<br><br>"
     "<b>For a system</b>, both equations transform, and you end up with two linear equations in <i>X</i>(<i>s</i>) and "
     "<i>Y</i>(<i>s</i>). Solve them the same way you would solve any pair of simultaneous equations, then invert each.")
    steps([
     ("(a) Transform both equations.",
      "Write <i>X</i> = <i>L</i>{<i>x</i>} and <i>Y</i> = <i>L</i>{<i>y</i>}. Using <i>x</i>(0) = 1 and <i>y</i>(0) = 0:"
      f'<div class="eq"><i>sX</i> &minus; 1 &minus; 2<i>Y</i> = {F("<i>s</i>","<i>s</i><sup>2</sup>+4")} '
      f'&nbsp;&nbsp;&rarr;&nbsp;&nbsp; <i>sX</i> &minus; 2<i>Y</i> = 1 + {F("<i>s</i>","<i>s</i><sup>2</sup>+4")} &nbsp;&hellip;(i)</div>'
      f'<div class="eq"><i>sY</i> + 2<i>X</i> = {F("2","<i>s</i><sup>2</sup>+4")} &nbsp;&nbsp;&rarr;&nbsp;&nbsp; '
      f'2<i>X</i> + <i>sY</i> = {F("2","<i>s</i><sup>2</sup>+4")} &nbsp;&hellip;(ii)</div>'),
     ("Eliminate <i>Y</i>.",
      "Multiply (i) by <i>s</i> and (ii) by 2, then add &mdash; the <i>Y</i> terms cancel:"
      f'<div class="eq"><i>s</i>&times;(i): &nbsp; <i>s</i><sup>2</sup><i>X</i> &minus; 2<i>sY</i> = <i>s</i> + '
      f'{F("<i>s</i><sup>2</sup>","<i>s</i><sup>2</sup>+4")}</div>'
      f'<div class="eq">2&times;(ii): &nbsp; 4<i>X</i> + 2<i>sY</i> = {F("4","<i>s</i><sup>2</sup>+4")}</div>'
      f'<div class="eq">Add: &nbsp; (<i>s</i><sup>2</sup>+4)<i>X</i> = <i>s</i> + '
      f'{F("<i>s</i><sup>2</sup> + 4","<i>s</i><sup>2</sup>+4")} = <i>s</i> + 1</div>'
      "<b>The right-hand side simplified beautifully.</b> So"
      f'<div class="eq"><i>X</i> = {F("<i>s</i> + 1","<i>s</i><sup>2</sup>+4")}</div>'),
     ("Invert to get <i>x</i>(<i>t</i>).",
      "Split the fraction:"
      f'<div class="eq"><i>X</i> = {F("<i>s</i>","<i>s</i><sup>2</sup>+4")} + {F("1","<i>s</i><sup>2</sup>+4")} '
      f'= {F("<i>s</i>","<i>s</i><sup>2</sup>+4")} + {F("1","2")}&thinsp;&middot;&thinsp;{F("2","<i>s</i><sup>2</sup>+4")}</div>'
      "The second term needed a 2 on top to match the sin formula, so we put in &frac12; outside to compensate."
      f'<div class="eq"><b><i>x</i>(<i>t</i>) = cos&nbsp;2<i>t</i> + {F("1","2")}sin&nbsp;2<i>t</i></b></div>'),
     ("Back-substitute for <i>Y</i>.",
      "From (ii): &nbsp;<i>sY</i> = "+F("2","<i>s</i><sup>2</sup>+4")+" &minus; 2<i>X</i>"
      f'<div class="eq">= {F("2","<i>s</i><sup>2</sup>+4")} &minus; {F("2(<i>s</i>+1)","<i>s</i><sup>2</sup>+4")} '
      f'= {F("2 &minus; 2<i>s</i> &minus; 2","<i>s</i><sup>2</sup>+4")} = {F("&minus;2<i>s</i>","<i>s</i><sup>2</sup>+4")}</div>'
      "Divide by <i>s</i>:"
      f'<div class="eq"><i>Y</i> = {F("&minus;2","<i>s</i><sup>2</sup>+4")} &nbsp;&nbsp;&rarr;&nbsp;&nbsp; '
      f'<b><i>y</i>(<i>t</i>) = &minus;sin&nbsp;2<i>t</i></b></div>'),
     ("(b) Transform the single ODE.",
      "With <i>y</i>(0) = 0 and <i>y</i>&prime;(0) = 0, both boundary terms vanish:"
      f'<div class="eq"><i>s</i><sup>2</sup><i>Y</i> + 4<i>sY</i> + 3<i>Y</i> = {F("1","<i>s</i>+1")}</div>'
      f'<div class="eq">(<i>s</i><sup>2</sup> + 4<i>s</i> + 3)<i>Y</i> = {F("1","<i>s</i>+1")} '
      f'&nbsp;&nbsp;&rarr;&nbsp;&nbsp; (<i>s</i>+1)(<i>s</i>+3)<i>Y</i> = {F("1","<i>s</i>+1")}</div>'
      f'<div class="eq"><i>Y</i> = {F("1","(<i>s</i>+1)<sup>2</sup>(<i>s</i>+3)")}</div>'
      "<b>Note the repeated factor</b> &mdash; the (<i>s</i>+1) from the forcing term meets the (<i>s</i>+1) from the "
      "characteristic polynomial and gives a square."),
     ("Partial fractions.",
      f'<div class="eq">{F("1","(<i>s</i>+1)<sup>2</sup>(<i>s</i>+3)")} = {F("<i>A</i>","<i>s</i>+1")} '
      f'+ {F("<i>B</i>","(<i>s</i>+1)<sup>2</sup>")} + {F("<i>C</i>","<i>s</i>+3")}</div>'
      "Multiply through by (<i>s</i>+1)<sup>2</sup>(<i>s</i>+3):"
      '<div class="eq">1 = <i>A</i>(<i>s</i>+1)(<i>s</i>+3) + <i>B</i>(<i>s</i>+3) + <i>C</i>(<i>s</i>+1)<sup>2</sup></div>'
      "Put <i>s</i> = &minus;1: &nbsp;1 = <i>B</i>(2) &nbsp;&rarr;&nbsp; <b><i>B</i> = &frac12;</b><br>"
      "Put <i>s</i> = &minus;3: &nbsp;1 = <i>C</i>(4) &nbsp;&rarr;&nbsp; <b><i>C</i> = &frac14;</b><br>"
      "Put <i>s</i> = 0: &nbsp;1 = 3<i>A</i> + 3(&frac12;) + &frac14; &nbsp;&rarr;&nbsp; 3<i>A</i> = 1 &minus; &sup7;&frasl;&#8324; "
      "= &minus;&frac34; &nbsp;&rarr;&nbsp; <b><i>A</i> = &minus;&frac14;</b>"),
     ("Invert term by term.",
      f'<div class="eq"><i>Y</i> = &minus;{F("1","4")}&middot;{F("1","<i>s</i>+1")} + {F("1","2")}&middot;'
      f'{F("1","(<i>s</i>+1)<sup>2</sup>")} + {F("1","4")}&middot;{F("1","<i>s</i>+3")}</div>'
      f'<div class="eq"><b><i>y</i>(<i>t</i>) = &minus;{F("1","4")}<i>e</i><sup>&minus;<i>t</i></sup> '
      f'+ {F("1","2")}<i>t e</i><sup>&minus;<i>t</i></sup> + {F("1","4")}<i>e</i><sup>&minus;3<i>t</i></sup></b></div>'),
     ("(c) The circuit &mdash; write the equation first.",
      "Kirchhoff&rsquo;s voltage law for a series <i>LR</i> circuit gives"
      f'<div class="eq"><i>L</i>{F("<i>di</i>","<i>dt</i>")} + <i>Ri</i> = <i>Ee</i><sup>&minus;<i>at</i></sup>, '
      f'&nbsp;&nbsp;<i>i</i>(0) = 0</div>'
      "Transform, using <i>i</i>(0) = 0:"
      f'<div class="eq"><i>L</i>(<i>sI</i>) + <i>RI</i> = {F("<i>E</i>","<i>s</i>+<i>a</i>")} '
      f'&nbsp;&rarr;&nbsp; <i>I</i> = {F("<i>E</i>","(<i>s</i>+<i>a</i>)(<i>Ls</i>+<i>R</i>)")}</div>'),
     ("Split and invert.",
      f"Take <i>L</i> out of the second bracket: &nbsp;<i>I</i> = {F('<i>E</i>/<i>L</i>','(<i>s</i>+<i>a</i>)(<i>s</i>+<i>R</i>/<i>L</i>)')}<br><br>"
      f"Use the standard split &nbsp;{F('1','(<i>s</i>+<i>p</i>)(<i>s</i>+<i>q</i>)')} = "
      f"{F('1','<i>q</i>&minus;<i>p</i>')}&#91;{F('1','<i>s</i>+<i>p</i>')} &minus; {F('1','<i>s</i>+<i>q</i>')}&#93; "
      f"with <i>p</i> = <i>a</i>, <i>q</i> = <i>R</i>/<i>L</i>. Since <i>q</i> &minus; <i>p</i> = (<i>R</i>&minus;<i>aL</i>)/<i>L</i>, "
      f"the <i>L</i>&rsquo;s cancel and the constant becomes <i>E</i>/(<i>R</i>&minus;<i>aL</i>):"
      f'<div class="eq"><i>I</i> = {F("<i>E</i>","<i>R</i>&minus;<i>aL</i>")}&#91;{F("1","<i>s</i>+<i>a</i>")} &minus; '
      f'{F("1","<i>s</i>+<i>R</i>/<i>L</i>")}&#93;</div>'
      f'<div class="eq"><b><i>i</i>(<i>t</i>) = {F("<i>E</i>","<i>R</i>&minus;<i>aL</i>")}'
      f'(<i>e</i><sup>&minus;<i>at</i></sup> &minus; <i>e</i><sup>&minus;<i>Rt/L</i></sup>)</b> &nbsp;&nbsp;&#8718;</div>')])
    blk("Check your answer","chk",
     f"<b>Always substitute back.</b> It is fast and it catches sign errors.<br><br>"
     f"<b>(a)</b> <i>x</i> = cos&nbsp;2<i>t</i> + &frac12;sin&nbsp;2<i>t</i>, &nbsp;<i>y</i> = &minus;sin&nbsp;2<i>t</i>.<br>"
     f"&nbsp;&nbsp;<i>x</i>&prime; = &minus;2sin&nbsp;2<i>t</i> + cos&nbsp;2<i>t</i>, so <i>x</i>&prime; &minus; 2<i>y</i> = "
     f"&minus;2sin&nbsp;2<i>t</i> + cos&nbsp;2<i>t</i> + 2sin&nbsp;2<i>t</i> = cos&nbsp;2<i>t</i> &nbsp;&#10003;<br>"
     f"&nbsp;&nbsp;<i>y</i>&prime; = &minus;2cos&nbsp;2<i>t</i>, so <i>y</i>&prime; + 2<i>x</i> = &minus;2cos&nbsp;2<i>t</i> "
     f"+ 2cos&nbsp;2<i>t</i> + sin&nbsp;2<i>t</i> = sin&nbsp;2<i>t</i> &nbsp;&#10003;<br>"
     f"&nbsp;&nbsp;<i>x</i>(0) = 1 &#10003;, &nbsp;<i>y</i>(0) = 0 &#10003;<br><br>"
     f"<b>(b)</b> <i>y</i>(0) = &minus;&frac14; + 0 + &frac14; = 0 &#10003;. And "
     f"<i>y</i>&prime;(0) = &frac14; + &frac12; &minus; &frac34; = 0 &#10003;. Both initial conditions recovered.")
    blk("Watch out","warn",
     "<ul><li><b>Put the initial conditions in at the transform step</b>, not at the end. That is the whole advantage of "
     "the method; forgetting them gives you a general solution with unknown constants and no marks.</li>"
     "<li><i>L</i>{<i>y</i>&Prime;} has <b>two</b> boundary terms: &minus;<i>sy</i>(0) <b>and</b> &minus;<i>y</i>&prime;(0). "
     "Dropping the second is the most common error in this question.</li>"
     "<li>When the forcing term shares a root with the characteristic polynomial (as in (b)), you get a "
     "<b>repeated factor</b> and the partial fractions need both <i>A</i>/(<i>s</i>+1) and <i>B</i>/(<i>s</i>+1)<sup>2</sup>.</li>"
     "<li>In a system, solve for one transform completely, then <b>substitute back</b> into the simpler of the two "
     "equations to get the other. Do not eliminate twice.</li></ul>")

def _s9():
    # ================= 9. SVD =================
    sec("V.4","Singular Value Decomposition","Unit V &middot; Q9c &middot; 10 marks &middot; 22 minutes")
    blk("The question","qbox", f"Find a singular value decomposition of &nbsp;<i>A</i> = {M([['1','1'],['3',sp+'3']])}")
    blk("Could it appear another way?","alt",
     """<b>SVD appeared in all four papers, with matrices of three different shapes.</b>
    <ul><li><b>2&times;2 [[1,1],[3,&minus;3]]</b> &mdash; Jun&nbsp;23 and Mar&nbsp;24. Solved here.</li>
    <li><b>3&times;2 [[1,&minus;1],[&minus;2,2],[2,&minus;2]]</b> &mdash; Apr&nbsp;23. Here <i>A</i><sup>T</sup><i>A</i> is 2&times;2
    (easy), but <i>U</i> is 3&times;3, so you get only <b>two</b> columns from
    <i>A</i><b>v</b><sub><i>i</i></sub>/&sigma;<sub><i>i</i></sub> and must find the third as any unit vector orthogonal to
    both. &Sigma; is 3&times;2 with a row of zeros at the bottom.</li>
    <li><b>2&times;3 [[4,11,14],[8,7,&minus;2]]</b> &mdash; Sep&nbsp;23. Now <i>A</i><sup>T</sup><i>A</i> is 3&times;3, so
    <i>V</i> is 3&times;3 with <b>three</b> eigenvectors, one of which belongs to eigenvalue 0. &Sigma; is 2&times;3.</li></ul>
    <b>Rule for the shapes:</b> <i>U</i> is <i>m</i>&times;<i>m</i>, &Sigma; is <i>m</i>&times;<i>n</i>, <i>V</i> is
    <i>n</i>&times;<i>n</i>. Write these down before you start &mdash; it tells you how many vectors you need.""")
    blk("Formulas you need","fbox",
     f"<b>Goal:</b> write <i>A</i> = <i>U</i>&Sigma;<i>V</i><sup>T</sup>."
     f"<ul><li>Form <i>A</i><sup>T</sup><i>A</i> (always square and symmetric).</li>"
     f"<li>Its eigenvalues {lm}<sub>1</sub> &ge; {lm}<sub>2</sub> &ge; &hellip; are all &ge; 0. "
     f"The <b>singular values</b> are {sg}<sub><i>i</i></sub> = {sq}{lm}<sub><i>i</i></sub>.</li>"
     f"<li>The unit eigenvectors of <i>A</i><sup>T</sup><i>A</i> are the columns of <b><i>V</i></b> "
     f"(largest eigenvalue first).</li>"
     f"<li>The columns of <b><i>U</i></b> come from &nbsp;<b>u</b><sub><i>i</i></sub> = "
     f"{F('<i>A</i><b>v</b><sub><i>i</i></sub>','{sg}<sub><i>i</i></sub>'.replace('{sg}',sg))}</li>"
     f"<li>&Sigma; is the same shape as <i>A</i>, with {sg}<sub>1</sub>, {sg}<sub>2</sub>, &hellip; down the diagonal and zeros elsewhere.</li></ul>")
    blk("Why this works","why",
     f"Any matrix, even a non-square one, can be broken into three simple actions: a rotation (<i>V</i><sup>T</sup>), a "
     f"stretch along the axes (&Sigma;), and another rotation (<i>U</i>). Finding those pieces directly is hard, but "
     f"<i>A</i><sup>T</sup><i>A</i> is symmetric, and symmetric matrices are easy &mdash; real eigenvalues, orthogonal "
     f"eigenvectors. So you find <i>V</i> from <i>A</i><sup>T</sup><i>A</i>, take square roots for the stretch factors, "
     f"and then <i>U</i> falls out of <i>A</i><b>v</b><sub><i>i</i></sub> = {sg}<sub><i>i</i></sub><b>u</b><sub><i>i</i></sub>. "
     f"<b>There is no calculus in this question at all</b> &mdash; it is eigenvectors, done twice.")
    steps([
     ("Compute <i>A</i><sup>T</sup><i>A</i>.",
      f'<div class="eq"><i>A</i><sup>T</sup> = {M([["1","3"],["1",sp+"3"]])}, &nbsp;&nbsp; '
      f'<i>A</i><sup>T</sup><i>A</i> = {M([["1","3"],["1",sp+"3"]])}{M([["1","1"],["3",sp+"3"]])}</div>'
      "Entry (1,1): (1)(1) + (3)(3) = 10<br>"
      "Entry (1,2): (1)(1) + (3)(&minus;3) = 1 &minus; 9 = &minus;8<br>"
      "Entry (2,1): (1)(1) + (&minus;3)(3) = &minus;8<br>"
      "Entry (2,2): (1)(1) + (&minus;3)(&minus;3) = 10"
      f'<div class="eq"><i>A</i><sup>T</sup><i>A</i> = {M([["10",sp+"8"],[sp+"8","10"]])}</div>'
      "It came out symmetric, which is the check that you multiplied correctly."),
     ("Find its eigenvalues.",
      f'<div class="eq">det({M([["10&minus;"+lm,sp+"8"],[sp+"8","10&minus;"+lm]])}) = (10&minus;{lm})<sup>2</sup> &minus; 64 = 0</div>'
      f"So (10 &minus; {lm})<sup>2</sup> = 64, giving 10 &minus; {lm} = &plusmn;8:"
      f'<div class="eq"><b>{lm}<sub>1</sub> = 18, &nbsp;&nbsp;{lm}<sub>2</sub> = 2</b></div>'
      f"<b>Shortcut worth knowing:</b> for a 2&times;2 of the form {M([['<i>a</i>','<i>b</i>'],['<i>b</i>','<i>a</i>']])} "
      f"the eigenvalues are always <i>a</i> + <i>b</i> and <i>a</i> &minus; <i>b</i>."),
     ("Take square roots to get the singular values.",
      f'<div class="eq">{sg}<sub>1</sub> = {sq}18 = <b>3{sq}2</b>, &nbsp;&nbsp;&nbsp; {sg}<sub>2</sub> = <b>{sq}2</b></div>'
      f"Always list them <b>largest first</b>."),
     (f"Find the eigenvectors of <i>A</i><sup>T</sup><i>A</i> &mdash; these give <i>V</i>.",
      f"<b>For {lm} = 18:</b> &nbsp;(<i>A</i><sup>T</sup><i>A</i> &minus; 18<i>I</i>)<b>v</b> = <b>0</b> gives"
      f'<div class="eq">&minus;8<i>v</i><sub>1</sub> &minus; 8<i>v</i><sub>2</sub> = 0 &nbsp;&rarr;&nbsp; '
      f'<i>v</i><sub>1</sub> = &minus;<i>v</i><sub>2</sub> &nbsp;&rarr;&nbsp; <b>v</b><sub>1</sub> = {V(["1",sp+"1"])}</div>'
      f"<b>For {lm} = 2:</b> &nbsp;8<i>v</i><sub>1</sub> &minus; 8<i>v</i><sub>2</sub> = 0 &nbsp;&rarr;&nbsp; "
      f"<i>v</i><sub>1</sub> = <i>v</i><sub>2</sub> &nbsp;&rarr;&nbsp; <b>v</b><sub>2</sub> = {V(['1','1'])}<br><br>"
      f"Both have length {sq}2, so normalise by dividing by {sq}2:"
      f'<div class="eq"><i>V</i> = {F("1",sq+"2")}{M([["1","1"],[sp+"1","1"]])}</div>'),
     (f"Get the columns of <i>U</i> from &nbsp;<b>u</b><sub><i>i</i></sub> = <i>A</i><b>v</b><sub><i>i</i></sub> / {sg}<sub><i>i</i></sub>.",
      f"<b>First column.</b> &nbsp;<i>A</i>&thinsp;{V(['1',sp+'1'])} = {V(['1&minus;1','3+3'])} = {V(['0','6'])}<br><br>"
      f"So <i>A</i><b>v</b><sub>1</sub> = {F('1',sq+'2')}{V(['0','6'])}, and dividing by {sg}<sub>1</sub> = 3{sq}2:"
      f'<div class="eq"><b>u</b><sub>1</sub> = {F("1",sq+"2 &middot; 3"+sq+"2")}{V(["0","6"])} '
      f'= {F("1","6")}{V(["0","6"])} = {V(["0","1"])}</div>'
      f"<b>Second column.</b> &nbsp;<i>A</i>&thinsp;{V(['1','1'])} = {V(['1+1','3&minus;3'])} = {V(['2','0'])}<br><br>"
      f'<div class="eq"><b>u</b><sub>2</sub> = {F("1",sq+"2 &middot; "+sq+"2")}{V(["2","0"])} '
      f'= {F("1","2")}{V(["2","0"])} = {V(["1","0"])}</div>'),
     ("Assemble the three matrices.",
      f'<div class="eq"><i>U</i> = {M([["0","1"],["1","0"]])}, &nbsp;&nbsp; '
      f'&Sigma; = {M(["3"+sq+"2","0"]) if False else M([["3"+sq+"2","0"],["0",sq+"2"]])}, &nbsp;&nbsp; '
      f'<i>V</i> = {F("1",sq+"2")}{M([["1","1"],[sp+"1","1"]])}</div>'
      f'<div class="eq"><b><i>A</i> = <i>U</i>&Sigma;<i>V</i><sup>T</sup></b></div>')])
    blk("Check your answer","chk",
     f"Multiply the three back together. Take <i>V</i><sup>T</sup> = {F('1',sq+'2')}{M([['1',sp+'1'],['1','1']])}.<br><br>"
     f"First &Sigma;<i>V</i><sup>T</sup> = {F('1',sq+'2')}{M([['3'+sq+'2','0'],['0',sq+'2']])}{M([['1',sp+'1'],['1','1']])} "
     f"= {M([['3',sp+'3'],['1','1']])}<br><br>"
     f"Then <i>U</i>(&Sigma;<i>V</i><sup>T</sup>) = {M([['0','1'],['1','0']])}{M([['3',sp+'3'],['1','1']])} "
     f"= {M([['1','1'],['3',sp+'3']])} = <i>A</i> &nbsp;&#10003;<br><br>"
     f"<b>Two faster checks if you are short of time:</b> the singular values squared must sum to the sum of all "
     f"<i>a<sub>ij</sub></i><sup>2</sup> &mdash; here 18 + 2 = 20 and 1+1+9+9 = 20 &#10003;. And "
     f"{sg}<sub>1</sub>{sg}<sub>2</sub> = |det <i>A</i>| &mdash; here 3{sq}2 &middot; {sq}2 = 6 and "
     f"|det <i>A</i>| = |&minus;3&minus;3| = 6 &#10003;.")
    blk("Watch out","warn",
     f"<ul><li>Use <i>A</i><sup>T</sup><i>A</i>, <b>not</b> <i>AA</i><sup>T</sup>, to find <i>V</i>. "
     f"(<i>AA</i><sup>T</sup> would give you <i>U</i> directly, but then the columns can come out with the wrong signs.)</li>"
     f"<li>The singular values are the <b>square roots</b> of the eigenvalues. Writing &Sigma; = diag(18, 2) is a "
     f"very common and very costly slip.</li>"
     f"<li>Order matters: largest singular value first, and the columns of <i>V</i> must be in the matching order.</li>"
     f"<li>Do not forget to <b>normalise</b> the eigenvectors before putting them into <i>V</i>.</li></ul>")

def _s10():
    # ================= 10. ORTHOGONAL DIAGONALIZATION =================
    sec("V.3","Orthogonal diagonalization","Unit V &middot; Q10c &middot; 10 marks &middot; 25 minutes")
    blk("The question","qbox",
     f"Orthogonally diagonalize &nbsp;<i>A</i> = {M([['3',sp+'1','1'],[sp+'1','5',sp+'1'],['1',sp+'1','3']])}<br><br>"
     f"<b>This exact matrix appeared in three of the four past papers.</b>")
    blk("Could it appear another way?","alt",
     """<b>The same 3&times;3 came up three times out of four.</b>
    <ul><li><b>[[3,&minus;1,1],[&minus;1,5,&minus;1],[1,&minus;1,3]]</b> &mdash; Apr&nbsp;23, Jun&nbsp;23, Mar&nbsp;24. Solved here.</li>
    <li><b>The 2&times;2 [[3,1],[1,3]]</b> &mdash; Sep&nbsp;23. Much quicker: eigenvalues 4 and 2, eigenvectors (1,1) and (1,&minus;1).</li></ul>
    <b>The version that needs Gram&ndash;Schmidt.</b> If an eigenvalue is <b>repeated</b>, its eigenspace is 2-dimensional
    and the two eigenvectors you find will generally not be perpendicular. Then you must apply Gram&ndash;Schmidt
    <b>within that eigenspace</b> before normalising. Vectors from <i>different</i> eigenvalues are still automatically
    orthogonal. <b>Check for a repeated root before you assume you can skip it.</b>
    <br><br><b>The close relative:</b> &ldquo;diagonalize <i>A</i> and hence find <i>A</i><sup><i>n</i></sup>&rdquo; appeared in
    three papers (Apr&nbsp;23 <i>A</i><sup>4</sup>, Jun&nbsp;23 <i>A</i><sup>5</sup>, Sep&nbsp;23 <i>A</i><sup>6</sup>) but
    <b>not</b> in Mar&nbsp;24 &mdash; so it is overdue. Same eigenvector work, then
    <i>A<sup>n</sup></i> = <i>PD<sup>n</sup>P</i><sup>&minus;1</sup> with <i>D<sup>n</sup></i> = diag(&lambda;<sub>1</sub><sup><i>n</i></sup>, &hellip;).""")
    blk("Formulas you need","fbox",
     f"<ul><li>Eigenvalues from &nbsp;det(<i>A</i> &minus; {lm}<i>I</i>) = 0</li>"
     f"<li>Eigenvectors from &nbsp;(<i>A</i> &minus; {lm}<i>I</i>)<b>x</b> = <b>0</b></li>"
     f"<li>For a <b>symmetric</b> matrix, eigenvectors belonging to <b>different</b> eigenvalues are automatically orthogonal.</li>"
     f"<li>Normalise each eigenvector (divide by its length) and use them as the columns of <i>P</i>. Then "
     f"<b><i>P</i><sup>T</sup><i>AP</i> = <i>D</i></b> = diag({lm}<sub>1</sub>, {lm}<sub>2</sub>, {lm}<sub>3</sub>).</li></ul>")
    blk("Why this works","why",
     f"Ordinary diagonalization gives <i>P</i><sup>&minus;1</sup><i>AP</i> = <i>D</i>, and inverting <i>P</i> is work. "
     f"But when <i>A</i> is symmetric you can choose the eigenvectors to be mutually perpendicular and of unit length. "
     f"For such a matrix the inverse is just the transpose, so <i>P</i><sup>&minus;1</sup> = <i>P</i><sup>T</sup> and no "
     f"inversion is needed. That is the whole point of the word &ldquo;orthogonally&rdquo;.<br><br>"
     f"<b>Here all three eigenvalues are different</b>, so the orthogonality is free &mdash; you do not need Gram&ndash;Schmidt. "
     f"<b>Say this in your answer.</b> You would only need Gram&ndash;Schmidt if an eigenvalue repeated.")
    steps([
     ("Form the characteristic equation.",
      f'<div class="eq">det{M([["3&minus;"+lm,sp+"1","1"],[sp+"1","5&minus;"+lm,sp+"1"],["1",sp+"1","3&minus;"+lm]])} = 0</div>'
      "Expanding along the first row gives"
      f'<div class="eq">{lm}<sup>3</sup> &minus; 11{lm}<sup>2</sup> + 36{lm} &minus; 36 = 0</div>'
      "<b>Shortcut for checking:</b> the coefficient 11 must equal the trace (3 + 5 + 3 = 11 &#10003;), and the constant "
      "36 must equal det <i>A</i> (&#10003;)."),
     ("Solve it &mdash; try small factors of 36.",
      f"Try {lm} = 2: &nbsp;8 &minus; 44 + 72 &minus; 36 = 0 &nbsp;&#10003;, so ({lm} &minus; 2) is a factor.<br><br>"
      f"Divide out: &nbsp;{lm}<sup>3</sup> &minus; 11{lm}<sup>2</sup> + 36{lm} &minus; 36 = "
      f"({lm} &minus; 2)({lm}<sup>2</sup> &minus; 9{lm} + 18) = ({lm} &minus; 2)({lm} &minus; 3)({lm} &minus; 6)"
      f'<div class="eq"><b>{lm} = 2, &nbsp;3, &nbsp;6</b></div>'
      f"All different &mdash; so the eigenvectors will come out orthogonal on their own."),
     (f"Eigenvector for {lm} = 2.",
      f'<div class="eq"><i>A</i> &minus; 2<i>I</i> = {M([["1",sp+"1","1"],[sp+"1","3",sp+"1"],["1",sp+"1","1"]])}</div>'
      "Row 3 is the same as row 1, so drop it. Add row 1 to row 2: &nbsp;(0, 2, 0), giving 2<i>y</i> = 0, so <b><i>y</i> = 0</b>.<br><br>"
      "Row 1 then says <i>x</i> &minus; 0 + <i>z</i> = 0, so <i>x</i> = &minus;<i>z</i>. Taking <i>z</i> = &minus;1:"
      f'<div class="eq"><b>v</b><sub>1</sub> = {V(["1","0",sp+"1"])}</div>'),
     (f"Eigenvector for {lm} = 3.",
      f'<div class="eq"><i>A</i> &minus; 3<i>I</i> = {M([["0",sp+"1","1"],[sp+"1","2",sp+"1"],["1",sp+"1","0"]])}</div>'
      "Row 3: &nbsp;<i>x</i> &minus; <i>y</i> = 0, so <i>x</i> = <i>y</i>.<br>"
      "Row 1: &nbsp;&minus;<i>y</i> + <i>z</i> = 0, so <i>z</i> = <i>y</i>.<br>"
      "Taking <i>y</i> = 1:"
      f'<div class="eq"><b>v</b><sub>2</sub> = {V(["1","1","1"])}</div>'
      "Check with row 2: &minus;1 + 2 &minus; 1 = 0 &#10003;"),
     (f"Eigenvector for {lm} = 6.",
      f'<div class="eq"><i>A</i> &minus; 6<i>I</i> = {M([[sp+"3",sp+"1","1"],[sp+"1",sp+"1",sp+"1"],["1",sp+"1",sp+"3"]])}</div>'
      "Row 2 gives &nbsp;<i>x</i> + <i>y</i> + <i>z</i> = 0. &nbsp;Row 3 gives &nbsp;<i>x</i> &minus; <i>y</i> &minus; 3<i>z</i> = 0.<br><br>"
      "Subtract the second from the first: &nbsp;2<i>y</i> + 4<i>z</i> = 0, so <b><i>y</i> = &minus;2<i>z</i></b>.<br>"
      "Then <i>x</i> = &minus;<i>y</i> &minus; <i>z</i> = 2<i>z</i> &minus; <i>z</i> = <i>z</i>. Taking <i>z</i> = 1:"
      f'<div class="eq"><b>v</b><sub>3</sub> = {V(["1",sp+"2","1"])}</div>'
      "Check with row 1: &minus;3(1) &minus; 1(&minus;2) + 1(1) = &minus;3 + 2 + 1 = 0 &#10003;"),
     ("Verify orthogonality &mdash; this earns marks, so write it out.",
      "<b>v</b><sub>1</sub>&middot;<b>v</b><sub>2</sub> = (1)(1) + (0)(1) + (&minus;1)(1) = <b>0</b> &nbsp;&#10003;<br>"
      "<b>v</b><sub>1</sub>&middot;<b>v</b><sub>3</sub> = (1)(1) + (0)(&minus;2) + (&minus;1)(1) = <b>0</b> &nbsp;&#10003;<br>"
      "<b>v</b><sub>2</sub>&middot;<b>v</b><sub>3</sub> = (1)(1) + (1)(&minus;2) + (1)(1) = <b>0</b> &nbsp;&#10003;<br><br>"
      "<b>All three are mutually perpendicular, as guaranteed because <i>A</i> is symmetric with distinct eigenvalues. "
      "No Gram&ndash;Schmidt is required.</b>"),
     ("Normalise and assemble <i>P</i>.",
      f"Lengths: &nbsp;|<b>v</b><sub>1</sub>| = {sq}(1+0+1) = {sq}2, &nbsp;|<b>v</b><sub>2</sub>| = {sq}3, "
      f"&nbsp;|<b>v</b><sub>3</sub>| = {sq}(1+4+1) = {sq}6"
      f'<div class="eq"><i>P</i> = {M([["1/"+sq+"2","1/"+sq+"3","1/"+sq+"6"],["0","1/"+sq+"3",sp+"2/"+sq+"6"],[sp+"1/"+sq+"2","1/"+sq+"3","1/"+sq+"6"]])}</div>'),
     ("State the conclusion.",
      f'<div class="eq"><b><i>P</i><sup>T</sup><i>AP</i> = {M([["2","0","0"],["0","3","0"],["0","0","6"]])}</b></div>'
      "The eigenvalues appear on the diagonal <b>in the same order as their eigenvectors sit in <i>P</i></b>.")])
    blk("Check your answer","chk",
     f"<b>Three checks, each ten seconds.</b><br><br>"
     f"1. <b>Trace:</b> the eigenvalues must add up to the trace. 2 + 3 + 6 = 11, and 3 + 5 + 3 = 11 &nbsp;&#10003;<br>"
     f"2. <b>Determinant:</b> the eigenvalues must multiply to det <i>A</i>. 2 &times; 3 &times; 6 = 36 &nbsp;&#10003;<br>"
     f"3. <b>Each eigenvector:</b> compute <i>A</i><b>v</b> and confirm it equals {lm}<b>v</b>. For example "
     f"<i>A</i>{V(['1','1','1'])} = {V(['3','3','3'])} = 3{V(['1','1','1'])} &nbsp;&#10003;")
    blk("Watch out","warn",
     f"<ul><li><b>Normalise.</b> Putting the raw eigenvectors into <i>P</i> gives <i>P</i><sup>&minus;1</sup><i>AP</i> = <i>D</i> "
     f"but <b>not</b> <i>P</i><sup>T</sup><i>AP</i> = <i>D</i>, and the question said <i>orthogonally</i>.</li>"
     f"<li>Keep the order consistent. If <b>v</b><sub>1</sub> (for {lm}=2) is the first column, then 2 must be the "
     f"first diagonal entry.</li>"
     f"<li>Do not waste time on Gram&ndash;Schmidt here. State that the eigenvalues are distinct and the orthogonality is automatic.</li>"
     f"<li>If you get an eigenvalue wrong, everything after it is wrong. <b>Use the trace check before going on.</b></li></ul>")

def _s11():
    # ================= 11. SPAN / BASIS =================
    sec("III.1","Span, basis and linear independence","Unit III &middot; Q5a &middot; 6 marks &middot; 12 minutes")
    blk("The question","qbox",
     f"<b>(a)</b> Determine whether &nbsp;{{{M([['1','2'],['0','1']])}, {M([['3','4'],['1','1']])}, "
     f"{M([['1','2'],['1','1']])}, {M([['0','2'],['1','2']])}}}&nbsp; is a basis of <i>M</i><sub>22</sub>, "
     f"the space of all 2&times;2 matrices.<br><br>"
     f"<b>(b)</b> Do &nbsp;{{(1,2,3), (&minus;1,&minus;1,0), (2,5,4)}}&nbsp; span <i>R</i><sup>3</sup>?<br><br>"
     f"<b>(c)</b> Is (1,&minus;2) a linear combination of (2,4) and (3,6)?")
    blk("Could it appear another way?","alt",
     """<b>Four disguises, one determinant.</b>
    <ul><li><b>Basis of <i>M</i><sub>22</sub></b> (Mar&nbsp;24 Q5a) &mdash; solved here. Flatten to <i>R</i><sup>4</sup>.</li>
    <li><b>&ldquo;Do these span <i>R</i><sup>3</sup>?&rdquo;</b> (Sep&nbsp;23 Q5a) &mdash; usually followed by
    <b>&ldquo;express (1, 3, &minus;2) in terms of them&rdquo;</b>, which means solving
    <i>c</i><sub>1</sub><b>v</b><sub>1</sub> + <i>c</i><sub>2</sub><b>v</b><sub>2</sub> + <i>c</i><sub>3</sub><b>v</b><sub>3</sub> = <b>b</b>.</li>
    <li><b>&ldquo;Is <b>v</b> a linear combination of &hellip;?&rdquo;</b> (Apr&nbsp;23 Q6a, Jun&nbsp;23 Q5a) &mdash; solve the system
    and look for a contradiction.</li>
    <li><b>&ldquo;Define linear dependence and independence, then check &hellip;&rdquo;</b> (Jun&nbsp;23 Q6a) &mdash; write the
    definition first (a set is dependent if some non-trivial combination gives <b>0</b>), then take the determinant.</li>
    <li>A <b><i>P</i><sub>2</sub> version</b> is equally possible &mdash; flatten <i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i> to (<i>a</i>,<i>b</i>,<i>c</i>).</li></ul>""")
    blk("Formulas you need","fbox",
     "<ul><li><b>Basis</b> = a set that is linearly independent <b>and</b> spans the space. For a space of dimension "
     "<i>n</i>, any <i>n</i> independent vectors form a basis automatically.</li>"
     "<li><b>Independence test:</b> stack the vectors as the rows (or columns) of a square matrix and take the "
     "<b>determinant</b>. Non-zero &rarr; independent. Zero &rarr; dependent.</li>"
     "<li><b>dim <i>R</i><sup>3</sup> = 3</b>, &nbsp;<b>dim <i>M</i><sub>22</sub> = 4</b>, &nbsp;<b>dim <i>P</i><sub>2</sub> = 3</b></li></ul>")
    blk("Why this works","why",
     "The key move is <b>coordinates</b>. A 2&times;2 matrix has four independent entries, so it behaves exactly like a "
     "vector in <i>R</i><sup>4</sup>; a quadratic behaves like a vector in <i>R</i><sup>3</sup>. Once you flatten each "
     "object into a plain list of numbers, every version of this question becomes the same determinant calculation. "
     "<b>Do not be thrown by the matrices or polynomials</b> &mdash; flatten and carry on.")
    steps([
     ("(a) Flatten each matrix into a list of four numbers, reading across the rows.",
      f'<div class="eq">{M([["1","2"],["0","1"]])} {ARR} (1, 2, 0, 1) &nbsp;&nbsp;&nbsp; '
      f'{M([["3","4"],["1","1"]])} {ARR} (3, 4, 1, 1)</div>'
      f'<div class="eq">{M([["1","2"],["1","1"]])} {ARR} (1, 2, 1, 1) &nbsp;&nbsp;&nbsp; '
      f'{M([["0","2"],["1","2"]])} {ARR} (0, 2, 1, 2)</div>'
      "You are now working in <i>R</i><sup>4</sup>. Four vectors, dimension four &mdash; so this is purely a question of "
      "independence."),
     ("Stack them as rows and take the determinant.",
      f'<div class="eq">det{M([["1","2","0","1"],["3","4","1","1"],["1","2","1","1"],["0","2","1","2"]])}</div>'
      "Row-reduce to make the first column mostly zeros. <i>R</i><sub>2</sub> &minus; 3<i>R</i><sub>1</sub> and "
      "<i>R</i><sub>3</sub> &minus; <i>R</i><sub>1</sub> do not change the determinant:"
      f'<div class="eq">= det{M([["1","2","0","1"],["0",sp+"2","1",sp+"2"],["0","0","1","0"],["0","2","1","2"]])}</div>'),
     ("Expand and finish.",
      "Expanding along the first column leaves the 3&times;3 determinant"
      f'<div class="eq">det{M([[sp+"2","1",sp+"2"],["0","1","0"],["2","1","2"]])}</div>'
      "Expand along the middle row (it has two zeros):"
      f'<div class="eq">= 1 &times; det{M([[sp+"2",sp+"2"],["2","2"]])} = (&minus;2)(2) &minus; (&minus;2)(2) = &minus;4 + 4 = <b>0</b></div>'),
     ("State the conclusion.",
      "<b>The determinant is zero, so the four matrices are linearly dependent. "
      "Therefore they do NOT form a basis of <i>M</i><sub>22</sub>.</b><br><br>"
      "You could add that the set spans only a 3-dimensional subspace of the 4-dimensional space "
      "<i>M</i><sub>22</sub>, so it cannot be a basis."),
     ("(b) The span question &mdash; same method.",
      f'<div class="eq">det{M([["1","2","3"],[sp+"1",sp+"1","0"],["2","5","4"]])}</div>'
      "Expanding: &nbsp;1(&minus;4 &minus; 0) &minus; 2(&minus;4 &minus; 0) + 3(&minus;5 + 2) = &minus;4 + 8 &minus; 9 = <b>&minus;5</b><br><br>"
      "Non-zero, so the three vectors are independent. Three independent vectors in a 3-dimensional space "
      "<b>do span <i>R</i><sup>3</sup></b>. If the question also asks you to express a particular vector, solve the "
      "system <i>c</i><sub>1</sub><b>v</b><sub>1</sub> + <i>c</i><sub>2</sub><b>v</b><sub>2</sub> + <i>c</i><sub>3</sub><b>v</b><sub>3</sub> = <b>b</b>."),
     ("(c) The linear-combination question &mdash; solve, do not take a determinant.",
      "You want scalars with &nbsp;<i>c</i><sub>1</sub>(2,4) + <i>c</i><sub>2</sub>(3,6) = (1,&minus;2):"
      '<div class="eq">2<i>c</i><sub>1</sub> + 3<i>c</i><sub>2</sub> = 1 &nbsp;&nbsp;&nbsp; '
      '4<i>c</i><sub>1</sub> + 6<i>c</i><sub>2</sub> = &minus;2</div>'
      "The second equation is exactly twice the left side of the first, so it demands 2(1) = &minus;2, i.e. 2 = &minus;2. "
      "<b>Contradiction &mdash; so (1,&minus;2) is NOT a linear combination of the two.</b><br><br>"
      "Geometrically: (2,4) and (3,6) are parallel, so they span only a line, and (1,&minus;2) is not on it.")])
    blk("Check your answer","chk",
     "<b>(a) determinant 0 &rarr; NOT a basis.</b> &nbsp;<b>(b) determinant &minus;5 &rarr; they DO span.</b> "
     "&nbsp;<b>(c) NOT a linear combination.</b><br><br>"
     "Fast sanity check for (a): look for an obvious relation among the flattened vectors. Here "
     "(1,2,0,1) + (1,2,1,1) = (2,4,1,2) and (3,4,1,1) &minus; (0,2,1,2) = (3,2,0,&minus;1) &mdash; not obvious, which is why "
     "the determinant is the reliable route. <b>Trust the determinant.</b>")
    blk("Watch out","warn",
     "<ul><li><b>Count first.</b> If the number of vectors is not equal to the dimension of the space, they cannot be a "
     "basis regardless of independence &mdash; too few cannot span, too many must be dependent. Say so and save yourself the work.</li>"
     "<li>Flatten consistently. Read every matrix across the rows, or every one down the columns, but do not mix.</li>"
     "<li>A determinant of zero means <b>dependent</b>, which means <b>not a basis</b>. Do not let the answer &ldquo;no&rdquo; "
     "make you doubt correct arithmetic &mdash; here the answer really is no.</li></ul>")

def _s12():
    # ================= 12. ROTATION PROOF =================
    sec("III.3","The rotation-operator proof","Unit III &middot; Q5c &middot; 7 marks &middot; 12 minutes")
    blk("The question","qbox",
     f"Show that the linear operator <i>T</i>&thinsp;:&thinsp;<i>R</i><sup>2</sup> {ARR} <i>R</i><sup>2</sup> defined by "
     f"<i>T</i>(<b>x</b>) = <i>A</i><b>x</b> rotates a vector <b>x</b> through an angle {th} about the origin, where<br>"
     f'<div class="eq"><i>A</i> = {M([["cos&#952;",sp+"sin&#952;"],["sin&#952;","cos&#952;"]])}</div>')
    blk("Could it appear another way?","alt",
     """<b>Identical wording both times it appeared</b> (Apr&nbsp;23 Q6b, Mar&nbsp;24 Q5c). Close relatives that could
    appear in the same slot:
    <ul><li><b>&ldquo;Find the matrix of the linear transformation&rdquo;</b> for a given <i>T</i> &mdash; apply <i>T</i> to each
    standard basis vector and use the results as the columns.</li>
    <li><b>&ldquo;Show that a reflection preserves length&rdquo;</b> &mdash; same structure, but the matrix is
    diag(1, &minus;1) and you show the angle is negated rather than shifted.</li>
    <li>The question may ask you to <b>verify with a specific vector</b> after the general proof. Use (1, 0) and
    &theta; = &pi;/2 &mdash; it maps to (0, 1).</li></ul>""")
    blk("Formulas you need","fbox",
     f"<ul><li><b>Polar form:</b> any vector in <i>R</i><sup>2</sup> can be written "
     f"<b>x</b> = (<i>r</i>&thinsp;cos&thinsp;{ph}, &nbsp;<i>r</i>&thinsp;sin&thinsp;{ph}), where "
     f"<i>r</i> = |<b>x</b>| is its length and {ph} is the angle it makes with the positive <i>x</i>-axis.</li>"
     f"<li><b>Compound angle formulae:</b><br>"
     f"cos({th} + {ph}) = cos&thinsp;{th}&thinsp;cos&thinsp;{ph} &minus; sin&thinsp;{th}&thinsp;sin&thinsp;{ph}<br>"
     f"sin({th} + {ph}) = sin&thinsp;{th}&thinsp;cos&thinsp;{ph} + cos&thinsp;{th}&thinsp;sin&thinsp;{ph}</li></ul>")
    blk("Why this works","why",
     f"A rotation is defined by two properties: it <b>keeps the length</b> of a vector the same, and it <b>increases the "
     f"angle</b> by a fixed amount. So the proof has to produce both facts. The trick is to write <b>x</b> in polar form, "
     f"because then the angle is visible as {ph}. Multiplying by <i>A</i> and applying the compound-angle formulae turns "
     f"{ph} into {th} + {ph} while leaving <i>r</i> untouched &mdash; and that <i>is</i> a rotation. "
     f"<b>Twelve minutes to learn, seven marks, no calculus.</b>")
    steps([
     ("State that <i>T</i> is linear.",
      "For any matrix <i>A</i>, the map <b>x</b> &#8614; <i>A</i><b>x</b> satisfies "
      "<i>A</i>(<b>u</b>+<b>v</b>) = <i>A</i><b>u</b> + <i>A</i><b>v</b> and <i>A</i>(<i>k</i><b>u</b>) = <i>k</i>(<i>A</i><b>u</b>) "
      "by the rules of matrix multiplication. <b>So <i>T</i> is a linear operator.</b> One line, but say it."),
     ("Write a general vector in polar form.",
      f"Let <b>x</b> have length <i>r</i> and make an angle {ph} with the positive <i>x</i>-axis:"
      f'<div class="eq"><b>x</b> = {V(["<i>r</i>&thinsp;cos&thinsp;"+ph,"<i>r</i>&thinsp;sin&thinsp;"+ph])}</div>'
      f"This is completely general &mdash; every vector in <i>R</i><sup>2</sup> can be written this way."),
     ("Multiply by <i>A</i>.",
      f'<div class="eq"><i>A</i><b>x</b> = {M([["cos&#952;",sp+"sin&#952;"],["sin&#952;","cos&#952;"]])}'
      f'{V(["<i>r</i>&thinsp;cos&thinsp;"+ph,"<i>r</i>&thinsp;sin&thinsp;"+ph])}</div>'
      "Taking the two rows in turn:"
      f'<div class="eq">= {V(["<i>r</i>&thinsp;cos&thinsp;"+th+"&thinsp;cos&thinsp;"+ph+" &minus; <i>r</i>&thinsp;sin&thinsp;"+th+"&thinsp;sin&thinsp;"+ph,"<i>r</i>&thinsp;sin&thinsp;"+th+"&thinsp;cos&thinsp;"+ph+" + <i>r</i>&thinsp;cos&thinsp;"+th+"&thinsp;sin&thinsp;"+ph])}</div>'),
     ("Take out the common factor <i>r</i>.",
      f'<div class="eq">= <i>r</i>&thinsp;{V(["cos&thinsp;"+th+"&thinsp;cos&thinsp;"+ph+" &minus; sin&thinsp;"+th+"&thinsp;sin&thinsp;"+ph,"sin&thinsp;"+th+"&thinsp;cos&thinsp;"+ph+" + cos&thinsp;"+th+"&thinsp;sin&thinsp;"+ph])}</div>'
      "<b>Now look carefully at the two entries</b> &mdash; each is exactly one of the compound-angle formulae."),
     ("Apply the compound-angle formulae.",
      f'<div class="eq"><i>A</i><b>x</b> = <i>r</i>&thinsp;{V(["cos("+th+" + "+ph+")","sin("+th+" + "+ph+")"])}</div>'),
     ("Read off the two facts that make it a rotation.",
      f"<b>Length.</b> &nbsp;|<i>A</i><b>x</b>| = <i>r</i>{sq}(cos<sup>2</sup>({th}+{ph}) + sin<sup>2</sup>({th}+{ph})) "
      f"= <i>r</i>&thinsp;&times;&thinsp;1 = <i>r</i> = |<b>x</b>|.<br>"
      f"<b>The length is unchanged.</b><br><br>"
      f"<b>Angle.</b> &nbsp;The original vector had angle {ph}; the image has angle {th} + {ph}. "
      f"<b>The angle has increased by exactly {th}.</b>"),
     ("Conclude.",
      f"Since <i>T</i> preserves length and increases the angle of every vector by {th}, "
      f"<b><i>T</i> rotates <b>x</b> through an angle {th} about the origin.</b> &nbsp;&#8718;")])
    blk("Check your answer","chk",
     f"Test it on a case you can see. Take {th} = 90&deg;, so cos&thinsp;{th} = 0 and sin&thinsp;{th} = 1:"
     f'<div class="eq"><i>A</i> = {M([["0",sp+"1"],["1","0"]])}, &nbsp;&nbsp; '
     f'<i>A</i>{V(["1","0"])} = {V(["0","1"])}</div>'
     f"The vector pointing along the <i>x</i>-axis has become the vector pointing along the <i>y</i>-axis &mdash; "
     f"a 90&deg; anticlockwise turn, exactly as claimed. &nbsp;&#10003;")
    blk("Watch out","warn",
     f"<ul><li><b>Do not use a specific vector</b> such as (1,0) as your proof. That demonstrates one case; the question "
     f"says &ldquo;a vector <b>x</b>&rdquo;, meaning any vector. Polar form is what makes it general.</li>"
     f"<li><b>You must mention the length.</b> Showing the angle increases by {th} is only half a rotation &mdash; a "
     f"spiral does that too. The proof needs |<i>A</i><b>x</b>| = |<b>x</b>|.</li>"
     f"<li>Watch the minus sign in the top-right entry of <i>A</i>. If you drop it you get a reflection, not a rotation.</li></ul>")

def _s13():
    # ================= 13. POSITIVE DEFINITE =================
    sec("V.1","Positive-definite check","Unit V &middot; Q10a &middot; 5 marks &middot; 8 minutes &middot; overtime item")
    blk("The question","qbox",
     f"Check whether &nbsp;<i>A</i> = {M([['1',sp+'2','1'],[sp+'2','4',sp+'2'],['1',sp+'2','1']])}&nbsp; is positive definite or not.")
    blk("Could it appear another way?","alt",
     """<b>Positive-definiteness appeared in all four papers, three different ways.</b>
    <ul><li><b>The 3&times;3 solved here</b> &mdash; Apr&nbsp;23 and Mar&nbsp;24. Answer: <b>not</b> positive definite.</li>
    <li><b>[[8,&minus;6,2],[&minus;6,7,&minus;4],[2,&minus;4,3]]</b> &mdash; Jun&nbsp;23. Same test; here the minors are
    8, 20 and 8, all positive, so it <b>is</b> positive definite. <b>Be ready for a &ldquo;yes&rdquo;.</b></li>
    <li><b>Given as a quadratic form</b> &mdash; Sep&nbsp;23 asked about
    3<i>x</i><sup>2</sup> + 5<i>y</i><sup>2</sup> + 3<i>z</i><sup>2</sup> &minus; 2<i>yz</i> + 2<i>zx</i> &minus; 2<i>xy</i>.
    Build the symmetric matrix first: the diagonal holds the squared coefficients, and the entry
    <i>a<sub>ij</sub></i> is <b>half</b> the coefficient of <i>x<sub>i</sub>x<sub>j</sub></i>. So here
    <i>A</i> = [[3,&minus;1,1],[&minus;1,5,&minus;1],[1,&minus;1,3]] &mdash; which is the same matrix as the orthogonal
    diagonalization question. Then apply Sylvester as usual.</li></ul>""")
    blk("Formulas you need","fbox",
     "<b>Sylvester&rsquo;s criterion.</b> A symmetric matrix is <b>positive definite</b> if and only if <b>every</b> "
     "leading principal minor is strictly greater than zero.<br><br>"
     "The leading principal minors are the determinants of the top-left 1&times;1, 2&times;2, 3&times;3 &hellip; blocks."
     "<ul><li>positive definite &nbsp;&hArr;&nbsp; all minors &gt; 0</li>"
     "<li>positive <b>semi</b>-definite &nbsp;&hArr;&nbsp; all eigenvalues &ge; 0 (some may be zero)</li></ul>")
    blk("Why this works","why",
     "&ldquo;Positive definite&rdquo; means <b>x</b><sup>T</sup><i>A</i><b>x</b> &gt; 0 for every non-zero <b>x</b> &mdash; "
     "the matrix always produces a positive number. Checking that directly for all <b>x</b> is impossible, so Sylvester&rsquo;s "
     "criterion gives you a finite test: just three determinants for a 3&times;3. "
     "<b>The word &ldquo;every&rdquo; matters</b> &mdash; one minor that is zero or negative kills it.")
    steps([
     ("First minor: the top-left entry.",
      f'<div class="eq"><i>D</i><sub>1</sub> = |1| = <b>1</b> &nbsp;&nbsp;(&gt; 0 &#10003;)</div>'),
     ("Second minor: the top-left 2&times;2 block.",
      f'<div class="eq"><i>D</i><sub>2</sub> = det{M([["1",sp+"2"],[sp+"2","4"]])} = (1)(4) &minus; (&minus;2)(&minus;2) '
      f'= 4 &minus; 4 = <b>0</b></div>'
      "<b>This is already fatal</b> &mdash; the criterion needs strictly greater than zero. But compute the third minor "
      "too, because it tells you what the matrix actually is."),
     ("Third minor: the whole determinant.",
      "Look at the matrix: <b>row 3 is identical to row 1</b>. A determinant with two equal rows is zero."
      f'<div class="eq"><i>D</i><sub>3</sub> = det <i>A</i> = <b>0</b></div>'),
     ("State the conclusion properly.",
      "The minors are 1, 0, 0. Not all are positive, so"
      '<div class="eq"><b><i>A</i> is NOT positive definite.</b></div>'
      "Now say what it <b>is</b>. Notice that"
      f'<div class="eq"><i>A</i> = <b>vv</b><sup>T</sup> &nbsp;where&nbsp; <b>v</b> = {V(["1",sp+"2","1"])}</div>'
      "so for any <b>x</b>,"
      '<div class="eq"><b>x</b><sup>T</sup><i>A</i><b>x</b> = <b>x</b><sup>T</sup><b>vv</b><sup>T</sup><b>x</b> '
      '= (<b>v</b><sup>T</sup><b>x</b>)<sup>2</sup> &ge; 0</div>'
      "<b>Therefore <i>A</i> is positive SEMI-definite.</b> Its eigenvalues are 0, 0 and 6.")])
    blk("Check your answer","chk",
     f"<b>Not positive definite; positive semi-definite.</b><br><br>"
     f"Confirm with the eigenvalues. Trace = 1 + 4 + 1 = 6 and det = 0, and since the matrix has rank 1 "
     f"(all rows are multiples of (1, &minus;2, 1)), two eigenvalues are 0 and the third must be 6 to make the trace work. "
     f"All are &ge; 0 but not all &gt; 0 &mdash; that is exactly semi-definite. &nbsp;&#10003;")
    blk("Watch out","warn",
     "<ul><li><b>Do not stop at &ldquo;no&rdquo;.</b> Naming it positive semi-definite, and giving a reason, is worth "
     "the difference between three marks and five.</li>"
     "<li>The minors must be the <b>leading</b> ones &mdash; always taken from the top-left corner. Any other 2&times;2 "
     "block is not part of the test.</li>"
     "<li>Spot repeated or proportional rows early. Here row 3 = row 1 tells you det = 0 before you calculate anything.</li></ul>")

def _s14():
    # ================= 14. FOUR SUBSPACES =================
    sec("IV.2","The four fundamental subspaces","Unit IV &middot; Q7c &middot; 7 marks &middot; 15 minutes &middot; overtime item")
    blk("The question","qbox",
     f"Find the dimension and a basis for the four fundamental subspaces of<br>"
     f'<div class="eq"><i>A</i> = {M([["1","2","0","1"],["0","1","1","0"],["1","2","0","1"]])}</div>'
     f"<b>This exact matrix appeared in three of the four past papers.</b>")
    blk("Could it appear another way?","alt",
     """<b>Same idea, three different wordings.</b>
    <ul><li><b>&ldquo;Dimension and basis for the four fundamental subspaces&rdquo;</b> &mdash; Apr&nbsp;23 and Mar&nbsp;24,
    the full version solved here.</li>
    <li><b>&ldquo;Find a basis for col(<i>A</i>) and nul(<i>A</i>)&rdquo;</b> &mdash; Jun&nbsp;23, same matrix, but only two of the
    four subspaces are wanted. Do not waste time on the other two.</li>
    <li><b>&ldquo;Basis for the null space and column space, and hence their dimensions&rdquo;</b> for a different 3&times;4 matrix
    &mdash; Sep&nbsp;23.</li></ul>
    <b>A related version:</b> &ldquo;solve <i>A</i><b>x</b> = <b>0</b> and <i>R</i><b>x</b> = <b>0</b> and show the solutions are
    the same&rdquo; &mdash; this is just the null-space part, with the point that row operations do not change the null space.""")
    blk("Formulas you need","fbox",
     "For an <i>m</i>&times;<i>n</i> matrix of rank <i>r</i> &mdash; here <i>m</i> = 3, <i>n</i> = 4:"
     "<ul><li><b>Column space</b> C(<i>A</i>) lives in <i>R<sup>m</sup></i>, dimension <i>r</i>. "
     "Basis = the <b>pivot columns of the original <i>A</i></b>.</li>"
     "<li><b>Row space</b> C(<i>A</i><sup>T</sup>) lives in <i>R<sup>n</sup></i>, dimension <i>r</i>. "
     "Basis = the non-zero rows of the reduced form.</li>"
     "<li><b>Null space</b> N(<i>A</i>) lives in <i>R<sup>n</sup></i>, dimension <i>n</i> &minus; <i>r</i>. "
     "Solve <i>A</i><b>x</b> = <b>0</b>.</li>"
     "<li><b>Left null space</b> N(<i>A</i><sup>T</sup>) lives in <i>R<sup>m</sup></i>, dimension <i>m</i> &minus; <i>r</i>. "
     "Solve <b>y</b><sup>T</sup><i>A</i> = <b>0</b>.</li></ul>")
    blk("Why this works","why",
     "Every matrix has four subspaces attached to it, and row reduction reveals all four at once. The rank <i>r</i> is "
     "the number of pivots, and it controls everything: two of the subspaces have dimension <i>r</i>, and the other two "
     "make up the difference. <b>The one thing to remember is that the basis for the column space comes from the "
     "ORIGINAL matrix, not the reduced one</b> &mdash; row operations change the column space, but they do not change "
     "<i>which</i> columns are pivot columns.")
    steps([
     ("Row-reduce, and notice the repeated row.",
      "Row 3 is identical to row 1, so <i>R</i><sub>3</sub> &minus; <i>R</i><sub>1</sub> wipes it out:"
      f'<div class="eq">{M([["1","2","0","1"],["0","1","1","0"],["1","2","0","1"]])} {ARR} '
      f'{M([["1","2","0","1"],["0","1","1","0"],["0","0","0","0"]])}</div>'
      "Now clear above the second pivot with <i>R</i><sub>1</sub> &minus; 2<i>R</i><sub>2</sub>:"
      f'<div class="eq">{ARR} {M([["1","0",sp+"2","1"],["0","1","1","0"],["0","0","0","0"]])}</div>'
      "<b>Pivots are in columns 1 and 2, so rank <i>r</i> = 2.</b>"),
     ("Column space &mdash; take the pivot columns of the ORIGINAL <i>A</i>.",
      f'<div class="eq">basis = {{ {V(["1","0","1"])}, {V(["2","1","2"])} }}, &nbsp;&nbsp; dim C(<i>A</i>) = <b>2</b></div>'
      "It is a 2-dimensional plane inside <i>R</i><sup>3</sup>."),
     ("Row space &mdash; take the non-zero rows of the reduced form.",
      '<div class="eq">basis = { (1, 0, &minus;2, 1), &nbsp;(0, 1, 1, 0) }, &nbsp;&nbsp; dim C(<i>A</i><sup>T</sup>) = <b>2</b></div>'
      "This one lives in <i>R</i><sup>4</sup>."),
     ("Null space &mdash; solve <i>A</i><b>x</b> = <b>0</b> from the reduced form.",
      "The reduced rows say"
      '<div class="eq"><i>x</i><sub>1</sub> &minus; 2<i>x</i><sub>3</sub> + <i>x</i><sub>4</sub> = 0 &nbsp;&nbsp;and&nbsp;&nbsp; '
      '<i>x</i><sub>2</sub> + <i>x</i><sub>3</sub> = 0</div>'
      "Columns 3 and 4 have no pivot, so <b><i>x</i><sub>3</sub> and <i>x</i><sub>4</sub> are free</b>. Express the others:"
      '<div class="eq"><i>x</i><sub>1</sub> = 2<i>x</i><sub>3</sub> &minus; <i>x</i><sub>4</sub>, &nbsp;&nbsp;'
      '<i>x</i><sub>2</sub> = &minus;<i>x</i><sub>3</sub></div>'
      "Set one free variable to 1 and the other to 0, then swap:"
      f'<div class="eq">{ARR} &nbsp;{V(["2",sp+"1","1","0"])} &nbsp;and&nbsp; {V([sp+"1","0","0","1"])}, '
      f'&nbsp;&nbsp; dim N(<i>A</i>) = <b>2</b></div>'),
     ("Left null space &mdash; find the combinations of rows that give zero.",
      "You need <b>y</b> with <b>y</b><sup>T</sup><i>A</i> = <b>0</b>, that is <i>y</i><sub>1</sub>(row 1) + "
      "<i>y</i><sub>2</sub>(row 2) + <i>y</i><sub>3</sub>(row 3) = <b>0</b>.<br><br>"
      "<b>You already know one:</b> row 3 = row 1, so row 1 &minus; row 3 = <b>0</b>. That is <i>y</i> = (1, 0, &minus;1)."
      f'<div class="eq">basis = {{ {V(["1","0",sp+"1"])} }}, &nbsp;&nbsp; dim N(<i>A</i><sup>T</sup>) = <b>1</b></div>'),
     ("Summarise in a table &mdash; this presentation earns marks.",
      '<table class="t"><tr><th>Subspace</th><th>Lives in</th><th class="c">Dimension</th><th>Basis</th></tr>'
      f'<tr><td>Column space C(<i>A</i>)</td><td><i>R</i><sup>3</sup></td><td class="c">2</td><td>(1,0,1), (2,1,2)</td></tr>'
      f'<tr><td>Row space C(<i>A</i><sup>T</sup>)</td><td><i>R</i><sup>4</sup></td><td class="c">2</td><td>(1,0,&minus;2,1), (0,1,1,0)</td></tr>'
      f'<tr><td>Null space N(<i>A</i>)</td><td><i>R</i><sup>4</sup></td><td class="c">2</td><td>(2,&minus;1,1,0), (&minus;1,0,0,1)</td></tr>'
      f'<tr><td>Left null space N(<i>A</i><sup>T</sup>)</td><td><i>R</i><sup>3</sup></td><td class="c">1</td><td>(1,0,&minus;1)</td></tr></table>')])
    blk("Check your answer","chk",
     "<b>The two dimension identities must both hold.</b><br><br>"
     "&bull;&nbsp; dim C(<i>A</i><sup>T</sup>) + dim N(<i>A</i>) = 2 + 2 = 4 = number of <b>columns</b> &nbsp;&#10003;<br>"
     "&bull;&nbsp; dim C(<i>A</i>) + dim N(<i>A</i><sup>T</sup>) = 2 + 1 = 3 = number of <b>rows</b> &nbsp;&#10003;<br><br>"
     "Also verify a null-space vector directly: &nbsp;<i>A</i>(2,&minus;1,1,0) = (2&minus;2+0+0, &nbsp;0&minus;1+1+0, "
     "&nbsp;2&minus;2+0+0) = (0,0,0) &nbsp;&#10003;")
    blk("Watch out","warn",
     "<ul><li><b>The column-space basis comes from the original <i>A</i>.</b> Using the reduced columns is the single "
     "most common mistake in this question. Row operations preserve which columns are pivots, but not the columns themselves.</li>"
     "<li>The null space and row space both live in <i>R</i><sup>4</sup>; the column space and left null space both live "
     "in <i>R</i><sup>3</sup>. Getting these the wrong way round loses marks.</li>"
     "<li>The left null space is easy to skip. It is a quarter of the question &mdash; here it is one vector, found by "
     "spotting that row 3 equals row 1.</li></ul>")

def _s15():
    # ================= 15. COMPLETE SOLUTION =================
    sec("IV.3","Complete solution of <i>Ax</i> = <i>b</i>","Unit IV &middot; Q7a &middot; 6 marks &middot; 15 minutes &middot; overtime item")
    blk("The question","qbox",
     "Find the complete solution of<br>"
     '<div class="eq"><i>x</i> + 3<i>y</i> + 3<i>z</i> = 1<br>2<i>x</i> + 6<i>y</i> + 9<i>z</i> = 5<br>'
     '&minus;<i>x</i> &minus; 3<i>y</i> + 3<i>z</i> = 5</div>')
    blk("Could it appear another way?","alt",
     """<b>Three presentations, one method.</b>
    <ul><li><b>Three equations written out</b> in <i>x</i>, <i>y</i>, <i>z</i> &mdash; Mar&nbsp;24, solved here.</li>
    <li><b><i>A</i> and <i>B</i> given as matrices</b> &mdash; Apr&nbsp;23. Build the augmented matrix yourself and proceed identically.</li>
    <li><b>&ldquo;by choosing an appropriate <i>B</i>&rdquo;</b> &mdash; Jun&nbsp;23. The right-hand side is left as
    <i>b</i><sub>1</sub>, <i>b</i><sub>2</sub>, <i>b</i><sub>3</sub> and <b>you</b> must pick values that make the system
    consistent. Row-reduce first, read off the consistency condition (something like
    <i>b</i><sub>3</sub> = <i>b</i><sub>1</sub> + <i>b</i><sub>2</sub>), then choose numbers that satisfy it.</li></ul>""")
    blk("Formulas you need","fbox",
     "<b>Complete solution = one particular solution + everything in the null space:</b>"
     '<div class="eq"><b>x</b> = <b>x</b><sub>p</sub> + <i>c</i><sub>1</sub><b>n</b><sub>1</sub> + <i>c</i><sub>2</sub><b>n</b><sub>2</sub> + &hellip;</div>'
     "<ul><li><b>x</b><sub>p</sub>: set every free variable to 0 and solve.</li>"
     "<li><b>n</b><sub><i>i</i></sub>: solutions of <i>A</i><b>x</b> = <b>0</b>, one for each free variable.</li></ul>")
    blk("Why this works","why",
     "If <b>x</b><sub>p</sub> solves <i>A</i><b>x</b> = <b>b</b> and <b>n</b> solves <i>A</i><b>n</b> = <b>0</b>, then "
     "<i>A</i>(<b>x</b><sub>p</sub> + <b>n</b>) = <b>b</b> + <b>0</b> = <b>b</b>, so the sum is also a solution. "
     "Conversely the difference of any two solutions lies in the null space. So the solution set is one particular point "
     "with the whole null space slid onto it &mdash; a line, a plane, or a single point, depending on how many free "
     "variables there are.")
    steps([
     ("Write the augmented matrix.",
      f'<div class="eq">{M([["1","3","3","|","1"],["2","6","9","|","5"],[sp+"1",sp+"3","3","|","5"]])}</div>'),
     ("Eliminate down the first column.",
      "<i>R</i><sub>2</sub> &minus; 2<i>R</i><sub>1</sub>: &nbsp;(0, 0, 3 | 3)<br>"
      "<i>R</i><sub>3</sub> + <i>R</i><sub>1</sub>: &nbsp;(0, 0, 6 | 6)"
      f'<div class="eq">{ARR} {M([["1","3","3","|","1"],["0","0","3","|","3"],["0","0","6","|","6"]])}</div>'),
     ("Finish reducing.",
      "<i>R</i><sub>3</sub> &minus; 2<i>R</i><sub>2</sub>: &nbsp;(0, 0, 0 | 0) &mdash; the third equation carried no new information."
      f'<div class="eq">{ARR} {M([["1","3","3","|","1"],["0","0","1","|","1"],["0","0","0","|","0"]])}</div>'
      "<b>Pivots are in columns 1 and 3, so <i>y</i> is the free variable.</b> The last row reads 0 = 0, so the system "
      "is consistent and a solution exists."),
     ("Find a particular solution: set the free variable to zero.",
      "Put <i>y</i> = 0. Row 2 gives <i>z</i> = 1. Row 1 gives <i>x</i> + 0 + 3(1) = 1, so <i>x</i> = &minus;2."
      f'<div class="eq"><b>x</b><sub>p</sub> = {V([sp+"2","0","1"])}</div>'),
     ("Find the null space: same reduction with zero on the right.",
      "Row 2: &nbsp;<i>z</i> = 0. &nbsp;Row 1: &nbsp;<i>x</i> + 3<i>y</i> + 0 = 0, so <i>x</i> = &minus;3<i>y</i>.<br><br>"
      "Take <i>y</i> = 1:"
      f'<div class="eq"><b>n</b> = {V([sp+"3","1","0"])}</div>'),
     ("Write the complete solution.",
      f'<div class="eq"><b>x</b> = {V([sp+"2","0","1"])} + <i>c</i>&thinsp;{V([sp+"3","1","0"])}, '
      f'&nbsp;&nbsp;<i>c</i> any real number</div>'
      "In coordinates: &nbsp;<i>x</i> = &minus;2 &minus; 3<i>c</i>, &nbsp;<i>y</i> = <i>c</i>, &nbsp;<i>z</i> = 1. "
      "<b>The solution set is a line in <i>R</i><sup>3</sup>.</b>")])
    blk("Check your answer","chk",
     "Substitute the general solution back into all three equations, keeping <i>c</i> symbolic. "
     "If it works for every <i>c</i>, you have the whole family, not just one point.<br><br>"
     "&bull;&nbsp; (&minus;2&minus;3<i>c</i>) + 3<i>c</i> + 3(1) = &minus;2 + 3 = 1 &nbsp;&#10003;<br>"
     "&bull;&nbsp; 2(&minus;2&minus;3<i>c</i>) + 6<i>c</i> + 9(1) = &minus;4 &minus; 6<i>c</i> + 6<i>c</i> + 9 = 5 &nbsp;&#10003;<br>"
     "&bull;&nbsp; &minus;(&minus;2&minus;3<i>c</i>) &minus; 3<i>c</i> + 3(1) = 2 + 3<i>c</i> &minus; 3<i>c</i> + 3 = 5 &nbsp;&#10003;<br><br>"
     "<b>The <i>c</i> terms cancel in every equation</b> &mdash; that is the signature of a correct null-space vector.")
    blk("Watch out","warn",
     "<ul><li><b>Check consistency first.</b> If a row reduces to (0 0 0 | <i>k</i>) with <i>k</i> &ne; 0, there is "
     "<b>no solution</b> and you should say so rather than forcing an answer.</li>"
     "<li>Free variables are the ones whose columns have <b>no pivot</b>. Here it is <i>y</i>, not <i>z</i> &mdash; "
     "read it from the reduced matrix, do not assume it is the last variable.</li>"
     "<li>Present the answer in the form <b>x</b><sub>p</sub> + <i>c</i><b>n</b>. Giving only <b>x</b><sub>p</sub> "
     "answers a different question and loses half the marks.</li></ul>")

def _s16():
    # ================= 16. COMPOSITION =================
    sec("III.4","Composition of matrix transformations","Unit III &middot; Q6a &middot; 6 marks &middot; 12 minutes &middot; overtime item")
    blk("The question","qbox",
     f"Determine the matrix that describes a reflection in the <i>x</i>-axis, followed by a rotation through {pi}/2, "
     f"followed by a contraction of factor 1/3. Find the image of the point {V(['4','1'])} under this sequence of mappings.")
    blk("Could it appear another way?","alt",
     """<b>Every element changes each paper &mdash; the axis, the angle, the factor and the point. The order does not.</b>
    <ul><li>reflect in <b><i>y</i></b>, rotate <b>&pi;/6</b>, dilate <b>3/2</b>, point (2, 1) &mdash; Apr&nbsp;23</li>
    <li>reflect in <i>x</i>, rotate &pi;/2, <b>contract 1/2</b>, point (4, &minus;1) &mdash; Jun&nbsp;23</li>
    <li>reflect in <i>x</i>, rotate &pi;/2, <b>dilate 3</b>, point (2, 1) &mdash; Sep&nbsp;23</li>
    <li>reflect in <i>x</i>, rotate &pi;/2, contract 1/3, point (4, 1) &mdash; Mar&nbsp;24, solved here</li></ul>
    <b>Be ready for &pi;/6 or &pi;/4</b>, where the entries are &radic;3/2 and &frac12; rather than 0 and 1 &mdash; the
    arithmetic is longer but identical. <b>And read the axis carefully:</b> reflection in <i>y</i> is diag(&minus;1, 1).""")
    blk("Formulas you need","fbox",
     f"<ul><li>Reflection in the <i>x</i>-axis: &nbsp;{M([['1','0'],['0',sp+'1']])} &nbsp;&nbsp;(<i>y</i> changes sign)</li>"
     f"<li>Reflection in the <i>y</i>-axis: &nbsp;{M([[sp+'1','0'],['0','1']])} &nbsp;&nbsp;(<i>x</i> changes sign)</li>"
     f"<li>Rotation through {th}: &nbsp;{M([['cos&#952;',sp+'sin&#952;'],['sin&#952;','cos&#952;']])}</li>"
     f"<li>Dilation or contraction by factor <i>k</i>: &nbsp;<i>kI</i> &mdash; just multiply the whole matrix by <i>k</i></li></ul>")
    blk("Why this works","why",
     "Applying transformation <i>S</i> first and then <i>T</i> means computing <i>T</i>(<i>S</i>(<b>x</b>)), which in "
     "matrices is <i>T</i>(<i>S</i><b>x</b>) = (<i>TS</i>)<b>x</b>. So the matrix of the composition is the product with "
     "<b>the first transformation on the right</b>. Matrix multiplication is not commutative, so the order genuinely "
     "matters: reflect-then-rotate is a different map from rotate-then-reflect. "
     "<b>Read the question left to right and build the product right to left.</b>")
    steps([
     ("Write down the three matrices in the order the question gives them.",
      f'<div class="eq">Reflect in <i>x</i>: &nbsp;<i>R<sub>f</sub></i> = {M([["1","0"],["0",sp+"1"]])}</div>'
      f'<div class="eq">Rotate {pi}/2: &nbsp;cos({pi}/2) = 0, sin({pi}/2) = 1, so &nbsp;'
      f'<i>R<sub>&#952;</sub></i> = {M([["0",sp+"1"],["1","0"]])}</div>'
      f'<div class="eq">Contract by 1/3: &nbsp;<i>C</i> = {F("1","3")}<i>I</i></div>'),
     ("Assemble the product in reverse order.",
      f'<div class="eq"><i>M</i> = <i>C</i> &middot; <i>R<sub>&#952;</sub></i> &middot; <i>R<sub>f</sub></i> '
      f'= {F("1","3")}{M([["0",sp+"1"],["1","0"]])}{M([["1","0"],["0",sp+"1"]])}</div>'
      "<b>The reflection is applied first, so it sits on the right.</b>"),
     ("Multiply the two matrices.",
      f'<div class="eq">{M([["0",sp+"1"],["1","0"]])}{M([["1","0"],["0",sp+"1"]])}</div>'
      "Row 1 &times; column 1: (0)(1) + (&minus;1)(0) = 0<br>"
      "Row 1 &times; column 2: (0)(0) + (&minus;1)(&minus;1) = 1<br>"
      "Row 2 &times; column 1: (1)(1) + (0)(0) = 1<br>"
      "Row 2 &times; column 2: (1)(0) + (0)(&minus;1) = 0"
      f'<div class="eq">= {M([["0","1"],["1","0"]])}</div>'),
     ("Include the contraction factor.",
      f'<div class="eq"><b><i>M</i> = {F("1","3")}{M([["0","1"],["1","0"]])} = {M([["0","1/3"],["1/3","0"]])}</b></div>'),
     ("Apply <i>M</i> to the point.",
      f'<div class="eq"><i>M</i>{V(["4","1"])} = {F("1","3")}{M([["0","1"],["1","0"]])}{V(["4","1"])} '
      f'= {F("1","3")}{V(["1","4"])} = {V(["1/3","4/3"])}</div>'
      f'<div class="eq"><b>The image is (1/3, &nbsp;4/3).</b></div>')])
    blk("Check your answer","chk",
     f"<b>Track the point through the three stages by hand</b> &mdash; if it matches, your matrix order is right.<br><br>"
     f"&bull;&nbsp; Start: &nbsp;(4, 1)<br>"
     f"&bull;&nbsp; Reflect in the <i>x</i>-axis (flip the sign of <i>y</i>): &nbsp;(4, &minus;1)<br>"
     f"&bull;&nbsp; Rotate {pi}/2 (the rule (<i>x</i>, <i>y</i>) {ARR} (&minus;<i>y</i>, <i>x</i>)): &nbsp;(1, 4)<br>"
     f"&bull;&nbsp; Contract by 1/3: &nbsp;<b>(1/3, 4/3)</b> &nbsp;&#10003;<br><br>"
     f"This matches the matrix answer, so the order <i>C R<sub>{th}</sub> R<sub>f</sub></i> is correct.")
    blk("Watch out","warn",
     f"<ul><li><b>Order is everything.</b> The first transformation mentioned goes on the <b>right</b> of the product. "
     f"Building it left to right gives a different matrix and no marks.</li>"
     f"<li>Reflection in the <i>x</i>-axis flips <b><i>y</i></b>, giving diag(1, &minus;1). It is easy to write diag(&minus;1, 1) "
     f"by mistake &mdash; that is reflection in the <i>y</i>-axis.</li>"
     f"<li>A <b>contraction</b> has <i>k</i> &lt; 1 and a <b>dilation</b> has <i>k</i> &gt; 1, but the matrix is <i>kI</i> "
     f"either way. Do not invert the factor.</li>"
     f"<li>Always do the by-hand check above. It takes twenty seconds and catches the order mistake.</li></ul>")


def _defI():
    sec("I.1","The 2-mark definition","Q1a and Q2a &middot; 2 marks &middot; one in EACH question, so you get it either way")
    blk("The question","qbox",
     "Any one of these:<br><br>"
     "&bull;&nbsp; Define the Laplace transform of a function.<br>"
     "&bull;&nbsp; Write the Laplace transform of a periodic function.<br>"
     "&bull;&nbsp; Define a periodic function with an example.")
    blk("Could it appear another way?","alt",
     "<b>Only three forms have ever been set, and all three are one line.</b>"
     "<ul><li>&ldquo;Define the Laplace transform&rdquo; &mdash; Mar&nbsp;24 Q2a</li>"
     "<li>&ldquo;Write the Laplace transform of a periodic function&rdquo; &mdash; Mar&nbsp;24 Q1a</li>"
     "<li>&ldquo;Define a periodic function with an example&rdquo; &mdash; Jun&nbsp;23 Q1a(i)</li></ul>"
     "<b>One more is overdue:</b> the syllabus lists <b>existence conditions</b> for the Laplace transform and they "
     "have never been asked. Learn the one sentence: <i>L</i>{<i>f</i>} exists if <i>f</i> is <b>piecewise continuous</b> "
     "on every finite interval and of <b>exponential order</b>, that is |<i>f</i>(<i>t</i>)| &le; <i>Me</i><sup><i>at</i></sup> "
     "for some constants <i>M</i> and <i>a</i>.")
    blk("What to write &mdash; learn these word for word","fbox",
     "<b>1. Laplace transform.</b> For <i>f</i>(<i>t</i>) defined for <i>t</i> &ge; 0,"
     '<div class="eq"><i>L</i>{<i>f</i>(<i>t</i>)} = <i>F</i>(<i>s</i>) = ' + INT + '<sub>0</sub><sup>' + inf +
     '</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></div>'
     "provided the integral converges.<br><br>"
     "<b>2. Periodic function.</b> <i>f</i> is periodic with period <i>T</i> if <i>f</i>(<i>t</i>+<i>T</i>) = "
     "<i>f</i>(<i>t</i>) for all <i>t</i>. Example: sin&nbsp;<i>t</i>, period 2" + pi + ".<br><br>"
     "<b>3. Transform of a periodic function</b> of period <i>T</i>:"
     '<div class="eq"><i>L</i>{<i>f</i>(<i>t</i>)} = ' + F("1","1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>") +
     INT + '<sub>0</sub><sup><i>T</i></sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></div>')
    blk("Watch out","warn",
     "<ul><li>Two marks for one line, and it is in <b>both</b> questions &mdash; never skip it.</li>"
     "<li>Add &ldquo;provided the integral converges&rdquo;. It shows you know the transform does not always exist.</li>"
     "<li>If asked for an <b>example</b>, give one and state its period.</li></ul>")

def _defII():
    sec("II.1","The 2-mark definition","Q3a and Q4a &middot; 2 marks &middot; one in EACH question")
    blk("The question","qbox",
     "&bull;&nbsp; Define the unit step function and represent it graphically.<br>"
     "&bull;&nbsp; Define the Dirac-delta function and sketch its graph.")
    blk("Could it appear another way?","alt",
     "<b>Both are new to the current format</b> (Mar&nbsp;24 Q3a and Q4a) &mdash; the 2-mark slot did not exist in the "
     "2023 papers. They appeared in the same paper, one in each question, so <b>you get one whichever you choose.</b>"
     "<ul><li>&ldquo;Represent graphically&rdquo;, &ldquo;sketch its graph&rdquo; and &ldquo;draw&rdquo; all mean the "
     "same thing: <b>draw the picture</b>. Half the mark is the sketch.</li>"
     "<li>A likely variant is <b>&ldquo;state the Laplace transform of&rdquo;</b> the unit step or the delta function. "
     "Both are one line, so learn them.</li>"
     "<li>Also possible: <b>state the convolution theorem</b> as a 2-marker &mdash; write "
     "<i>L</i><sup>&minus;1</sup>{<i>F</i>(<i>s</i>)<i>G</i>(<i>s</i>)} = " + INT +
     "<sub>0</sub><sup><i>t</i></sup><i>f</i>(<i>u</i>)<i>g</i>(<i>t</i>&minus;<i>u</i>)&thinsp;<i>du</i>.</li></ul>")
    blk("What to write &mdash; learn these word for word","fbox",
     "<b>1. Unit step (Heaviside) function.</b>"
     '<div class="eq"><i>u</i>(<i>t</i>&minus;<i>a</i>) = 0 &nbsp;for <i>t</i> &lt; <i>a</i>, &nbsp;&nbsp;&nbsp;'
     '<i>u</i>(<i>t</i>&minus;<i>a</i>) = 1 &nbsp;for <i>t</i> &ge; <i>a</i></div>'
     "<b>Graph:</b> flat along zero, a vertical jump of height 1 at <i>t</i> = <i>a</i>, then flat at 1. "
     "Label the axes and mark <i>t</i> = <i>a</i>.<br>"
     "<b>Its transform:</b> <i>L</i>{<i>u</i>(<i>t</i>&minus;<i>a</i>)} = <i>e</i><sup>&minus;<i>as</i></sup>/<i>s</i><br><br>"
     "<b>2. Dirac-delta (unit impulse) function.</b> &#948;(<i>t</i>&minus;<i>a</i>) is the limit, as &#949; &rarr; 0, of a "
     "rectangular pulse of width &#949; and height 1/&#949; at <i>t</i> = <i>a</i>. It satisfies"
     '<div class="eq">&#948;(<i>t</i>&minus;<i>a</i>) = 0 for <i>t</i> &ne; <i>a</i>, &nbsp;&nbsp;and&nbsp;&nbsp; ' +
     INT + '<sub>&minus;' + inf + '</sub><sup>' + inf + '</sup>&#948;(<i>t</i>&minus;<i>a</i>)&thinsp;<i>dt</i> = 1</div>'
     "<b>Graph:</b> a single vertical arrow at <i>t</i> = <i>a</i>, labelled with area 1.<br>"
     "<b>Its transform:</b> <i>L</i>{&#948;(<i>t</i>&minus;<i>a</i>)} = <i>e</i><sup>&minus;<i>as</i></sup>")
    blk("Watch out","warn",
     "<ul><li><b>Draw the graph.</b> A definition without the sketch usually scores one out of two.</li>"
     "<li>The delta function has zero width and infinite height but <b>area exactly 1</b>. Say the area &mdash; that is "
     "what distinguishes it from &ldquo;a very tall spike&rdquo;.</li>"
     "<li>The step is defined with &ge; at <i>t</i> = <i>a</i>. Small detail, easy mark.</li></ul>")

w("</div>")
w('<div class="uw">')
w('<div class="lbl">How this document is organised</div>')
w('<p style="margin:0 0 8px">One section per unit, each in its own colour. Within a unit the questions run in the order they appear on the paper. The last column shows where each sits in your 3-hour plan &mdash; work in <b>that</b> order, revise in <b>this</b> one.</p>')
w('<table class="idx"><tr><th style="width:8%">Section</th><th>Question</th><th style="width:11%" class="c">On the paper</th><th style="width:8%" class="c">Marks</th><th style="width:15%">Study step</th></tr>')
w('<tr><td class="c1">I.1</td><td>The 2-mark definition</td><td class="c">Q1a / Q2a</td><td class="c"><b>02</b></td><td>step 7</td></tr>')
w('<tr><td class="c1">I.2</td><td>Show the cos&nbsp;&radic;<i>t</i> result</td><td class="c">Q1b</td><td class="c"><b>04</b></td><td>step 6</td></tr>')
w('<tr><td class="c1">I.3</td><td>Prove the <i>t<sup>n</sup></i> rule</td><td class="c">Q1c</td><td class="c"><b>07</b></td><td>step 4</td></tr>')
w('<tr><td class="c2">II.1</td><td>The 2-mark definition</td><td class="c">Q3a / Q4a</td><td class="c"><b>02</b></td><td>step 7</td></tr>')
w('<tr><td class="c2">II.2</td><td>Piecewise function via Heaviside</td><td class="c">Q3c</td><td class="c"><b>07</b></td><td>step 5</td></tr>')
w('<tr><td class="c2">II.3</td><td>Solve ODEs by Laplace transforms</td><td class="c">Q3d / Q4d</td><td class="c"><b>07</b></td><td>step 8</td></tr>')
w('<tr><td class="c3">III.1</td><td>Span, basis, independence</td><td class="c">Q5a</td><td class="c"><b>06</b></td><td>step 11</td></tr>')
w('<tr><td class="c3">III.2</td><td>Prove <i>T</i> is linear, find images</td><td class="c">Q5b</td><td class="c"><b>07</b></td><td>step 2</td></tr>')
w('<tr><td class="c3">III.3</td><td>The rotation-operator proof</td><td class="c">Q5c</td><td class="c"><b>07</b></td><td>step 12</td></tr>')
w('<tr><td class="c3">III.4</td><td>Composition of transformations</td><td class="c">Q6a</td><td class="c"><b>06</b></td><td>overtime</td></tr>')
w('<tr><td class="c4">IV.1</td><td>Least-squares solution</td><td class="c">Q8b</td><td class="c"><b>10</b></td><td>step 3</td></tr>')
w('<tr><td class="c4">IV.2</td><td>The four fundamental subspaces</td><td class="c">Q7c</td><td class="c"><b>07</b></td><td>overtime</td></tr>')
w('<tr><td class="c4">IV.3</td><td>Complete solution of <i>Ax</i> = <i>b</i></td><td class="c">Q7a</td><td class="c"><b>06</b></td><td>overtime</td></tr>')
w('<tr><td class="c5">V.1</td><td>Positive-definite check</td><td class="c">Q10a</td><td class="c"><b>05</b></td><td>overtime</td></tr>')
w('<tr><td class="c5">V.2</td><td>Unitary and Hermitian check</td><td class="c">Q10b</td><td class="c"><b>05</b></td><td>step 1</td></tr>')
w('<tr><td class="c5">V.3</td><td>Orthogonal diagonalization</td><td class="c">Q10c</td><td class="c"><b>10</b></td><td>step 10</td></tr>')
w('<tr><td class="c5">V.4</td><td>Singular Value Decomposition</td><td class="c">Q9c</td><td class="c"><b>10</b></td><td>step 9</td></tr>')
w("</table>")
w("</div>")
openu('u1')
banner('I', 'Laplace Transforms', 'Answer <b>Q1</b> &mdash; the question containing the <i>t<sup>n</sup></i> proof', '<b>20 marks</b> &middot; Q1 or Q2 &middot; a(2) + b(4) + c(7) + d(7)<br><b>You can answer a, b and c &mdash; 13 of 20.</b> The d part is a long evaluation and is deliberately cut.<br><b>Trigger:</b> in all four past papers the <i>t<sup>n</sup></i> proof and the sin&nbsp;&radic;<i>t</i> question sit in the <b>same</b> question, and the periodic-function problem sits in the other one.')
_defI()
_s6()
_s4()
closeu()
openu('u2')
banner('II', 'Application of Laplace Transforms', 'Answer <b>Q3</b> &mdash; the question containing the piecewise function', '<b>20 marks</b> &middot; Q3 or Q4 &middot; a(2) + b(4) + c(7) + d(7)<br><b>You can answer a, c and d &mdash; 14 of 20.</b> The b part, a short inverse transform, is an overtime item.<br><b>Trigger:</b> in all four papers an ODE-type problem sits directly next to the Heaviside question. That pairing is 14 marks.')
_defII()
_s5()
_s8()
closeu()
openu('u3')
banner('III', 'Vector Space and Linear Transformation', 'Answer <b>Q5</b> &mdash; a full 20', '<b>20 marks</b> &middot; Q5 or Q6 &middot; a(6) + b(7) + c(7)<br><b>You can answer all three parts of Q5 &mdash; 20 of 20.</b><br><b>Your strongest unit:</b> no calculus anywhere, and every question type this unit has ever asked is covered here. III.4 is your Q6 backup in case Q5c turns out not to be the rotation proof.')
_s11()
_s2()
_s12()
_s16()
closeu()
openu('u4')
banner('IV', 'Orthogonal Projections', 'Answer <b>Q8</b> &mdash; or <b>Q7</b> if you finished the overtime items', '<b>20 marks</b> &middot; Q7 is a(6) + b(7) + c(7) &nbsp;|&nbsp; Q8 is a(10) + b(10)<br><b>You can answer Q8b alone &mdash; 10 of 20.</b> With IV.2 and IV.3 done, Q7 gives you 13 instead.<br><b>QR factorization is deliberately cut:</b> it appeared in all four papers, but the matrix changed every single time, so there is nothing to rehearse.')
_s3()
_s14()
_s15()
closeu()
openu('u5')
banner('V', 'Applications of Eigenvalue Decomposition', 'Answer <b>Q10</b> &mdash; the question with &ldquo;orthogonally diagonalize&rdquo;', '<b>20 marks</b> &middot; Q9 or Q10 &middot; a(5) + b(5) + c(10)<br><b>You can answer Q10b and Q10c &mdash; 15 of 20</b>, and a full 20 once V.1 is done.<br><b>The best-value unit on the paper:</b> the two 5-mark checks take about two minutes each, and the 10-marker used the same matrix in three of the four papers. V.4 covers the other question, Q9.')
_s13()
_s1()
_s10()
_s9()
closeu()

# ================= EMIT =================
doc="<!doctype html><html><head><meta charset='utf-8'><title>24CS31 Worked Solutions</title><style>"+CSS+"</style></head><body>"+"".join(H)+"</body></html>"
import io,os
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"24CS31_Worked_Solutions.html")
io.open(out,"w",encoding="utf-8").write(doc); print("wrote",out,len(doc),"bytes")

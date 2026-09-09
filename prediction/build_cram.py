#!/usr/bin/env python3
def M(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat"><table>{b}</table></span>'
def V(c): return M([[x] for x in c])
def PW(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat pw"><table>{b}</table></span>'
def F(n,d): return f'<span class="f"><span class="n">{n}</span><span class="d">{d}</span></span>'
sp="&#8722;"; inf="&#8734;"; pi="&#960;"; th="&#952;"; om="&#969;"; sq="&#8730;"; INT="&#8747;"
ARR="&#8594;"; LEQ="&#8804;"; inv="<i>L</i><sup>&minus;1</sup>"

CSS = """
@page { size:A4; margin:8mm 8mm 9mm 8mm; }
*{box-sizing:border-box}
body{font-family:"DejaVu Serif",Georgia,serif;font-size:8.2pt;line-height:1.3;color:#14161b;margin:0}
h1{font-size:16pt;margin:0;letter-spacing:-.3px}
.hd{border:2px solid #14161b;border-radius:4px;padding:7px 10px;margin-bottom:7px}
.hd .s{font-size:8.6pt;color:#39414f;margin-top:1px}
.unit{background:#1d2433;color:#fff;padding:4px 8px;border-radius:3px;margin:9px 0 0;
      font-size:10.5pt;font-weight:700;display:flex;justify-content:space-between}
.unit .rule{font-size:8.2pt;font-weight:400;color:#cfd6e4}
.pick{background:#e8f3ec;border:1px solid #0d7a45;border-left:5px solid #0d7a45;border-radius:0 3px 3px 0;
      padding:4px 8px;font-size:8.3pt;margin:0 0 4px}
.pick b{color:#0d5c34}
table.g{width:100%;border-collapse:collapse;margin:0 0 4px;font-size:8.1pt}
table.g th{background:#39414f;color:#fff;text-align:left;padding:3px 5px;font-size:7.6pt;border:.7px solid #39414f}
table.g td{border:.7px solid #b9c0cc;padding:3px 5px;vertical-align:middle}
table.g tr:nth-child(even) td{background:#f5f7fa}
.c{text-align:center}
.lk{background:#0d7a45!important;color:#fff;font-weight:700;text-align:center;font-size:7.4pt}
.hi{background:#3f8f5f!important;color:#fff;font-weight:700;text-align:center;font-size:7.4pt}
.md{background:#b8842a!important;color:#fff;font-weight:700;text-align:center;font-size:7.4pt}
.lo{background:#7a4fa3!important;color:#fff;font-weight:700;text-align:center;font-size:7.4pt}
.z{background:#6b7280!important;color:#fff;font-weight:700;text-align:center;font-size:7.4pt}
.sec{font-weight:700;color:#0d5c34;text-align:center}
.sec2{font-weight:700;color:#8a5a12;text-align:center}
.mat{display:inline-block;vertical-align:middle;position:relative;padding:1px 6px;margin:0 1px}
.mat::before,.mat::after{content:"";position:absolute;top:0;bottom:0;width:3px;border:1px solid #14161b}
.mat::before{left:0;border-right:none}
.mat::after{right:0;border-left:none}
.mat.pw::after{display:none}
.mat.pw td{text-align:left;padding-right:7px!important}
.mat table{border-collapse:collapse}
.mat td{padding:0 3px!important;text-align:center;font-size:.88em;line-height:1.12;
        border:none!important;background:transparent!important}
.f{display:inline-block;vertical-align:-.45em;text-align:center;margin:0 2px}
.f .n{display:block;border-bottom:1px solid #14161b;padding:0 3px}
.f .d{display:block;padding:0 3px}
.foot{margin-top:8px;border-top:1px solid #b9c0cc;padding-top:4px;font-size:7.2pt;color:#5b6472}
.brk{page-break-before:always}
.avoid{page-break-inside:avoid}
.box{border:1.5px solid #a04545;background:#fdf6f6;border-radius:3px;padding:6px 9px;margin:7px 0;font-size:8pt}
.box.g{border-color:#0d7a45;background:#f2faf5}
.box b{color:#14161b}
"""
H=[]
def w(s): H.append(s)

w(f"""<div class="hd"><h1>24CS31 &mdash; Last-Minute Prediction Sheet</h1>
<div class="s">Laplace Transforms &amp; Vector Space &middot; SEE 100 marks / 3 hrs &middot;
<b>Answer one full question from each unit</b> &middot; Q1|Q2 &rarr; Unit I &nbsp; Q3|Q4 &rarr; II &nbsp;
Q5|Q6 &rarr; III &nbsp; Q7|Q8 &rarr; IV &nbsp; Q9|Q10 &rarr; V</div></div>

<div class="box g avoid"><b>THE 60-SECOND RULE.</b> Don't read all ten questions. In each unit, find the
<b>one trigger</b> below and answer <b>that</b> question &mdash; the rest of its parts are the ones you studied.
&nbsp;<b>I:</b> the <i>t<sup>n</sup></i> proof &nbsp;&bull;&nbsp; <b>II:</b> the Heaviside piecewise
&nbsp;&bull;&nbsp; <b>III:</b> the reflection&rarr;rotation&rarr;contraction question &nbsp;&bull;&nbsp;
<b>IV:</b> QR + least-squares (that's Q8) &nbsp;&bull;&nbsp; <b>V:</b> orthogonally diagonalize.
</div>

<div class="box avoid"><b>READ THE TWO RIGHT-HAND COLUMNS SEPARATELY &mdash; they mean different things.</b><br>
<b>&ldquo;Topic came up&rdquo;</b> = how many of the four papers asked <i>this kind of question at all</i>, with any
numbers. <b>&ldquo;SAME values&rdquo;</b> = how many asked it with the <i>identical matrix, function or constants</i>
printed here. A row reading <b>4/4 topic / 0/4 same</b> (e.g. QR factorization) is <b>certain to appear but the matrix
will be new</b> &mdash; you must own the method, not an answer. A row reading <b>4/4 / 3/4</b> (orthogonal
diagonalization) is a question you can rehearse end-to-end and reproduce.<br>
Colour is just the size of the number: <span class="lk">&nbsp;4/4&nbsp;</span>
<span class="hi">&nbsp;3/4&nbsp;</span> <span class="md">&nbsp;2/4&nbsp;</span>
<span class="lo">&nbsp;1/4&nbsp;</span> <span class="z">&nbsp;0/4&nbsp;</span>.
Proofs count as &ldquo;same values&rdquo; when the wording is identical. The <b>2-mark definition slot only exists in the
March&nbsp;2024 format</b>, so it can never score above 1/4 &mdash; it is still near-certain under the current pattern.</div>""")

def unit(n, title, rule, pick, rows):
    w(f'<div class="unit"><span>UNIT {n} &mdash; {title}</span><span class="rule">{rule}</span></div>')
    w(f'<div class="pick">{pick}</div>')
    w('<table class="g"><tr><th style="width:4%" class="c">#</th><th>Question &mdash; write this</th>'
      '<th class="c" style="width:6%">Marks</th><th class="c" style="width:12%">Section</th>'
      '<th class="c" style="width:7%">Topic<br>came up</th><th class="c" style="width:7%">SAME<br>values</th></tr>')
    for i,(q,mk,sec,tf,tc,ef,ec) in enumerate(rows,1):
        sc = "sec" if tc in ("lk","hi") and "OTHER" not in sec else "sec2"
        w(f'<tr><td class="c"><b>{i}</b></td><td>{q}</td><td class="c"><b>{mk}</b></td>'
          f'<td class="{sc}">{sec}</td><td class="{tc}">{tf}</td><td class="{ec}">{ef}</td></tr>')
    w("</table>")

# ---------------- UNIT I ----------------
unit("I","Laplace Transforms","20 marks &middot; a(2) + b(4) + c(7) + d(7)",
 "<b>PICK the question containing the <i>t<sup>n</sup></i> proof.</b> The sin&nbsp;&radic;<i>t</i> question is "
 "<b>always</b> in the same one (4/4 papers) &mdash; that's 11 marks together. The periodic-function problem is "
 "always in the <i>other</i> one.",
 [(f"<b>Prove</b> &nbsp;<i>L</i>{{<i>t<sup>n</sup>f</i>(<i>t</i>)}} = (&minus;1)<sup><i>n</i></sup> "
   + F("<i>d<sup>n</sup></i>","<i>ds<sup>n</sup></i>") + "{<i>F</i>(<i>s</i>)}, &nbsp;<i>n</i> a positive integer. "
   "<span style='color:#0d5c34'><b>&larr; THE trigger. Do this first.</b></span>","07","Q1c or Q2b","4/4","lk","4/4","lk"),
  (f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = "+F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")+
   f"<i>e</i><sup>&minus;1/4<i>s</i></sup>, &nbsp;<b>show</b> &nbsp;<i>L</i>{{"+F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")+"} = "
   +F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>","04","Q1b &mdash; with #1","4/4","lk","2/4","md"),
  (f"<b>Evaluate</b> &nbsp;(i) <i>L</i>{{<i>t e</i><sup>&minus;4<i>t</i></sup> sin&nbsp;3<i>t</i>}} &nbsp;&nbsp; "
   f"(ii) <i>L</i>{{"+F("<i>t</i> &minus; sinh&nbsp;<i>at</i>","<i>t</i>")+"} &nbsp;&nbsp;"
   "<span class='mut'>(multiply by <i>t</i> &rarr; &minus;<i>F</i>&prime;(<i>s</i>); divide by <i>t</i> &rarr; "
   f"{INT}<sub>s</sub><sup>{inf}</sup><i>F</i>)</span>","07","Q1d or Q2c","4/4","lk","1/4","lo"),
  (f"<b>Evaluate</b> &nbsp;(i) {INT}<sub>0</sub><sup>{inf}</sup> "+F("<i>e</i><sup>&minus;<i>t</i></sup> sin&nbsp;<i>t</i>","<i>t</i>")
   +f"<i>dt</i> &nbsp;&nbsp;(<i>ans</i> {pi}/4) &nbsp;&nbsp;(ii) <i>L</i>{{<i>t</i>&thinsp;sin&nbsp;3<i>t</i>&thinsp;cos&nbsp;2<i>t</i>}}","07","Q1d","3/4","hi","1/4","lo"),
  ("<b>Periodic function.</b> Triangular wave, period 2<i>a</i>: &nbsp;<i>f</i>(<i>t</i>) = "
   +PW([["<i>t</i>,",f"0 {LEQ} <i>t</i> {LEQ} <i>a</i>"],["2<i>a</i> &minus; <i>t</i>,",f"<i>a</i> {LEQ} <i>t</i> {LEQ} 2<i>a</i>"]])
   +f" &nbsp;<i>ans</i> "+F("1","<i>s</i><sup>2</sup>")+f"tanh("+F("<i>as</i>","2")+f") &nbsp;&nbsp;<span style='color:#8a5a12'>OR</span> half-rectifier "
   f"<i>E</i>&thinsp;sin({om}<i>t</i>) on (0,{pi}/{om}), 0 after","07","<b>OTHER</b> question","4/4","lk","2/4","md"),
  (f"<b>Obtain</b> &nbsp;<i>L</i>{{({sq}<i>t</i> + 1/{sq}<i>t</i>)<sup>3</sup>}} &nbsp;&nbsp; "
   f"<span style='color:#8a5a12'>(expand first, then term-by-term)</span>","04","Q2b","2/4","md","1/4","lo"),
  ("<b>Definition (2 marks &mdash; free).</b> &ldquo;Write the Laplace transform of a periodic function&rdquo; = "
   +F("1",f"1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>")+INT+"<sub>0</sub><sup><i>T</i></sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)<i>dt</i>"
   " &nbsp;&bull;&nbsp; or &ldquo;Define the Laplace transform&rdquo;","02","Q1a &amp; Q2a","2/4","md","1/4","lo"),
 ])

# ---------------- UNIT II ----------------
unit("II","Application of Laplace Transforms","20 marks &middot; a(2) + b(4) + c(7) + d(7)",
 "<b>PICK the question containing the Heaviside piecewise function.</b> An ODE problem is <b>always</b> sitting "
 "next to it (4/4 papers) &mdash; that's <b>14 guaranteed marks</b> in one question. Convolution is in the other one.",
 [("<b>Express in terms of the Heaviside function and find its LT:</b> &nbsp;<i>f</i>(<i>t</i>) = "
   +PW([["<i>t</i><sup>2</sup>,","0 &lt; <i>t</i> &lt; 2"],["4<i>t</i>,","2 &lt; <i>t</i> &lt; 4"],["8,","<i>t</i> &gt; 4"]])
   +" <span style='color:#0d5c34'><b>&larr; THE trigger. Same values twice.</b></span>","07","Q3c","4/4","lk","2/4","md"),
  ("<b>Solve by Laplace transforms</b> (one of these, in the <i>same</i> question as #1):<br>"
   "&bull; <i>dx</i>/<i>dt</i> &minus; 2<i>y</i> = cos&nbsp;2<i>t</i>; &nbsp;<i>dy</i>/<i>dt</i> + 2<i>x</i> = sin&nbsp;2<i>t</i>, &nbsp;<i>x</i>(0)=1, <i>y</i>(0)=0<br>"
   "&bull; <i>y</i>&Prime; + 4<i>y</i>&prime; + 3<i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup> &nbsp;(set twice, different ICs)<br>"
   "&bull; LR circuit: <i>L di</i>/<i>dt</i> + <i>Ri</i> = <i>Ee</i><sup>&minus;<i>at</i></sup> &rarr; <i>i</i> = "
   +F("<i>E</i>","<i>R</i>&minus;<i>aL</i>")+"(<i>e</i><sup>&minus;<i>at</i></sup> &minus; <i>e</i><sup>&minus;<i>Rt/L</i></sup>)",
   "07","Q3d / Q4d &mdash; with #1","4/4","lk","2/4","md"),
  ("<b>Convolution theorem.</b> &nbsp;"+inv+"{"+F("<i>s</i><sup>2</sup>","(<i>s</i><sup>2</sup>+<i>a</i><sup>2</sup>)(<i>s</i><sup>2</sup>+<i>b</i><sup>2</sup>)")
   +"} &nbsp;&nbsp;<span style='color:#8a5a12'>OR</span> verify it for <i>f</i><sub>1</sub>=<i>t</i>, <i>f</i><sub>2</sub>=cos&nbsp;<i>t</i>",
   "07","<b>OTHER</b> question","4/4","lk","2/4","md"),
  ("<b>Evaluate</b> &nbsp;"+inv+"{ log "+F("<i>s</i><sup>2</sup>+1","<i>s</i>(<i>s</i>+1)")+" } &nbsp;&nbsp;"
   "<span style='color:#8a5a12'>differentiate <i>F</i>, then "+inv+"{<i>F</i>&prime;} = &minus;<i>t f</i>(<i>t</i>)</span>","04","Q3b","3/4","hi","2/4","md"),
  ("<b>Find</b> &nbsp;"+inv+"{"+F("3<i>s</i>+2","<i>s</i><sup>2</sup>&minus;<i>s</i>&minus;2")+"} &nbsp;&mdash; partial fractions. "
   "Every paper carries a short inverse LT in <i>both</i> options.","04","Q4b","4/4","lk","1/4","lo"),
  ("<b>Definition (2 marks &mdash; free).</b> Define the unit step function + graph &nbsp;&bull;&nbsp; "
   "Define the Dirac-delta function + sketch","02","Q3a &amp; Q4a","1/4","lo","1/4","lo"),
 ])

# ---------------- UNIT III ----------------
A_KER=M([["1","2","3"],["0",sp+"1","1"],["1","1","4"]])
A_ROT=M([["cos&#952;",sp+"sin&#952;"],["sin&#952;","cos&#952;"]])
unit("III","Vector Space and Linear Transformation","20 marks &middot; a(6) + b(7) + c(7)",
 "<b>PICK the question containing the reflection&rarr;rotation&rarr;contraction problem</b> (usually <b>Q6</b>). "
 "In the two newest papers that question also held the transition matrix <i>and</i> kernel&amp;range &mdash; three "
 "4/4 topics, a clean 20.",
 [(f"<b>Matrix of a composition + image of a point.</b> Reflection in the <i>x</i>-axis, then rotation {pi}/2, "
   f"then contraction of factor 1/3. Find the image of {V(['4','1'])}. "
   "<span style='color:#0d5c34'><b>&larr; THE trigger.</b></span><br>"
   "<span style='color:#8a5a12'>Multiply <b>right to left</b>: <i>k R</i><sub>&theta;</sub> <i>Ref</i>. "
   "Reflect in <i>x</i> = diag(1,&minus;1); in <i>y</i> = diag(&minus;1,1).</span>","06","Q6a","4/4","lk","1/4","lo"),
  (f"<b>Transition matrix.</b> <i>B</i> = {{(1,&nbsp;2), (3,&nbsp;&minus;1)}}, &nbsp;<i>B</i>&prime; = {{(3,&nbsp;1), (5,&nbsp;2)}} of <i>R</i><sup>2</sup>. "
   f"Find the transition matrix from <i>B</i> to <i>B</i>&prime;; if [<i>u</i>]<sub><i>B</i></sub> = {V(['2','1'])}, find [<i>u</i>]<sub><i>B</i>&prime;</sub>. "
   "<span style='color:#0d5c34'><b>Same bases twice running.</b></span>","07","Q6b &mdash; with #1","4/4","lk","2/4","md"),
  (f"<b>Kernel and range + verify rank&ndash;nullity</b> for &nbsp;<i>A</i> = {A_KER} &nbsp;&nbsp;"
   "<span style='color:#8a5a12'>(rank 2, nullity 1)</span>. Be ready for the formula version too, e.g. "
   "<i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>, <i>x</i>&minus;<i>y</i>, <i>y</i>).","07","Q6c &mdash; with #1, #2","4/4","lk","1/4","lo"),
  (f"<b>Prove <i>T</i> is linear + find images.</b> <i>T</i>:<i>P</i><sub>2</sub>{ARR}<i>P</i><sub>2</sub>, "
   f"<i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup>+<i>c</i>; image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1. "
   f"<span style='color:#8a5a12'>OR <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>); images of (1,2), (2,&minus;5)</span>","07","<b>Q5b</b> &mdash; all 4 papers","4/4","lk","2/4","md"),
  ("<b>Span / linear combination / independence / basis.</b> e.g. is a set of four 2&times;2 matrices a basis of "
   "<i>M</i><sub>22</sub>? (flatten each to a 4-vector, take the 4&times;4 determinant) &nbsp;&bull;&nbsp; "
   "or: does {(1,2,3), (&minus;1,&minus;1,0), (2,5,4)} span <i>R</i><sup>3</sup>?","06","Q5a","4/4","lk","1/4","lo"),
  (f"<b>Prove</b> <i>T</i>(<i>x</i>) = <i>Ax</i> rotates <i>x</i> through {th} about the origin if "
   f"<i>A</i> = {A_ROT} &nbsp;&mdash; bookwork escape hatch if Q6 looks ugly.","07","Q5c","2/4","md","2/4","md"),
 ])

# ---------------- UNIT IV ----------------
A_SUB=M([["1","2","0","1"],["0","1","1","0"],["1","2","0","1"]])
A_LS=M([["1","3","5"],["1","1","0"],["1","1","2"],["1","3","3"]])
B_LS=V(["3","5","7",sp+"3"])
A_QR=M([["3",sp+"5","1"],["1","1","1"],[sp+"1","5",sp+"2"],["3",sp+"7","8"]])
unit("IV","Orthogonal Projections","20 marks &middot; <b>Q7 = 6+7+7</b> &nbsp;|&nbsp; <b>Q8 = 10+10</b>",
 "<b>Q8 is QR + least-squares</b> &mdash; both 4/4, and that's the whole 20. Take it if your algebra holds up. "
 "<b>Q7 is the safer three-problem question</b> &mdash; and the four-subspaces question is <i>always</i> in Q7 (4/4).",
 [(f"<b>QR factorization.</b> Mar&nbsp;24 used {A_QR}. Matrix changes every paper &mdash; own the method: "
   "Gram&ndash;Schmidt the columns, normalise &rarr; <i>Q</i>, then <b><i>R</i> = <i>Q</i><sup>T</sup><i>A</i></b>.","10","<b>Q8a</b>","4/4","lk","0/4","z"),
  (f"<b>Least-squares solution of <i>AX</i> = <i>b</i>:</b> &nbsp;<i>A</i> = {A_LS} &nbsp;<i>b</i> = {B_LS} "
   "<span style='color:#0d5c34'><b>&larr; identical values, twice.</b></span> Solve <i>A</i><sup>T</sup><i>A</i>&#770;<i>x</i> = <i>A</i><sup>T</sup><i>b</i>.","10","<b>Q8b</b> &mdash; with #1","4/4","lk","2/4","md"),
  (f"<b>Dimension and basis for the four fundamental subspaces</b> of &nbsp;<i>A</i> = {A_SUB} "
   "<span style='color:#0d5c34'><b>&larr; same matrix in 3 of 4 papers.</b></span> "
   "<span style='color:#8a5a12'>row&nbsp;3 = row&nbsp;1 &rArr; rank 2; dim&nbsp;nul = 2, dim&nbsp;left-nul = 1</span>","07","<b>Q7</b> &mdash; always","4/4","lk","3/4","hi"),
  ("<b>Complete solution of <i>Ax</i> = <i>b</i>.</b> Mar&nbsp;24: <i>x</i>+3<i>y</i>+3<i>z</i>=1, "
   "2<i>x</i>+6<i>y</i>+9<i>z</i>=5, &minus;<i>x</i>&minus;3<i>y</i>+3<i>z</i>=5. "
   "Answer as <i>x</i> = <i>x<sub>p</sub></i> + <i>c</i><sub>1</sub><i>n</i><sub>1</sub> + &hellip;","06","Q7a","3/4","hi","0/4","z"),
  (f"<b>Orthogonal projection.</b> <i>y</i> = {V(['2','3'])}, <i>u</i> = {V(['4',sp+'7'])}. Find proj of <i>y</i> onto <i>u</i>; "
   "split <i>y</i> into a part in span{<i>u</i>} and a part orthogonal to it. "
   "<span style='color:#8a5a12'>proj = ((<i>y</i>&middot;<i>u</i>)/(<i>u</i>&middot;<i>u</i>))<i>u</i> &mdash; 5 minutes, 7 marks</span>","07","Q7b","1/4","lo","1/4","lo"),
  ("<b>Gram&ndash;Schmidt orthonormal basis</b> &mdash; e.g. span{(1,1,1,1), (0,1,1,1), (0,0,1,1)}. "
   "You already know this from QR: just stop before forming <i>R</i>.","10","Q8a substitute","1/4","lo","1/4","lo"),
 ])

# ---------------- UNIT V ----------------
A_OR=M([["3",sp+"1","1"],[sp+"1","5",sp+"1"],["1",sp+"1","3"]])
A_PD=M([["1",sp+"2","1"],[sp+"2","4",sp+"2"],["1",sp+"2","1"]])
A_SV=M([["1","1"],["3",sp+"3"]])
A_UN=M([["0","<i>i</i>"],[sp+"<i>i</i>","0"]])
A_HE=M([["3","7"+sp+"4<i>i</i>",sp+"2+5<i>i</i>"],["7+4<i>i</i>",sp+"2","3+<i>i</i>"],[sp+"2"+sp+"5<i>i</i>","3"+sp+"<i>i</i>","4"]])
A_MK=M([["0.95","0.03"],["0.05","0.97"]])
unit("V","Applications of Eigenvalue Decomposition","20 marks &middot; a(5) + b(5) + c(10)",
 "<b>PICK the question containing &ldquo;orthogonally diagonalize&rdquo;</b> (Q10 in Mar&nbsp;24). The two "
 "property-checks travel with it in 3 of 4 papers &mdash; 10 + 5 + 5, and the 5-markers are ten minutes total. "
 "SVD sits in the <i>other</i> question.",
 [(f"<b>Orthogonally diagonalize</b> &nbsp;<i>A</i> = {A_OR} "
   "<span style='color:#0d5c34'><b>&larr; THE trigger. Same matrix, 3 of 4 papers.</b></span><br>"
   "<span style='color:#8a5a12'>eigenvalues <b>2, 3, 6</b> &mdash; all distinct, so eigenvectors come out orthogonal "
   "on their own. Normalise &rarr; <i>P</i>, then <i>P</i><sup>T</sup><i>AP</i> = <i>D</i>.</span>","10","Q10c","4/4","lk","3/4","hi"),
  (f"<b>Is</b> &nbsp;<i>A</i> = {A_PD} <b>positive definite?</b> "
   "<span style='color:#8a5a12'>minors 1, 0, 0 &rarr; <b>positive semi-definite, NOT positive definite</b>. Say so explicitly.</span>","05","Q10a &mdash; with #1","4/4","lk","2/4","md"),
  (f"<b>Is</b> &nbsp;<i>A</i> = {A_UN} <b>unitary?</b> Show <i>A</i><sup>*</sup><i>A</i> = <i>I</i> &nbsp;(<b>yes</b>) "
   f"&nbsp;&nbsp;<span style='color:#8a5a12'>OR the Hermitian version:</span> is {A_HE} Hermitian? &nbsp;(<b>yes</b>)","05","Q10b &mdash; with #1, #2","4/4","lk","2/4","md"),
  (f"<b>Find the SVD of</b> &nbsp;<i>A</i> = {A_SV} "
   f"<span style='color:#8a5a12'>&nbsp;<i>A</i><sup>T</sup><i>A</i> = {M([['10',sp+'8'],[sp+'8','10']])}, "
   f"eigenvalues 18 and 2 &rArr; singular values 3{sq}2 and {sq}2</span>","10","<b>OTHER</b> question (Q9c)","4/4","lk","2/4","md"),
  ("<b>Quadratic form &rarr; no cross-product terms.</b> <i>Q</i>(<i>x</i>) = <i>x</i><sub>1</sub><sup>2</sup> "
   "&minus; 8<i>x</i><sub>1</sub><i>x</i><sub>2</sub> &minus; 5<i>x</i><sub>2</sub><sup>2</sup>. "
   "<span style='color:#8a5a12'>Build the symmetric matrix, orthogonally diagonalise, substitute <i>x</i> = <i>Py</i>.</span>","05","Q9a","2/4","md","0/4","z"),
  (f"<b>Steady state of the Markov matrix</b> &nbsp;<i>A</i> = {A_MK} &nbsp;&nbsp;"
   "<span style='color:#8a5a12'>solve (<i>A</i>&minus;<i>I</i>)<i>x</i> = 0, scale so entries sum to 1</span>","05","Q9b","1/4","lo","1/4","lo"),
  ("<b>Diagonalize and hence find <i>A<sup>n</sup></i></b> &nbsp;(<i>A<sup>n</sup></i> = <i>PD<sup>n</sup>P</i><sup>&minus;1</sup>). "
   "Appeared 3 papers straight, then <b>skipped in Mar&nbsp;24</b> &mdash; which makes it <b>overdue</b>, not safe.","10","Q9 (10-mark slot)","3/4","hi","0/4","z"),
 ])

w(f"""<div class="box avoid"><b>IF YOU HAVE 20 SPARE MINUTES &mdash; the one hole in your prep.</b>
<b>PCA</b> is named in your syllabus <i>and</i> in CO5, and has <b>never</b> been asked in four papers. If it comes,
it's 5 marks in Unit&nbsp;V, most likely next to the SVD. All you need: centre the data (subtract the column means),
form the covariance matrix <i>C</i> = """+F("1","<i>n</i>&minus;1")+"""<i>X</i><sup>T</sup><i>X</i>, find its
eigenvalues and eigenvectors, take the eigenvector of the largest eigenvalue as the first principal component, and
report {LAM}<sub>1</sub>/&Sigma;{LAM}<sub>i</sub> as the variance it explains. <b>Conic sections</b> is the same
gap &mdash; diagonalise the quadratic form; both eigenvalues the same sign &rarr; ellipse, opposite signs &rarr; hyperbola.
</div>

<div class="foot"><b>How to read this:</b> &ldquo;Section&rdquo; is the slot the question occupied in the March&nbsp;2024 paper
(the only one under your current course title) with the older papers cross-checked. &ldquo;Freq&rdquo; is how many of the
four papers carried that topic. Items marked <b>identical values</b> have been set with the same numbers more than once.
Predictions are inferences from four papers &mdash; strong, not guaranteed. Full 22-page analysis, pairing laws and the
complete question index are in <i>24CS31_Prediction_Sheet.pdf</i>.</div>""".replace("{LAM}","&lambda;"))

doc="<!doctype html><html><head><meta charset='utf-8'><title>24CS31 Cram Sheet</title><style>"+CSS+"</style></head><body>"+"".join(H)+"</body></html>"
import io,os
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"24CS31_LastMinute_Cram_Sheet.html")
io.open(out,"w",encoding="utf-8").write(doc); print("wrote",out)

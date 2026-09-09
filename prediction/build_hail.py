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
ARR="&#8594;"; inv="<i>L</i><sup>&minus;1</sup>"

CSS="""
@page{size:A4;margin:8mm 8mm 9mm 8mm}
*{box-sizing:border-box}
body{font-family:"DejaVu Serif",Georgia,serif;font-size:8.2pt;line-height:1.3;color:#14161b;margin:0}
h1{font-size:16.5pt;margin:0;letter-spacing:-.3px}
.hd{border:2.5px solid #a04545;border-radius:4px;padding:7px 10px;margin-bottom:6px;background:#fdf6f6}
.hd .s{font-size:8.5pt;color:#39414f;margin-top:2px}
.bar{background:#1d2433;color:#fff;padding:4px 8px;border-radius:3px;margin:10px 0 4px;font-size:10.5pt;
     font-weight:700;display:flex;justify-content:space-between}
.bar .r{font-size:8.2pt;font-weight:400;color:#cfd6e4}
.bar.ot{background:#8a5a12}
table.g{width:100%;border-collapse:collapse;margin:0 0 5px;font-size:8.1pt}
table.g th{background:#39414f;color:#fff;text-align:left;padding:3px 5px;font-size:7.6pt;border:.7px solid #39414f}
table.g td{border:.7px solid #b9c0cc;padding:3px 5px;vertical-align:middle}
table.g tr:nth-child(even) td{background:#f5f7fa}
.c{text-align:center}
.pass td{background:#0d7a45!important;color:#fff!important;font-weight:700}
/* question map */
table.qm{width:100%;border-collapse:collapse;margin:2px 0 5px;font-size:7.8pt;table-layout:fixed}
table.qm th{background:#29334a;color:#fff;padding:2.5px 4px;font-size:7.3pt;border:.7px solid #29334a;text-align:center}
table.qm td{border:.7px solid #b9c0cc;padding:3px 5px;vertical-align:top;background:#fff}
table.qm td.q{background:#29334a!important;color:#fff;font-weight:700;text-align:center;width:6%}
table.qm td.ok{background:#e8f3ec!important;border-left:3px solid #0d7a45}
table.qm td.no{background:#f1f2f4!important;color:#8b929c}
table.qm .mk{font-weight:700;color:#14161b}
table.qm td.no .mk{color:#8b929c}
table.qm .tick{float:right;font-weight:700;color:#0d7a45}
table.qm td.no .tick{color:#b0b5bd}
.verd{background:#e8f3ec;border:1px solid #0d7a45;border-left:5px solid #0d7a45;border-radius:0 3px 3px 0;
      padding:4px 8px;font-size:8.3pt;margin:0 0 6px}
.verd b{color:#0d5c34}
.stp{border:1px solid #c2c9d4;border-left:5px solid #0d7a45;border-radius:0 3px 3px 0;padding:6px 9px;margin:5px 0;background:#fbfcfd}
.stp.ot{border-left-color:#b8842a}
.sh{font-weight:700;font-size:8.8pt;color:#14161b;margin-bottom:3px}
.sh .n{display:inline-block;background:#0d7a45;color:#fff;border-radius:2px;padding:.5px 6px;margin-right:6px;font-size:7.9pt}
.stp.ot .sh .n{background:#b8842a}
.sh .mk{float:right;font-size:7.9pt;color:#39414f;font-weight:400}
.ans{background:#eef4ef;border-left:3px solid #0d7a45;padding:3px 7px;margin-top:4px;font-size:8pt}
.ans b{color:#0d5c34}
.with{background:#fff8e8;border-left:3px solid #b8842a;padding:3px 7px;margin-top:3px;font-size:7.8pt}
.with b{color:#8a5a12}
.mut{color:#6b7280}
.mat{display:inline-block;vertical-align:middle;position:relative;padding:1px 6px;margin:0 1px}
.mat::before,.mat::after{content:"";position:absolute;top:0;bottom:0;width:3px;border:1px solid #14161b}
.mat::before{left:0;border-right:none}.mat::after{right:0;border-left:none}
.mat.pw::after{display:none}.mat.pw td{text-align:left;padding-right:7px!important}
.mat table{border-collapse:collapse}
.mat td{padding:0 3px!important;text-align:center;font-size:.88em;line-height:1.12;border:none!important;background:transparent!important}
.f{display:inline-block;vertical-align:-.45em;text-align:center;margin:0 2px}
.f .n{display:block;border-bottom:1px solid #14161b;padding:0 3px}
.f .d{display:block;padding:0 3px}
.box{border:1.5px solid #a04545;background:#fdf6f6;border-radius:3px;padding:6px 9px;margin:6px 0;font-size:8pt}
.box.g{border-color:#0d7a45;background:#f2faf5}
.brk{page-break-before:always}
.avoid{page-break-inside:avoid}
.foot{margin-top:8px;border-top:1px solid #b9c0cc;padding-top:4px;font-size:7.2pt;color:#5b6472}
"""
H=[]; w=H.append

w(f"""<div class="hd"><h1>24CS31 &mdash; 3-HOUR HAIL MARY <span style="font-size:10pt">&middot; v2, corrected</span></h1>
<div class="s">Organised <b>unit by unit</b>, with a map of exactly how each question will be printed and which parts
you can answer. <b>Steps 1&ndash;7 are unchanged from v1</b> &mdash; nothing you have already done is wasted.</div></div>

<div class="box avoid"><b>WHAT CHANGED AND WHY.</b> Re-running the optimiser with <i>nothing</i> pre-cut found three
topics I had wrongly dropped. All three beat items I had kept:<br>
&bull; <b>ODE / simultaneous ODE by Laplace (07)</b> &mdash; 4/4 papers and <b>+7 on every single one</b>. The only
topic that gains on all four. Cutting it was my biggest mistake.<br>
&bull; <b>SVD (10)</b> &mdash; 4/4, <b>no calculus at all</b> (it is <i>A</i><sup>T</sup><i>A</i>, eigenvalues,
eigenvectors), and the <b>same matrix twice</b> including the most recent paper. It passes your own rule and I cut it anyway.<br>
&bull; <b>Rotation-operator proof (07)</b> &mdash; <b>pure bookwork, zero calculus, 12 minutes</b>, and it completes Q5
in Unit&nbsp;III. I dismissed it on a 2/4 frequency without noticing it is free marks.<br>
<b>Result: the worst-case floor rises from 59 to 65</b> (72 with overtime) in the same three hours.</div>

<div class="bar"><span>THE CLOCK &mdash; study in this order</span><span class="r">stop anywhere; the total is the worst of 4 papers</span></div>
<table class="g">
<tr><th class="c" style="width:4%">#</th><th style="width:32%">Study this</th><th class="c" style="width:8%">Unit</th>
<th class="c" style="width:9%">Appears as</th><th class="c" style="width:6%">Marks</th><th class="c" style="width:6%">Mins</th>
<th class="c" style="width:7%">Clock</th><th class="c" style="width:10%">Running total</th></tr>""")
NEW="&nbsp;<span style='color:#a04545;font-size:7pt'>&#9679;&nbsp;ADDED</span>"
CLOCK=[("Unitary / Hermitian check","V","Q10b","05","08","0:08","5",0),
 ("Prove <i>T</i> is linear + find images","III","<b>Q5b</b>","07","12","0:20","12",0),
 ("Least-squares solution","IV","<b>Q8b</b>","10","20","0:40","22",0),
 ("<i>t<sup>n</sup></i>-multiplication proof","I","Q1c / Q2b","07","15","0:55","29",0),
 ("Heaviside piecewise + LT","II","Q3c","07","20","1:15","36",0),
 (f"<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} {ARR} <i>L</i>{{cos&nbsp;{sq}<i>t</i>/{sq}<i>t</i>}}","I","Q1b","04","12","1:27","40",0),
 ("The Unit&nbsp;I 2-mark definition","I","Q1a / Q2a","02","05","1:32","42",0),
 ("<b>ODE / simultaneous ODE by LT</b>"+NEW,"II","Q3d / Q4d","07","22","1:54","49",0),
 ("<b>Singular Value Decomposition</b>"+NEW,"V","Q9c","10","22","2:16","54",1),
 ("Orthogonal diagonalization","V","<b>Q10c</b>","10","25","2:41","59",0),
 ("Span / basis / linear independence","III","Q5a","06","12","2:53","64",0),
 ("<b>Rotation-operator proof</b>"+NEW,"III","Q5c","07","12","3:05","65",0)]
for i,(t,u,ap,mk,mn,ck,rt,ps) in enumerate(CLOCK,1):
    cls=' class="pass"' if ps else ''
    w(f'<tr{cls}><td class="c"><b>{i}</b></td><td>{t}</td><td class="c">{u}</td><td class="c">{ap}</td>'
      f'<td class="c">{mk}</td><td class="c">{mn}</td><td class="c">{ck}</td>'
      f'<td class="c"><b>{rt}</b>{" &#9989; PASS" if ps else ""}</td></tr>')
w('<tr><td colspan="8" class="c" style="background:#b8842a!important;color:#fff;font-weight:700">'
  '&mdash;&mdash;  3 HOURS UP &mdash; overtime below takes the floor to 72  &mdash;&mdash;</td></tr>')
for i,(t,u,ap,mk,mn,why) in enumerate([
 ("Positive-definite check","V","Q10a","05","08","completes Unit&nbsp;V's 5+5 &rarr; <b>Q10 becomes a full 20</b>"),
 ("Composition of transformations","III","Q6a","06","12","backs up Unit&nbsp;III if the rotation proof is absent"),
 ("Kernel &amp; range + rank&ndash;nullity","III","Q6c","07","15","with the above, Q6 becomes an alternative 13"),
 (f"{inv}{{log(&hellip;)}}","II","Q3b","04","12","+4 in Unit&nbsp;II"),
 ("The Unit&nbsp;II 2-mark definition","II","Q3a / Q4a","02","05","+2, five minutes &mdash; <b>Q3 becomes a full 20</b>"),
 ("Four fundamental subspaces","IV","Q7c","07","15","<b>+10 in Unit&nbsp;IV</b> &mdash; always in Q7"),
 ("Complete solution of <i>Ax</i> = <i>b</i>","IV","Q7a","06","15","with the above, <b>Q7 becomes a full 20</b>"),
 ("Transition matrix","III","Q6b","07","15","completes Q6 as a second full 20")],13):
    w(f'<tr><td class="c">{i}</td><td>{t}</td><td class="c">{u}</td><td class="c">{ap}</td><td class="c">{mk}</td>'
      f'<td class="c">{mn}</td><td class="c mut">&mdash;</td><td>{why}</td></tr>')
w("</table>")

w(f"""<div class="box avoid"><b>STILL CUT &mdash; and now for the right reasons.</b> Each is either long with values that
change every paper, or adds <b>nothing</b> to your worst case because it sits in a question you would not answer:<br>
<b>QR factorization</b> (4/4, but the matrix changed in all four papers &mdash; +0 to the floor) &nbsp;&bull;&nbsp;
<b>convolution</b> (sits opposite Heaviside) &nbsp;&bull;&nbsp; <b>periodic functions</b> (+0 &mdash; it is always in the
question you are <i>not</i> answering) &nbsp;&bull;&nbsp; improper integrals {INT}<sub>0</sub><sup>{inf}</sup>
&nbsp;&bull;&nbsp; <i>L</i>{{<i>t e<sup>at</sup></i> trig}} / division by <i>t</i> &nbsp;&bull;&nbsp;
({sq}<i>t</i>+1/{sq}<i>t</i>)<sup>3</sup> &nbsp;&bull;&nbsp; diagonalize + <i>A<sup>n</sup></i> &nbsp;&bull;&nbsp;
Gram&ndash;Schmidt &nbsp;&bull;&nbsp; orthogonal projection &nbsp;&bull;&nbsp; Markov &nbsp;&bull;&nbsp;
quadratic forms &nbsp;&bull;&nbsp; PCA.</div>

<div class="box g avoid"><b>IN THE HALL.</b> Read both questions in a unit, tick the parts you can do, answer the one
with more ticks. <b>Write every part you know and never leave a unit blank.</b> Answer the parts, not the question.</div>""")

def qmap(cols, rows, verdict):
    w('<table class="qm"><tr><th style="width:6%"></th>'+"".join(f'<th>{c}</th>' for c in cols)+'</tr>')
    for label, cells in rows:
        w(f'<tr><td class="q">{label}</td>')
        for txt, mk, ok in cells:
            w(f'<td class="{"ok" if ok else "no"}"><span class="mk">({mk})</span> '
              f'<span class="tick">{"&#10003;" if ok else "&#10007;"}</span><br>{txt}</td>')
        w('</tr>')
    w('</table>'); w(f'<div class="verd">{verdict}</div>')

def step(n,title,marks,slot,body,ans,with_=None,ot=False):
    w(f"""<div class="stp{' ot' if ot else ''} avoid"><div class="sh"><span class="n">{n}</span>{title}
    <span class="mk">{marks} marks &middot; {slot}</span></div><div>{body}</div>""")
    if with_: w(f'<div class="with"><b>Appears alongside:</b> {with_}</div>')
    w(f'<div class="ans">{ans}</div></div>')

# ============ UNIT I ============
w('<div class="brk"></div><div class="bar"><span>UNIT&nbsp;I &mdash; Laplace Transforms</span>'
  '<span class="r">20 marks &middot; Q1 <i>or</i> Q2 &middot; a(02)+b(04)+c(07)+d(07) &middot; you score <b>13</b></span></div>')
qmap(["a &mdash; definition","b &mdash; short result","c &mdash; proof","d &mdash; long evaluation"],
 [("Q1",[("Write the LT of a periodic function &nbsp;<b>step&nbsp;7</b>","02",True),
         (f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show the cos&nbsp;{sq}<i>t</i> result &nbsp;<b>step&nbsp;6</b>","04",True),
         ("<b><i>t<sup>n</sup></i>-multiplication proof &nbsp;step&nbsp;4</b>","07",True),
         (f"{INT}<sub>0</sub><sup>{inf}</sup> integral + <i>L</i>{{<i>t</i>sin3<i>t</i>cos2<i>t</i>}} &mdash; <i>cut</i>","07",False)]),
  ("Q2",[("Define the Laplace transform &nbsp;<b>step&nbsp;7</b>","02",True),
         (f"<i>L</i>{{({sq}<i>t</i>+1/{sq}<i>t</i>)<sup>3</sup>}} &mdash; <i>cut</i>","04",False),
         ("<i>L</i>{<i>te</i><sup>&minus;4<i>t</i></sup>sin3<i>t</i>} / division by <i>t</i> &mdash; <i>cut</i>","07",False),
         ("Periodic function &mdash; <i>cut</i>","07",False)])],
 "<b>&rarr; ANSWER Q1 &mdash; 13 of 20.</b> Trigger: the <i>t<sup>n</sup></i> proof. In all four papers it sits in the "
 "<b>same</b> question as the sin&nbsp;&radic;<i>t</i> result, and the periodic-function problem sits in the <b>other</b> one.")

step(4,"Prove the <i>t<sup>n</sup></i>-multiplication rule","07","Q1c or Q2b &mdash; <b>4/4 papers, word for word</b>",
 "If <i>L</i>{<i>f</i>(<i>t</i>)} = <i>F</i>(<i>s</i>), prove &nbsp;<i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup><i>n</i></sup> "
 +F("<i>d<sup>n</sup></i>","<i>ds<sup>n</sup></i>")+"{<i>F</i>(<i>s</i>)}, &nbsp;<i>n</i> a positive integer.",
 f"<b>Four lines.</b> <i>F</i>(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)<i>dt</i>. "
 f"Differentiate under the integral: <i>F</i>&prime;(<i>s</i>) = &minus;<i>L</i>{{<i>tf</i>(<i>t</i>)}}. Each further "
 f"differentiation drops another (&minus;<i>t</i>). Close with <b>induction on <i>n</i></b>, base case <i>n</i>=1.",
 "the sin&nbsp;&radic;<i>t</i> result (step 6) &mdash; <b>always</b>. 11 marks in one question.")

step(6,f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show the cos&nbsp;{sq}<i>t</i> result","04","Q1b &mdash; same statement in Jun&nbsp;23 and Mar&nbsp;24",
 f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = "+F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>, show "
 "<i>L</i>{"+F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")+"} = "+F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>.",
 F("<i>d</i>","<i>dt</i>")+f"(sin&nbsp;{sq}<i>t</i>) = "+F(f"cos&nbsp;{sq}<i>t</i>",f"2{sq}<i>t</i>")+
 ", so the target = <b>2 &times; <i>L</i>{that derivative}</b>. Apply <i>L</i>{<i>f</i>&prime;} = <i>sF</i>(<i>s</i>) &minus; <i>f</i>(0), "
 "<i>f</i>(0) = 0. <b>Three lines.</b>","the <i>t<sup>n</sup></i> proof (step 4).")

step(7,"The Unit&nbsp;I 2-mark definition","02","<b>Q1a and Q2a &mdash; one in each</b>",
 "&ldquo;Write the LT of a periodic function&rdquo; &nbsp;&bull;&nbsp; &ldquo;Define the Laplace transform&rdquo;",
 f"<b>Periodic, period <i>T</i>:</b> "+F("1","1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>")+
 f"{INT}<sub>0</sub><sup><i>T</i></sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)<i>dt</i>. &nbsp;"
 f"<b>Definition:</b> {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)<i>dt</i>. "
 f"<b>Formula, not a paragraph.</b>","whichever question you choose.")

# ============ UNIT II ============
w('<div class="bar"><span>UNIT&nbsp;II &mdash; Application of Laplace Transforms</span>'
  '<span class="r">20 marks &middot; Q3 <i>or</i> Q4 &middot; you score <b>14</b>, or <b>20</b> with overtime</span></div>')
qmap(["a &mdash; definition","b &mdash; short inverse","c &mdash; main problem","d &mdash; ODE / application"],
 [("Q3",[("Dirac-delta definition &nbsp;<b>overtime&nbsp;17</b>","02",False),
         (f"{inv}{{log(&hellip;)}} &nbsp;<b>overtime&nbsp;16</b>","04",False),
         ("<b>Heaviside piecewise + LT &nbsp;step&nbsp;5</b>","07",True),
         ("<b>LR-circuit current &nbsp;step&nbsp;8</b>","07",True)]),
  ("Q4",[("Unit-step definition &nbsp;<b>overtime&nbsp;17</b>","02",False),
         ("Partial-fraction inverse &mdash; <i>cut</i>","04",False),
         ("Verify the convolution theorem &mdash; <i>cut</i>","07",False),
         ("<b>Simultaneous ODEs by LT &nbsp;step&nbsp;8</b>","07",True)])],
 "<b>&rarr; ANSWER Q3 &mdash; 14 of 20, and a full 20 after two 17-minute overtime items.</b> This is the unit the "
 "correction fixed: the <b>d</b> part &mdash; an ODE, a system of ODEs, or the circuit problem &mdash; appears in "
 "<b>both</b> questions in every paper, so step&nbsp;8 pays whichever you pick.")

step(5,"Heaviside piecewise + Laplace transform","07","Q3c &mdash; same function in Apr&nbsp;23 and Mar&nbsp;24",
 "Express &nbsp;<i>f</i>(<i>t</i>) = "+PW([["<i>t</i><sup>2</sup>,","0 &lt; <i>t</i> &lt; 2"],["4<i>t</i>,","2 &lt; <i>t</i> &lt; 4"],["8,","<i>t</i> &gt; 4"]])
 +" via the Heaviside function; hence find its Laplace transform.",
 "<b>1 &mdash; stack the jumps:</b> <i>f</i> = <i>t</i><sup>2</sup> + (4<i>t</i>&minus;<i>t</i><sup>2</sup>)<i>u</i>(<i>t</i>&minus;2) + (8&minus;4<i>t</i>)<i>u</i>(<i>t</i>&minus;4). "
 "<b>2 &mdash; rewrite each bracket in (<i>t</i>&minus;<i>a</i>):</b> 4&minus;&tau;<sup>2</sup> and &minus;8&minus;4&tau;. "
 "<b>3 &mdash; second shifting:</b> <b><i>L</i>{<i>f</i>} = 2/<i>s</i><sup>3</sup> + <i>e</i><sup>&minus;2<i>s</i></sup>(4/<i>s</i> &minus; 2/<i>s</i><sup>3</sup>) "
 "+ <i>e</i><sup>&minus;4<i>s</i></sup>(&minus;8/<i>s</i> &minus; 4/<i>s</i><sup>2</sup>)</b>",
 "the ODE / circuit problem in the <b>d</b> slot (step 8) &mdash; in all four papers. <b>That pairing is 14 marks.</b>")

step(8,"Solve ODEs and simultaneous ODEs by Laplace transforms","07","Q3d or Q4d &mdash; <b>4/4 papers &middot; the item I wrongly cut</b>",
 "<b>(a) Simultaneous</b> &mdash; " + F("<i>dx</i>","<i>dt</i>") + " &minus; 2<i>y</i> = cos&nbsp;2<i>t</i>; &nbsp;"
 + F("<i>dy</i>","<i>dt</i>") + " + 2<i>x</i> = sin&nbsp;2<i>t</i>, &nbsp;<i>x</i>(0)=1, <i>y</i>(0)=0.<br>"
 "<b>(b) Single ODE</b> &mdash; <i>y</i>&Prime; + 4<i>y</i>&prime; + 3<i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup> "
 "<span class='mut'>(set twice, with different initial conditions)</span>.<br>"
 "<b>(c) Circuit</b> &mdash; <i>L</i>" + F("<i>di</i>","<i>dt</i>") + " + <i>Ri</i> = <i>Ee</i><sup>&minus;<i>at</i></sup>, <i>i</i>(0)=0 &nbsp;&rarr;&nbsp; "
 "<i>i</i> = " + F("<i>E</i>","<i>R</i> &minus; <i>aL</i>") + "(<i>e</i><sup>&minus;<i>at</i></sup> &minus; <i>e</i><sup>&minus;<i>Rt/L</i></sup>).",
 "<b>One method for all three.</b> Transform every term with <i>L</i>{<i>y</i>&prime;} = <i>sY</i> &minus; <i>y</i>(0) and "
 "<i>L</i>{<i>y</i>&Prime;} = <i>s</i><sup>2</sup><i>Y</i> &minus; <i>sy</i>(0) &minus; <i>y</i>&prime;(0). For a single ODE, "
 "solve for <i>Y</i>(<i>s</i>) and invert by partial fractions. For a system, you get two linear equations in "
 "<i>X</i>(<i>s</i>) and <i>Y</i>(<i>s</i>) &mdash; solve them as simultaneous algebra, then invert each. "
 "<b>The initial conditions do the work; write them in at the transform step and the rest is algebra.</b>",
 "the Heaviside question (step 5) in the same question &mdash; 4/4 papers.")

# ============ UNIT III ============
w('<div class="brk"></div><div class="bar"><span>UNIT&nbsp;III &mdash; Vector Space and Linear Transformation</span>'
  '<span class="r">20 marks &middot; Q5 <i>or</i> Q6 &middot; you score <b>13&ndash;20</b></span></div>')
qmap(["a &mdash; vector space (06)","b &mdash; transformation (07)","c &mdash; the long one (07)"],
 [("Q5",[("<b>Span / basis / independence &nbsp;step&nbsp;11</b>","06",True),
         ("<b>Prove <i>T</i> is linear + images &nbsp;step&nbsp;2</b>","07",True),
         ("<b>Rotation-operator proof &nbsp;step&nbsp;12</b>","07",True)]),
  ("Q6",[("Composition of transformations &nbsp;<b>overtime&nbsp;14</b>","06",False),
         ("Transition matrix &nbsp;<b>overtime&nbsp;20</b>","07",False),
         ("Kernel &amp; range &nbsp;<b>overtime&nbsp;15</b>","07",False)])],
 "<b>&rarr; ANSWER Q5 &mdash; a full 20</b> once step&nbsp;12 is done. That is what adding the rotation proof buys: "
 "Q5's three parts become 6 + 7 + 7 = 20. The proof appeared in Apr&nbsp;23 and Mar&nbsp;24; in the other two papers "
 "Q5c was the kernel/transition question instead, which is why <b>overtime 14&ndash;15 is your insurance</b>.")

step(2,"Prove <i>T</i> is linear + find images","07","<b>Q5b &mdash; all four papers, same slot</b>",
 f"<b>(a)</b> <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>); images of (1,&nbsp;2) and (2,&nbsp;&minus;5).<br>"
 f"<b>(b)</b> <i>T</i>:<i>P</i><sub>2</sub>{ARR}<i>P</i><sub>2</sub>, <i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup>+<i>c</i>; image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1.",
 "Show <i>T</i>(<b>u</b>+<b>v</b>) = <i>T</i>(<b>u</b>)+<i>T</i>(<b>v</b>) and <i>T</i>(<i>k</i><b>u</b>) = <i>kT</i>(<b>u</b>), then substitute. "
 "<b>Answers:</b> <i>T</i>(1,2) = <b>(5, 4, &minus;1)</b>, <i>T</i>(2,&minus;5) = <b>(1, &minus;10, 7)</b>, "
 "<i>T</i>(5<i>x</i><sup>2</sup>+6<i>x</i>+1) = <b>11<i>x</i><sup>2</sup> + 1</b>.",
 "span/basis at Q5a and the rotation proof at Q5c &mdash; the three together are Q5's full 20.")

step(11,"Span / basis / linear independence","06","Q5a &mdash; all four papers",
 f"Is {{{M([['1','2'],['0','1']])}, {M([['3','4'],['1','1']])}, {M([['1','2'],['1','1']])}, {M([['0','2'],['1','2']])}}} a basis of "
 f"<i>M</i><sub>22</sub>? &nbsp;<span class='mut'>or</span>&nbsp; do {{(1,2,3), (&minus;1,&minus;1,0), (2,5,4)}} span <i>R</i><sup>3</sup>?",
 "<b>One method for every version:</b> flatten each object to a coordinate vector (a 2&times;2 matrix &rarr; a 4-vector), "
 "stack as rows of a square matrix, take the <b>determinant</b>. Non-zero &rArr; independent &rArr; basis / spans.",
 "the prove-<i>T</i>-is-linear question at Q5b.")

step(12,"Rotation-operator proof","07","Q5c &mdash; Apr&nbsp;23 and Mar&nbsp;24 &middot; <b>the item I wrongly cut</b>",
 f"Show that the linear operator <i>T</i>:<i>R</i><sup>2</sup>{ARR}<i>R</i><sup>2</sup> defined by <i>T</i>(<b>x</b>) = "
 f"<i>A</i><b>x</b> rotates <b>x</b> through an angle {th} about the origin, where "
 f"<i>A</i> = {M([['cos&#952;',sp+'sin&#952;'],['sin&#952;','cos&#952;']])}",
 f"<b>Pure bookwork &mdash; twelve minutes, no calculus, 7 marks.</b> Write <b>x</b> in polar form: "
 f"<b>x</b> = (<i>r</i>cos&nbsp;&phi;, <i>r</i>sin&nbsp;&phi;). Multiply out <i>A</i><b>x</b> and you get "
 f"(<i>r</i>cos&thinsp;{th}cos&thinsp;&phi; &minus; <i>r</i>sin&thinsp;{th}sin&thinsp;&phi;, &nbsp;"
 f"<i>r</i>sin&thinsp;{th}cos&thinsp;&phi; + <i>r</i>cos&thinsp;{th}sin&thinsp;&phi;). Apply the compound-angle "
 f"formulae &rarr; (<i>r</i>cos({th}+&phi;), <i>r</i>sin({th}+&phi;)). Same modulus <i>r</i>, argument increased by "
 f"{th} &mdash; so it is a rotation through {th}. State linearity (<i>T</i>(<b>x</b>) = <i>A</i><b>x</b> is linear for any matrix <i>A</i>) and you are done.",
 "the span/basis and prove-linear questions &mdash; <b>this is the part that turns Q5 into a full 20</b>.")

# ============ UNIT IV ============
w('<div class="bar"><span>UNIT&nbsp;IV &mdash; Orthogonal Projections</span>'
  '<span class="r">20 marks &middot; Q7 (06+07+07) <i>or</i> Q8 (10+10) &middot; you score <b>10</b>, or <b>20</b> with overtime</span></div>')
qmap(["a","b","c"],
 [("Q7",[("Complete solution of <i>Ax</i>=<i>b</i> &nbsp;<b>overtime&nbsp;19</b> (06)","06",False),
         ("Orthogonal projection &mdash; <i>cut</i> (07)","07",False),
         ("Four fundamental subspaces &nbsp;<b>overtime&nbsp;18</b> (07)","07",False)]),
  ("Q8",[("QR factorization &mdash; <i>cut</i> (10)","10",False),
         ("<b>Least-squares solution &nbsp;step&nbsp;3</b> (10)","10",True),
         ("&mdash;","&mdash;",False)])],
 "<b>&rarr; ANSWER Q8 &mdash; 10 of 20 from one part.</b> Overtime 18 and 19 turn <b>Q7 into a full 20</b> and are the "
 "best-paying overtime on the sheet (+10 in this unit). QR stays cut: 4/4, but its matrix changed in every single "
 "paper, so it adds <b>nothing</b> to your worst case.")

step(3,"Least-squares solution of <i>Ax</i> = <i>b</i>","10","<b>Q8b</b> &mdash; all four papers",
 f"<i>A</i> = {M([['1','3','5'],['1','1','0'],['1','1','2'],['1','3','3']])} &nbsp; <i>b</i> = {V(['3','5','7',sp+'3'])} "
 f"&nbsp;<span class='mut'>&mdash; identical in Jun&nbsp;23 and Mar&nbsp;24</span>",
 f"<b>Solve the normal equations <i>A</i><sup>T</sup><i>A</i>&#770;<i>x</i> = <i>A</i><sup>T</sup><i>b</i>.</b> That is the whole question. "
 f"<i>A</i><sup>T</sup><i>A</i> = {M([['4','8','10'],['8','20','26'],['10','26','38']])}, "
 f"<i>A</i><sup>T</sup><i>b</i> = {V(['12','12','20'])} &rArr; <b>&#770;<i>x</i> = (10, &minus;6, 2)</b>. Substitute back to check.",
 "the QR factorization at Q8a, which you are skipping.")

# ============ UNIT V ============
w('<div class="brk"></div><div class="bar"><span>UNIT&nbsp;V &mdash; Applications of Eigenvalue Decomposition</span>'
  '<span class="r">20 marks &middot; Q9 <i>or</i> Q10 &middot; a(05)+b(05)+c(10) &middot; you score <b>15&ndash;20</b></span></div>')
qmap(["a &mdash; 5-mark check","b &mdash; 5-mark check","c &mdash; the 10-marker"],
 [("Q9",[("Quadratic form &mdash; <i>cut</i>","05",False),
         ("Markov steady state &mdash; <i>cut</i>","05",False),
         ("<b>SVD &nbsp;step&nbsp;9</b>","10",True)]),
  ("Q10",[("Positive-definite check &nbsp;<b>overtime&nbsp;13</b>","05",False),
          ("<b>Unitary / Hermitian check &nbsp;step&nbsp;1</b>","05",True),
          ("<b>Orthogonal diagonalization &nbsp;step&nbsp;10</b>","10",True)])],
 "<b>&rarr; ANSWER Q10 &mdash; 15 of 20, a full 20 after overtime 13 (eight minutes).</b> Adding SVD covers the "
 "<i>other</i> question too: in Apr&nbsp;23 orthogonal diagonalization and SVD were <b>both in Q10</b>, which is exactly "
 "why cutting SVD cost 10 marks on that paper &mdash; the worst one.")

step(1,"Unitary / Hermitian check","05","Q10b &mdash; a property check appears in <b>all four papers</b>",
 f"Is <i>A</i> = {M([['0','<i>i</i>'],[sp+'<i>i</i>','0']])} unitary? &nbsp;<span class='mut'>or</span>&nbsp; is "
 f"{M([['3','7'+sp+'4<i>i</i>',sp+'2+5<i>i</i>'],['7+4<i>i</i>',sp+'2','3+<i>i</i>'],[sp+'2'+sp+'5<i>i</i>','3'+sp+'<i>i</i>','4']])} Hermitian?",
 "Write <i>A</i><sup>*</sup> = conjugate of the transpose. <b>Hermitian</b> &hArr; <i>A</i><sup>*</sup> = <i>A</i>; "
 "<b>unitary</b> &hArr; <i>A</i><sup>*</sup><i>A</i> = <i>I</i>. <b>Both answer YES.</b> Show <i>A</i><sup>*</sup> in full.",
 "the positive-definite check &mdash; the property checks travel as a pair in all four papers.")

step(9,"Singular Value Decomposition","10","Q9c &mdash; <b>4/4 papers &middot; same matrix twice &middot; the item I wrongly cut</b>",
 f"Find the SVD of &nbsp;<i>A</i> = {M([['1','1'],['3',sp+'3']])} &nbsp;<span class='mut'>&mdash; identical in Jun&nbsp;23 and Mar&nbsp;24</span>",
 f"<b>No calculus at all &mdash; it is eigenvectors twice over.</b> "
 f"<i>A</i><sup>T</sup><i>A</i> = {M([['10',sp+'8'],[sp+'8','10']])}, eigenvalues <b>18 and 2</b>, so the singular values are "
 f"&sigma;<sub>1</sub> = 3{sq}2, &sigma;<sub>2</sub> = {sq}2. Eigenvectors of <i>A</i><sup>T</sup><i>A</i> are "
 f"(1,&minus;1)/{sq}2 and (1,1)/{sq}2 &rarr; those are the columns of <b><i>V</i></b>. Then "
 f"<b><i>u<sub>i</sub></i> = <i>Av<sub>i</sub></i> / &sigma;<sub>i</sub></b> gives the columns of <b><i>U</i></b>, and "
 f"&Sigma; = diag(3{sq}2, {sq}2). Write <b><i>A</i> = <i>U</i>&Sigma;<i>V</i><sup>T</sup></b>.",
 "the quadratic-form and Markov 5-markers (Mar&nbsp;24 Q9) &mdash; or, in Apr&nbsp;23, orthogonal diagonalization itself.")

step(10,"Orthogonal diagonalization","10","<b>Q10c &mdash; same matrix in 3 of the 4 papers</b>",
 f"Orthogonally diagonalize &nbsp;<i>A</i> = {M([['3',sp+'1','1'],[sp+'1','5',sp+'1'],['1',sp+'1','3']])}",
 f"<b>You already know the answer &mdash; rehearse producing it.</b> Eigenvalues <b>2, 3, 6</b>, all distinct, so the "
 f"eigenvectors are automatically orthogonal &mdash; <u>no Gram&ndash;Schmidt</u>, and saying so earns marks. "
 f"Eigenvectors {V(['1','0',sp+'1'])}, {V(['1','1','1'])}, {V(['1',sp+'2','1'])}; normalise by {sq}2, {sq}3, {sq}6 to get "
 f"the columns of <i>P</i>. Then <b><i>P</i><sup>T</sup><i>AP</i> = diag(2,&nbsp;3,&nbsp;6)</b>. Show the three dot products are 0.",
 "the two 5-mark property checks &mdash; in 3 of 4 papers they share this question.")

step(13,"Positive-definite check","05","Q10a &mdash; same matrix in Apr&nbsp;23 and Mar&nbsp;24",
 f"Is &nbsp;<i>A</i> = {M([['1',sp+'2','1'],[sp+'2','4',sp+'2'],['1',sp+'2','1']])} positive definite?",
 "Leading principal minors are <b>1, 0, 0</b> &rArr; <b>NOT positive definite</b>; it is positive <i>semi</i>-definite "
 "(row 3 = row 1, eigenvalues 0, 0, 6). <b>Say that explicitly.</b> Eight minutes, and it completes Q10 as a full 20.",
 "the unitary/Hermitian check (step 1).", ot=True)

w("""<div class="foot"><b>Why this version differs from v1:</b> the first pass pre-cut every calculus-heavy topic before
optimising. Re-running with nothing pre-cut showed three of those cuts were wrong &mdash; the ODE question gains 7 marks
on <i>every</i> paper, SVD is calculus-free and repeats verbatim, and the rotation proof is 7 marks of bookwork that
completes Q5. Worst-case floor: <b>59 &rarr; 65</b>, and <b>72</b> with overtime. Steps 1&ndash;7 are unchanged.
Working in <i>coverage_audit.py</i>.</div>""")

doc="<!doctype html><html><head><meta charset='utf-8'><title>24CS31 3-Hour Hail Mary</title><style>"+CSS+"</style></head><body>"+"".join(H)+"</body></html>"
import io,os
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"24CS31_3Hour_HailMary.html")
io.open(out,"w",encoding="utf-8").write(doc); print("wrote",out)

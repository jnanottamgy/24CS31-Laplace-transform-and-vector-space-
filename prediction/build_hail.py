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

# ==================== COVER + CLOCK ====================
w(f"""<div class="hd"><h1>24CS31 &mdash; 3-HOUR HAIL MARY</h1>
<div class="s">Organised <b>unit by unit</b>, with a map of exactly how each question will be printed and which
parts you will be able to answer. Study in the <b>clock order</b> below; walk into the hall with the <b>unit maps</b>.</div></div>

<div class="box avoid"><b>THE ONE THING TO UNDERSTAND.</b> &ldquo;Running total&rdquo; is what you would score on the
<b>worst</b> of the four past papers if you stopped studying at that row. You cross the pass mark at <b>2 h 14</b>.
Two hours of this leaves you at <b>44</b>. <b>Steps 1&ndash;12 are the whole plan &mdash; finish them.</b></div>

<div class="bar"><span>THE CLOCK &mdash; study in this order</span><span class="r">stop anywhere; the total is the worst of 4 papers</span></div>
<table class="g">
<tr><th class="c" style="width:4%">#</th><th style="width:32%">Study this</th><th class="c" style="width:8%">Unit</th>
<th class="c" style="width:9%">Appears as</th><th class="c" style="width:6%">Marks</th><th class="c" style="width:6%">Mins</th>
<th class="c" style="width:7%">Clock</th><th class="c" style="width:10%">Running total</th></tr>""")
CLOCK=[("Unitary / Hermitian check","V","Q10b (5+5 pair)","05","08","0:08","5",0),
 ("Prove <i>T</i> is linear + find images","III","<b>Q5b</b>","07","12","0:20","12",0),
 ("Least-squares solution","IV","<b>Q8b</b>","10","20","0:40","22",0),
 ("<i>t<sup>n</sup></i>-multiplication proof","I","Q1c / Q2b","07","15","0:55","29",0),
 ("Heaviside piecewise + LT","II","Q3c","07","20","1:15","36",0),
 (f"<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} {ARR} <i>L</i>{{cos&nbsp;{sq}<i>t</i>/{sq}<i>t</i>}}","I","Q1b","04","12","1:27","40",0),
 ("<b>All four 2-mark definitions</b>","I &amp; II","Q1a Q2a Q3a Q4a","02&times;2","10","1:37","44",0),
 ("Orthogonal diagonalization","V","<b>Q10c</b>","10","25","2:02","49",0),
 (f"{inv}{{log(&hellip;)}}","II","Q3b","04","12","2:14","52",1),
 ("Span / basis / linear independence","III","Q5a","06","12","2:26","53",0),
 ("Composition of transformations","III","Q6a","06","12","2:38","58",0),
 ("Kernel &amp; range + rank&ndash;nullity","III","Q6c","07","15","2:53","59",0)]
for i,(t,u,ap,mk,mn,ck,rt,ps) in enumerate(CLOCK,1):
    cls=' class="pass"' if ps else ''
    w(f'<tr{cls}><td class="c"><b>{i}</b></td><td><b>{t}</b></td><td class="c">{u}</td><td class="c">{ap}</td>'
      f'<td class="c">{mk}</td><td class="c">{mn}</td><td class="c">{ck}</td>'
      f'<td class="c"><b>{rt}</b>{" &#9989; PASS" if ps else ""}</td></tr>')
w('<tr><td colspan="8" class="c" style="background:#b8842a!important;color:#fff;font-weight:700">'
  '&mdash;&mdash;  3 HOURS UP &mdash; overtime below, best-paying first  &mdash;&mdash;</td></tr>')
for i,(t,u,ap,mk,mn,rt) in enumerate([
 ("Transition matrix / change of basis","III","Q6b","07","15","<b>65</b> &nbsp;(+6)"),
 ("Positive-definite check","V","Q10a","05","08","65"),
 ("Four fundamental subspaces","IV","Q7c","07","15","65"),
 ("Complete solution of <i>Ax</i> = <i>b</i>","IV","Q7a","06","15","65"),
 ("Short inverse LT (partial fractions)","II","Q4b","04","10","65")],13):
    w(f'<tr><td class="c">{i}</td><td>{t}</td><td class="c">{u}</td><td class="c">{ap}</td><td class="c">{mk}</td>'
      f'<td class="c">{mn}</td><td class="c mut">&mdash;</td><td class="c">{rt}</td></tr>')
w("</table>")

w(f"""<div class="box avoid"><b>CUT &mdash; do not open these.</b> All real, several 4/4, but long and the numbers change
every paper: ODEs and simultaneous ODEs &nbsp;&bull;&nbsp; convolution &nbsp;&bull;&nbsp; improper integrals
{INT}<sub>0</sub><sup>{inf}</sup> &nbsp;&bull;&nbsp; <i>L</i>{{<i>t e<sup>at</sup></i> trig}} / division by <i>t</i>
&nbsp;&bull;&nbsp; periodic functions &nbsp;&bull;&nbsp; ({sq}<i>t</i>+1/{sq}<i>t</i>)<sup>3</sup> &nbsp;&bull;&nbsp;
<b>QR</b> &nbsp;&bull;&nbsp; <b>SVD</b> &nbsp;&bull;&nbsp; diagonalize + <i>A<sup>n</sup></i> &nbsp;&bull;&nbsp;
Gram&ndash;Schmidt &nbsp;&bull;&nbsp; projection &nbsp;&bull;&nbsp; Markov &nbsp;&bull;&nbsp; quadratic forms
&nbsp;&bull;&nbsp; rotation proof &nbsp;&bull;&nbsp; PCA.<br>
<b>The four calculus items kept</b> (steps 4, 5, 6, 9) survived your own rule &mdash; each set with
<b>identical wording or identical values</b> in at least two papers.</div>

<div class="box g avoid"><b>IN THE HALL.</b> Read the two questions in a unit, tick the parts you can do, answer the
one with more ticks. <b>Write every part you know and never leave a unit blank</b> &mdash; a 5-mark check you can do
beats a 10-mark decomposition you half-remember. <b>Answer the parts, not the question.</b></div>""")

# ==================== HELPERS ====================
def qmap(cols, rows, verdict):
    w('<table class="qm"><tr><th style="width:6%"></th>'+"".join(f'<th>{c}</th>' for c in cols)+'</tr>')
    for label, cells in rows:
        w(f'<tr><td class="q">{label}</td>')
        for txt, mk, ok in cells:
            cls="ok" if ok else "no"
            tick="&#10003;" if ok else "&#10007;"
            w(f'<td class="{cls}"><span class="mk">({mk})</span> <span class="tick">{tick}</span><br>{txt}</td>')
        w('</tr>')
    w('</table>')
    w(f'<div class="verd">{verdict}</div>')

def step(n,title,marks,slot,body,ans,with_=None,ot=False):
    w(f"""<div class="stp{' ot' if ot else ''} avoid"><div class="sh"><span class="n">{n}</span>{title}
    <span class="mk">{marks} marks &middot; {slot}</span></div><div>{body}</div>""")
    if with_: w(f'<div class="with"><b>Appears alongside:</b> {with_}</div>')
    w(f'<div class="ans">{ans}</div></div>')

# ==================== UNIT I ====================
w('<div class="brk"></div><div class="bar"><span>UNIT&nbsp;I &mdash; Laplace Transforms</span>'
  '<span class="r">20 marks &middot; Q1 <i>or</i> Q2 &middot; a(02) + b(04) + c(07) + d(07) &middot; you will score <b>13</b></span></div>')
w('<p style="margin:0 0 3px"><b>How the two questions will be printed</b> &mdash; layout taken from March&nbsp;2024, '
  'the only paper under your current course title. Green = you have it after the clock above.</p>')
qmap(["a &mdash; definition","b &mdash; short result","c &mdash; proof / evaluation","d &mdash; long evaluation"],
 [("Q1",[("Write the LT of a periodic function","02",True),
         (f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show the cos&nbsp;{sq}<i>t</i> result &nbsp;<b>step&nbsp;6</b>","04",True),
         ("<b><i>t<sup>n</sup></i>-multiplication proof &nbsp;step&nbsp;4</b>","07",True),
         (f"{INT}<sub>0</sub><sup>{inf}</sup> integral + <i>L</i>{{<i>t</i> sin3<i>t</i> cos2<i>t</i>}} &mdash; <i>cut</i>","07",False)]),
  ("Q2",[("Define the Laplace transform","02",True),
         (f"<i>L</i>{{({sq}<i>t</i>+1/{sq}<i>t</i>)<sup>3</sup>}} &mdash; <i>cut</i>","04",False),
         ("<i>L</i>{<i>t e</i><sup>&minus;4<i>t</i></sup>sin3<i>t</i>} and division by <i>t</i> &mdash; <i>cut</i>","07",False),
         ("Periodic function, half-rectifier &mdash; <i>cut</i>","07",False)])],
 "<b>&rarr; ANSWER Q1 &mdash; you have 13 of its 20.</b> The trigger is the <i>t<sup>n</sup></i> proof: in all four "
 "papers it sits in the <b>same question</b> as the sin&nbsp;&radic;<i>t</i> result, and the periodic-function problem "
 "sits in the <b>other</b> one. Find the proof, answer that question, and take the 2-mark definition on your way past.")

step(4,"Prove the <i>t<sup>n</sup></i>-multiplication rule","07","Q1c or Q2b &mdash; <b>4/4 papers, word for word</b>",
 "If <i>L</i>{<i>f</i>(<i>t</i>)} = <i>F</i>(<i>s</i>), prove that &nbsp;<i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = "
 "(&minus;1)<sup><i>n</i></sup> " + F("<i>d<sup>n</sup></i>","<i>ds<sup>n</sup></i>") + "{<i>F</i>(<i>s</i>)}, &nbsp;<i>n</i> a positive integer.",
 f"<b>Script &mdash; four lines.</b> <i>F</i>(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i>. "
 f"Differentiate under the integral sign: <i>F</i>&prime;(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup>(&minus;<i>t</i>)<i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)<i>dt</i> "
 f"= &minus;<i>L</i>{{<i>t f</i>(<i>t</i>)}}. Each further differentiation drops another factor of (&minus;<i>t</i>). "
 f"Close with <b>induction on <i>n</i></b> and state the base case <i>n</i> = 1.",
 "the sin&nbsp;&radic;<i>t</i> result (step 6) &mdash; <b>always, in all four papers</b>. That pairing is 11 marks in one question.")

step(6,f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show the cos&nbsp;{sq}<i>t</i> result","04","Q1b &mdash; same statement in Jun&nbsp;23 and Mar&nbsp;24",
 f"Given &nbsp;<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = "+F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>, &nbsp;show that &nbsp;"
 "<i>L</i>{"+F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")+"} = "+F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>.",
 f"<b>Method:</b> "+F("<i>d</i>","<i>dt</i>")+f"(sin&nbsp;{sq}<i>t</i>) = "+F(f"cos&nbsp;{sq}<i>t</i>",f"2{sq}<i>t</i>")+
 ", so the target equals <b>2 &times; <i>L</i>{that derivative}</b>. Apply <i>L</i>{<i>f</i>&prime;} = <i>sF</i>(<i>s</i>) &minus; <i>f</i>(0) "
 f"with <i>f</i>(0) = sin&nbsp;0 = 0 &rarr; 2 &middot; <i>s</i> &middot; "+F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup> = "
 +F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>. <b>Three lines.</b>",
 "the <i>t<sup>n</sup></i> proof (step 4) &mdash; they are never separated.")

step(7,"The Unit&nbsp;I 2-mark definition","02","<b>Q1a and Q2a &mdash; one in each, so you get it either way</b>",
 "&ldquo;Write the Laplace transform of a periodic function&rdquo; &nbsp;&bull;&nbsp; &ldquo;Define the Laplace transform of a function&rdquo; "
 "&nbsp;&bull;&nbsp; &ldquo;Define a periodic function with an example&rdquo;",
 f"<b>Periodic, period <i>T</i>:</b> <i>L</i>{{<i>f</i>}} = "+F("1","1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>")+
 f"{INT}<sub>0</sub><sup><i>T</i></sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i>. &nbsp;&nbsp;"
 f"<b>Definition:</b> <i>L</i>{{<i>f</i>}} = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i>, "
 f"where the integral converges. &nbsp;<b>Write the formula, not a paragraph.</b>",
 "whichever question you choose &mdash; both open with one of these.")

# ==================== UNIT II ====================
w('<div class="bar"><span>UNIT&nbsp;II &mdash; Application of Laplace Transforms</span>'
  '<span class="r">20 marks &middot; Q3 <i>or</i> Q4 &middot; a(02) + b(04) + c(07) + d(07) &middot; you will score <b>13</b></span></div>')
qmap(["a &mdash; definition","b &mdash; short inverse","c &mdash; main problem","d &mdash; application"],
 [("Q3",[("Define the Dirac-delta function + sketch","02",True),
         (f"{inv}{{log(&hellip;)}} &nbsp;<b>step&nbsp;9</b>","04",True),
         ("<b>Heaviside piecewise + LT &nbsp;step&nbsp;5</b>","07",True),
         ("LR-circuit current &mdash; <i>cut</i>","07",False)]),
  ("Q4",[("Define the unit step function + graph","02",True),
         ("Partial-fraction inverse &mdash; <i>overtime&nbsp;17</i>","04",False),
         ("Verify the convolution theorem &mdash; <i>cut</i>","07",False),
         ("Simultaneous ODEs by LT &mdash; <i>cut</i>","07",False)])],
 "<b>&rarr; ANSWER Q3 &mdash; you have 13 of its 20.</b> The trigger is the <b>Heaviside piecewise function</b>. In "
 "all four papers an ODE-type problem sits next to it (that is the <i>d</i> part you are skipping) and the convolution "
 "question sits in the <b>other</b> question. If the log-inverse turns up in Q4 instead, go there &mdash; count ticks, don't assume.")

step(5,"Heaviside piecewise + Laplace transform","07","Q3c &mdash; same function in Apr&nbsp;23 and Mar&nbsp;24",
 "Express &nbsp;<i>f</i>(<i>t</i>) = " + PW([["<i>t</i><sup>2</sup>,","0 &lt; <i>t</i> &lt; 2"],["4<i>t</i>,","2 &lt; <i>t</i> &lt; 4"],["8,","<i>t</i> &gt; 4"]])
 + " in terms of the Heaviside function, and hence find its Laplace transform.",
 "<b>Step 1 &mdash; stack the jumps:</b> <i>f</i>(<i>t</i>) = <i>t</i><sup>2</sup> + (4<i>t</i>&minus;<i>t</i><sup>2</sup>)<i>u</i>(<i>t</i>&minus;2) + (8&minus;4<i>t</i>)<i>u</i>(<i>t</i>&minus;4). "
 "<b>Step 2 &mdash; rewrite each bracket in (<i>t</i>&minus;<i>a</i>):</b> at <i>t</i>=&tau;+2, 4<i>t</i>&minus;<i>t</i><sup>2</sup> = 4&minus;&tau;<sup>2</sup>; "
 "at <i>t</i>=&tau;+4, 8&minus;4<i>t</i> = &minus;8&minus;4&tau;. <b>Step 3 &mdash; second shifting</b> "
 "(<i>L</i>{<i>g</i>(<i>t</i>&minus;<i>a</i>)<i>u</i>(<i>t</i>&minus;<i>a</i>)} = <i>e</i><sup>&minus;<i>as</i></sup><i>G</i>(<i>s</i>)):<br>"
 "<b><i>L</i>{<i>f</i>} = 2/<i>s</i><sup>3</sup> + <i>e</i><sup>&minus;2<i>s</i></sup>(4/<i>s</i> &minus; 2/<i>s</i><sup>3</sup>) + <i>e</i><sup>&minus;4<i>s</i></sup>(&minus;8/<i>s</i> &minus; 4/<i>s</i><sup>2</sup>)</b>",
 "an ODE-type problem in the <i>d</i> slot &mdash; in all four papers. You are skipping that 7, deliberately.")

step(9,"Inverse Laplace transform of a logarithm","04","Q3b &mdash; same expression in Apr&nbsp;23 and Mar&nbsp;24",
 "Evaluate &nbsp;"+inv+"{ log "+F("<i>s</i><sup>2</sup> + 1","<i>s</i>(<i>s</i> + 1)")+" }",
 "<b>Method:</b> split &rarr; <i>F</i>(<i>s</i>) = ln(<i>s</i><sup>2</sup>+1) &minus; ln&nbsp;<i>s</i> &minus; ln(<i>s</i>+1). Differentiate: "
 "<i>F</i>&prime;(<i>s</i>) = "+F("2<i>s</i>","<i>s</i><sup>2</sup>+1")+" &minus; "+F("1","<i>s</i>")+" &minus; "+F("1","<i>s</i>+1")+
 ". Invert term by term &rarr; 2cos&nbsp;<i>t</i> &minus; 1 &minus; <i>e</i><sup>&minus;<i>t</i></sup>. Then use "+inv+"{<i>F</i>&prime;} = &minus;<i>t f</i>(<i>t</i>):<br>"
 "<b>answer = "+F("1 + <i>e</i><sup>&minus;<i>t</i></sup> &minus; 2&thinsp;cos&nbsp;<i>t</i>","<i>t</i>")+"</b> "
 "&nbsp;<span class='mut'>&mdash; the row that takes you past 50.</span>",
 "the Heaviside question in Mar&nbsp;24 (both in Q3) &mdash; so one question can hand you 11 of these 13 marks.")

step(7,"The Unit&nbsp;II 2-mark definition","02","<b>Q3a and Q4a &mdash; one in each</b>",
 "&ldquo;Define the Dirac-delta function and sketch its graph&rdquo; &nbsp;&bull;&nbsp; &ldquo;Define the unit step function and represent it graphically&rdquo;",
 "<b>Unit step:</b> <i>u</i>(<i>t</i>&minus;<i>a</i>) = 0 for <i>t</i> &lt; <i>a</i>, 1 for <i>t</i> &ge; <i>a</i> &mdash; draw the step at <i>t</i>=<i>a</i>. "
 f"<b>Dirac delta:</b> &delta;(<i>t</i>&minus;<i>a</i>) is the limit of a unit-area pulse; zero everywhere except <i>t</i>=<i>a</i>, "
 f"with {INT}<sub>&minus;{inf}</sub><sup>{inf}</sup>&delta;(<i>t</i>&minus;<i>a</i>)<i>dt</i> = 1 &mdash; draw the spike arrow at <i>t</i>=<i>a</i>. "
 "<b>Both are 2 marks for one sentence and one sketch.</b>",
 "whichever question you choose &mdash; both open with one.")

# ==================== UNIT III ====================
w('<div class="brk"></div><div class="bar"><span>UNIT&nbsp;III &mdash; Vector Space and Linear Transformation</span>'
  '<span class="r">20 marks &middot; Q5 <i>or</i> Q6 &middot; a(06) + b(07) + c(07) &middot; you will score <b>13</b>, or <b>20</b> with overtime</span></div>')
w('<p style="margin:0 0 3px"><b>This is your strongest unit</b> &mdash; zero calculus, and every question type it has '
  'ever asked is on this sheet. After overtime step&nbsp;13 <u>both</u> questions become fully answerable.</p>')
qmap(["a &mdash; vector space (06)","b &mdash; transformation (07)","c &mdash; the long one (07)"],
 [("Q5",[("Span / basis / independence &nbsp;<b>step&nbsp;10</b>","06",True),
         ("<b>Prove <i>T</i> is linear + images &nbsp;step&nbsp;2</b>","07",True),
         ("Rotation-operator proof &mdash; <i>cut</i>","07",False)]),
  ("Q6",[("<b>Composition of transformations &nbsp;step&nbsp;11</b>","06",True),
         ("Transition matrix &nbsp;<b>overtime&nbsp;13</b>","07",False),
         ("<b>Kernel &amp; range + rank&ndash;nullity &nbsp;step&nbsp;12</b>","07",True)])],
 "<b>&rarr; EITHER gives you 13.</b> Q5 = 6 + 7, Q6 = 6 + 7. If you do overtime step&nbsp;13 (transition matrix, "
 "15 minutes), <b>Q6 becomes a full 20</b> &mdash; the single biggest jump left in the whole plan, worth +6 on the "
 "worst paper. In Apr&nbsp;23 and Jun&nbsp;23 the transition matrix was in Q5 instead, so it pays off either way.")

step(2,"Prove <i>T</i> is linear + find images","07","<b>Q5b &mdash; all four papers, same slot</b>",
 f"<b>(a)</b> <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>); find the images of (1,&nbsp;2) and (2,&nbsp;&minus;5).<br>"
 f"<b>(b)</b> <i>T</i>:<i>P</i><sub>2</sub>{ARR}<i>P</i><sub>2</sub>, <i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup>+<i>c</i>; image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1.",
 "<b>Method (identical both times):</b> show <i>T</i>(<b>u</b>+<b>v</b>) = <i>T</i>(<b>u</b>)+<i>T</i>(<b>v</b>) and "
 "<i>T</i>(<i>k</i><b>u</b>) = <i>kT</i>(<b>u</b>), then substitute the two vectors. &nbsp;<b>Answers:</b> "
 "<i>T</i>(1,2) = <b>(5, 4, &minus;1)</b>, <i>T</i>(2,&minus;5) = <b>(1, &minus;10, 7)</b>, "
 "<i>T</i>(5<i>x</i><sup>2</sup>+6<i>x</i>+1) = <b>11<i>x</i><sup>2</sup> + 1</b>.",
 "the span/basis question at Q5a (step 10) &mdash; together they are 13 of Q5's 20.")

step(10,"Span / basis / linear independence","06","Q5a &mdash; all four papers",
 f"Is &nbsp;{{{M([['1','2'],['0','1']])}, {M([['3','4'],['1','1']])}, {M([['1','2'],['1','1']])}, {M([['0','2'],['1','2']])}}} a basis of <i>M</i><sub>22</sub>? "
 f"&nbsp;<span class='mut'>&mdash; or &mdash;</span>&nbsp; do {{(1,2,3), (&minus;1,&minus;1,0), (2,5,4)}} span <i>R</i><sup>3</sup>? "
 f"&nbsp;<span class='mut'>&mdash; or &mdash;</span>&nbsp; is (1,&minus;2) a linear combination of (2,4) and (3,6)?",
 "<b>One method covers every version.</b> Flatten each object to a coordinate vector (a 2&times;2 matrix becomes a "
 "4-vector; a polynomial becomes its coefficient vector), stack them as rows of a square matrix, take the "
 "<b>determinant</b>. Non-zero &rArr; independent &rArr; basis / spans. Zero &rArr; dependent. For "
 "&ldquo;is <b>v</b> a combination of &hellip;&rdquo;, solve the system and show it is consistent.",
 "the prove-<i>T</i>-is-linear question at Q5b (step 2).")

step(11,"Composition of matrix transformations","06","Q6a &mdash; all four papers",
 f"Determine the matrix for: reflection in the <i>x</i>-axis, then rotation through {pi}/2, then contraction of "
 f"factor 1/3; find the image of {V(['4','1'])}. &nbsp;<span class='mut'>(the axis, angle, factor and point change every paper &mdash; the method never does)</span>",
 f"<b>Multiply RIGHT to LEFT:</b> <i>M</i> = <i>k</i> &middot; <i>R</i><sub>{th}</sub> &middot; <i>Ref</i>. "
 f"Reflect in <i>x</i>: {M([['1','0'],['0',sp+'1']])} &nbsp; reflect in <i>y</i>: {M([[sp+'1','0'],['0','1']])} &nbsp; "
 f"rotate: {M([['cos&#952;',sp+'sin&#952;'],['sin&#952;','cos&#952;']])} &nbsp; dilation/contraction by <i>k</i>: scale the whole matrix. "
 f"For {pi}/2 the rotation is {M([['0',sp+'1'],['1','0']])}. Then apply <i>M</i> to the point.",
 "the kernel &amp; range question at Q6c (step 12), and the transition matrix at Q6b (overtime 13).")

step(12,"Kernel and range + verify rank&ndash;nullity","07","Q6c &mdash; all four papers",
 f"Determine the kernel and range of the transformation defined by &nbsp;<i>A</i> = {M([['1','2','3'],['0',sp+'1','1'],['1','1','4']])}, "
 f"and hence verify the rank&ndash;nullity theorem.",
 "<b>Method:</b> row-reduce <i>A</i>. The <b>pivot columns of the original <i>A</i></b> give a basis for the range; "
 "solving <i>Ax</i> = <b>0</b> gives a basis for the kernel. Here <b>rank = 2, nullity = 1</b>, and 2 + 1 = 3 = "
 "number of columns. <b>Also be ready for the formula version</b> (e.g. <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>, "
 "<i>x</i>&minus;<i>y</i>, <i>y</i>)) &mdash; write its matrix first, then the work is identical.",
 "the composition question at Q6a (step 11).")

step(13,"Transition matrix / change of basis","07","Q6b &mdash; same bases in Sep&nbsp;23 and Mar&nbsp;24",
 f"<i>B</i> = {{(1,&nbsp;2), (3,&nbsp;&minus;1)}} and <i>B</i>&prime; = {{(3,&nbsp;1), (5,&nbsp;2)}} of <i>R</i><sup>2</sup>. Find the transition "
 f"matrix from <i>B</i> to <i>B</i>&prime;; if [<i>u</i>]<sub><i>B</i></sub> = {V(['2','1'])}, find [<i>u</i>]<sub><i>B</i>&prime;</sub>.",
 "<b>Method:</b> put the <i>B</i>&prime; vectors as columns of <i>Q</i> and the <i>B</i> vectors as columns of <i>P</i>. "
 "The transition matrix is <b><i>Q</i><sup>&minus;1</sup><i>P</i></b>, and [<i>u</i>]<sub><i>B</i>&prime;</sub> = "
 "(<i>Q</i><sup>&minus;1</sup><i>P</i>)[<i>u</i>]<sub><i>B</i></sub>. One 2&times;2 inverse. "
 "<b>+6 on the worst paper &mdash; the biggest single gain left.</b>",
 "the composition and kernel&amp;range questions &mdash; doing this completes Q6 as a full 20.", ot=True)

# ==================== UNIT IV ====================
w('<div class="brk"></div><div class="bar"><span>UNIT&nbsp;IV &mdash; Orthogonal Projections</span>'
  '<span class="r">20 marks &middot; Q7 (06+07+07) <i>or</i> Q8 (10+10) &middot; you will score <b>10</b>, or <b>13</b> with overtime</span></div>')
w('<p style="margin:0 0 3px"><b>Your weakest unit, and that is deliberate</b> &mdash; QR and Gram&ndash;Schmidt are '
  'long and their matrices change every paper, so three hours cannot buy them. You take the least-squares 10 and move on.</p>')
qmap(["a","b","c"],
 [("Q7",[("Complete solution of <i>Ax</i>=<i>b</i> &nbsp;<b>overtime&nbsp;16</b> &nbsp;(06)","06",False),
         ("Orthogonal projection of <i>y</i> onto <i>u</i> &mdash; <i>cut</i> &nbsp;(07)","07",False),
         ("Four fundamental subspaces &nbsp;<b>overtime&nbsp;15</b> &nbsp;(07)","07",False)]),
  ("Q8",[("QR factorization &mdash; <i>cut</i> &nbsp;(10)","10",False),
         ("<b>Least-squares solution &nbsp;step&nbsp;3</b> &nbsp;(10)","10",True),
         ("&mdash;","&mdash;",False)])],
 "<b>&rarr; ANSWER Q8 &mdash; you have 10 of its 20</b>, from one part. If you reach overtime steps 15 and 16, "
 "<b>Q7 gives you 13</b> instead and becomes the better choice. Note the four-subspaces question is in <b>Q7 in all "
 "four papers</b> without exception, so that is where those marks live.")

step(3,"Least-squares solution of <i>Ax</i> = <i>b</i>","10","<b>Q8b</b> &mdash; least-squares appears in all four papers",
 f"Find the least-squares solution of <i>AX</i> = <i>b</i> for &nbsp;<i>A</i> = {M([['1','3','5'],['1','1','0'],['1','1','2'],['1','3','3']])} "
 f"&nbsp;and&nbsp; <i>b</i> = {V(['3','5','7',sp+'3'])} &nbsp;&nbsp;<span class='mut'>&mdash; identical in Jun&nbsp;23 and Mar&nbsp;24</span>",
 f"<b>Method:</b> solve the normal equations <i>A</i><sup>T</sup><i>A</i>&#770;<i>x</i> = <i>A</i><sup>T</sup><i>b</i>. That is the whole question.<br>"
 f"<b>Work it once now:</b> <i>A</i><sup>T</sup><i>A</i> = {M([['4','8','10'],['8','20','26'],['10','26','38']])}, "
 f"<i>A</i><sup>T</sup><i>b</i> = {V(['12','12','20'])} &nbsp;&rArr;&nbsp; <b>&#770;<i>x</i> = (10, &minus;6, 2)</b>. "
 f"Substitute back to check &mdash; it costs thirty seconds and confirms the whole 10 marks.",
 "the QR factorization at Q8a, which you are skipping. Ten marks from one part is still the best available here.")

step(15,"Four fundamental subspaces","07","<b>Q7 &mdash; in all four papers. Same matrix in 3 of 4.</b>",
 f"Find the dimension and basis for the four fundamental subspaces of &nbsp;<i>A</i> = {M([['1','2','0','1'],['0','1','1','0'],['1','2','0','1']])} "
 f"&nbsp;<span class='mut'>(Jun&nbsp;23 phrased it &ldquo;basis for col(<i>A</i>) and nul(<i>A</i>)&rdquo; &mdash; same matrix, same work)</span>",
 "<b>Row 3 = row 1</b>, so rank = 2 straight away. dim col(<i>A</i>) = dim row(<i>A</i>) = <b>2</b>; "
 "dim nul(<i>A</i>) = 4 &minus; 2 = <b>2</b>; dim nul(<i>A</i><sup>T</sup>) = 3 &minus; 2 = <b>1</b>. "
 "Row-reduce once and read a basis off each. One of the cheapest 7 marks on the paper.",
 "the complete solution at Q7a (overtime 16) &mdash; together they turn Q7 into 13.", ot=True)

step(16,"Complete solution of <i>Ax</i> = <i>b</i>","06","Q7a &mdash; 3 of 4 papers",
 "Find the complete solution of &nbsp;<i>x</i> + 3<i>y</i> + 3<i>z</i> = 1, &nbsp;2<i>x</i> + 6<i>y</i> + 9<i>z</i> = 5, "
 "&nbsp;&minus;<i>x</i> &minus; 3<i>y</i> + 3<i>z</i> = 5.",
 "<b>Method:</b> row-reduce the augmented matrix, take any particular solution <b><i>x</i><sub>p</sub></b>, then add "
 "the null-space basis. Always present it as <b><i>x</i> = <i>x</i><sub>p</sub> + <i>c</i><sub>1</sub><b>n</b><sub>1</sub> "
 "+ &hellip;</b> and state the consistency condition. Same row-reduction skill as step&nbsp;15.",
 "the four-subspaces question at Q7c (overtime 15).", ot=True)

# ==================== UNIT V ====================
w('<div class="brk"></div><div class="bar"><span>UNIT&nbsp;V &mdash; Applications of Eigenvalue Decomposition</span>'
  '<span class="r">20 marks &middot; Q9 <i>or</i> Q10 &middot; a(05) + b(05) + c(10) &middot; you will score <b>15</b>, or <b>20</b> with overtime</span></div>')
w('<p style="margin:0 0 3px"><b>The best-value unit on the paper.</b> The two 5-mark property checks are about two '
  'minutes of work each, and the 10-marker has used the same matrix in 3 of the 4 papers.</p>')
qmap(["a &mdash; 5-mark check","b &mdash; 5-mark check","c &mdash; the 10-marker"],
 [("Q9",[("Quadratic form, no cross terms &mdash; <i>cut</i>","05",False),
         ("Markov steady state &mdash; <i>cut</i>","05",False),
         ("SVD &mdash; <i>cut</i>","10",False)]),
  ("Q10",[("Positive-definite check &nbsp;<b>overtime&nbsp;14</b>","05",False),
          ("<b>Unitary / Hermitian check &nbsp;step&nbsp;1</b>","05",True),
          ("<b>Orthogonal diagonalization &nbsp;step&nbsp;8</b>","10",True)])],
 "<b>&rarr; ANSWER Q10 &mdash; you have 15 of its 20</b>, and <b>a full 20</b> after overtime step&nbsp;14. The "
 "trigger is &ldquo;orthogonally diagonalize&rdquo;: in 3 of 4 papers the property-checks sit in the same question as "
 "it, and SVD sits in the <b>other</b> one. In Apr&nbsp;23 the checks were in Q9 with the property pair &mdash; if that "
 "happens, take whichever question holds two of your three items.")

step(1,"Unitary / Hermitian check","05","Q10b &mdash; a property check appears in <b>all four papers</b>",
 f"Is &nbsp;<i>A</i> = {M([['0','<i>i</i>'],[sp+'<i>i</i>','0']])} unitary? &nbsp;&nbsp;<span class='mut'>&mdash; or the Hermitian version &mdash;</span>&nbsp; is "
 f"{M([['3','7'+sp+'4<i>i</i>',sp+'2+5<i>i</i>'],['7+4<i>i</i>',sp+'2','3+<i>i</i>'],[sp+'2'+sp+'5<i>i</i>','3'+sp+'<i>i</i>','4']])} Hermitian?",
 "<b>Method:</b> write <i>A</i><sup>*</sup> = the conjugate of the transpose. <b>Hermitian</b> &hArr; <i>A</i><sup>*</sup> = <i>A</i>. "
 "<b>Unitary</b> &hArr; <i>A</i><sup>*</sup><i>A</i> = <i>I</i>. &nbsp;<b>Both of these answer YES</b> &mdash; the 2&times;2 is "
 "unitary (and Hermitian as well); the 3&times;3 is Hermitian, with a real diagonal and every "
 "<i>a<sub>ij</sub></i> = conj(<i>a<sub>ji</sub></i>). Show <i>A</i><sup>*</sup> written out in full.",
 "the positive-definite check &mdash; in all four papers the property checks travel as a pair, either as (i)/(ii) of one "
 "10-marker or as the 5+5.")

step(8,"Orthogonal diagonalization","10","<b>Q10c &mdash; same matrix in 3 of the 4 papers</b>",
 f"Orthogonally diagonalize &nbsp;<i>A</i> = {M([['3',sp+'1','1'],[sp+'1','5',sp+'1'],['1',sp+'1','3']])}",
 f"<b>You already know the answer &mdash; rehearse producing it.</b> Eigenvalues <b>2, 3, 6</b>, all distinct, so the "
 f"eigenvectors come out mutually orthogonal on their own &mdash; <u>no Gram&ndash;Schmidt needed</u>, and saying so earns marks.<br>"
 f"Eigenvectors {V(['1','0',sp+'1'])} for 2, &nbsp;{V(['1','1','1'])} for 3, &nbsp;{V(['1',sp+'2','1'])} for 6. Normalise by "
 f"{sq}2, {sq}3, {sq}6 &mdash; those are the columns of <i>P</i>. Then <b><i>P</i><sup>T</sup><i>AP</i> = diag(2,&nbsp;3,&nbsp;6)</b>. "
 f"Verify all three pairwise dot products are 0 in your answer.",
 "the two 5-mark property checks &mdash; in 3 of 4 papers they are in the same question. That is the full 20.")

step(14,"Positive-definite check","05","Q10a &mdash; same matrix in Apr&nbsp;23 and Mar&nbsp;24",
 f"Check whether &nbsp;<i>A</i> = {M([['1',sp+'2','1'],[sp+'2','4',sp+'2'],['1',sp+'2','1']])} is positive definite or not.",
 "<b>Method:</b> leading principal minors. They are <b>1, 0, 0</b>, so it is <b>NOT positive definite</b> &mdash; it is "
 "positive <i>semi</i>-definite (row 3 = row 1, eigenvalues 0, 0, 6). <b>Say that explicitly</b>; writing only "
 "&ldquo;no&rdquo; loses marks. Two minutes of work.",
 "the unitary/Hermitian check (step 1) &mdash; doing both completes Q10's 5+5 and makes the unit a full 20.", ot=True)

step(17,"Short inverse Laplace transform","04","Q4b &mdash; a short inverse appears in <b>both</b> Unit II questions",
 "Find &nbsp;"+inv+"{"+F("3<i>s</i> + 2","<i>s</i><sup>2</sup> &minus; <i>s</i> &minus; 2")+"}",
 "<b>Method:</b> factor the denominator (<i>s</i>&minus;2)(<i>s</i>+1), split into partial fractions, and invert with "
 "the standard table. This is insurance for the case where the log-inverse (step&nbsp;9) turns up in the question you "
 "did <i>not</i> choose &mdash; one of the two 4-mark inverses is always reachable.", ot=True)

w("""<div class="foot"><b>How this was built:</b> each candidate topic was costed in study minutes and scored by the
marks it adds to the <i>worst</i> of the four past papers, respecting the fact that only one question per unit can be
answered. The list is greedy-ordered by worst-case marks per minute, so stopping at any row leaves the best score
reachable in the time spent. Question maps use the March&nbsp;2024 layout &mdash; the only paper printed under your
current course title. Running totals are computed, not estimated; the working is in <i>coverage_audit.py</i>.</div>""")

doc="<!doctype html><html><head><meta charset='utf-8'><title>24CS31 3-Hour Hail Mary</title><style>"+CSS+"</style></head><body>"+"".join(H)+"</body></html>"
import io,os
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"24CS31_3Hour_HailMary.html")
io.open(out,"w",encoding="utf-8").write(doc); print("wrote",out)

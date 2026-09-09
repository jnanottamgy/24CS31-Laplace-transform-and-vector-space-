#!/usr/bin/env python3
def M(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat"><table>{b}</table></span>'
def V(c): return M([[x] for x in c])
def PW(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat pw"><table>{b}</table></span>'
def F(n,d): return f'<span class="f"><span class="n">{n}</span><span class="d">{d}</span></span>'
sp="&#8722;"; inf="&#8734;"; pi="&#960;"; th="&#952;"; sq="&#8730;"; INT="&#8747;"; ARR="&#8594;"; inv="<i>L</i><sup>&minus;1</sup>"

CSS="""
@page{size:A4;margin:8mm 8mm 9mm 8mm}
*{box-sizing:border-box}
body{font-family:"DejaVu Serif",Georgia,serif;font-size:8.2pt;line-height:1.3;color:#14161b;margin:0}
h1{font-size:16.5pt;margin:0;letter-spacing:-.3px}
.hd{border:2.5px solid #a04545;border-radius:4px;padding:7px 10px;margin-bottom:6px;background:#fdf6f6}
.hd .s{font-size:8.5pt;color:#39414f;margin-top:2px}
.bar{background:#1d2433;color:#fff;padding:4px 8px;border-radius:3px;margin:9px 0 4px;font-size:10.5pt;
     font-weight:700;display:flex;justify-content:space-between}
.bar .r{font-size:8.2pt;font-weight:400;color:#cfd6e4}
table.g{width:100%;border-collapse:collapse;margin:0 0 5px;font-size:8.1pt}
table.g th{background:#39414f;color:#fff;text-align:left;padding:3px 5px;font-size:7.6pt;border:.7px solid #39414f}
table.g td{border:.7px solid #b9c0cc;padding:3px 5px;vertical-align:middle}
table.g tr:nth-child(even) td{background:#f5f7fa}
.c{text-align:center}
.pass td{background:#0d7a45!important;color:#fff!important;font-weight:700}
.pass td i,.pass td b{color:#fff!important}
.stp{border:1px solid #c2c9d4;border-left:5px solid #0d7a45;border-radius:0 3px 3px 0;padding:6px 9px;margin:6px 0;background:#fbfcfd}
.stp.ot{border-left-color:#b8842a}
.sh{font-weight:700;font-size:8.9pt;color:#14161b;margin-bottom:3px}
.sh .n{display:inline-block;background:#0d7a45;color:#fff;border-radius:2px;padding:.5px 6px;margin-right:6px;font-size:8pt}
.stp.ot .sh .n{background:#b8842a}
.sh .mk{float:right;font-size:8pt;color:#39414f;font-weight:400}
.ans{background:#eef4ef;border-left:3px solid #0d7a45;padding:3px 7px;margin-top:4px;font-size:8pt}
.ans b{color:#0d5c34}
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
H=[];  w=H.append

w(f"""<div class="hd"><h1>24CS31 &mdash; 3-HOUR HAIL MARY</h1>
<div class="s">Ordered by <b>worst-case marks per minute</b>, computed against all four past papers. Do them
<b>in this exact order</b>. Every calculus-heavy question has been cut <b>except</b> the four that repeat verbatim.</div></div>

<div class="box avoid"><b>THE ONE THING TO UNDERSTAND.</b> The &ldquo;running total&rdquo; column is the mark you
would score on the <b>worst</b> of the four past papers if you stopped studying at that row. You cross the pass mark
at <b>2 h 09</b>. You do <b>not</b> get to stop before then &mdash; two hours of this leaves you at 42.
<b>Steps 1&ndash;12 are the whole plan. Finish them.</b></div>

<div class="bar"><span>THE CLOCK</span><span class="r">stop-anywhere score = worst of 4 papers</span></div>
<table class="g">
<tr><th class="c" style="width:4%">#</th><th style="width:30%">Study this</th><th class="c" style="width:7%">Unit</th>
<th class="c" style="width:6%">Marks</th><th class="c" style="width:6%">Mins</th><th class="c" style="width:8%">Clock</th>
<th class="c" style="width:11%">Running total</th><th>Why it is this high up</th></tr>""")

CLOCK=[("Unitary / Hermitian check","V","05","08","0:08","5","Two minutes of work in the exam. Nothing on the paper pays better per minute.",0),
 ("Prove <i>T</i> is linear + find images","III","07","12","0:20","12","<b>Q5b in all four papers.</b> Zero calculus, zero matrices.",0),
 ("Least-squares solution","IV","10","20","0:40","22","10 marks, <b>identical <i>A</i> and <i>b</i> twice</b>, and it is only <i>A</i><sup>T</sup><i>A</i>&#770;<i>x</i> = <i>A</i><sup>T</sup><i>b</i>.",0),
 ("<i>t<sup>n</sup></i>-multiplication proof","I","07","15","0:55","29","4/4 papers, identical wording. Calculus on paper, pure recall in practice.",0),
 ("Heaviside piecewise + LT","II","07","20","1:15","36","Same function twice. Mechanical once you have the shift pattern.",0),
 (f"<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} {ARR} <i>L</i>{{cos&nbsp;{sq}<i>t</i>/{sq}<i>t</i>}}","I","04","12","1:27","40","Same statement twice. Four lines of differentiation.",0),
 ("The Unit&nbsp;I 2-mark definition","I","02","05","1:32","42","Five minutes for two marks, and it is in <i>both</i> options.",0),
 ("Orthogonal diagonalization","V","10","25","1:57","47","Same matrix 3/4. Longest item here, but you already know the eigenvalues.",0),
 (f"{inv}{{log(&hellip;)}}","II","04","12","2:09","52","Same expression twice. <b>This is the row that crosses 50.</b>",1),
 ("Span / basis / linear independence","III","06","12","2:21","53","Backs up Q5 so Unit&nbsp;III is safe whichever question appears.",0),
 ("Composition of transformations","III","06","12","2:33","58","Three 2&times;2 matrices multiplied. Opens up Q6.",0),
 ("Kernel &amp; range + rank&ndash;nullity","III","07","15","2:48","59","Completes Q6 &mdash; now <b>both</b> Unit&nbsp;III questions are fully answerable.",0)]
for i,(t,u,mk,mn,ck,rt,why,ps) in enumerate(CLOCK,1):
    cls=' class="pass"' if ps else ''
    w(f'<tr{cls}><td class="c"><b>{i}</b></td><td><b>{t}</b></td><td class="c">{u}</td><td class="c">{mk}</td>'
      f'<td class="c">{mn}</td><td class="c">{ck}</td><td class="c"><b>{rt}</b>{" &#9989;" if ps else ""}</td><td>{why}</td></tr>')
w("""<tr><td class="c" colspan="8" style="background:#b8842a!important;color:#fff;font-weight:700">
&mdash;&mdash;  3 HOURS UP. Everything below is overtime, in the order that pays best.  &mdash;&mdash;</td></tr>""")
for i,(t,u,mk,mn,rt,why) in enumerate([
 ("Transition matrix / change of basis","III","07","15","65","<b>Biggest remaining jump: +6.</b> If you can steal 15 minutes anywhere, steal them for this."),
 ("Positive-definite check","V","05","08","65","Three determinants. Pairs with step&nbsp;1 to finish Unit&nbsp;V's 5+5."),
 ("Four fundamental subspaces","IV","07","15","65","Same matrix 3/4, one row reduction. <b>Always in Q7.</b>"),
 ("Complete solution of <i>Ax</i> = <i>b</i>","IV","06","15","65","Same row-reduction skill you just used."),
 ("Unit&nbsp;II definitions + short inverse LT","II","06","15","65","Unit step, Dirac delta, and one partial-fraction inverse.")],13):
    w(f'<tr><td class="c">{i}</td><td>{t}</td><td class="c">{u}</td><td class="c">{mk}</td><td class="c">{mn}</td>'
      f'<td class="c mut">&mdash;</td><td class="c">{rt}</td><td>{why}</td></tr>')
w("</table>")

w(f"""<div class="box avoid"><b>CUT. DO NOT OPEN THESE.</b> Every one is real and several are 4/4 &mdash; but each is
long, calculus-heavy, and the numbers change every paper, so three hours cannot buy them:<br>
ODEs and simultaneous ODEs by Laplace &nbsp;&bull;&nbsp; convolution theorem &nbsp;&bull;&nbsp;
improper integrals {INT}<sub>0</sub><sup>{inf}</sup> &nbsp;&bull;&nbsp; <i>L</i>{{<i>t e<sup>at</sup></i> trig}} and
division by <i>t</i> &nbsp;&bull;&nbsp; periodic functions / triangular wave &nbsp;&bull;&nbsp;
({sq}<i>t</i>+1/{sq}<i>t</i>)<sup>3</sup> &nbsp;&bull;&nbsp; <b>QR factorization</b> &nbsp;&bull;&nbsp;
<b>SVD</b> &nbsp;&bull;&nbsp; diagonalize and find <i>A<sup>n</sup></i> &nbsp;&bull;&nbsp; Gram&ndash;Schmidt
&nbsp;&bull;&nbsp; orthogonal projection &nbsp;&bull;&nbsp; Markov &nbsp;&bull;&nbsp; quadratic forms
&nbsp;&bull;&nbsp; rotation-operator proof &nbsp;&bull;&nbsp; PCA.<br>
<b>The four calculus items that survived</b> (steps 4, 5, 6, 9) survived on your own rule: each has been set with
<b>identical wording or identical values</b> in at least two papers.</div>

<div class="box g avoid"><b>IN THE HALL.</b> You will not be able to answer every unit fully &mdash; that is fine and
it is priced in. Rule: <b>write every part you know, in every unit, and never leave a unit blank.</b> A 5-mark
property check you can do beats a 10-mark decomposition you half-remember. Answer the parts, not the question.</div>""")

# ============================ THE QUESTIONS ============================
def step(n,title,marks,unit,sec,body,ans,ot=False):
    w(f"""<div class="stp{' ot' if ot else ''} avoid"><div class="sh"><span class="n">{n}</span>{title}
    <span class="mk">{marks} marks &middot; Unit {unit} &middot; {sec}</span></div>
    <div>{body}</div><div class="ans">{ans}</div></div>""")

w('<div class="brk"></div><div class="bar"><span>STEPS 1&ndash;6 &nbsp;&middot;&nbsp; first 1 h 27</span><span class="r">running total 40 / 100</span></div>')

step(1,"Unitary / Hermitian check","05","V","Q10a or Q10b (the 5+5 pair)",
 f"Is &nbsp;<i>A</i> = {M([['0','<i>i</i>'],[sp+'<i>i</i>','0']])} unitary? &nbsp;&nbsp;<span class='mut'>and the other version:</span>&nbsp; "
 f"is &nbsp;{M([['3','7'+sp+'4<i>i</i>',sp+'2+5<i>i</i>'],['7+4<i>i</i>',sp+'2','3+<i>i</i>'],[sp+'2'+sp+'5<i>i</i>','3'+sp+'<i>i</i>','4']])} Hermitian?",
 "<b>Method:</b> write <i>A</i><sup>*</sup> = conjugate of the transpose. <b>Hermitian</b> &hArr; <i>A</i><sup>*</sup> = <i>A</i>. "
 "<b>Unitary</b> &hArr; <i>A</i><sup>*</sup><i>A</i> = <i>I</i>. &nbsp;<b>Both answers here are YES</b> &mdash; the 2&times;2 "
 "is unitary (and Hermitian too), and the 3&times;3 is Hermitian: diagonal is real and every <i>a<sub>ij</sub></i> = conj(<i>a<sub>ji</sub></i>).")

step(2,"Prove <i>T</i> is linear + find images","07","III","<b>Q5b &mdash; all four papers, same slot</b>",
 f"<b>(a)</b> <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>); find images of (1,&nbsp;2) and (2,&nbsp;&minus;5).<br>"
 f"<b>(b)</b> <i>T</i>:<i>P</i><sub>2</sub>{ARR}<i>P</i><sub>2</sub>, <i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup>+<i>c</i>; image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1.",
 "<b>Method (same both times):</b> show <i>T</i>(<b>u</b>+<b>v</b>) = <i>T</i>(<b>u</b>)+<i>T</i>(<b>v</b>) and "
 "<i>T</i>(<i>k</i><b>u</b>) = <i>kT</i>(<b>u</b>), then substitute. &nbsp;<b>Answers:</b> "
 "<i>T</i>(1,2) = <b>(5, 4, &minus;1)</b>, &nbsp;<i>T</i>(2,&minus;5) = <b>(1, &minus;10, 7)</b>; &nbsp;"
 "<i>T</i>(5<i>x</i><sup>2</sup>+6<i>x</i>+1) = <b>11<i>x</i><sup>2</sup> + 1</b>.")

step(3,"Least-squares solution of <i>Ax</i> = <i>b</i>","10","IV","Q8b (or Q7b) &mdash; all four papers",
 f"<i>A</i> = {M([['1','3','5'],['1','1','0'],['1','1','2'],['1','3','3']])} &nbsp;&nbsp; <i>b</i> = {V(['3','5','7',sp+'3'])} "
 f"&nbsp;&nbsp;<span class='mut'>&mdash; identical in Jun&nbsp;23 and Mar&nbsp;24</span>",
 f"<b>Method:</b> solve the normal equations <i>A</i><sup>T</sup><i>A</i>&#770;<i>x</i> = <i>A</i><sup>T</sup><i>b</i>. That is all.<br>"
 f"<b>Work it once now and memorise the shape:</b> &nbsp;<i>A</i><sup>T</sup><i>A</i> = {M([['4','8','10'],['8','20','26'],['10','26','38']])}, "
 f"&nbsp;<i>A</i><sup>T</sup><i>b</i> = {V(['12','12','20'])}, &nbsp;&rArr;&nbsp; <b>&#770;<i>x</i> = (10, &minus;6, 2)</b>.")

step(4,"Prove the <i>t<sup>n</sup></i>-multiplication rule","07","I","Q1c or Q2b &mdash; <b>4/4 papers, word for word</b>",
 "If <i>L</i>{<i>f</i>(<i>t</i>)} = <i>F</i>(<i>s</i>), prove that &nbsp;<i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = "
 "(&minus;1)<sup><i>n</i></sup> " + F("<i>d<sup>n</sup></i>","<i>ds<sup>n</sup></i>") + "{<i>F</i>(<i>s</i>)}, &nbsp;<i>n</i> a positive integer.",
 f"<b>Script &mdash; learn these four lines.</b> <i>F</i>(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i>. "
 f"Differentiate under the integral sign: <i>F</i>&prime;(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup>(&minus;<i>t</i>)<i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)<i>dt</i> "
 f"= &minus;<i>L</i>{{<i>t f</i>(<i>t</i>)}}. Repeat <i>n</i> times &rarr; each pass drops one factor of (&minus;<i>t</i>). "
 f"Finish by <b>induction on <i>n</i></b>: assume true for <i>n</i>, differentiate once more, get <i>n</i>+1. State the base case <i>n</i>=1.")

step(5,"Heaviside piecewise + Laplace transform","07","II","Q3c &mdash; same function in Apr&nbsp;23 and Mar&nbsp;24",
 "Express &nbsp;<i>f</i>(<i>t</i>) = " + PW([["<i>t</i><sup>2</sup>,","0 &lt; <i>t</i> &lt; 2"],["4<i>t</i>,","2 &lt; <i>t</i> &lt; 4"],["8,","<i>t</i> &gt; 4"]])
 + " in terms of the Heaviside function, and hence find its Laplace transform.",
 "<b>Step 1 &mdash; stack the jumps:</b> <i>f</i>(<i>t</i>) = <i>t</i><sup>2</sup> + (4<i>t</i> &minus; <i>t</i><sup>2</sup>)<i>u</i>(<i>t</i>&minus;2) "
 "+ (8 &minus; 4<i>t</i>)<i>u</i>(<i>t</i>&minus;4). &nbsp;<b>Step 2 &mdash; rewrite each bracket in (<i>t</i>&minus;<i>a</i>):</b> "
 "at <i>t</i> = &tau;+2, &nbsp;4<i>t</i>&minus;<i>t</i><sup>2</sup> = 4 &minus; &tau;<sup>2</sup>; at <i>t</i> = &tau;+4, &nbsp;8&minus;4<i>t</i> = &minus;8 &minus; 4&tau;. "
 "<b>Step 3 &mdash; second shifting</b> (<i>L</i>{<i>g</i>(<i>t</i>&minus;<i>a</i>)<i>u</i>(<i>t</i>&minus;<i>a</i>)} = <i>e</i><sup>&minus;<i>as</i></sup><i>G</i>(<i>s</i>)):<br>"
 "<b><i>L</i>{<i>f</i>} = 2/<i>s</i><sup>3</sup> + <i>e</i><sup>&minus;2<i>s</i></sup>(4/<i>s</i> &minus; 2/<i>s</i><sup>3</sup>) "
 "+ <i>e</i><sup>&minus;4<i>s</i></sup>(&minus;8/<i>s</i> &minus; 4/<i>s</i><sup>2</sup>)</b>")

step(6,f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show the cos&nbsp;{sq}<i>t</i> result","04","I","Q1b &mdash; same statement in Jun&nbsp;23 and Mar&nbsp;24",
 f"Given &nbsp;<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = "+F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>, &nbsp;show that &nbsp;"
 "<i>L</i>{"+F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")+"} = "+F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>.",
 f"<b>Method:</b> notice "+F("<i>d</i>","<i>dt</i>")+f"(sin&nbsp;{sq}<i>t</i>) = "+F(f"cos&nbsp;{sq}<i>t</i>",f"2{sq}<i>t</i>")+
 ". So the target is <b>2 &times; <i>L</i>{derivative}</b>. Apply <i>L</i>{<i>f</i>&prime;(<i>t</i>)} = <i>s F</i>(<i>s</i>) &minus; <i>f</i>(0), "
 f"with <i>f</i>(0) = sin&nbsp;0 = 0. That gives 2 &middot; <i>s</i> &middot; "+F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")+
 "<i>e</i><sup>&minus;1/4<i>s</i></sup> = "+F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>. <b>Three lines.</b>")

w('<div class="brk"></div><div class="bar"><span>STEPS 7&ndash;12 &nbsp;&middot;&nbsp; 1 h 27 to 2 h 48</span><span class="r">running total 59 / 100 &mdash; you pass at step 9</span></div>')

step(7,"The Unit&nbsp;I 2-mark definition","02","I","<b>Q1a and Q2a &mdash; you get one whichever you choose</b>",
 "&ldquo;Write the Laplace transform of a periodic function&rdquo; &nbsp;&bull;&nbsp; &ldquo;Define the Laplace transform of a function&rdquo;",
 f"<b>Periodic, period <i>T</i>:</b> &nbsp;<i>L</i>{{<i>f</i>(<i>t</i>)}} = "+F("1","1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>")+
 f"{INT}<sub>0</sub><sup><i>T</i></sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i>. &nbsp;&nbsp;"
 f"<b>Definition:</b> <i>L</i>{{<i>f</i>(<i>t</i>)}} = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i>, "
 f"provided the integral converges. <b>Write the formula, not a paragraph.</b>")

step(8,"Orthogonally diagonalize","10","V","Q10c &mdash; <b>same matrix in 3 of the 4 papers</b>",
 f"Orthogonally diagonalize &nbsp;<i>A</i> = {M([['3',sp+'1','1'],[sp+'1','5',sp+'1'],['1',sp+'1','3']])}",
 f"<b>You already know the answer &mdash; rehearse producing it.</b> Eigenvalues <b>2, 3, 6</b> (all distinct, so the "
 f"eigenvectors are automatically orthogonal &mdash; <u>no Gram&ndash;Schmidt needed</u>; say that in your answer).<br>"
 f"Eigenvectors: &nbsp;{V(['1','0',sp+'1'])} for 2, &nbsp;{V(['1','1','1'])} for 3, &nbsp;{V(['1',sp+'2','1'])} for 6. "
 f"Normalise by {sq}2, {sq}3, {sq}6 &rarr; those are the columns of <i>P</i>. Then <b><i>P</i><sup>T</sup><i>AP</i> = "
 f"diag(2,&nbsp;3,&nbsp;6)</b>. Check all three dot products are 0 in your answer &mdash; it earns marks.")

step(9,f"Inverse Laplace transform of a logarithm","04","II","Q3b &mdash; same expression in Apr&nbsp;23 and Mar&nbsp;24",
 "Evaluate &nbsp;"+inv+"{ log "+F("<i>s</i><sup>2</sup> + 1","<i>s</i>(<i>s</i> + 1)")+" }",
 "<b>Method:</b> split the log &rarr; <i>F</i>(<i>s</i>) = ln(<i>s</i><sup>2</sup>+1) &minus; ln&nbsp;<i>s</i> &minus; ln(<i>s</i>+1). "
 "Differentiate: <i>F</i>&prime;(<i>s</i>) = "+F("2<i>s</i>","<i>s</i><sup>2</sup>+1")+" &minus; "+F("1","<i>s</i>")+" &minus; "+F("1","<i>s</i>+1")+
 ". Invert term by term: 2&thinsp;cos&nbsp;<i>t</i> &minus; 1 &minus; <i>e</i><sup>&minus;<i>t</i></sup>. "
 "Then use "+inv+"{<i>F</i>&prime;(<i>s</i>)} = &minus;<i>t f</i>(<i>t</i>):<br>"
 "<b>answer = "+F("1 + <i>e</i><sup>&minus;<i>t</i></sup> &minus; 2&thinsp;cos&nbsp;<i>t</i>","<i>t</i>")+"</b> &nbsp;&nbsp;"
 "<span class='mut'>&mdash; this is the row that takes you past 50.</span>")

step(10,"Span / basis / linear independence","06","III","Q5a &mdash; all four papers",
 f"Is &nbsp;{{{M([['1','2'],['0','1']])}, {M([['3','4'],['1','1']])}, {M([['1','2'],['1','1']])}, {M([['0','2'],['1','2']])}}} a basis of "
 f"<i>M</i><sub>22</sub>? &nbsp;&nbsp;<span class='mut'>or:</span> do {{(1,2,3), (&minus;1,&minus;1,0), (2,5,4)}} span <i>R</i><sup>3</sup>?",
 "<b>One method for every version:</b> flatten each object into a coordinate vector (a 2&times;2 matrix becomes a "
 "4-vector, a polynomial becomes its coefficient vector), stack them as the rows of a square matrix, and take the "
 "<b>determinant</b>. Non-zero &rArr; independent &rArr; basis / spans. Zero &rArr; dependent. "
 "For &ldquo;is <b>v</b> a linear combination of &hellip;&rdquo;, solve the system instead and show it is consistent.")

step(11,"Composition of matrix transformations","06","III","Q6a &mdash; all four papers",
 f"Determine the matrix for: reflection in the <i>x</i>-axis, then rotation through {pi}/2, then contraction of factor 1/3. "
 f"Find the image of {V(['4','1'])}. &nbsp;<span class='mut'>(the axis, angle, factor and point change every paper &mdash; the method does not)</span>",
 f"<b>Multiply RIGHT to LEFT:</b> &nbsp;<i>M</i> = <i>k</i> &middot; <i>R</i><sub>{th}</sub> &middot; <i>Ref</i>. &nbsp;"
 f"Reflection in <i>x</i>: {M([['1','0'],['0',sp+'1']])} &nbsp;&middot;&nbsp; in <i>y</i>: {M([[sp+'1','0'],['0','1']])} &nbsp;&middot;&nbsp; "
 f"rotation: {M([['cos&#952;',sp+'sin&#952;'],['sin&#952;','cos&#952;']])} &nbsp;&middot;&nbsp; dilation/contraction by <i>k</i>: multiply the whole matrix by <i>k</i>. "
 f"For {pi}/2 the rotation is {M([['0',sp+'1'],['1','0']])}. Then apply <i>M</i> to the point.")

step(12,"Kernel and range + verify rank&ndash;nullity","07","III","Q6c &mdash; all four papers",
 f"Determine the kernel and range of the transformation defined by &nbsp;<i>A</i> = {M([['1','2','3'],['0',sp+'1','1'],['1','1','4']])}, "
 f"and hence verify the rank&ndash;nullity theorem.",
 "<b>Method:</b> row-reduce <i>A</i>. The <b>pivot columns of the original <i>A</i></b> are a basis for the range; "
 "solving <i>Ax</i> = <b>0</b> gives a basis for the kernel. Here <b>rank = 2, nullity = 1</b>, and "
 "rank + nullity = 3 = number of columns. &nbsp;<b>Also be ready for the formula version</b> "
 "(e.g. <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>, <i>x</i>&minus;<i>y</i>, <i>y</i>)) &mdash; write its matrix first, then identical work.")

w('<div class="bar" style="background:#b8842a"><span>OVERTIME &mdash; only if the clock allows</span><span class="r">each row adds to the floor</span></div>')

step(13,"Transition matrix / change of basis","07","III","Q6b &mdash; same bases in Sep&nbsp;23 and Mar&nbsp;24",
 f"<i>B</i> = {{(1,&nbsp;2), (3,&nbsp;&minus;1)}}, &nbsp;<i>B</i>&prime; = {{(3,&nbsp;1), (5,&nbsp;2)}} of <i>R</i><sup>2</sup>. Find the transition matrix "
 f"from <i>B</i> to <i>B</i>&prime;; if [<i>u</i>]<sub><i>B</i></sub> = {V(['2','1'])}, find [<i>u</i>]<sub><i>B</i>&prime;</sub>.",
 "<b>Method:</b> put the <i>B</i>&prime; vectors as the columns of <i>Q</i> and the <i>B</i> vectors as the columns of <i>P</i>. "
 "The transition matrix is <b><i>Q</i><sup>&minus;1</sup><i>P</i></b>; then [<i>u</i>]<sub><i>B</i>&prime;</sub> = "
 "(<i>Q</i><sup>&minus;1</sup><i>P</i>)[<i>u</i>]<sub><i>B</i></sub>. One 2&times;2 inverse &mdash; "
 "<b>+6 to your worst-case score, the biggest single jump left.</b>", ot=True)

step(14,"Positive-definite check","05","V","Q10a &mdash; same matrix in Apr&nbsp;23 and Mar&nbsp;24",
 f"Is &nbsp;<i>A</i> = {M([['1',sp+'2','1'],[sp+'2','4',sp+'2'],['1',sp+'2','1']])} positive definite?",
 "<b>Method:</b> leading principal minors. Here they are <b>1, 0, 0</b> &mdash; so it is <b>NOT positive definite</b>; "
 "it is positive <i>semi</i>-definite (row 3 = row 1, eigenvalues 0, 0, 6). <b>Say that explicitly</b> &mdash; students "
 "who just write &ldquo;no&rdquo; lose marks. Pairs with step&nbsp;1 to close out Unit&nbsp;V's 5+5.", ot=True)

step(15,"Four fundamental subspaces","07","IV","<b>Q7 &mdash; always. Same matrix 3 of 4 papers.</b>",
 f"Find the dimension and basis for the four fundamental subspaces of &nbsp;<i>A</i> = {M([['1','2','0','1'],['0','1','1','0'],['1','2','0','1']])}",
 "<b>Row 3 = row 1</b>, so rank = 2 immediately. dim&nbsp;col(<i>A</i>) = dim&nbsp;row(<i>A</i>) = <b>2</b>; "
 "dim&nbsp;nul(<i>A</i>) = 4 &minus; 2 = <b>2</b>; dim&nbsp;nul(<i>A</i><sup>T</sup>) = 3 &minus; 2 = <b>1</b>. "
 "Row-reduce once and read off a basis for each. One of the cheapest 7 marks on the paper.", ot=True)

step(16,"Complete solution of <i>Ax</i> = <i>b</i> &nbsp;+&nbsp; Unit II definitions","06+02","IV, II","Q7a &nbsp;&middot;&nbsp; Q3a and Q4a",
 "<b>(a)</b> Complete solution of &nbsp;<i>x</i>+3<i>y</i>+3<i>z</i> = 1, &nbsp;2<i>x</i>+6<i>y</i>+9<i>z</i> = 5, &nbsp;&minus;<i>x</i>&minus;3<i>y</i>+3<i>z</i> = 5.<br>"
 "<b>(b)</b> Define the unit step function (+ graph) &nbsp;&bull;&nbsp; Define the Dirac-delta function (+ sketch).",
 "<b>(a)</b> Row-reduce the augmented matrix, take any particular solution <b><i>x</i><sub>p</sub></b>, add the null-space "
 "basis: write the answer as <b><i>x</i> = <i>x</i><sub>p</sub> + <i>c</i><sub>1</sub><b>n</b><sub>1</sub> + &hellip;</b> "
 "<b>(b)</b> <i>u</i>(<i>t</i>&minus;<i>a</i>) = 0 for <i>t</i> &lt; <i>a</i>, 1 for <i>t</i> &ge; <i>a</i> &mdash; draw the step. "
 "&delta;(<i>t</i>&minus;<i>a</i>) is the limit of a unit-area pulse, zero everywhere except <i>t</i> = <i>a</i>, with "
 f"{INT}&delta; = 1 &mdash; draw the spike arrow.", ot=True)

w("""<div class="foot"><b>How this order was built:</b> each of the 18 candidate topics was costed in minutes and
scored by how many marks it adds to the <i>worst</i> of the four past papers, respecting the fact that you can only
collect from one question per unit. The list is then greedy-ordered by worst-case marks per minute, so stopping at
any row leaves you with the best score reachable in the time spent. Running totals are computed, not estimated.
Full working: <i>coverage_audit.py</i> in the repo.</div>""")

doc="<!doctype html><html><head><meta charset='utf-8'><title>24CS31 3-Hour Hail Mary</title><style>"+CSS+"</style></head><body>"+"".join(H)+"</body></html>"
import io,os
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"24CS31_3Hour_HailMary.html")
io.open(out,"w",encoding="utf-8").write(doc); print("wrote",out)

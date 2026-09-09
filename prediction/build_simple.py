#!/usr/bin/env python3
def M(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat"><table>{b}</table></span>'
def V(c): return M([[x] for x in c])
def PW(rows):
    b="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<span class="mat pw"><table>{b}</table></span>'
def F(n,d): return f'<span class="f"><span class="n">{n}</span><span class="d">{d}</span></span>'
sp="&#8722;"; inf="&#8734;"; pi="&#960;"; th="&#952;"; sq="&#8730;"; INT="&#8747;"; ARR="&#8594;"
inv="<i>L</i><sup>&minus;1</sup>"

CSS="""
@page{size:A4;margin:11mm 12mm}
*{box-sizing:border-box}
body{font-family:"DejaVu Serif",Georgia,serif;font-size:10.2pt;line-height:1.5;color:#14161b;margin:0}
h1{font-size:20pt;margin:0 0 3px}
.sub{font-size:11pt;color:#4a5361;margin-bottom:8px}
.unit{background:#1d2433;color:#fff;padding:9px 14px;border-radius:4px;margin:0 0 12px;font-size:15pt;font-weight:700}
.answer{font-size:15pt;font-weight:700;color:#0d5c34;margin:0 0 4px}
.trigger{font-size:10.5pt;color:#4a5361;margin:0 0 16px}
.part{border-left:4px solid #0d7a45;padding:0 0 0 13px;margin:0 0 18px}
.part.skip{border-left-color:#c9ced6}
.ph{font-size:12pt;font-weight:700;margin:0 0 5px}
.ph .slot{display:inline-block;background:#0d7a45;color:#fff;border-radius:3px;padding:1px 8px;margin-right:8px;font-size:10.5pt}
.part.skip .ph{color:#8b929c}
.part.skip .ph .slot{background:#c9ced6;color:#fff}
.qtext{margin:0 0 7px}
.how{background:#f2f7f4;border-radius:4px;padding:8px 12px;margin:0}
.how b{color:#0d5c34}
.how ul{margin:3px 0 0 16px;padding:0}
.how li{margin:3px 0}
table.o{width:100%;border-collapse:collapse;font-size:11pt;margin:10px 0 0}
table.o th{background:#1d2433;color:#fff;text-align:left;padding:5px 9px;font-size:10pt}
table.o td{border-bottom:1px solid #d5dae1;padding:4.5px 9px}
table.o tr.hit td{background:#e8f3ec;font-weight:700}
.c{text-align:center}
.note{background:#fff8e8;border-left:4px solid #b8842a;padding:7px 12px;margin:9px 0;font-size:9.6pt;line-height:1.42}
.big{background:#f2faf5;border:2px solid #0d7a45;border-radius:5px;padding:8px 13px;margin:9px 0;font-size:10pt;line-height:1.42}
.big b{color:#0d5c34}
.mat{display:inline-block;vertical-align:middle;position:relative;padding:2px 7px;margin:0 2px}
.mat::before,.mat::after{content:"";position:absolute;top:0;bottom:0;width:4px;border:1.1px solid #14161b}
.mat::before{left:0;border-right:none}.mat::after{right:0;border-left:none}
.mat.pw::after{display:none}.mat.pw td{text-align:left;padding-right:9px!important}
.mat table{border-collapse:collapse}
.mat td{padding:0 4px!important;text-align:center;font-size:.9em;line-height:1.2;border:none!important;background:transparent!important}
.f{display:inline-block;vertical-align:-.45em;text-align:center;margin:0 3px}
.f .n{display:block;border-bottom:1.1px solid #14161b;padding:0 4px}
.f .d{display:block;padding:0 4px}
.brk{page-break-before:always}
.avoid{page-break-inside:avoid}
"""
H=[]; w=H.append

# ---------------- PAGE 1 ----------------
w(f"""<h1>24CS31 &mdash; 3 Hour Plan</h1>
<div class="sub">Do these twelve things, in this order. Nothing else.</div>

<table class="o">
<tr><th style="width:6%">#</th><th>Study this</th><th class="c" style="width:12%">Minutes</th>
<th class="c" style="width:12%">Clock</th><th class="c" style="width:14%">Marks so far</th></tr>""")
for i,(t,mn,ck,rt,hit) in enumerate([
 ("Unitary / Hermitian check","8","0:08","5",0),
 ("Prove <i>T</i> is linear + find images","12","0:20","12",0),
 ("Least-squares solution","20","0:40","22",0),
 ("<i>t<sup>n</sup></i>-multiplication proof","15","0:55","29",0),
 ("Heaviside piecewise + LT","20","1:15","36",0),
 (f"<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} {ARR} <i>L</i>{{cos&nbsp;{sq}<i>t</i>/{sq}<i>t</i>}}","12","1:27","40",0),
 ("The Unit I definition","5","1:32","42",0),
 ("Solve ODEs by Laplace","22","1:54","49",0),
 ("SVD","22","2:16","54 &nbsp;&#9989; you pass here",1),
 ("Orthogonal diagonalization","25","2:41","59",0),
 ("Span / basis / independence","12","2:53","64",0),
 ("Rotation-operator proof","12","3:05","65",0)],1):
    w(f'<tr class="{"hit" if hit else ""}"><td class="c"><b>{i}</b></td><td>{t}</td>'
      f'<td class="c">{mn}</td><td class="c">{ck}</td><td class="c">{rt}</td></tr>')
w("</table>")

w("""<div class="big avoid"><b>What &ldquo;marks so far&rdquo; means.</b><br>
If you stop studying at that row, that is what you score on the hardest of the four past papers.<br>
You need 50. You get there at step 9.</div>

<div class="note avoid"><b>If you run out of time, do these next, in this order:</b><br>
13. Positive-definite check &mdash; 8 min &mdash; makes Unit V a full 20<br>
14. Four fundamental subspaces &mdash; 15 min &mdash; adds 10 in Unit IV<br>
15. Complete solution of <i>Ax</i> = <i>b</i> &mdash; 15 min &mdash; makes Unit IV a full 20<br>
16. Composition of transformations &mdash; 12 min &mdash; backup for Unit III<br>
All four take you to <b>72</b>.</div>

<div class="note avoid"><b>Do not open these.</b> QR factorization &middot; convolution &middot; periodic functions &middot;
improper integrals &middot; Gram&ndash;Schmidt &middot; Markov &middot; quadratic forms &middot; PCA &middot;
diagonalize and find <i>A<sup>n</sup></i> &middot; orthogonal projection.<br>
They are long, and the numbers change every paper.</div>

<div class="big avoid"><b>In the exam.</b><br>
Read both questions in a unit. Tick the parts you can do. Answer the one with more ticks.<br>
Write every part you know. Never leave a unit blank.</div>""")

# ---------------- HELPER ----------------
def part(slot, marks, title, q, how, skip=False):
    w(f'<div class="part{" skip" if skip else ""} avoid"><div class="ph">'
      f'<span class="slot">{slot}</span>{title} &nbsp;<span style="font-weight:400;font-size:10.5pt">&mdash; {marks} marks</span></div>')
    if q: w(f'<div class="qtext">{q}</div>')
    if how: w(f'<div class="how">{how}</div>')
    w('</div>')

def unit(n, name, answer, trigger):
    w(f'<div class="brk"></div><div class="unit">UNIT {n} &mdash; {name}</div>')
    w(f'<div class="answer">{answer}</div><div class="trigger">{trigger}</div>')

# ---------------- UNIT I ----------------
unit("I","Laplace Transforms","Answer Q1 &nbsp;&rarr;&nbsp; you get 13 of 20",
 f"Look for the question with the <b><i>t<sup>n</sup></i> proof</b> in it. That is the one to answer.<br>"
 f"In every past paper, the sin&nbsp;{sq}<i>t</i> question is in the same one.")

part("Q1a","2","Definition",
 "&ldquo;Write the Laplace transform of a periodic function&rdquo; &nbsp;or&nbsp; &ldquo;Define the Laplace transform&rdquo;",
 f"<b>Just write the formula.</b><ul>"
 f"<li>Periodic, period <i>T</i>: &nbsp;{F('1','1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>')} "
 f"{INT}<sub>0</sub><sup><i>T</i></sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></li>"
 f"<li>Definition: &nbsp;<i>L</i>{{<i>f</i>}} = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></li></ul>")

part("Q1b","4",f"Show the cos&nbsp;{sq}<i>t</i> result",
 f"Given &nbsp;<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = "+F(f"{sq}{pi}","2<i>s</i><sup>3/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>,<br>"
 f"show &nbsp;<i>L</i>{{"+F(f"cos&nbsp;{sq}<i>t</i>",f"{sq}<i>t</i>")+"} = "+F(f"{sq}{pi}","<i>s</i><sup>1/2</sup>")+"<i>e</i><sup>&minus;1/4<i>s</i></sup>",
 "<b>Three lines.</b><ul>"
 f"<li>"+F("<i>d</i>","<i>dt</i>")+f"(sin&nbsp;{sq}<i>t</i>) = "+F(f"cos&nbsp;{sq}<i>t</i>",f"2{sq}<i>t</i>")+"</li>"
 "<li>So what you want is <b>2 &times; <i>L</i>{that derivative}</b></li>"
 "<li>Use <i>L</i>{<i>f</i>&prime;} = <i>sF</i>(<i>s</i>) &minus; <i>f</i>(0), and <i>f</i>(0) = 0</li></ul>")

part("Q1c","7","Prove the <i>t<sup>n</sup></i> rule",
 "Prove &nbsp;<i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup><i>n</i></sup> "+F("<i>d<sup>n</sup></i>","<i>ds<sup>n</sup></i>")+"{<i>F</i>(<i>s</i>)}",
 f"<b>Learn this as a script. It has been asked word-for-word in all four papers.</b><ul>"
 f"<li>Start: <i>F</i>(<i>s</i>) = {INT}<sub>0</sub><sup>{inf}</sup><i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i></li>"
 f"<li>Differentiate under the integral sign &rarr; <i>F</i>&prime;(<i>s</i>) = &minus;<i>L</i>{{<i>t f</i>(<i>t</i>)}}</li>"
 f"<li>Each further differentiation drops another (&minus;<i>t</i>)</li>"
 f"<li>Finish with <b>induction on <i>n</i></b>. State the base case <i>n</i> = 1.</li></ul>")

part("Q1d","7","Long evaluation &mdash; SKIP","", "Leave this one. You have 13 of 20 without it.", skip=True)

# ---------------- UNIT II ----------------
unit("II","Application of Laplace Transforms","Answer Q3 &nbsp;&rarr;&nbsp; you get 14 of 20",
 "Look for the question with the <b>piecewise function</b> in it (the one with <i>t</i><sup>2</sup>, 4<i>t</i>, 8).<br>"
 "In every past paper, an <b>ODE question</b> sits right next to it.")

part("Q3c","7","Piecewise function + Laplace transform",
 "Express &nbsp;<i>f</i>(<i>t</i>) = "+PW([["<i>t</i><sup>2</sup>,","0 &lt; <i>t</i> &lt; 2"],["4<i>t</i>,","2 &lt; <i>t</i> &lt; 4"],["8,","<i>t</i> &gt; 4"]])
 +"&nbsp; using the Heaviside function, then find its Laplace transform.",
 "<b>Three steps.</b><ul>"
 "<li><b>Stack the jumps:</b> &nbsp;<i>f</i> = <i>t</i><sup>2</sup> + (4<i>t</i>&minus;<i>t</i><sup>2</sup>)<i>u</i>(<i>t</i>&minus;2) + (8&minus;4<i>t</i>)<i>u</i>(<i>t</i>&minus;4)</li>"
 "<li><b>Rewrite each bracket</b> in terms of (<i>t</i>&minus;<i>a</i>) &rarr; you get 4 &minus; &tau;<sup>2</sup> &nbsp;and&nbsp; &minus;8 &minus; 4&tau;</li>"
 "<li><b>Apply second shifting:</b> &nbsp;<i>L</i>{<i>g</i>(<i>t</i>&minus;<i>a</i>)<i>u</i>(<i>t</i>&minus;<i>a</i>)} = <i>e</i><sup>&minus;<i>as</i></sup><i>G</i>(<i>s</i>)</li></ul>"
 "<b>Answer:</b> &nbsp;2/<i>s</i><sup>3</sup> + <i>e</i><sup>&minus;2<i>s</i></sup>(4/<i>s</i> &minus; 2/<i>s</i><sup>3</sup>) + <i>e</i><sup>&minus;4<i>s</i></sup>(&minus;8/<i>s</i> &minus; 4/<i>s</i><sup>2</sup>)")

part("Q3d","7","Solve an ODE by Laplace transforms",
 "It will be <b>one of these three</b>:<br>"
 "&bull;&nbsp; " + F("<i>dx</i>","<i>dt</i>") + " &minus; 2<i>y</i> = cos&nbsp;2<i>t</i> &nbsp;and&nbsp; "
 + F("<i>dy</i>","<i>dt</i>") + " + 2<i>x</i> = sin&nbsp;2<i>t</i>, &nbsp;<i>x</i>(0)=1, <i>y</i>(0)=0<br>"
 "&bull;&nbsp; <i>y</i>&Prime; + 4<i>y</i>&prime; + 3<i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup><br>"
 "&bull;&nbsp; A circuit: &nbsp;<i>L</i>" + F("<i>di</i>","<i>dt</i>") + " + <i>Ri</i> = <i>Ee</i><sup>&minus;<i>at</i></sup>",
 "<b>Same method for all three.</b><ul>"
 "<li>Transform every term. Use <i>L</i>{<i>y</i>&prime;} = <i>sY</i> &minus; <i>y</i>(0) &nbsp;and&nbsp; "
 "<i>L</i>{<i>y</i>&Prime;} = <i>s</i><sup>2</sup><i>Y</i> &minus; <i>sy</i>(0) &minus; <i>y</i>&prime;(0)</li>"
 "<li>Put the initial conditions in <b>at this step</b>. Then it is just algebra.</li>"
 "<li>One equation &rarr; solve for <i>Y</i>(<i>s</i>), invert by partial fractions.</li>"
 "<li>Two equations &rarr; solve them like simultaneous equations in <i>X</i>(<i>s</i>) and <i>Y</i>(<i>s</i>), then invert each.</li></ul>")

part("Q3a, Q3b","2 + 4","Definition and short inverse &mdash; SKIP unless you have spare time","",
 "These are overtime items 17 and 16. If you get them, Q3 becomes a full 20.", skip=True)

# ---------------- UNIT III ----------------
unit("III","Vector Space and Linear Transformation","Answer Q5 &nbsp;&rarr;&nbsp; you get all 20",
 "This is your best unit. No calculus anywhere.<br>"
 "Q5 has three parts and <b>you will have all three</b>.")

part("Q5a","6","Span / basis / independence",
 f"Is &nbsp;{{{M([['1','2'],['0','1']])}, {M([['3','4'],['1','1']])}, {M([['1','2'],['1','1']])}, {M([['0','2'],['1','2']])}}} "
 f"a basis of <i>M</i><sub>22</sub>?<br>"
 f"<span style='color:#6b7280'>Or: do {{(1,2,3), (&minus;1,&minus;1,0), (2,5,4)}} span <i>R</i><sup>3</sup>?</span>",
 "<b>One method works for every version.</b><ul>"
 "<li>Turn each object into a plain list of numbers. A 2&times;2 matrix becomes a list of 4.</li>"
 "<li>Stack those lists as the rows of a square matrix.</li>"
 "<li>Take the <b>determinant</b>.</li>"
 "<li>Not zero &rarr; independent &rarr; it is a basis / it spans. Zero &rarr; dependent.</li></ul>")

part("Q5b","7","Prove <i>T</i> is linear, then find images",
 f"<b>(a)</b> &nbsp;<i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, &nbsp;2<i>y</i>, &nbsp;<i>x</i>&minus;<i>y</i>). Find the images of (1,&nbsp;2) and (2,&nbsp;&minus;5).<br>"
 f"<b>(b)</b> &nbsp;<i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup>+<i>c</i>. Find the image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1.",
 "<b>To prove it is linear, show two things:</b><ul>"
 "<li><i>T</i>(<b>u</b> + <b>v</b>) = <i>T</i>(<b>u</b>) + <i>T</i>(<b>v</b>)</li>"
 "<li><i>T</i>(<i>k</i><b>u</b>) = <i>k T</i>(<b>u</b>)</li></ul>"
 "Then just substitute the vectors.<br>"
 "<b>Answers:</b> &nbsp;(5, 4, &minus;1) &nbsp;&middot;&nbsp; (1, &minus;10, 7) &nbsp;&middot;&nbsp; 11<i>x</i><sup>2</sup> + 1")

part("Q5c","7","Rotation proof",
 f"Show that <i>T</i>(<b>x</b>) = <i>A</i><b>x</b> rotates <b>x</b> through an angle {th} about the origin, where<br>"
 f"<i>A</i> = {M([['cos&#952;',sp+'sin&#952;'],['sin&#952;','cos&#952;']])}",
 f"<b>Bookwork. Twelve minutes. No calculus.</b><ul>"
 f"<li>Write <b>x</b> in polar form: &nbsp;<b>x</b> = (<i>r</i>&thinsp;cos&thinsp;&phi;, &nbsp;<i>r</i>&thinsp;sin&thinsp;&phi;)</li>"
 f"<li>Multiply out <i>A</i><b>x</b></li>"
 f"<li>Use the compound-angle formulae &rarr; you get (<i>r</i>&thinsp;cos({th}+&phi;), &nbsp;<i>r</i>&thinsp;sin({th}+&phi;))</li>"
 f"<li>Same length <i>r</i>, angle increased by {th}. That is a rotation. Done.</li></ul>")

# ---------------- UNIT IV ----------------
unit("IV","Orthogonal Projections","Answer Q8 &nbsp;&rarr;&nbsp; you get 10 of 20",
 "Your weakest unit, on purpose. You take one 10-mark part and move on.<br>"
 "<b>Do not attempt QR factorization</b> &mdash; it is long and the matrix changes every paper.")

part("Q8b","10","Least-squares solution",
 f"Find the least-squares solution of <i>AX</i> = <i>b</i>, where<br>"
 f"<i>A</i> = {M([['1','3','5'],['1','1','0'],['1','1','2'],['1','3','3']])} &nbsp;&nbsp;and&nbsp;&nbsp; <i>b</i> = {V(['3','5','7',sp+'3'])}",
 f"<b>The whole question is one equation:</b> &nbsp;<i>A</i><sup>T</sup><i>A</i>&#770;<i>x</i> = <i>A</i><sup>T</sup><i>b</i><ul>"
 f"<li><i>A</i><sup>T</sup><i>A</i> = {M([['4','8','10'],['8','20','26'],['10','26','38']])}</li>"
 f"<li><i>A</i><sup>T</sup><i>b</i> = {V(['12','12','20'])}</li>"
 f"<li>Solve it &rarr; <b>&#770;<i>x</i> = (10, &minus;6, 2)</b></li>"
 f"<li>Substitute back to check. Thirty seconds, and it confirms all 10 marks.</li></ul>"
 f"<b>This exact matrix and vector appeared twice, including in the most recent paper.</b>")

# ---------------- UNIT V ----------------
unit("V","Applications of Eigenvalue Decomposition","Answer Q10 &nbsp;&rarr;&nbsp; you get 15 of 20",
 "Look for the question with <b>&ldquo;orthogonally diagonalize&rdquo;</b> in it.<br>"
 "The best-value unit on the paper &mdash; the two 5-mark parts take two minutes each.")

part("Q10b","5","Unitary or Hermitian check",
 f"Is &nbsp;<i>A</i> = {M([['0','<i>i</i>'],[sp+'<i>i</i>','0']])} unitary?<br>"
 f"<span style='color:#6b7280'>Or: is &nbsp;{M([['3','7'+sp+'4<i>i</i>',sp+'2+5<i>i</i>'],['7+4<i>i</i>',sp+'2','3+<i>i</i>'],[sp+'2'+sp+'5<i>i</i>','3'+sp+'<i>i</i>','4']])} Hermitian?</span>",
 "<b>Two minutes.</b><ul>"
 "<li>Write <i>A</i><sup>*</sup> &mdash; transpose it, then flip the sign of every <i>i</i>.</li>"
 "<li><b>Hermitian</b> if <i>A</i><sup>*</sup> = <i>A</i></li>"
 "<li><b>Unitary</b> if <i>A</i><sup>*</sup><i>A</i> = <i>I</i></li>"
 "<li><b>Both of these say YES.</b> Show <i>A</i><sup>*</sup> written out in full.</li></ul>")

part("Q10c","10","Orthogonally diagonalize",
 f"Orthogonally diagonalize &nbsp;<i>A</i> = {M([['3',sp+'1','1'],[sp+'1','5',sp+'1'],['1',sp+'1','3']])}",
 f"<b>This exact matrix appeared in 3 of the 4 papers. You already know the answer &mdash; practise producing it.</b><ul>"
 f"<li>Eigenvalues: &nbsp;<b>2, 3, 6</b></li>"
 f"<li>Eigenvectors: &nbsp;{V(['1','0',sp+'1'])} &nbsp;{V(['1','1','1'])} &nbsp;{V(['1',sp+'2','1'])}</li>"
 f"<li>All three eigenvalues are different, so the eigenvectors are <b>already orthogonal</b> &mdash; "
 f"<b>no Gram&ndash;Schmidt needed.</b> Say this in your answer, it earns marks.</li>"
 f"<li>Divide them by {sq}2, {sq}3, {sq}6. Those are the columns of <i>P</i>.</li>"
 f"<li>Then <b><i>P</i><sup>T</sup><i>AP</i> = diag(2, 3, 6)</b></li>"
 f"<li>Show the three dot products are 0.</li></ul>")

part("Q9c","10","SVD &mdash; this is in the OTHER question",
 f"Find the SVD of &nbsp;<i>A</i> = {M([['1','1'],['3',sp+'3']])}",
 f"<b>No calculus &mdash; it is eigenvectors, twice.</b> Do it as insurance in case Q10 looks wrong.<ul>"
 f"<li><i>A</i><sup>T</sup><i>A</i> = {M([['10',sp+'8'],[sp+'8','10']])}</li>"
 f"<li>Eigenvalues <b>18</b> and <b>2</b> &rarr; singular values <b>3{sq}2</b> and <b>{sq}2</b></li>"
 f"<li>Its eigenvectors (1,&minus;1)/{sq}2 and (1,1)/{sq}2 are the columns of <b><i>V</i></b></li>"
 f"<li>Then <b><i>u<sub>i</sub></i> = <i>A v<sub>i</sub></i> / &sigma;<sub>i</sub></b> gives the columns of <b><i>U</i></b></li>"
 f"<li>Write <b><i>A</i> = <i>U</i>&Sigma;<i>V</i><sup>T</sup></b></li></ul>")

part("Q10a","5","Positive-definite check &mdash; overtime item 13",
 f"Is &nbsp;<i>A</i> = {M([['1',sp+'2','1'],[sp+'2','4',sp+'2'],['1',sp+'2','1']])} positive definite?",
 "<b>Eight minutes, and it makes this unit a full 20.</b><ul>"
 "<li>Work out the three leading minors: they are <b>1, 0, 0</b></li>"
 "<li>So the answer is <b>NO &mdash; it is not positive definite</b></li>"
 "<li>It is positive <b>semi</b>-definite. <b>Write that word</b> &mdash; just saying &ldquo;no&rdquo; loses marks.</li></ul>")

doc="<!doctype html><html><head><meta charset='utf-8'><title>24CS31 3 Hour Plan</title><style>"+CSS+"</style></head><body>"+"".join(H)+"</body></html>"
import io,os
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"24CS31_3Hour_Plan_SIMPLE.html")
io.open(out,"w",encoding="utf-8").write(doc); print("wrote",out)

#!/usr/bin/env python3
"""24CS31 SEE Prediction Sheet -> HTML (printed to PDF by headless Chromium)."""

def M(rows):
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<span class="mat"><table>{body}</table></span>'

def V(col):
    return M([[c] for c in col])

def F(n, d):
    return f'<span class="f"><span class="n">{n}</span><span class="d">{d}</span></span>'

sp = "&#8722;"   # minus
inf = "&#8734;"
pi = "&#960;"
th = "&#952;"
om = "&#969;"
sq = "&#8730;"
INT = "&#8747;"
ARR = "&#8594;"
LEQ = "&#8804;"
inv = "<i>L</i><sup>&minus;1</sup>"

# ============================== MATRICES ==============================
A_SUB   = M([["1","2","0","1"],["0","1","1","0"],["1","2","0","1"]])
A_LS    = M([["1","3","5"],["1","1","0"],["1","1","2"],["1","3","3"]])
B_LS    = V(["3","5","7",sp+"3"])
A_ORTH  = M([["3",sp+"1","1"],[sp+"1","5",sp+"1"],["1",sp+"1","3"]])
A_PD    = M([["1",sp+"2","1"],[sp+"2","4",sp+"2"],["1",sp+"2","1"]])
A_SVD   = M([["1","1"],["3",sp+"3"]])
A_HERM  = M([["3","7"+sp+"4<i>i</i>",sp+"2+5<i>i</i>"],
             ["7+4<i>i</i>",sp+"2","3+<i>i</i>"],
             [sp+"2"+sp+"5<i>i</i>","3"+sp+"<i>i</i>","4"]])
A_ROT   = M([["cos&#952;",sp+"sin&#952;"],["sin&#952;","cos&#952;"]])
A_QR24  = M([["3",sp+"5","1"],["1","1","1"],[sp+"1","5",sp+"2"],["3",sp+"7","8"]])
A_UNI   = M([["0","<i>i</i>"],[sp+"<i>i</i>","0"]])
A_MARK  = M([["0.95","0.03"],["0.05","0.97"]])
A_KER24 = M([["1","2","3"],["0",sp+"1","1"],["1","1","4"]])
U21     = V(["2","1"])
U41     = V(["4","1"])

# ============================== CSS ==============================
CSS = """
@page { size: A4; margin: 11mm 10mm 13mm 10mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 8.9pt; line-height: 1.38;
       color: #16181d; margin: 0; }
h1 { font-size: 21pt; margin: 0 0 2px; letter-spacing: -0.4px; font-weight: 700; }
h2 { font-size: 12.4pt; margin: 20px 0 7px; padding: 5px 9px; background: #1d2433; color: #fff;
     border-radius: 3px; font-weight: 700; letter-spacing: .2px; }
h3 { font-size: 10.2pt; margin: 13px 0 5px; color: #1d2433; border-bottom: 1.6px solid #1d2433;
     padding-bottom: 2px; font-weight: 700; }
h4 { font-size: 9.3pt; margin: 9px 0 3px; color: #2c3446; font-weight: 700; }
p  { margin: 4px 0; }
ul, ol { margin: 4px 0 4px 16px; padding: 0; }
li { margin: 1.5px 0; }
.small { font-size: 8pt; }
.muted { color: #5b6472; }
.cover { border: 2.4px solid #1d2433; border-radius: 5px; padding: 14px 16px; margin-bottom: 12px; }
.sub { font-size: 10.4pt; color: #3a4353; margin-top: 2px; }
.kv { font-size: 8.4pt; color: #444c59; margin-top: 8px; }

table.g { width: 100%; border-collapse: collapse; margin: 6px 0 9px; font-size: 8.15pt; }
table.g th { background: #29334a; color: #fff; text-align: left; padding: 4px 5px;
             font-weight: 700; border: .8px solid #29334a; font-size: 8pt; }
table.g td { border: .8px solid #b9c0cc; padding: 3.5px 5px; vertical-align: top; }
table.g tr:nth-child(even) td { background: #f4f6f9; }
td.c, th.c { text-align: center; }
.hit4 { background:#0d7a45 !important; color:#fff; font-weight:700; text-align:center; }
.hit3 { background:#3f8f5f !important; color:#fff; font-weight:700; text-align:center; }
.hit2 { background:#b8842a !important; color:#fff; font-weight:700; text-align:center; }
.hit1 { background:#a04545 !important; color:#fff; font-weight:700; text-align:center; }
.hit0 { background:#6b7280 !important; color:#fff; font-weight:700; text-align:center; }

.q { border: 1px solid #c2c9d4; border-left: 5px solid #29334a; border-radius: 3px;
     padding: 7px 9px; margin: 7px 0; background: #fbfcfd; }
.q.t1 { border-left-color: #0d7a45; }
.q.t2 { border-left-color: #b8842a; }
.q.t3 { border-left-color: #7a4fa3; }
.qh { font-weight: 700; font-size: 8.6pt; color: #1d2433; margin-bottom: 3px; }
.qh .id { display:inline-block; background:#1d2433; color:#fff; border-radius:2px;
          padding:0.5px 5px; margin-right:6px; font-size:7.9pt; }
.q.t1 .qh .id { background:#0d7a45; }
.q.t2 .qh .id { background:#b8842a; }
.q.t3 .qh .id { background:#7a4fa3; }
.qb { margin: 3px 0 5px; }
.meta { font-size: 7.7pt; color: #3d4654; background:#eef1f6; border-radius:2px;
        padding: 3px 6px; margin-top: 4px; }
.meta b { color:#1d2433; }
.tag { display:inline-block; border:1px solid #99a2b0; border-radius:9px; padding:0 6px;
       font-size:7.4pt; margin-right:4px; background:#fff; }

.law { border:1px solid #c2c9d4; border-radius:3px; padding:6px 9px; margin:6px 0; background:#fbfcfd; }
.law .lh { font-weight:700; color:#1d2433; font-size:8.7pt; }
.law .ev { font-size:7.7pt; color:#4a5361; margin-top:2px; font-family:"DejaVu Sans",sans-serif; }
.pill { display:inline-block; background:#0d7a45; color:#fff; border-radius:9px; padding:0 7px;
        font-size:7.5pt; font-weight:700; margin-left:5px; }
.pill.w { background:#b8842a; }
.pill.r { background:#a04545; }

.box { border:1.6px solid #1d2433; border-radius:4px; padding:9px 11px; margin:9px 0; background:#f7f9fb; }
.box.warn { border-color:#a04545; background:#fdf6f6; }
.box.go { border-color:#0d7a45; background:#f2faf5; }
.box h4 { margin-top:0; }

.mat { display:inline-block; vertical-align:middle; position:relative; padding:1.5px 7px; margin:0 2px; }
.mat::before, .mat::after { content:""; position:absolute; top:0; bottom:0; width:3.5px;
                            border:1.05px solid #16181d; }
.mat::before { left:0; border-right:none; }
.mat.pw::after { display:none; }
.mat.pw td { text-align:left; padding-right:9px; }
.mat::after  { right:0; border-left:none; }
.mat table { border-collapse:collapse; }
.mat td { padding:0 3.5px !important; text-align:center; font-size:0.9em; line-height:1.18;
           border:none !important; background:transparent !important; }
.f { display:inline-block; vertical-align:-0.48em; text-align:center; margin:0 2.5px; }
.f .n { display:block; border-bottom:1.05px solid #16181d; padding:0 3px; }
.f .d { display:block; padding:0 3px; }
i { font-style: italic; }
.brk { page-break-before: always; }
.avoid { page-break-inside: avoid; }
.foot { margin-top:14px; border-top:1px solid #b9c0cc; padding-top:5px; font-size:7.5pt; color:#5b6472; }
"""

H = []
def w(s): H.append(s)

# ============================== COVER ==============================
w(f"""
<div class="cover">
  <h1>24CS31 &mdash; SEE Prediction Sheet</h1>
  <div class="sub">Laplace Transforms &amp; Vector Space &middot; III Semester B.E. CSE &middot; Batch 2024</div>
  <div class="kv">
    <b>Built from:</b> 4 distinct previous question papers (Apr 2023, Jun 2023 Make-up,
    Aug/Sep 2023 Backlog, Mar 2024 SEE) &middot; every question transcribed and verified against the page image.<br>
    <b>Filtered against:</b> the official 24CS31 syllabus (Ramaiah Institute of Technology, curriculum AY 2025&ndash;26).<br>
    <b>Back-test:</b> the Tier&nbsp;1 + Tier&nbsp;2 list below scores <b>100 / 100</b> on all four papers when the
    recommended section is chosen. See &sect;9.
  </div>
</div>

<div class="box warn avoid">
<h4>Read this first &mdash; two honest caveats</h4>
<ol class="small" style="margin-bottom:0">
<li><b>Two of your five uploads are the same paper.</b> <code>SEE_25.pdf</code> and
<code>IS131_MATH_SEE_2024_1.pdf</code> are both the <b>SEMESTER END EXAMINATIONS &ndash; MARCH 2024</b> paper
(one is a clean digital copy, the other a scan). They are identical question-for-question. So the evidence base is
<b>4 papers, not 5</b> &mdash; and nothing here double-counts them.</li>
<li><b>Almost nothing in these papers is out of your syllabus.</b> You asked me to rule out off-syllabus material;
I checked all 4&nbsp;&times;&nbsp;10 questions against the 24CS31 unit list and only <b>one</b> item
(Markov steady-state, Mar 2024 Q9b) is not literally named in the syllabus text &mdash; and it still appeared under
your exact course title, so it stays in. The real gap runs the other way: <b>PCA and conic sections are in your
syllabus and have never been asked.</b> That is the actual risk, and it is handled in &sect;8.</li>
</ol>
</div>
""")

# ============================== §1 SYLLABUS ==============================
w("<h2>&sect;1 &nbsp; Your syllabus &mdash; the filter everything was judged against</h2>")
w("""
<table class="g">
<tr><th style="width:5%">Unit</th><th style="width:14%">Title</th><th>Content (official)</th><th style="width:9%" class="c">CO</th></tr>
<tr><td class="c"><b>I</b></td><td><b>Laplace Transforms</b></td>
<td>Definition; transforms of elementary functions; properties; existence conditions; transform of derivatives;
transform of integrals; multiplication by <i>t</i><sup>n</sup>; division by <i>t</i>; evaluation of integrals by
Laplace transforms; transform of a periodic function.</td><td class="c">CO1</td></tr>
<tr><td class="c"><b>II</b></td><td><b>Application of Laplace Transforms</b></td>
<td>Unit-step function; unit-impulse function; inverse transforms; convolution theorem; solution of linear
differential equations and simultaneous linear differential equations; engineering applications.</td><td class="c">CO2</td></tr>
<tr><td class="c"><b>III</b></td><td><b>Vector Space &amp; Linear Transformation</b></td>
<td>Vector space; linear combination and span; linearly independent / dependent vectors; basis and dimension;
linear transformations; matrix of transformations; rotation about the origin; dilation, contraction and reflection;
composition of matrix transformations; kernel and range; change of basis.</td><td class="c">CO3</td></tr>
<tr><td class="c"><b>IV</b></td><td><b>Orthogonal Projections</b></td>
<td>Null space of <i>A</i>; solving <i>Ax</i>=0 and <i>Rx</i>=0; complete solution to <i>Ax</i>=<i>b</i>;
dimensions of the four subspaces; orthogonality of the four subspaces; projections; orthonormal bases and
Gram&ndash;Schmidt; QR-factorization; least-squares approximations.</td><td class="c">CO4</td></tr>
<tr><td class="c"><b>V</b></td><td><b>Applications of Eigenvalue Decomposition</b></td>
<td>Eigenvalues and eigenvectors; similarity and diagonalization; symmetric matrices; complex matrices;
Hermitian and unitary matrices; positive definite matrices; SVD; <b>PCA</b>; applications to linear recurrence
relations; quadratic forms and <b>conic sections</b>.</td><td class="c">CO5</td></tr>
</table>

<h4>Syllabus verdict on the 40 questions analysed</h4>
<table class="g">
<tr><th style="width:22%">Verdict</th><th style="width:8%" class="c">Count</th><th>Detail</th></tr>
<tr><td><b>In syllabus</b></td><td class="c">39 / 40</td><td>Every Unit I&ndash;IV question and all but one Unit V question maps directly onto a named syllabus line.</td></tr>
<tr><td><b>Borderline &mdash; keep</b></td><td class="c">1 / 40</td><td>Markov steady-state (Mar 2024 Q9b, 5 m). Not named in the syllabus text, but it is an eigenvalue-decomposition application and it appeared under your exact course title. Cost to learn: ~15 minutes. Keep it.</td></tr>
<tr><td><b>Out of syllabus &mdash; drop</b></td><td class="c">0 / 40</td><td>Nothing. The 2023 papers ran under the older title &ldquo;Linear Algebra and Laplace Transforms&rdquo;, but their content sits inside your five units without remainder.</td></tr>
<tr><td><b>In syllabus, never asked</b></td><td class="c">&mdash;</td><td><b>PCA</b>; <b>conic sections</b>; existence conditions of the Laplace transform; a direct linear-recurrence (Fibonacci-style) question. These are your blind spots &mdash; see &sect;8.</td></tr>
</table>
""")

# ============================== §2 PATTERN ==============================
w("<h2>&sect;2 &nbsp; The SEE paper pattern &mdash; anatomy</h2>")
w("""
<p><b>Constant across all four papers:</b> Max marks <b>100</b> &middot; Duration <b>3 hours</b> &middot;
10 questions &middot; <b>&ldquo;Answer one full question from each unit.&rdquo;</b> There is no separate Part-A/Part-B,
no compulsory question, and no internal choice inside a question &mdash; the choice is at question level only.</p>

<table class="g">
<tr><th style="width:9%" class="c">Unit</th><th style="width:16%" class="c">Your choice</th>
<th class="c">Structure &mdash; Mar 2024 (current, CS/IS/AI/AD/CY/CI31)</th>
<th class="c">Structure &mdash; 2023 papers (older title)</th><th style="width:9%" class="c">Unit total</th></tr>
<tr><td class="c"><b>I</b></td><td class="c"><b>Q1 <i>or</i> Q2</b></td>
<td class="c">a (02) + b (04) + c (07) + d (07)</td><td class="c">a (06) + b (07) + c (07)</td><td class="c"><b>20</b></td></tr>
<tr><td class="c"><b>II</b></td><td class="c"><b>Q3 <i>or</i> Q4</b></td>
<td class="c">a (02) + b (04) + c (07) + d (07)</td><td class="c">a (06) + b (07) + c (07)</td><td class="c"><b>20</b></td></tr>
<tr><td class="c"><b>III</b></td><td class="c"><b>Q5 <i>or</i> Q6</b></td>
<td class="c">a (06) + b (07) + c (07)</td><td class="c">a (06) + b (07) + c (07)</td><td class="c"><b>20</b></td></tr>
<tr><td class="c"><b>IV</b></td><td class="c"><b>Q7 <i>or</i> Q8</b></td>
<td class="c"><b>Q7:</b> a (06)+b (07)+c (07) &nbsp;|&nbsp; <b>Q8:</b> a (10)+b (10)</td>
<td class="c">a (10) + b (10)</td><td class="c"><b>20</b></td></tr>
<tr><td class="c"><b>V</b></td><td class="c"><b>Q9 <i>or</i> Q10</b></td>
<td class="c">a (05) + b (05) + c (10)</td><td class="c">a (10) + b (10)</td><td class="c"><b>20</b></td></tr>
</table>

<div class="box go avoid">
<h4>The blueprint to plan against</h4>
<p style="margin-bottom:3px"><b>Use the March 2024 shape.</b> It is the only paper printed under your exact course
name (<i>Laplace Transforms and Vector Space</i>) and your exact course code family
(<i>CS/IS/AI/AD/CY/CI31</i>). The 2023 papers ran the older course. What changed in 2024:</p>
<ul class="small" style="margin-bottom:0">
<li>Units I and II gained a <b>2-mark definition</b> and a <b>4-mark short problem</b> &mdash; 6 nearly-free marks per unit, 12 across the paper.</li>
<li>Unit V split from 10+10 into <b>5 + 5 + 10</b> &mdash; two short property-checks plus one big decomposition.</li>
<li>Unit IV became <b>asymmetric</b>: Q7 is 6+7+7 (three smaller problems), Q8 is 10+10 (two heavy ones). Expect this to persist &mdash; it lets the examiner put QR and least-squares together in Q8.</li>
</ul>
</div>

<h4>Mark-weight per unit under the current blueprint</h4>
<table class="g">
<tr><th>Unit</th><th class="c">2 m</th><th class="c">4 m</th><th class="c">5 m</th><th class="c">6 m</th><th class="c">7 m</th><th class="c">10 m</th><th class="c">Total</th></tr>
<tr><td><b>I</b> &mdash; Laplace Transforms</td><td class="c">1</td><td class="c">1</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">2</td><td class="c">&ndash;</td><td class="c"><b>20</b></td></tr>
<tr><td><b>II</b> &mdash; Applications of LT</td><td class="c">1</td><td class="c">1</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">2</td><td class="c">&ndash;</td><td class="c"><b>20</b></td></tr>
<tr><td><b>III</b> &mdash; Vector Space</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">1</td><td class="c">2</td><td class="c">&ndash;</td><td class="c"><b>20</b></td></tr>
<tr><td><b>IV</b> &mdash; Orthogonal Projections</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">1*</td><td class="c">2*</td><td class="c">2*</td><td class="c"><b>20</b></td></tr>
<tr><td><b>V</b> &mdash; Eigenvalue Decomposition</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">2</td><td class="c">&ndash;</td><td class="c">&ndash;</td><td class="c">1</td><td class="c"><b>20</b></td></tr>
</table>
<p class="small muted">* Unit IV: Q7 gives 6+7+7, Q8 gives 10+10. You pick one shape.</p>
""")

# ============================== §3 FREQUENCY ==============================
w('<h2 class="brk">&sect;3 &nbsp; Frequency analysis &mdash; every topic, every paper</h2>')
w("""<p class="small"><b>A</b> = Apr 2023 &middot; <b>M</b> = Jun 2023 Make-up &middot; <b>S</b> = Aug/Sep 2023 Backlog &middot;
<b>N</b> = Mar 2024 SEE (newest, current syllabus). Cell shows the question slot it occupied.</p>""")

def freq_table(title, rows):
    w(f"<h3>{title}</h3>")
    w('<table class="g"><tr><th style="width:34%">Topic</th><th class="c" style="width:11%">A &middot; Apr&nbsp;23</th>'
      '<th class="c" style="width:11%">M &middot; Jun&nbsp;23</th><th class="c" style="width:11%">S &middot; Sep&nbsp;23</th>'
      '<th class="c" style="width:11%">N &middot; Mar&nbsp;24</th><th class="c" style="width:8%">Hits</th>'
      '<th class="c" style="width:14%">Verdict</th></tr>')
    for topic, a, m, s, n, verdict in rows:
        cnt = sum(1 for x in (a, m, s, n) if x != "&ndash;")
        w(f'<tr><td>{topic}</td><td class="c">{a}</td><td class="c">{m}</td><td class="c">{s}</td>'
          f'<td class="c">{n}</td><td class="hit{cnt}">{cnt}/4</td><td class="c small">{verdict}</td></tr>')
    w("</table>")

freq_table("Unit I &mdash; Laplace Transforms", [
 ("<b>Proof:</b> <i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup>n</sup> <i>d<sup>n</sup>F</i>/<i>ds<sup>n</sup></i>", "Q2b (7)","Q1b (7)","Q2c (7)","Q1c (7)","LOCK"),
 (f"<i>L</i>{{sin&nbsp;{sq}<i>t</i>}} / <i>L</i>{{cos&nbsp;{sq}<i>t</i> / {sq}<i>t</i>}}","Q2a (6)","Q1c (7)","Q2a (6)","Q1b (4)","LOCK"),
 ("Laplace transform of a <b>periodic function</b>","Q1c (7)","Q2c (7)","Q1b (7)","Q1a (2)<br>Q2d (7)","LOCK"),
 ("<b>Division by <i>t</i>:</b> evaluate <i>L</i>{<i>f</i>(<i>t</i>)/<i>t</i>}","Q1b (7)","Q1a, Q2b","Q1a (6)","Q2c (7)","LOCK"),
 ("<b>Multiplication by <i>t<sup>n</sup></i> / first shifting</b> &mdash; <i>L</i>{<i>t e<sup>at</sup></i> trig}","Q2c (7)","Q2a (6)","Q1a, Q2b","Q1d, Q2c","LOCK"),
 (f"Evaluate {INT}<sub>0</sub><sup>{inf}</sup> &hellip; <i>dt</i> using Laplace transforms","Q2c (7)","&ndash;","Q1c (7)","Q1d (7)","Very high"),
 (f"<b>Transform of an integral</b> <i>L</i>{{{INT}<sub>0</sub><sup>t</sup> &hellip;}}","Q1a (6)","Q2a (6)","&ndash;","&ndash;","Medium"),
 (f"<i>L</i>{{({sq}<i>t</i> &plusmn; 1/{sq}<i>t</i>)<sup>3</sup>}}","Q1a (6)","&ndash;","&ndash;","Q2b (4)","Medium"),
 (f"<b>Proof:</b> <i>L</i>{{<i>f</i>(<i>t</i>)/<i>t</i>}} = {INT}<sub>s</sub><sup>{inf}</sup><i>F</i>(<i>s</i>)<i>ds</i>","&ndash;","Q2b (7)","&ndash;","&ndash;","Low"),
 ("<b>Proof:</b> <i>L</i>{(sinh&nbsp;<i>at</i>)<i>f</i>(<i>t</i>)}","&ndash;","&ndash;","Q2b (7)","&ndash;","Low"),
 ("2-mark definition (LT / periodic function)","&ndash;","Q1a(i)","&ndash;","Q1a, Q2a","New format"),
])

freq_table("Unit II &mdash; Application of Laplace Transforms", [
 ("<b>Heaviside / unit-step</b> piecewise expression + LT","Q4b (7)","Q4b (7)","Q3b (7)","Q3c (7)","LOCK"),
 ("<b>Convolution theorem</b> (apply, verify, or state &amp; prove)","Q3b (7)","Q3b (7)","Q3a, Q4c","Q4c (7)","LOCK"),
 ("<b>Simultaneous ODEs</b> by LT (incl. particle-on-curve)","Q3c (7)","Q4c (7)","Q3c (7)","Q4d (7)","LOCK"),
 ("<b>Solve a single ODE</b> by Laplace transforms","Q4c (7)","Q3c (7)","Q4b (7)","&ndash;","Very high"),
 (f"<b>Inverse LT of log(&hellip;)</b>","Q4a (6)","&ndash;","Q4a (6)","Q3b (4)","Very high"),
 ("Inverse LT &mdash; partial fractions / shifting / tan<sup>&minus;1</sup>","Q3a (6)","Q3a, Q4a","&ndash;","Q4b (4)","Very high"),
 ("2-mark definition (unit step / Dirac delta)","&ndash;","&ndash;","&ndash;","Q3a, Q4a","New format"),
 ("<b>Engineering application</b> (LR circuit current)","&ndash;","&ndash;","&ndash;","Q3d (7)","New &mdash; watch"),
])

freq_table("Unit III &mdash; Vector Space and Linear Transformation", [
 ("<b>Composition</b> reflection &rarr; rotation &rarr; dilation/contraction, + image of a point","Q5a (6)","Q6c (7)","Q6a (6)","Q6a (6)","LOCK"),
 ("<b>Transition matrix</b> / change of basis","Q5c (7)","Q5c (7)","Q6c (7)","Q6b (7)","LOCK"),
 ("<b>Kernel &amp; range</b> + verify rank&ndash;nullity","Q6c (7)","Q6b (7)","Q5c (7)","Q6c (7)","LOCK"),
 ("<b>Prove <i>T</i> is linear</b> + find images","Q5b (7)","Q5b (7)","Q5b (7)","Q5b (7)","LOCK"),
 ("Linear combination / span / LI&ndash;LD / basis of a space","Q6a (6)","Q5a, Q6a","Q5a (6)","Q5a (6)","LOCK"),
 ("<b>Proof:</b> <i>T</i>(<i>x</i>) = <i>Ax</i> rotates <i>x</i> through &theta;","Q6b (7)","&ndash;","&ndash;","Q5c (7)","Medium"),
])

freq_table("Unit IV &mdash; Orthogonal Projections", [
 ("<b>QR factorization</b>","Q8b (10)","Q8a (10)","Q7a (10)","Q8a (10)","LOCK"),
 ("<b>Least-squares solution</b> of <i>Ax</i> = <i>b</i>","Q7b (10)","Q8b (10)","Q8b (10)","Q8b (10)","LOCK"),
 ("<b>Four fundamental subspaces</b> / basis of col(<i>A</i>) &amp; nul(<i>A</i>)","Q7a (10)","Q7a (10)","Q7b (10)","Q7c (7)","LOCK"),
 ("<b>Complete solution</b> to <i>Ax</i> = <i>b</i>","Q8a (10)","Q7b (10)","&ndash;","Q7a (6)","Very high"),
 ("<b>Gram&ndash;Schmidt</b> orthonormal basis","&ndash;","&ndash;","Q8a (10)","&ndash;","Live risk"),
 ("<b>Orthogonal projection</b> of <i>y</i> onto <i>u</i>","&ndash;","&ndash;","&ndash;","Q7b (7)","New &mdash; watch"),
])

freq_table("Unit V &mdash; Applications of Eigenvalue Decomposition", [
 ("<b>Orthogonally diagonalize</b> a symmetric matrix","Q10a (10)","Q9a (10)","Q10a (10)","Q10c (10)","LOCK"),
 ("<b>Singular Value Decomposition (SVD)</b>","Q10b (10)","Q10b (10)","Q9b (10)","Q9c (10)","LOCK"),
 ("<b>Positive definite</b> check","Q9b(ii)","Q9b(ii)","Q10b(ii)","Q10a (5)","LOCK"),
 ("<b>Hermitian</b> matrix check","Q9b(i)","Q9b(i)","Q10b(i)","&ndash;","Very high"),
 ("<b>Diagonalize</b> and hence find <i>A<sup>n</sup></i>","Q9a (10)","Q10a(i)","Q9a (10)","&ndash;","Very high"),
 ("<b>Unitary</b> matrix check","&ndash;","Q10a(ii)","&ndash;","Q10b (5)","Medium"),
 ("<b>Quadratic form</b> &rarr; no cross-product terms / definiteness","&ndash;","&ndash;","Q10b(ii)","Q9a (5)","Medium"),
 ("<b>Markov</b> steady-state vector","&ndash;","&ndash;","&ndash;","Q9b (5)","New &mdash; watch"),
 ("<b>PCA</b> &mdash; <i>in syllabus, never asked</i>","&ndash;","&ndash;","&ndash;","&ndash;","BLIND SPOT"),
 ("<b>Conic sections</b> &mdash; <i>in syllabus, never asked</i>","&ndash;","&ndash;","&ndash;","&ndash;","BLIND SPOT"),
])

# ============================== §4 CO-OCCURRENCE ==============================
w('<h2 class="brk">&sect;4 &nbsp; Section-pairing laws &mdash; which questions travel together</h2>')
w("""<p>This is the part that decides <b>which of the two questions you attempt</b>. Each unit offers two
questions and you answer one whole question &mdash; so what matters is not just <i>which topics appear</i>, but
<i>which topics land in the same question</i>. These laws were extracted by cross-tabulating all 40 questions.</p>""")

LAWS = [
 ("LAW 1", "Unit I", "4/4",
  "The <b><i>t<sup>n</sup></i>-multiplication proof</b> and the <b>sin&nbsp;&radic;<i>t</i> / cos&nbsp;&radic;<i>t</i></b> question are <u>always in the same question</u>.",
  "Apr&nbsp;23: Q2a + Q2b &nbsp;&bull;&nbsp; Jun&nbsp;23: Q1b + Q1c &nbsp;&bull;&nbsp; Sep&nbsp;23: Q2a + Q2c &nbsp;&bull;&nbsp; Mar&nbsp;24: Q1b + Q1c",
  "That is <b>11 marks (7+4)</b> sitting in one question. Find that question in the hall &mdash; it is your Unit&nbsp;I answer.", "go"),
 ("LAW 2", "Unit I", "4/4",
  "The full <b>periodic-function problem</b> is <u>always in the opposite question</u> to the pair in Law&nbsp;1.",
  "Apr&nbsp;23: periodic Q1c &harr; pair Q2 &nbsp;&bull;&nbsp; Jun&nbsp;23: Q2c &harr; Q1 &nbsp;&bull;&nbsp; Sep&nbsp;23: Q1b &harr; Q2 &nbsp;&bull;&nbsp; Mar&nbsp;24: Q2d &harr; Q1",
  "You cannot get both. Prepare both anyway &mdash; the periodic one is 7 marks of pure formula.", "go"),
 ("LAW 3", "Unit II", "4/4",
  "The <b>Heaviside piecewise question</b> and an <b>ODE-type problem</b> (single ODE, simultaneous ODEs, or the circuit application) are <u>always in the same question</u>.",
  "Apr&nbsp;23: Q4b + Q4c &nbsp;&bull;&nbsp; Jun&nbsp;23: Q4b + Q4c &nbsp;&bull;&nbsp; Sep&nbsp;23: Q3b + Q3c &nbsp;&bull;&nbsp; Mar&nbsp;24: Q3c + Q3d",
  "<b>14 guaranteed marks (7+7)</b> in one question. This is the single most valuable pairing on the paper.", "go"),
 ("LAW 4", "Unit II", "3/4",
  "The <b>convolution</b> question sits in the <u>opposite</u> question to the Heaviside one.",
  "Apr&nbsp;23 &check; &nbsp;&bull;&nbsp; Jun&nbsp;23 &check; &nbsp;&bull;&nbsp; Sep&nbsp;23 &#10007; (Sep 23 put convolution in both) &nbsp;&bull;&nbsp; Mar&nbsp;24 &check;",
  "So you will almost certainly have to choose between Heaviside+ODE and convolution. Take Heaviside+ODE (Law&nbsp;3).", "w"),
 ("LAW 5", "Unit III", "3/4",
  "The <b>vector-space pair</b> &mdash; {linear combination / span / LI&ndash;LD / basis} and {prove <i>T</i> is linear + find images} &mdash; sit together in <b>Q5</b>.",
  "Jun&nbsp;23: Q5a + Q5b &nbsp;&bull;&nbsp; Sep&nbsp;23: Q5a + Q5b &nbsp;&bull;&nbsp; Mar&nbsp;24: Q5a + Q5b &nbsp;&bull;&nbsp; Apr&nbsp;23 &#10007;",
  "Q5 is the &ldquo;definitions and proofs&rdquo; question. Easier if you are shaky on computation.", "w"),
 ("LAW 6", "Unit III", "3/4",
  "The <b>composition-of-transformations</b> question and the <b>transition-matrix</b> question sit together &mdash; and in the two newest papers the <b>kernel&amp;range</b> question joins them.",
  "Apr&nbsp;23: Q5a + Q5c &nbsp;&bull;&nbsp; Sep&nbsp;23: Q6a + Q6c &nbsp;&bull;&nbsp; Mar&nbsp;24: <b>Q6a + Q6b + Q6c</b> (all three) &nbsp;&bull;&nbsp; Jun&nbsp;23 &#10007;",
  "Mar&nbsp;24&rsquo;s Q6 is three LOCK topics in one 20-mark question. <b>Target the question containing the composition problem.</b>", "go"),
 ("LAW 7", "Unit IV", "4/4",
  "The <b>four-subspaces / column-space &amp; null-space</b> question is <u>always in Q7</u> &mdash; the first question of Unit&nbsp;IV.",
  "Apr&nbsp;23: Q7a &nbsp;&bull;&nbsp; Jun&nbsp;23: Q7a &nbsp;&bull;&nbsp; Sep&nbsp;23: Q7b &nbsp;&bull;&nbsp; Mar&nbsp;24: Q7c",
  "Perfectly consistent across four papers. If you want the four-subspaces marks, you must answer <b>Q7</b>.", "go"),
 ("LAW 8", "Unit IV", "2/4 &mdash; but both newest",
  "<b>QR factorization + least-squares</b> sit together in <b>Q8</b>.",
  "Jun&nbsp;23: Q8a + Q8b &nbsp;&bull;&nbsp; Mar&nbsp;24: Q8a + Q8b &nbsp;&bull;&nbsp; Apr&nbsp;23 &#10007; &nbsp;&bull;&nbsp; Sep&nbsp;23 &#10007;",
  "<b>20 marks from two LOCK topics in one question.</b> The most recent paper does exactly this. This is your Unit&nbsp;IV target &mdash; but see the decision card in &sect;7.", "go"),
 ("LAW 9", "Unit V", "3/4",
  "<b>Orthogonal diagonalization</b> and <b>SVD</b> are in <u>opposite</u> questions.",
  "Jun&nbsp;23 &check; &nbsp;&bull;&nbsp; Sep&nbsp;23 &check; &nbsp;&bull;&nbsp; Mar&nbsp;24 &check; &nbsp;&bull;&nbsp; Apr&nbsp;23 &#10007; (both in Q10)",
  "You get one 10-mark decomposition, not both. Prepare both &mdash; they share the <i>A</i><sup>T</sup><i>A</i> machinery.", "w"),
 ("LAW 10", "Unit V", "4/4",
  "The <b>matrix-property checks</b> (Hermitian / positive-definite / unitary) always travel <u>together as a block</u> &mdash; either as (i)/(ii) of one 10-marker or as the 5+5 pair.",
  "Apr&nbsp;23: Q9b(i)+(ii) &nbsp;&bull;&nbsp; Jun&nbsp;23: Q9b(i)+(ii) &nbsp;&bull;&nbsp; Sep&nbsp;23: Q10b(i)+(ii) &nbsp;&bull;&nbsp; Mar&nbsp;24: Q10a + Q10b",
  "<b>10 marks of 10-minute work.</b> Two definition-checks, no heavy algebra. Never skip these.", "go"),
 ("LAW 11", "Unit V", "3/4",
  "<b>Orthogonal diagonalization travels with the property-check block.</b>",
  "Jun&nbsp;23: Q9a + Q9b &nbsp;&bull;&nbsp; Sep&nbsp;23: Q10a + Q10b &nbsp;&bull;&nbsp; Mar&nbsp;24: Q10a + Q10b + Q10c &nbsp;&bull;&nbsp; Apr&nbsp;23 &#10007;",
  "Combined with Law&nbsp;10 this gives the Unit&nbsp;V target: <b>the question containing orthogonal diagonalization is a full 20.</b>", "go"),
 ("LAW 12", "Unit V", "3/4",
  "<b>SVD travels with</b> either &ldquo;diagonalize and find <i>A<sup>n</sup></i>&rdquo; or the short quadratic-form / Markov questions.",
  "Jun&nbsp;23: Q10a + Q10b &nbsp;&bull;&nbsp; Sep&nbsp;23: Q9a + Q9b &nbsp;&bull;&nbsp; Mar&nbsp;24: Q9a + Q9b + Q9c &nbsp;&bull;&nbsp; Apr&nbsp;23 &#10007;",
  "Your fallback question if the orthogonal-diagonalization matrix looks unfamiliar.", "w"),
]
for tag, unit, strength, claim, ev, why, tone in LAWS:
    pc = {"go":"pill","w":"pill w","r":"pill r"}[tone]
    w(f"""<div class="law avoid"><div class="lh">{tag} &mdash; {unit}
    <span class="{pc}">{strength}</span></div>
    <div style="margin-top:2px">{claim}</div>
    <div class="ev">Evidence &mdash; {ev}</div>
    <div class="ev" style="color:#1d2433"><b>So what:</b> {why}</div></div>""")


# ============================== QUESTION CARD HELPER ==============================
def card(tier, idx, title, body, unit, marks, section, partner, freq, note=""):
    cls = {"1":"t1","2":"t2","3":"t3"}[tier]
    w(f"""<div class="q {cls} avoid">
      <div class="qh"><span class="id">{idx}</span>{title}</div>
      <div class="qb">{body}</div>
      <div class="meta"><b>Unit:</b> {unit} &nbsp;|&nbsp; <b>Marks:</b> {marks} &nbsp;|&nbsp;
      <b>Section:</b> {section} &nbsp;|&nbsp; <b>Appears alongside:</b> {partner} &nbsp;|&nbsp;
      <b>History:</b> {freq}{(' &nbsp;|&nbsp; <b>Note:</b> ' + note) if note else ''}</div>
    </div>""")

# ============================== §5 TIER 1 ==============================
w('<h2 class="brk">&sect;5 &nbsp; TIER 1 &mdash; repeating with the SAME VALUES</h2>')
w("""<div class="box go">
<p style="margin:0"><b>What qualifies:</b> the question has already been set <b>two or more times with numerically
identical data</b>, and in most cases the most recent appearance is the March 2024 paper. These are not
&ldquo;topics&rdquo; &mdash; they are specific problems with specific matrices and specific functions. Work each one
end-to-end until you can reproduce it from memory. <b>Marks covered by this tier alone: 63 of 100.</b></p></div>""")

card("1","T1-01","Orthogonally diagonalize the symmetric matrix",
  f"Orthogonally diagonalize &nbsp; <i>A</i> = {A_ORTH}",
  "V &mdash; symmetric matrices","10",
  "Q9 or Q10 &mdash; the <b>c</b> part (10 m). Was <b>Q10c</b> in Mar&nbsp;24, <b>Q9a</b> in Jun&nbsp;23, <b>Q10a</b> in Apr&nbsp;23.",
  "the positive-definite check and the Hermitian/unitary check (Laws&nbsp;10&nbsp;&amp;&nbsp;11) &mdash; that whole question is a clean 20",
  "3 of 4 papers, identical matrix every time",
  "eigenvalues are <b>2, 3 and 6</b> &mdash; all distinct, so the eigenvectors come out mutually orthogonal on their own. Just normalise them to build <i>P</i>, then <i>P</i><sup>T</sup><i>AP</i> = <i>D</i>")

card("1","T1-02","Least-squares solution of <i>Ax</i> = <i>b</i>",
  f"Find the least-squares solution of <i>AX</i> = <i>b</i> for &nbsp; <i>A</i> = {A_LS} &nbsp; and &nbsp; <i>b</i> = {B_LS}",
  "IV &mdash; least-squares approximations","10",
  "<b>Q8b</b> &mdash; it was Q8b in Mar&nbsp;24 and Q8b in Jun&nbsp;23.",
  "the QR factorization (Law&nbsp;8) &mdash; together they are the full 20 of Q8",
  "2 of 4 papers with identical <i>A</i> and <i>b</i>; the same <i>A</i> was also the QR matrix in Apr&nbsp;23",
  "this matrix is the examiner&rsquo;s favourite &mdash; it has appeared three times in four papers in some role")

card("1","T1-03","Four fundamental subspaces &mdash; dimension and basis",
  f"Find the dimension and basis for the four fundamental subspaces of &nbsp; <i>A</i> = {A_SUB}"
  f"<div class='small muted' style='margin-top:3px'>Phrased in Jun&nbsp;23 as &ldquo;find a basis for col(<i>A</i>) and nul(<i>A</i>)&rdquo; &mdash; same matrix, same work.</div>",
  "IV &mdash; dimensions of the four subspaces","7 (was 10 in the 2023 papers)",
  "<b>Q7</b> &mdash; always. Q7a in Apr&nbsp;23, Q7a in Jun&nbsp;23, Q7b in Sep&nbsp;23, Q7c in Mar&nbsp;24 (Law&nbsp;7).",
  "the complete solution of <i>Ax</i> = <i>b</i> and the orthogonal projection (that is the whole of Mar&nbsp;24 Q7)",
  "3 of 4 papers, identical matrix",
  "row 3 = row 1, so rank = 2; dim of nul = 2, dim of left-nul = 1")

card("1","T1-04","Proof &mdash; multiplication by <i>t<sup>n</sup></i>",
  "If <i>L</i>{<i>f</i>(<i>t</i>)} = <i>F</i>(<i>s</i>), prove that "
  "<i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup>n</sup> "
  + F("<i>d<sup>n</sup></i>", "<i>ds<sup>n</sup></i>") +
  " {<i>F</i>(<i>s</i>)}, &nbsp;where <i>n</i> is a positive integer.",
  "I &mdash; multiplication by <i>t<sup>n</sup></i>","7",
  "Q1 or Q2, the <b>c</b> part in the new format. Q1c in Mar&nbsp;24, Q1b in Jun&nbsp;23, Q2b in Apr&nbsp;23, Q2c in Sep&nbsp;23.",
  f"the sin&nbsp;{sq}<i>t</i> / cos&nbsp;{sq}<i>t</i> question &mdash; <b>always</b> (Law&nbsp;1)",
  "4 of 4 papers, word-for-word identical",
  "the single most reliable question on the entire paper &mdash; proof by induction on <i>n</i>")

card("1","T1-05","Positive-definiteness check",
  f"Check whether the following matrix is positive definite or not: &nbsp; <i>A</i> = {A_PD}",
  "V &mdash; positive definite matrices","5 (was part of a 10 in 2023)",
  "<b>Q10a</b> in Mar&nbsp;24; was Q9b(ii) in Apr&nbsp;23.",
  "the Hermitian or unitary check &mdash; the property-check block never splits (Law&nbsp;10)",
  "2 of 4 papers with this exact matrix; the <i>topic</i> is 4 of 4",
  "leading minors are 1, 0, 0 &mdash; it is <b>positive semi-definite, not positive definite</b>. Say so explicitly")

card("1","T1-06","Singular Value Decomposition",
  f"Find the singular value decomposition (SVD) of &nbsp; <i>A</i> = {A_SVD}",
  "V &mdash; SVD","10",
  "the <b>c</b> part of Q9 or Q10. Q9c in Mar&nbsp;24, Q10b in Jun&nbsp;23.",
  "the quadratic form and Markov questions (Mar&nbsp;24 Q9) or the diagonalize-and-find-<i>A<sup>n</sup></i> question (Jun&nbsp;23 Q10)",
  "2 of 4 papers with this exact matrix; the <i>topic</i> is 4 of 4",
  f"<i>A</i><sup>T</sup><i>A</i> = {M([['10', sp+'8'],[sp+'8','10']])} with eigenvalues 18 and 2, so the singular values are 3{sq}2 and {sq}2")

card("1","T1-07","Transition matrix / change of basis",
  f"Consider the bases <i>B</i> = {{(1,&nbsp;2), (3,&nbsp;&minus;1)}} and <i>B</i>&prime; = {{(3,&nbsp;1), (5,&nbsp;2)}} of <i>R</i><sup>2</sup>. "
  f"Find the transition matrix from <i>B</i> to <i>B</i>&prime;. If <i>u</i> is a vector such that "
  f"[<i>u</i>]<sub><i>B</i></sub> = {U21}, find [<i>u</i>]<sub><i>B</i>&prime;</sub>.",
  "III &mdash; change of basis","7",
  "<b>Q6b</b> in Mar&nbsp;24; <b>Q6c</b> in Sep&nbsp;23. (Apr&nbsp;23 and Jun&nbsp;23 used Q5c with the standard basis as <i>B</i>&prime;.)",
  "the composition-of-transformations question and the kernel&amp;range question &mdash; the three-LOCK Q6 block (Law&nbsp;6)",
  "2 of 4 papers with these exact bases and this exact <i>u</i>; the <i>topic</i> is 4 of 4",
  "back-to-back in the two most recent papers &mdash; strongest same-values signal in Unit III")

card("1","T1-08","Heaviside representation + Laplace transform",
  "Express the function &nbsp;<i>f</i>(<i>t</i>) = "
  + M([["<i>t</i><sup>2</sup>,","0 &lt; <i>t</i> &lt; 2,"],
       ["4<i>t</i>,","2 &lt; <i>t</i> &lt; 4,"],
       ["8,","<i>t</i> &gt; 4."]]).replace('class="mat"','class="mat pw"')
  + " in terms of the Heaviside function and hence find its Laplace transform.",
  "II &mdash; unit-step function","7",
  "<b>Q3c</b> in Mar&nbsp;24; <b>Q4b</b> in Apr&nbsp;23.",
  "an ODE-type problem &mdash; single ODE, simultaneous ODEs, or the circuit application (Law&nbsp;3). <b>14 marks in one question.</b>",
  "2 of 4 papers with this exact piecewise function; the <i>topic</i> is 4 of 4",
  "the other two papers used cos&nbsp;<i>t</i>/cos&nbsp;2<i>t</i>/cos&nbsp;3<i>t</i> and 1/<i>t</i>/<i>t</i><sup>2</sup> &mdash; same method")

card("1","T1-09","Inverse Laplace transform of a logarithm",
  "Evaluate &nbsp; " + "L<sup>&minus;1</sup>" + " { log " + F("<i>s</i><sup>2</sup> + 1", "<i>s</i>(<i>s</i> + 1)") + " }",
  "II &mdash; inverse transforms","4 (was 6 in the 2023 papers)",
  "<b>Q3b</b> in Mar&nbsp;24; <b>Q4a</b> in Apr&nbsp;23.",
  "the Heaviside question (Mar&nbsp;24 Q3) &mdash; so it sits in the <i>same</i> question as your 14-mark Law&nbsp;3 pair",
  "2 of 4 papers with this exact expression; a log-inverse appeared in 3 of 4",
  "differentiate <i>F</i>(<i>s</i>), then use <i>L</i><sup>&minus;1</sup>{<i>F</i>&prime;(<i>s</i>)} = &minus;<i>t f</i>(<i>t</i>)")

card("1","T1-10","Proof &mdash; the rotation operator",
  f"Show that a linear operator <i>T</i>&nbsp;:&nbsp;<i>R</i><sup>2</sup> {ARR} <i>R</i><sup>2</sup> defined by "
  f"<i>T</i>(<i>x</i>) = <i>Ax</i> rotates a vector <i>x</i> through an angle {th} about the origin if "
  f"<i>A</i> = {A_ROT}",
  "III &mdash; rotation about the origin","7",
  "<b>Q5c</b> in Mar&nbsp;24; <b>Q6b</b> in Apr&nbsp;23.",
  "the &ldquo;prove <i>T</i> is linear&rdquo; question and the vector-space basis question &mdash; the Q5 proof block (Law&nbsp;5)",
  "2 of 4 papers, identical statement",
  "your escape hatch if the Q6 computational block looks ugly &mdash; it is a bookwork proof")

card("1","T1-11","Convolution theorem &mdash; the standard inverse",
  "Find &nbsp; L<sup>&minus;1</sup> { " + F("<i>s</i><sup>2</sup>", "(<i>s</i><sup>2</sup> + <i>a</i><sup>2</sup>)(<i>s</i><sup>2</sup> + <i>b</i><sup>2</sup>)") + " } &nbsp; using the convolution theorem.",
  "II &mdash; convolution theorem","7",
  "<b>Q3b</b> in both Apr&nbsp;23 and Jun&nbsp;23. Mar&nbsp;24 instead asked you to <i>verify</i> the theorem for <i>f</i><sub>1</sub> = <i>t</i>, <i>f</i><sub>2</sub> = cos&nbsp;<i>t</i> at Q4c.",
  "the opposite question to Heaviside (Law&nbsp;4) &mdash; usually with a plain inverse-LT part and an ODE",
  "2 of 4 identical; the <i>topic</i> is 4 of 4",
  f"Sep&nbsp;23 set the same thing with <i>a</i>=1, <i>b</i>=2. Learn the general form and both specialisations")

card("1","T1-12","Hermitian matrix check",
  f"Determine whether the matrix &nbsp; <i>A</i> = {A_HERM} &nbsp; is Hermitian.",
  "V &mdash; complex / Hermitian matrices","5 (was half of a 10 in 2023)",
  "the property-check block &mdash; Q9b(i) in Apr&nbsp;23, Q10b(i) in Sep&nbsp;23.",
  "the positive-definite check &mdash; they are the (i) and (ii) of the same part (Law&nbsp;10)",
  "2 of 4 papers with this exact matrix; the <i>topic</i> is 3 of 4",
  "it <b>is</b> Hermitian &mdash; the diagonal is real and every <i>a<sub>ij</sub></i> equals the conjugate of <i>a<sub>ji</sub></i>. Write out <i>A</i><sup>*</sup> in full and compare entry by entry")

card("1","T1-13",f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show the cos&nbsp;{sq}<i>t</i> result",
  f"Given &nbsp; <i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = " + F(f"{sq}{pi}", "2<i>s</i><sup>3/2</sup>") +
  f" <i>e</i><sup>&minus;1/4<i>s</i></sup>, &nbsp; show that &nbsp; <i>L</i>{{" +
  F(f"cos&nbsp;{sq}<i>t</i>", f"{sq}<i>t</i>") + "} = " + F(f"{sq}{pi}", "<i>s</i><sup>1/2</sup>") +
  " <i>e</i><sup>&minus;1/4<i>s</i></sup>.",
  "I &mdash; transforms of elementary functions","4 (was 6&ndash;7 in the 2023 papers)",
  "<b>Q1b</b> in Mar&nbsp;24; <b>Q1c</b> in Jun&nbsp;23.",
  f"the <i>t<sup>n</sup></i>-multiplication proof &mdash; <b>always</b> (Law&nbsp;1)",
  "2 of 4 with this exact wording; the sin&nbsp;&radic;<i>t</i> family is 4 of 4",
  "differentiate the given result with respect to <i>t</i>, or use the series for sin&nbsp;&radic;<i>t</i>")

card("1","T1-14","Triangular wave &mdash; periodic function transform",
  "Find the Laplace transform of the triangular wave function of period 2<i>a</i>, given by &nbsp;"
  "<i>f</i>(<i>t</i>) = " + M([["<i>t</i>,", f"for 0 {LEQ} <i>t</i> {LEQ} <i>a</i>"],
                              ["2<i>a</i> &minus; <i>t</i>,", f"for <i>a</i> {LEQ} <i>t</i> {LEQ} 2<i>a</i>"]]).replace('class="mat"','class="mat pw"'),
  "I &mdash; transform of a periodic function","7",
  "the <b>d</b> part of whichever question does <i>not</i> carry the Law-1 pair. Q1c in Apr&nbsp;23, Q2c in Jun&nbsp;23.",
  "the other members of its question &mdash; typically a division-by-<i>t</i> evaluation and a definition",
  "2 of 4 papers with this exact wave; the periodic-function <i>topic</i> is 4 of 4",
  f"answer: (1/<i>s</i><sup>2</sup>)&thinsp;tanh(<i>as</i>/2). Sep&nbsp;23 used the 2{pi} sawtooth, Mar&nbsp;24 the half-sine rectifier")

# ============================== §6 TIER 2 ==============================
w('<h2 class="brk">&sect;6 &nbsp; TIER 2 &mdash; certain to repeat, but with DIFFERENT VALUES</h2>')
w("""<div class="box">
<p style="margin:0"><b>What qualifies:</b> the <b>topic</b> has appeared in every paper (or 3 of 4), but the examiner
changes the matrix, the function or the constants each time. You cannot memorise an answer &mdash; you must own the
<b>method</b>. Each card below states the method checkpoint that actually earns the marks.
<b>Marks covered by Tier&nbsp;1 + Tier&nbsp;2 together: 100 of 100 on every paper analysed.</b></p></div>""")

card("2","T2-01","QR factorization",
  f"Find the QR factorization of a 3&times;3 or 4&times;3 matrix. Mar&nbsp;24 used {A_QR24}"
  f" &nbsp;&mdash;&nbsp; Jun&nbsp;23 used the 4&times;3 staircase {M([['1','0','0'],['1','1','0'],['1','1','1'],['1','1','1']])}"
  f" and Sep&nbsp;23 the 3&times;3 staircase {M([['1','0','0'],['1','1','0'],['1','1','1']])}.",
  "IV &mdash; QR-factorization","10",
  "<b>Q8a</b> in Mar&nbsp;24 and Jun&nbsp;23; Q7a in Sep&nbsp;23; Q8b in Apr&nbsp;23.",
  "the least-squares question (T1-02) &mdash; together they are all 20 marks of Q8 (Law&nbsp;8)",
  "4 of 4 papers &mdash; matrix changes every single time",
  "Gram&ndash;Schmidt the columns, normalise to get <i>Q</i>, then <i>R</i> = <i>Q</i><sup>T</sup><i>A</i>. Always state <i>R</i> is upper triangular")

card("2","T2-02","Composition of matrix transformations + image of a point",
  "Determine the matrix that describes a reflection in the <i>x</i>- (or <i>y</i>-) axis, followed by a rotation "
  f"through {th}, followed by a dilation or contraction of factor <i>k</i>. Find the image of a given point."
  f"<div class='small muted' style='margin-top:3px'>Mar&nbsp;24: reflect in <i>x</i>, rotate {pi}/2, contract 1/3, point {U41} &nbsp;&bull;&nbsp; "
  f"Sep&nbsp;23: reflect in <i>x</i>, rotate {pi}/2, dilate 3, point {U21} &nbsp;&bull;&nbsp; "
  f"Jun&nbsp;23: reflect in <i>x</i>, rotate {pi}/2, contract 1/2, point {V(['4', sp+'1'])} &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23: reflect in <i>y</i>, rotate {pi}/6, dilate 3/2, point {U21}</div>",
  "III &mdash; composition of matrix transformations","6",
  "<b>Q6a</b> in Mar&nbsp;24 and Sep&nbsp;23; Q6c in Jun&nbsp;23; Q5a in Apr&nbsp;23.",
  "the transition matrix (T1-07) and the kernel&amp;range question &mdash; the three-LOCK block (Law&nbsp;6)",
  "4 of 4 papers &mdash; only the axis, angle, factor and point change",
  f"multiply <b>right to left</b>: <i>k</i>&thinsp;<i>R</i><sub>{th}</sub>&thinsp;<i>Ref</i>. Reflection in <i>x</i> is diag(1,&minus;1); in <i>y</i> is diag(&minus;1,1)")

card("2","T2-03","Kernel and range + verify rank&ndash;nullity",
  f"Determine the kernel and range of the transformation defined by a matrix, and hence verify the rank&ndash;nullity theorem."
  f"<div class='small muted' style='margin-top:3px'>Mar&nbsp;24: <i>A</i> = {A_KER24} &nbsp;&bull;&nbsp; "
  f"Sep&nbsp;23: a 3&times;4 matrix &nbsp;&bull;&nbsp; Jun&nbsp;23: {M([['1','2'],['3','0']])} &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23: <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>, <i>x</i>&minus;<i>y</i>, <i>y</i>) given as a formula, not a matrix</div>",
  "III &mdash; kernel and range","7",
  "<b>Q6c</b> in Mar&nbsp;24; Q6b in Jun&nbsp;23; Q5c in Sep&nbsp;23; Q6c in Apr&nbsp;23.",
  "the composition and transition-matrix questions in the newest papers (Law&nbsp;6)",
  "4 of 4 papers",
  "row-reduce, read nul(<i>A</i>) for the kernel and pivot columns for the range, then show rank + nullity = number of columns. Be ready for the <i>formula</i> version too")

card("2","T2-04","Prove a transformation is linear + find images",
  f"Prove that a given <i>T</i> is linear and find the images of two specified vectors."
  f"<div class='small muted' style='margin-top:3px'>Mar&nbsp;24: <i>T</i>&thinsp;:&thinsp;<i>P</i><sub>2</sub> {ARR} <i>P</i><sub>2</sub>, "
  f"<i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup>+<i>c</i>; image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1 &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23 &amp; Sep&nbsp;23: <i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>); images of (1,2) and (2,&minus;5) &nbsp;&bull;&nbsp; "
  f"Jun&nbsp;23: <i>T</i>(<i>x</i>,<i>y</i>) = (2<i>x</i>, <i>x</i>+<i>y</i>); images of (1,2) and (&minus;1,&minus;4)</div>",
  "III &mdash; linear transformations","7",
  "<b>Q5b</b> &mdash; in all four papers, without exception.",
  "the vector-space basis / span question at Q5a and the rotation proof at Q5c (Law&nbsp;5)",
  "4 of 4 papers, always in the same slot",
  "check additivity and homogeneity separately, then substitute. The polynomial-space version is the newest twist &mdash; be ready for it")

card("2","T2-05","Solve ODEs / simultaneous ODEs by Laplace transforms",
  f"Either a single linear ODE with initial conditions, or a pair of simultaneous ODEs."
  f"<div class='small muted' style='margin-top:3px'>Mar&nbsp;24 Q4d: <i>dx</i>/<i>dt</i> &minus; 2<i>y</i> = cos&nbsp;2<i>t</i>; "
  f"<i>dy</i>/<i>dt</i> + 2<i>x</i> = sin&nbsp;2<i>t</i>, <i>x</i>(0)=1, <i>y</i>(0)=0 &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23 &amp; Jun&nbsp;23: the &ldquo;particle moving on a plane curve&rdquo; version leading to "
  f"4<i>x</i><sup>2</sup>+4<i>xy</i>+5<i>y</i><sup>2</sup> = 4 &nbsp;&bull;&nbsp; "
  f"Jun&nbsp;23 &amp; Sep&nbsp;23: <i>y</i>&Prime; + 4<i>y</i>&prime; + 3<i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup> &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23: <i>y</i>&#8244; + 2<i>y</i>&Prime; &minus; <i>y</i>&prime; &minus; 2<i>y</i> = 0</div>",
  "II &mdash; solution of linear and simultaneous ODEs","7",
  "the <b>d</b> part of Q3 or Q4 in the new format &mdash; and it sits with the Heaviside question (Law&nbsp;3).",
  "the Heaviside piecewise question (T1-08) &mdash; <b>the 14-mark pairing</b>",
  "4 of 4 papers",
  "the <i>y</i>&Prime;+4<i>y</i>&prime;+3<i>y</i> = <i>e</i><sup>&minus;t</sup> problem has been set twice with different initial conditions &mdash; do both versions")

card("2","T2-06","Laplace transform of a periodic function",
  f"Find <i>L</i>{{<i>f</i>(<i>t</i>)}} for a periodic <i>f</i> of period <i>T</i>, using "
  + F(f"1", f"1 &minus; <i>e</i><sup>&minus;<i>sT</i></sup>") + INT + "<sub>0</sub><sup><i>T</i></sup> <i>e</i><sup>&minus;<i>st</i></sup><i>f</i>(<i>t</i>)&thinsp;<i>dt</i>."
  f"<div class='small muted' style='margin-top:3px'>Mar&nbsp;24 Q2d: half-wave rectifier, <i>f</i>(<i>t</i>) = <i>E</i>&thinsp;sin({om}<i>t</i>) on "
  f"0 &lt; <i>t</i> &lt; {pi}/{om}, 0 on {pi}/{om} &lt; <i>t</i> &lt; 2{pi}/{om} &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23 &amp; Jun&nbsp;23: triangular wave of period 2<i>a</i> (see T1-14) &nbsp;&bull;&nbsp; "
  f"Sep&nbsp;23: <i>f</i>(<i>t</i>) = <i>t</i> on (0,{pi}), {pi}&minus;<i>t</i> on ({pi},2{pi})</div>",
  "I &mdash; transform of a periodic function","7 &nbsp;(+ a 2-mark &ldquo;write the formula&rdquo; version)",
  "the question <i>opposite</i> the Law-1 pair. Q2d in Mar&nbsp;24, Q1c in Apr&nbsp;23, Q2c in Jun&nbsp;23, Q1b in Sep&nbsp;23.",
  "a division-by-<i>t</i> or multiplication-by-<i>t</i> evaluation, plus the 2-mark definition",
  "4 of 4 papers",
  "Mar&nbsp;24 also asked the <b>formula itself</b> as a 2-mark question (Q1a). Memorise the statement, not just the technique")

card("2","T2-07","Complete solution of <i>Ax</i> = <i>b</i>",
  f"Find the complete solution &mdash; particular solution plus null-space basis."
  f"<div class='small muted' style='margin-top:3px'>Mar&nbsp;24 Q7a: <i>x</i>+3<i>y</i>+3<i>z</i>=1, 2<i>x</i>+6<i>y</i>+9<i>z</i>=5, &minus;<i>x</i>&minus;3<i>y</i>+3<i>z</i>=5 &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23 Q8a: <i>A</i> = {M([['1','0','2','3'],['1','3','2','0'],['2','0','4','9']])}, <i>B</i> = {V(['2','5','10'])} &nbsp;&bull;&nbsp; "
  f"Jun&nbsp;23 Q7b: a 3&times;4 system in <i>b</i><sub>1</sub>, <i>b</i><sub>2</sub>, <i>b</i><sub>3</sub> &mdash; &ldquo;by choosing appropriate <i>B</i>&rdquo;</div>",
  "IV &mdash; complete solution to <i>Ax</i> = <i>b</i>","6 (was 10 in the 2023 papers)",
  "<b>Q7a</b> in Mar&nbsp;24; Q7b in Jun&nbsp;23; Q8a in Apr&nbsp;23.",
  "the four-subspaces question (T1-03) and the orthogonal projection &mdash; all of Mar&nbsp;24 Q7",
  "3 of 4 papers",
  "always write the answer as <i>x</i> = <i>x</i><sub>p</sub> + <i>c</i><sub>1</sub><i>n</i><sub>1</sub> + &hellip; and state the consistency condition")

card("2","T2-08","Short inverse Laplace transforms",
  f"A 4-mark (formerly 6-mark) inverse transform by partial fractions, shifting, or a standard form."
  f"<div class='small muted' style='margin-top:3px'>Mar&nbsp;24 Q4b: {inv}{{" + F("3<i>s</i>+2","<i>s</i><sup>2</sup>&minus;<i>s</i>&minus;2") + "}} &nbsp;&bull;&nbsp; "
  f"Jun&nbsp;23: {inv}{{" + F("<i>e</i><sup>&minus;<i>s</i></sup>(<i>s</i>+2)","(<i>s</i>+1)<sup>2</sup>") + "}} and {inv}{{tan<sup>&minus;1</sup>(2/<i>s</i>)}}, "
  f"and {inv}{{" + F("5<i>s</i>+3","(<i>s</i>&minus;1)(<i>s</i><sup>2</sup>+2<i>s</i>+5)") + "}} &nbsp;&bull;&nbsp; "
  f"Apr&nbsp;23: {inv}{{" + F("<i>s</i><sup>3</sup>+6<i>s</i><sup>2</sup>+12<i>s</i>+8","<i>s</i><sup>6</sup>") + "}}</div>",
  "II &mdash; inverse transforms","4",
  "the <b>b</b> part of Q3 or Q4 &mdash; both questions carry one.",
  "whatever else is in that question &mdash; you get one of these no matter which you pick",
  "4 of 4 papers",
  "guaranteed marks in <b>both</b> options, so it never affects your choice")

card("2","T2-09",f"Evaluate an improper integral {INT}<sub>0</sub><sup>{inf}</sup> using Laplace transforms",
  f"Mar&nbsp;24 Q1d(i): {INT}<sub>0</sub><sup>{inf}</sup> " + F("<i>e</i><sup>&minus;<i>t</i></sup> sin&nbsp;<i>t</i>","<i>t</i>") + "<i>dt</i>"
  f" &nbsp;&bull;&nbsp; Apr&nbsp;23 Q2c(i): {INT}<sub>0</sub><sup>{inf}</sup> " + F("<i>e</i><sup>&minus;3<i>t</i></sup> &minus; <i>e</i><sup>&minus;2<i>t</i></sup>","<i>t</i>") + "<i>dt</i>"
  f" &nbsp;&bull;&nbsp; Sep&nbsp;23 Q1c: {INT}<sub>0</sub><sup>{inf}</sup> <i>t e</i><sup>&minus;2<i>t</i></sup> cos&nbsp;3<i>t</i>&thinsp;<i>dt</i>",
  "I &mdash; evaluation of integrals by Laplace transforms","7 (as one half of the <b>d</b> part)",
  "<b>Q1d</b> in Mar&nbsp;24; Q2c in Apr&nbsp;23; Q1c in Sep&nbsp;23.",
  f"a multiplication-by-<i>t</i> transform such as <i>L</i>{{<i>t</i>&thinsp;sin&nbsp;3<i>t</i>&thinsp;cos&nbsp;2<i>t</i>}} &mdash; the two halves of one 7-mark part",
  "3 of 4 papers",
  f"recognise the integral as <i>L</i>{{<i>f</i>(<i>t</i>)}} evaluated at the <i>s</i> in the exponent &mdash; here <i>s</i>=1 gives {pi}/4. With no exponential, put <i>s</i> = 0")

card("2","T2-10",f"<i>L</i>{{<i>t e<sup>at</sup></i> trig}} and division by <i>t</i>",
  f"Mar&nbsp;24 Q2c: (i) <i>L</i>{{<i>t e</i><sup>&minus;4<i>t</i></sup> sin&nbsp;3<i>t</i>}} &nbsp;(ii) <i>L</i>{{" + F("<i>t</i> &minus; sinh&nbsp;<i>at</i>","<i>t</i>") + "}}"
  f" &nbsp;&bull;&nbsp; Sep&nbsp;23 Q1a: <i>L</i>{{<i>t e</i><sup>&minus;<i>t</i></sup> sin&nbsp;3<i>t</i>}}, <i>L</i>{{(1&minus;<i>e<sup>t</sup></i>)/<i>t</i>}}"
  f" &nbsp;&bull;&nbsp; Jun&nbsp;23 Q1a(ii): <i>L</i>{{(cos&nbsp;4<i>t</i> &minus; cos&nbsp;2<i>t</i>)/<i>t</i>}}"
  f" &nbsp;&bull;&nbsp; Apr&nbsp;23 Q1b: <i>L</i>{{2<sup><i>t</i></sup> + (cos&nbsp;2<i>t</i> &minus; cos&nbsp;3<i>t</i>)/<i>t</i> + <i>t</i>&thinsp;sin&nbsp;<i>t</i>}}",
  "I &mdash; multiplication by <i>t<sup>n</sup></i>, division by <i>t</i>","7",
  "the <b>c</b> or <b>d</b> part of either Q1 or Q2 &mdash; it appears in some form in <i>both</i>.",
  "everything &mdash; this is the connective tissue of Unit I; you cannot avoid it",
  "4 of 4 papers",
  f"the two workhorses: <i>L</i>{{<i>t f</i>}} = &minus;<i>F</i>&prime;(<i>s</i>) and <i>L</i>{{<i>f</i>/<i>t</i>}} = {INT}<sub>s</sub><sup>{inf}</sup><i>F</i>(<i>u</i>)&thinsp;<i>du</i>")

card("2","T2-11","Diagonalize a matrix and hence find <i>A<sup>n</sup></i>",
  f"Apr&nbsp;23 Q9a: <i>A</i> = {M([['1','1','3'],['1','5','1'],['3','1','1']])}, find <i>A</i><sup>4</sup>"
  f" &nbsp;&bull;&nbsp; Sep&nbsp;23 Q9a: <i>A</i> = {M([['1',sp+'1'],['2','4']])}, find <i>A</i><sup>6</sup>"
  f" &nbsp;&bull;&nbsp; Jun&nbsp;23 Q10a(i): <i>A</i> = {M([[sp+'1','4'],['0','3']])}, find <i>A</i><sup>5</sup>",
  "V &mdash; similarity and diagonalization; linear recurrence relations","10",
  "the 10-mark <b>c</b> part of whichever question does <i>not</i> carry orthogonal diagonalization.",
  "the SVD question (Law&nbsp;12) &mdash; they share the same question in Jun&nbsp;23 and Sep&nbsp;23",
  "3 of 4 papers &mdash; absent only from Mar&nbsp;24",
  "<i>A<sup>n</sup></i> = <i>PD<sup>n</sup>P</i><sup>&minus;1</sup>. Its absence from the newest paper makes it <b>more</b> likely to return, not less")

card("2","T2-12","Linear combination / span / linear independence / basis",
  f"Mar&nbsp;24 Q5a: is {{{M([['1','2'],['0','1']])}, {M([['3','4'],['1','1']])}, {M([['1','2'],['1','1']])}, {M([['0','2'],['1','2']])}}} a basis of <i>M</i><sub>22</sub>?"
  f" &nbsp;&bull;&nbsp; Sep&nbsp;23: do {{(1,2,3), (&minus;1,&minus;1,0), (2,5,4)}} span <i>R</i><sup>3</sup>?"
  f" &nbsp;&bull;&nbsp; Jun&nbsp;23: is (1,&minus;2) a linear combination of (2,4) and (3,6)? and check independence of {{(1,0,1),(2,1,3),(&minus;1,3,2)}}"
  f" &nbsp;&bull;&nbsp; Apr&nbsp;23: is (4,&minus;4,6) a linear combination of (1,2,&minus;3), (2,&minus;4,6), (&minus;1,2,&minus;3)?",
  "III &mdash; linear combination, span, basis and dimension","6",
  "<b>Q5a</b> in the three newest papers; Q6a in Apr&nbsp;23.",
  "the &ldquo;prove <i>T</i> is linear&rdquo; question at Q5b (Law&nbsp;5)",
  "4 of 4 papers",
  "the <i>M</i><sub>22</sub> matrix-space version is the newest twist &mdash; flatten each matrix to a 4-vector and test the 4&times;4 determinant")

card("2","T2-13","Unitary matrix check",
  f"Mar&nbsp;24 Q10b: is <i>A</i> = {A_UNI} unitary? &nbsp;&bull;&nbsp; "
  f"Jun&nbsp;23 Q10a(ii): is <i>A</i> = &frac12;{M([['1+<i>i</i>','1&minus;<i>i</i>'],['1&minus;<i>i</i>','1+<i>i</i>']])} unitary?",
  "V &mdash; unitary matrices","5",
  "the property-check block &mdash; <b>Q10b</b> in Mar&nbsp;24.",
  "the positive-definite check (T1-05) &mdash; they are the 5+5 pair (Law&nbsp;10)",
  "2 of 4 papers, but 1 of 1 under the current format",
  f"show <i>A</i><sup>*</sup><i>A</i> = <i>I</i>, where <i>A</i><sup>*</sup> is the conjugate transpose. Two minutes of work for 5 marks")

card("2","T2-14","Quadratic form &mdash; remove cross-product terms / test definiteness",
  f"Mar&nbsp;24 Q9a: express <i>Q</i>(<i>x</i>) = <i>x</i><sub>1</sub><sup>2</sup> &minus; 8<i>x</i><sub>1</sub><i>x</i><sub>2</sub> &minus; 5<i>x</i><sub>2</sub><sup>2</sup> "
  f"as a quadratic form with no cross-product terms &nbsp;&bull;&nbsp; "
  f"Sep&nbsp;23 Q10b(ii): is 3<i>x</i><sup>2</sup> + 5<i>y</i><sup>2</sup> + 3<i>z</i><sup>2</sup> &minus; 2<i>yz</i> + 2<i>zx</i> &minus; 2<i>xy</i> positive definite?",
  "V &mdash; quadratic forms","5",
  "<b>Q9a</b> in Mar&nbsp;24; part of Q10b in Sep&nbsp;23.",
  "the Markov steady-state question and the SVD (Law&nbsp;12) &mdash; all of Mar&nbsp;24 Q9",
  "2 of 4 papers, and it is in the current format",
  "build the symmetric matrix, orthogonally diagonalise it, substitute <i>x</i> = <i>Py</i>. This is orthogonal diagonalization wearing a hat")

card("2","T2-15","The 2-mark definitions",
  "Write the Laplace transform of a periodic function &nbsp;&bull;&nbsp; Define the Laplace transform of a function "
  "&nbsp;&bull;&nbsp; Define the Dirac-delta function and sketch its graph &nbsp;&bull;&nbsp; "
  "Define the unit step function and represent it graphically &nbsp;&bull;&nbsp; Define a periodic function with an example.",
  "I and II","2 &times; 2 = 4 marks per paper",
  "the <b>a</b> part of Q1, Q2, Q3 and Q4 &mdash; every one of the four questions opens with one.",
  "everything &mdash; you get one free regardless of which question you choose",
  "new in the March 2024 format; Jun 23 had one embedded in a 6-marker",
  "four marks for four sentences and two sketches. Also learn <b>existence conditions</b> and the <b>convolution statement</b> &mdash; both are in your syllabus and both are natural 2-markers")


# ============================== §7 TIER 3 ==============================
w('<h2 class="brk">&sect;7 &nbsp; TIER 3 &mdash; probable, and the ones that can ambush you</h2>')
w("""<div class="box">
<p style="margin:0"><b>What qualifies:</b> topics that appeared once, or that sit in your syllabus but have never
been asked. Tier 1 and Tier 2 will carry you to a first class on their own. <b>This tier is what separates a
75 from a 95</b> &mdash; and it is where a paper can surprise you, because every one of these is a legitimate
question the examiner is entitled to set.</p></div>""")

card("3","T3-01","PCA &mdash; Principal Component Analysis",
  "<b>The biggest single risk on this sheet.</b> PCA is named explicitly in Unit V of your syllabus and in CO5 "
  "(&ldquo;obtain eigenvalue decomposition of a matrix and use it to study the concepts of SVD and PCA&rdquo;), "
  "yet it does not appear in <i>any</i> of the four papers. Expect: form the covariance matrix of a small data set, "
  "find its eigenvalues and eigenvectors, identify the first principal component, and state the proportion of "
  "variance it explains.",
  "V &mdash; principal component analysis","5 (or half a 10-marker with SVD)",
  "the <b>a</b> or <b>b</b> part of Q9 or Q10 &mdash; wherever the two 5-mark slots are.",
  "SVD, almost certainly &mdash; they are the same machinery and the syllabus lists them in one breath",
  "<b>0 of 4 papers</b> &mdash; but 1 of 1 syllabuses and 1 of 1 course outcomes",
  "cheapest insurance on this sheet: centre the data, compute <i>C</i> = (1/(<i>n</i>&minus;1))<i>X</i><sup>T</sup><i>X</i>, diagonalise. One hour of work")

card("3","T3-02","Conic sections from a quadratic form",
  "Classify a conic <i>ax</i><sup>2</sup> + <i>bxy</i> + <i>cy</i><sup>2</sup> = <i>d</i> by diagonalising its "
  "symmetric matrix, and identify it as an ellipse, hyperbola or parabola in the rotated axes.",
  "V &mdash; quadratic forms and conic sections","5",
  "the same 5-mark slot as the quadratic-form question (Mar&nbsp;24 Q9a).",
  "the Markov / SVD block (Law&nbsp;12)",
  "<b>0 of 4 papers</b>, but explicitly in the syllabus",
  "the Mar&nbsp;24 quadratic-form question is one sentence away from being this question. Learn the sign rule: both eigenvalues same sign &rarr; ellipse, opposite signs &rarr; hyperbola")

card("3","T3-03","Gram&ndash;Schmidt &mdash; construct an orthonormal basis",
  f"Sep&nbsp;23 Q8a: construct an orthonormal basis for <i>W</i> = span{{<i>x</i><sub>1</sub>, <i>x</i><sub>2</sub>, <i>x</i><sub>3</sub>}} "
  f"{'&#8834;'} <i>R</i><sup>4</sup>, where <i>x</i><sub>1</sub> = {V(['1','1','1','1'])}, "
  f"<i>x</i><sub>2</sub> = {V(['0','1','1','1'])}, <i>x</i><sub>3</sub> = {V(['0','0','1','1'])}, using the Gram&ndash;Schmidt process.",
  "IV &mdash; orthonormal bases and Gram&ndash;Schmidt","10",
  "<b>Q8a</b> &mdash; the slot QR normally occupies. It is QR&rsquo;s natural substitute.",
  "the least-squares question (it was Q8b in Sep&nbsp;23, exactly as in Mar&nbsp;24)",
  "1 of 4 papers &mdash; but you get it for free with QR",
  "if you can do QR you can already do this. Just stop before forming <i>R</i>")

card("3","T3-04","Orthogonal projection of one vector onto another",
  f"Let <i>y</i> = {V(['2','3'])} and <i>u</i> = {V(['4', sp+'7'])}. Find the orthogonal projection of <i>y</i> onto "
  f"<i>u</i>, and write <i>y</i> as the sum of two orthogonal vectors, one in span{{<i>u</i>}} and one orthogonal to <i>u</i>.",
  "IV &mdash; projections","7",
  "<b>Q7b</b> in Mar&nbsp;24 &mdash; brand new in the current format.",
  "the complete solution at Q7a and the four-subspaces question at Q7c &mdash; all of Mar&nbsp;24 Q7",
  "1 of 4 papers, but 1 of 1 under the current syllabus, whose Unit&nbsp;IV is literally titled <b>Orthogonal Projections</b>",
  "proj = ((<i>y</i>&middot;<i>u</i>)/(<i>u</i>&middot;<i>u</i>))<i>u</i>. Five minutes for 7 marks &mdash; do not lose these")

card("3","T3-05","Engineering application &mdash; LR circuit by Laplace transforms",
  f"A voltage <i>Ee</i><sup>&minus;<i>at</i></sup> is applied at <i>t</i> = 0 to a circuit of inductance <i>L</i> and "
  f"resistance <i>R</i>. Show that the current at time <i>t</i> is "
  + F("<i>E</i>", "<i>R</i> &minus; <i>aL</i>") +
  "(<i>e</i><sup>&minus;<i>at</i></sup> &minus; <i>e</i><sup>&minus;<i>Rt</i>/<i>L</i></sup>), using Laplace transforms.",
  "II &mdash; engineering applications","7",
  "<b>Q3d</b> in Mar&nbsp;24.",
  "the Heaviside question at Q3c &mdash; this <i>is</i> the ODE half of the Law-3 pairing in that paper",
  "1 of 4 papers, but 1 of 1 under the current syllabus, which names &ldquo;engineering applications&rdquo; outright",
  "it is just <i>L</i>&thinsp;<i>di</i>/<i>dt</i> + <i>Ri</i> = <i>Ee</i><sup>&minus;<i>at</i></sup>, <i>i</i>(0)=0. If Law&nbsp;3 holds, this or an ODE sits next to your Heaviside marks &mdash; learn it")

card("3","T3-06","Markov matrix &mdash; steady-state vector",
  f"Find the steady-state solution of the Markov matrix &nbsp; <i>A</i> = {A_MARK}",
  "V &mdash; eigenvalue applications (not named in the syllabus text)","5",
  "<b>Q9b</b> in Mar&nbsp;24.",
  "the quadratic form at Q9a and the SVD at Q9c",
  "1 of 4 papers &mdash; and it is the only borderline-syllabus item on this sheet",
  "solve (<i>A</i> &minus; <i>I</i>)<i>x</i> = 0 and scale so the entries sum to 1. Fifteen minutes to learn, 5 marks")

card("3","T3-07","Proofs you have seen once &mdash; and the two that are overdue",
  f"<b>Seen once:</b> <i>L</i>{{<i>f</i>(<i>t</i>)/<i>t</i>}} = {INT}<sub>s</sub><sup>{inf}</sup><i>F</i>(<i>s</i>)&thinsp;<i>ds</i> "
  f"(Jun&nbsp;23 Q2b, with <i>L</i>{{sin&nbsp;4<i>t</i>/<i>t</i>}}) &nbsp;&bull;&nbsp; "
  f"<i>L</i>{{(sinh&nbsp;<i>at</i>)<i>f</i>(<i>t</i>)}} = &frac12;[<i>F</i>(<i>s</i>&minus;<i>a</i>) &minus; <i>F</i>(<i>s</i>+<i>a</i>)] "
  f"(Sep&nbsp;23 Q2b, with <i>L</i>[<i>t</i><sup>8</sup> sinh&nbsp;2<i>t</i>]) &nbsp;&bull;&nbsp; "
  f"state and prove the convolution theorem (Sep&nbsp;23 Q3a).<br>"
  f"<b>Overdue &mdash; in the syllabus, never asked:</b> <b>existence conditions</b> for the Laplace transform "
  f"(a natural 2-marker) &nbsp;&bull;&nbsp; transform of <b>derivatives</b> stated as a proof &nbsp;&bull;&nbsp; "
  f"a direct <b>linear recurrence relation</b> (Fibonacci-style) solved by diagonalization.",
  "I, II and V","2 to 7",
  "the <b>a</b> (2 m), <b>c</b> (7 m) or 10-mark slots depending on which appears.",
  "varies &mdash; proofs cluster with the other bookwork in whichever question carries them",
  "1 of 4 each, or 0 of 4 for the overdue ones",
  "the examiner has a stock of about six Unit-I proofs and rotates them. The <i>t<sup>n</sup></i> proof (T1-04) has come up four times; these are the alternates")

# ============================== §8 DECISION CARD ==============================
w('<h2 class="brk">&sect;8 &nbsp; The exam-hall decision card</h2>')
w(f"""
<div class="box go">
<h4>Your first three minutes: do not start writing. Read all ten questions and mark your five.</h4>
<p class="small" style="margin-bottom:0">Each rule below tells you what to <b>look for</b>, not what to assume.
The laws in &sect;4 predict where things land, but the paper in front of you is the authority. Use the trigger.</p>
</div>

<table class="g">
<tr><th style="width:7%" class="c">Unit</th><th style="width:22%">Trigger &mdash; scan for this</th>
<th style="width:26%">Then answer</th><th>Why &mdash; and what you are giving up</th></tr>

<tr><td class="c"><b>I</b></td>
<td>Find the question containing the <b><i>t<sup>n</sup></i>-multiplication proof</b>.</td>
<td><b>That question.</b> It also holds the sin&nbsp;&radic;<i>t</i> / cos&nbsp;&radic;<i>t</i> problem (Law&nbsp;1, 4/4).</td>
<td>7 + 4 = <b>11 marks of pure recall</b> in one question. You give up the periodic-function problem, which lands in the other one (Law&nbsp;2) &mdash; so prepare it anyway, because if the proof is missing, the periodic question <i>is</i> your answer.</td></tr>

<tr><td class="c"><b>II</b></td>
<td>Find the question containing the <b>Heaviside / unit-step piecewise</b> function.</td>
<td><b>That question.</b> An ODE, a system of ODEs, or the circuit application will be sitting next to it (Law&nbsp;3, 4/4).</td>
<td>7 + 7 = <b>14 guaranteed marks</b>, plus a 2-mark definition and a 4-mark inverse transform to complete the 20. You give up the convolution question, which sits opposite (Law&nbsp;4).</td></tr>

<tr><td class="c"><b>III</b></td>
<td>Find the question containing the <b>composition of transformations</b> (reflection &rarr; rotation &rarr; dilation/contraction).</td>
<td><b>That question.</b> In the two newest papers it also carried the transition matrix <i>and</i> the kernel&amp;range question (Law&nbsp;6).</td>
<td>6 + 7 + 7 = <b>20 marks from three LOCK topics</b>. If the composition question is instead paired with something unfamiliar, fall back on the Q5 proof block: basis/span + prove-<i>T</i>-is-linear + rotation proof (Law&nbsp;5).</td></tr>

<tr><td class="c"><b>IV</b></td>
<td>Compare the two shapes. <b>Q7</b> is 6+7+7; <b>Q8</b> is 10+10.</td>
<td><b>Q8</b> if it is QR + least-squares (Law&nbsp;8, and what Mar&nbsp;24 did). <b>Q7</b> if you want the four-subspaces marks &mdash; that question is <i>always</i> Q7 (Law&nbsp;7, 4/4).</td>
<td>Q8 = two LOCK topics, but two long computations with no partial safety net. Q7 = three shorter problems, more forgiving if one goes wrong. <b>If your algebra is shaky under time pressure, take Q7.</b></td></tr>

<tr><td class="c"><b>V</b></td>
<td>Find the question containing <b>orthogonal diagonalization</b>.</td>
<td><b>That question.</b> The property-check block (positive definite / Hermitian / unitary) travels with it (Laws&nbsp;10 &amp; 11).</td>
<td>10 + 5 + 5 = <b>20</b>, where the two 5-markers are ten minutes of work between them. You give up SVD, which sits opposite (Law&nbsp;9) &mdash; but SVD is a LOCK too, so prepare both.</td></tr>
</table>

<div class="box warn avoid">
<h4>Three ways this plan can fail &mdash; and the counter</h4>
<ol class="small" style="margin-bottom:0">
<li><b>A law breaks.</b> Every law is 3/4 or 4/4, not 5/5. If the composition question is <i>not</i> next to the transition matrix, don&rsquo;t force it &mdash; count the marks you can actually secure in each question and take the larger number. The laws are a shortcut, not a substitute for reading the paper.</li>
<li><b>A brand-new question appears.</b> March 2024 introduced three at once &mdash; the LR circuit, the orthogonal projection and the Markov steady state. That is 19 marks of novelty in a single paper. Tier&nbsp;3 exists precisely for this; it is the reason the realistic ceiling is 95, not 100.</li>
<li><b>PCA is set.</b> It is in your syllabus and your course outcomes and it has never been asked. If it appears it will be worth 5 marks in Unit&nbsp;V. One hour of preparation removes this risk entirely.</li>
</ol>
</div>
""")

# ============================== §9 BACK-TEST ==============================
w('<h2>&sect;9 &nbsp; Back-test &mdash; what this sheet would actually have scored</h2>')
w("""<p>Every prediction sheet should be tested against the evidence it was built from. Below: for each paper, the
questions the &sect;8 decision card would have selected, and the marks that Tier&nbsp;1 + Tier&nbsp;2 preparation alone
would have secured.</p>

<table class="g">
<tr><th style="width:20%">Paper</th><th class="c" style="width:24%">Questions selected</th>
<th class="c" style="width:12%">Tier 1+2</th><th class="c" style="width:10%">Score</th><th>Anything not covered</th></tr>
<tr><td><b>April 2023</b><br><span class="small muted">Regular SEE</span></td><td class="c">Q1, Q4, Q5, Q7, Q10</td>
<td class="c">100 / 100</td><td class="hit4">100</td><td class="small">Nothing. Every part maps to a Tier 1 or Tier 2 card.</td></tr>
<tr><td><b>June 2023</b><br><span class="small muted">Make-up</span></td><td class="c">Q1, Q3, Q5, Q8, Q9</td>
<td class="c">100 / 100</td><td class="hit4">100</td><td class="small">Nothing.</td></tr>
<tr><td><b>Aug/Sep 2023</b><br><span class="small muted">Backlog</span></td><td class="c">Q1, Q3, Q5, Q7, Q10</td>
<td class="c">100 / 100</td><td class="hit4">100</td><td class="small">Nothing on the selected path. Had you taken Q8 instead of Q7 you would have met Gram&ndash;Schmidt (T3-03, 10 m).</td></tr>
<tr><td><b>March 2024</b><br><span class="small muted">SEE &mdash; current format</span></td><td class="c">Q1, Q4, Q6, Q8, Q10</td>
<td class="c">100 / 100</td><td class="hit4">100</td><td class="small">Nothing on the selected path. Q3 would have cost you 7 marks (the LR circuit, T3-05) and Q7 would have cost 7 (the projection, T3-04).</td></tr>
</table>

<div class="box avoid">
<h4>What that number does and does not mean</h4>
<p class="small" style="margin-bottom:4px">A 100/100 back-test is <b>partly circular</b> &mdash; the tiers were built from these
four papers, so of course they cover them. What it honestly demonstrates is narrower but still useful: <b>the choice
rules in &sect;8 select a fully-covered question in every unit of every paper</b>, and the syllabus is small enough
that roughly 30 distinct problem types exhaust it.</p>
<p class="small" style="margin-bottom:0">The forward-looking estimate is different, and here it is straight:</p>
<table class="g" style="margin-top:6px">
<tr><th>If you prepare&hellip;</th><th class="c" style="width:14%">Expected</th><th class="c" style="width:14%">Floor</th><th>Reasoning</th></tr>
<tr><td><b>Tier 1 only</b></td><td class="c">55&ndash;65</td><td class="c">45</td><td class="small">63 marks of the March 2024 paper sat in Tier&nbsp;1, but you cannot always reach all of it through the choice structure.</td></tr>
<tr><td><b>Tier 1 + Tier 2</b></td><td class="c"><b>80&ndash;92</b></td><td class="c"><b>70</b></td><td class="small">Covers every topic that has appeared more than once. The floor assumes two brand-new questions land in your chosen sections, as happened in March 2024.</td></tr>
<tr><td><b>Tier 1 + 2 + 3</b></td><td class="c">90&ndash;98</td><td class="c">82</td><td class="small">The only remaining exposure is a genuinely unprecedented question. Tier&nbsp;3 is roughly six extra hours of work.</td></tr>
</table>
</div>
""")


# ============================== §10 STUDY ORDER ==============================
w('<h2 class="brk">&sect;10 &nbsp; Study order &mdash; highest marks per hour first</h2>')
w("""
<table class="g">
<tr><th style="width:6%" class="c">#</th><th style="width:28%">Do this</th><th class="c" style="width:9%">Marks<br>defended</th>
<th class="c" style="width:9%">Rough<br>hours</th><th>Why it is in this position</th></tr>

<tr><td class="c"><b>1</b></td><td><b>T1-04</b> <i>t<sup>n</sup></i> proof &nbsp;+&nbsp; <b>T1-13</b> sin&nbsp;&radic;<i>t</i> / cos&nbsp;&radic;<i>t</i></td>
<td class="c">11</td><td class="c">1.5</td>
<td>4/4 frequency, they sit in the same question (Law&nbsp;1), and both are reproducible from memory. Nothing else on the paper is this reliable.</td></tr>

<tr><td class="c"><b>2</b></td><td><b>T1-08</b> Heaviside &nbsp;+&nbsp; <b>T2-05</b> ODEs by Laplace transforms</td>
<td class="c">14</td><td class="c">3</td>
<td>The Law-3 pairing &mdash; 4/4, and the largest guaranteed block on the paper. Do the <i>t</i><sup>2</sup>/4<i>t</i>/8 function until it is automatic.</td></tr>

<tr><td class="c"><b>3</b></td><td><b>T1-01</b> orthogonal diagonalization &nbsp;+&nbsp; <b>T1-05</b> positive definite &nbsp;+&nbsp; <b>T2-13</b> unitary &nbsp;+&nbsp; <b>T1-12</b> Hermitian</td>
<td class="c">20</td><td class="c">3</td>
<td>Laws 10 &amp; 11 put all four in one question. The three property-checks are ten minutes of work for 10 marks &mdash; the best rate on the entire paper.</td></tr>

<tr><td class="c"><b>4</b></td><td><b>T2-02</b> composition &nbsp;+&nbsp; <b>T1-07</b> transition matrix &nbsp;+&nbsp; <b>T2-03</b> kernel &amp; range</td>
<td class="c">20</td><td class="c">3.5</td>
<td>Three LOCK topics that formed one whole question in the two newest papers (Law&nbsp;6). Memorise the transition-matrix problem exactly &mdash; same bases twice running.</td></tr>

<tr><td class="c"><b>5</b></td><td><b>T2-01</b> QR &nbsp;+&nbsp; <b>T1-02</b> least-squares</td>
<td class="c">20</td><td class="c">4</td>
<td>Both 4/4 and paired in Q8 (Law&nbsp;8). Slower than the blocks above because the arithmetic is long &mdash; but the least-squares data has repeated verbatim.</td></tr>

<tr><td class="c"><b>6</b></td><td><b>T1-03</b> four subspaces &nbsp;+&nbsp; <b>T2-07</b> complete solution &nbsp;+&nbsp; <b>T3-04</b> projection</td>
<td class="c">20</td><td class="c">3</td>
<td>Your Unit&nbsp;IV alternative (Q7). Cheap because the four-subspaces matrix has never changed. Gives you a genuine choice on the day.</td></tr>

<tr><td class="c"><b>7</b></td><td><b>T1-06</b> SVD &nbsp;+&nbsp; <b>T2-11</b> diagonalize and find <i>A<sup>n</sup></i></td>
<td class="c">10</td><td class="c">2.5</td>
<td>SVD is 4/4 but lands in the question you are <i>not</i> answering (Law&nbsp;9). Insurance, not primary. <i>A<sup>n</sup></i> is overdue &mdash; absent from March 2024 after three straight appearances.</td></tr>

<tr><td class="c"><b>8</b></td><td><b>T2-06</b> periodic functions &nbsp;+&nbsp; <b>T1-14</b> triangular wave &nbsp;+&nbsp; <b>T2-15</b> the 2-mark definitions</td>
<td class="c">11</td><td class="c">2</td>
<td>Covers the Unit&nbsp;I question you did <i>not</i> choose, so nothing in that unit can hurt you. The definitions are four marks for four sentences.</td></tr>

<tr><td class="c"><b>9</b></td><td><b>T2-04</b> prove <i>T</i> linear &nbsp;+&nbsp; <b>T2-12</b> span/basis &nbsp;+&nbsp; <b>T1-10</b> rotation proof</td>
<td class="c">20</td><td class="c">2</td>
<td>The Q5 fallback block (Law&nbsp;5). Fast, because it is mostly bookwork. Buy yourself a second option in Unit&nbsp;III.</td></tr>

<tr><td class="c"><b>10</b></td><td><b>T2-08</b> short inverse transforms &nbsp;+&nbsp; <b>T2-09</b> improper integrals &nbsp;+&nbsp; <b>T2-10</b> <i>t e<sup>at</sup></i> / division by <i>t</i> &nbsp;+&nbsp; <b>T1-09</b>, <b>T1-11</b></td>
<td class="c">22</td><td class="c">3</td>
<td>The connective tissue of Units I and II. Individually small, collectively large, and they appear in <i>both</i> options of both units.</td></tr>

<tr><td class="c"><b>11</b></td><td><b>T3-01 PCA</b> &nbsp;+&nbsp; <b>T3-02</b> conic sections &nbsp;+&nbsp; <b>T3-06</b> Markov</td>
<td class="c">10&ndash;15</td><td class="c">2</td>
<td><b>Do not skip this row.</b> Three cheap topics that close your only real syllabus blind spots. PCA in particular is named in your course outcomes and has never been asked &mdash; which makes it overdue, not safe.</td></tr>

<tr><td class="c"><b>12</b></td><td><b>T3-03</b> Gram&ndash;Schmidt &nbsp;+&nbsp; <b>T3-05</b> LR circuit &nbsp;+&nbsp; <b>T3-07</b> the alternate proofs</td>
<td class="c">10&ndash;20</td><td class="c">2.5</td>
<td>Last, because each is one appearance in four papers. But Gram&ndash;Schmidt is free once you know QR, and the circuit problem sits right next to your 14-mark Heaviside block.</td></tr>
</table>

<p class="small muted">Rows 1&ndash;6 alone defend every unit and total roughly 18 hours. If you have three days,
that is the plan. If you have a week, do all twelve.</p>
""")

# ============================== §11 APPENDIX ==============================
w('<h2 class="brk">&sect;11 &nbsp; Appendix &mdash; complete question index of all four papers</h2>')
w("""<p class="small">Everything the prediction is built on, so you can check any claim yourself.
<b>T</b> = the tier card that covers it.</p>""")

def paper(title, meta, rows):
    w(f'<h3>{title}</h3><p class="small muted" style="margin-top:-3px">{meta}</p>')
    w('<table class="g"><tr><th style="width:6%" class="c">Q</th><th style="width:6%" class="c">Marks</th>'
      '<th>Question</th><th style="width:9%" class="c">Tier card</th></tr>')
    for q, mk, txt, tier in rows:
        w(f'<tr><td class="c"><b>{q}</b></td><td class="c">{mk}</td><td>{txt}</td><td class="c small">{tier}</td></tr>')
    w("</table>")

paper("Paper N &mdash; SEMESTER END EXAMINATIONS, MARCH 2024 &nbsp;<span style='color:#0d7a45'>(current format &mdash; plan against this one)</span>",
 "Course: Laplace Transforms and Vector Space &middot; Code CS/IS/AI/AD/CY/CI31 &middot; 100 marks / 3 hrs &middot; "
 "This is the paper contained in <i>both</i> SEE_25.pdf and IS131_MATH_SEE_2024_1.pdf.",
 [("1a","02","Write the Laplace transform of a periodic function.","T2-15"),
  ("1b","04",f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = {F(sq+pi,'2<i>s</i><sup>3/2</sup>')}<i>e</i><sup>&minus;1/4<i>s</i></sup>, show <i>L</i>{{cos&nbsp;{sq}<i>t</i>/{sq}<i>t</i>}} = {F(sq+pi,'<i>s</i><sup>1/2</sup>')}<i>e</i><sup>&minus;1/4<i>s</i></sup>.","T1-13"),
  ("1c","07","Prove <i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup>n</sup> <i>d<sup>n</sup></i>{<i>F</i>(<i>s</i>)}/<i>ds<sup>n</sup></i>.","T1-04"),
  ("1d","07",f"Evaluate (i) {INT}<sub>0</sub><sup>{inf}</sup> {F('<i>e</i><sup>&minus;<i>t</i></sup> sin&nbsp;<i>t</i>','<i>t</i>')}<i>dt</i> &nbsp; (ii) <i>L</i>{{<i>t</i>&thinsp;sin&nbsp;3<i>t</i>&thinsp;cos&nbsp;2<i>t</i>}}.","T2-09 / T2-10"),
  ("2a","02","Define the Laplace transform of a function.","T2-15"),
  ("2b","04",f"Obtain the Laplace transform of ({sq}<i>t</i> + 1/{sq}<i>t</i>)<sup>3</sup>.","T2-10"),
  ("2c","07",f"Evaluate (i) <i>L</i>{{<i>t e</i><sup>&minus;4<i>t</i></sup> sin&nbsp;3<i>t</i>}} &nbsp; (ii) <i>L</i>{{{F('<i>t</i> &minus; sinh&nbsp;<i>at</i>','<i>t</i>')}}}.","T2-10"),
  ("2d","07",f"Periodic function of period 2{pi}/{om}: <i>f</i>(<i>t</i>) = <i>E</i>&thinsp;sin({om}<i>t</i>) on 0&lt;<i>t</i>&lt;{pi}/{om}, 0 on {pi}/{om}&lt;<i>t</i>&lt;2{pi}/{om}. Show <i>L</i>{{<i>f</i>}} = <i>E</i>{om}/((<i>s</i><sup>2</sup>+{om}<sup>2</sup>)(1&minus;<i>e</i><sup>&minus;{pi}<i>s</i>/{om}</sup>)).","T2-06"),
  ("3a","02","Define the Dirac-Delta function and sketch its graph.","T2-15"),
  ("3b","04",f"Evaluate {inv}{{log&nbsp;{F('<i>s</i><sup>2</sup>+1','<i>s</i>(<i>s</i>+1)')}}}.","T1-09"),
  ("3c","07","Express <i>f</i>(<i>t</i>) = <i>t</i><sup>2</sup> (0&lt;<i>t</i>&lt;2), 4<i>t</i> (2&lt;<i>t</i>&lt;4), 8 (<i>t</i>&gt;4) via the Heaviside function; find its LT.","T1-08"),
  ("3d","07","LR circuit: voltage <i>Ee</i><sup>&minus;<i>at</i></sup> at <i>t</i>=0; show the current is (<i>E</i>/(<i>R</i>&minus;<i>aL</i>))(<i>e</i><sup>&minus;<i>at</i></sup> &minus; <i>e</i><sup>&minus;<i>Rt/L</i></sup>).","T3-05"),
  ("4a","02","Define the unit step function and represent it graphically.","T2-15"),
  ("4b","04",f"Find {inv}{{{F('3<i>s</i>+2','<i>s</i><sup>2</sup>&minus;<i>s</i>&minus;2')}}}.","T2-08"),
  ("4c","07","Verify the convolution theorem for <i>f</i><sub>1</sub>(<i>t</i>) = <i>t</i> and <i>f</i><sub>2</sub>(<i>t</i>) = cos&nbsp;<i>t</i>.","T1-11"),
  ("4d","07","Solve <i>dx/dt</i> &minus; 2<i>y</i> = cos&nbsp;2<i>t</i>; <i>dy/dt</i> + 2<i>x</i> = sin&nbsp;2<i>t</i>, <i>x</i>(0)=1, <i>y</i>(0)=0.","T2-05"),
  ("5a","06",f"Is {{{M([['1','2'],['0','1']])},{M([['3','4'],['1','1']])},{M([['1','2'],['1','1']])},{M([['0','2'],['1','2']])}}} a basis of <i>M</i><sub>22</sub>?","T2-12"),
  ("5b","07",f"<i>T</i>:<i>P</i><sub>2</sub>{ARR}<i>P</i><sub>2</sub>, <i>T</i>(<i>ax</i><sup>2</sup>+<i>bx</i>+<i>c</i>) = (<i>a</i>+<i>b</i>)<i>x</i><sup>2</sup>+<i>c</i>. Show linear; image of 5<i>x</i><sup>2</sup>+6<i>x</i>+1.","T2-04"),
  ("5c","07",f"Show <i>T</i>(<i>x</i>) = <i>Ax</i> rotates <i>x</i> through {th} if <i>A</i> = {A_ROT}.","T1-10"),
  ("6a","06",f"Reflection in <i>x</i>-axis, then rotation {pi}/2, then contraction 1/3. Image of {U41}.","T2-02"),
  ("6b","07",f"<i>B</i>={{(1,2),(3,&minus;1)}}, <i>B</i>&prime;={{(3,1),(5,2)}}. Transition matrix; [<i>u</i>]<sub><i>B</i></sub>={U21}, find [<i>u</i>]<sub><i>B</i>&prime;</sub>.","T1-07"),
  ("6c","07",f"Kernel and range of <i>A</i> = {A_KER24}; verify rank&ndash;nullity.","T2-03"),
  ("7a","06","Complete solution of <i>x</i>+3<i>y</i>+3<i>z</i>=1, 2<i>x</i>+6<i>y</i>+9<i>z</i>=5, &minus;<i>x</i>&minus;3<i>y</i>+3<i>z</i>=5.","T2-07"),
  ("7b","07",f"<i>y</i>={V(['2','3'])}, <i>u</i>={V(['4',sp+'7'])}: orthogonal projection of <i>y</i> onto <i>u</i>; split <i>y</i> into two orthogonal parts.","T3-04"),
  ("7c","07",f"Dimension and basis for the four fundamental subspaces of <i>A</i> = {A_SUB}.","T1-03"),
  ("8a","10",f"QR factorization of <i>A</i> = {A_QR24}.","T2-01"),
  ("8b","10",f"Least-square solution of <i>AX</i>=<i>b</i>, <i>A</i>={A_LS}, <i>b</i>={B_LS}.","T1-02"),
  ("9a","05","Express <i>Q</i>(<i>x</i>) = <i>x</i><sub>1</sub><sup>2</sup> &minus; 8<i>x</i><sub>1</sub><i>x</i><sub>2</sub> &minus; 5<i>x</i><sub>2</sub><sup>2</sup> with no cross-product terms.","T2-14"),
  ("9b","05",f"Steady-state solution of the Markov matrix <i>A</i> = {A_MARK}.","T3-06"),
  ("9c","10",f"SVD of <i>A</i> = {A_SVD}.","T1-06"),
  ("10a","05",f"Is <i>A</i> = {A_PD} positive definite?","T1-05"),
  ("10b","05",f"Is <i>A</i> = {A_UNI} unitary?","T2-13"),
  ("10c","10",f"Orthogonally diagonalize <i>A</i> = {A_ORTH}.","T1-01"),
 ])

paper("Paper A &mdash; SEMESTER END EXAMINATIONS, APRIL 2023",
 "Course: Linear Algebra and Laplace Transforms &middot; Code CS/IS/AI/AD31 &middot; older title, same five units",
 [("1a","06",f"(i) <i>L</i>{{({sq}<i>t</i> &minus; 1/{sq}<i>t</i>)<sup>3</sup>}} &nbsp;(ii) <i>L</i>{{{INT}<sub>0</sub><sup><i>t</i></sup> <i>e</i><sup>&minus;<i>t</i></sup>cos&nbsp;<i>t dt</i>}}","T2-10"),
  ("1b","07","<i>L</i>{2<sup><i>t</i></sup> + (cos&nbsp;2<i>t</i> &minus; cos&nbsp;3<i>t</i>)/<i>t</i> + <i>t</i>&thinsp;sin&nbsp;<i>t</i>}","T2-10"),
  ("1c","07","Triangular wave of period 2<i>a</i>: <i>t</i> on [0,<i>a</i>], 2<i>a</i>&minus;<i>t</i> on [<i>a</i>,2<i>a</i>].","T1-14"),
  ("2a","06",f"Find <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}.","T1-13"),
  ("2b","07","Prove <i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup>n</sup><i>d<sup>n</sup></i>{<i>F</i>(<i>s</i>)}/<i>ds<sup>n</sup></i>.","T1-04"),
  ("2c","07",f"(i) {INT}<sub>0</sub><sup>{inf}</sup>(<i>e</i><sup>&minus;3<i>t</i></sup>&minus;<i>e</i><sup>&minus;2<i>t</i></sup>)/<i>t dt</i> &nbsp;(ii) <i>L</i>{{<i>e</i><sup>&minus;3<i>t</i></sup><i>t</i><sup>8</sup>}}","T2-09"),
  ("3a","06",f"(i) {inv}{{(<i>s</i><sup>3</sup>+6<i>s</i><sup>2</sup>+12<i>s</i>+8)/<i>s</i><sup>6</sup>}} &nbsp;(ii) {inv}{{(<i>se</i><sup>&minus;<i>s</i>/2</sup>+{pi}<i>e</i><sup>&minus;<i>s</i></sup>)/(<i>s</i><sup>2</sup>+{pi}<sup>2</sup>)}}","T2-08"),
  ("3b","07",f"{inv}{{<i>s</i><sup>2</sup>/((<i>s</i><sup>2</sup>+<i>a</i><sup>2</sup>)(<i>s</i><sup>2</sup>+<i>b</i><sup>2</sup>))}} by convolution.","T1-11"),
  ("3c","07","Particle on a plane curve: <i>y</i>&prime;+2<i>x</i>=sin&nbsp;2<i>t</i>, <i>x</i>&prime;&minus;2<i>y</i>=cos&nbsp;2<i>t</i>; show 4<i>x</i><sup>2</sup>+4<i>xy</i>+5<i>y</i><sup>2</sup>=4.","T2-05"),
  ("4a","06",f"{inv}{{log((<i>s</i><sup>2</sup>+1)/(<i>s</i>(<i>s</i>+1)))}}","T1-09"),
  ("4b","07","Heaviside form of <i>t</i><sup>2</sup> / 4<i>t</i> / 8 and its LT.","T1-08"),
  ("4c","07","Solve <i>y</i>&#8244;+2<i>y</i>&Prime;&minus;<i>y</i>&prime;&minus;2<i>y</i>=0, <i>y</i>(0)=0, <i>y</i>&prime;(0)=0, <i>y</i>&Prime;(0)=6.","T2-05"),
  ("5a","06",f"Reflection in <i>y</i>-axis, rotation {pi}/6, dilation 3/2. Image of {U21}.","T2-02"),
  ("5b","07",f"<i>T</i>(<i>x</i>,<i>y</i>) = (3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>): linear? Images of (1,2), (2,&minus;5).","T2-04"),
  ("5c","07",f"Transition matrix from <i>B</i>={{(2,3),(1,2)}} to <i>B</i>&prime;={{(1,0),(0,1)}}; <i>u<sub>B</sub></i>={V(['1','2'])}.","T1-07"),
  ("6a","06","Is (4,&minus;4,6) a linear combination of (1,2,&minus;3), (2,&minus;4,6), (&minus;1,2,&minus;3)?","T2-12"),
  ("6b","07",f"Show <i>T</i>(<i>X</i>)=<i>AX</i> rotates <i>x</i> through {th}, <i>A</i>={A_ROT}.","T1-10"),
  ("6c","07",f"Range and kernel of <i>T</i>(<i>x</i>,<i>y</i>)=(3<i>x</i>, <i>x</i>&minus;<i>y</i>, <i>y</i>); verify rank&ndash;nullity.","T2-03"),
  ("7a","10",f"Four fundamental subspaces of <i>A</i>={A_SUB}.","T1-03"),
  ("7b","10","Least-squares for the 6&times;4 block-design matrix with <i>b</i>=(&minus;3,&minus;1,0,2,5,1).","T1-02"),
  ("8a","10",f"Complete solution: <i>A</i>={M([['1','0','2','3'],['1','3','2','0'],['2','0','4','9']])}, <i>B</i>={V(['2','5','10'])}.","T2-07"),
  ("8b","10",f"QR factorization of <i>A</i>={A_LS}.","T2-01"),
  ("9a","10",f"Diagonalize <i>A</i>={M([['1','1','3'],['1','5','1'],['3','1','1']])}; find <i>A</i><sup>4</sup>.","T2-11"),
  ("9b","10",f"(i) Is {A_HERM} Hermitian? &nbsp;(ii) Is {A_PD} positive definite?","T1-12 / T1-05"),
  ("10a","10",f"Orthogonally diagonalize <i>A</i>={A_ORTH}.","T1-01"),
  ("10b","10",f"SVD of <i>A</i>={M([['1',sp+'1'],[sp+'2','2'],['2',sp+'2']])}.","T1-06"),
 ])

paper("Paper M &mdash; MAKE UP EXAMINATIONS, JUNE 2023",
 "Course: Linear Algebra and Laplace Transforms &middot; Code CS/IS/AI/AD31",
 [("1a","06","(i) Define a periodic function with an example &nbsp;(ii) <i>L</i>{(cos&nbsp;4<i>t</i>&minus;cos&nbsp;2<i>t</i>)/<i>t</i>}","T2-15 / T2-10"),
  ("1b","07","Prove <i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup>n</sup><i>d<sup>n</sup></i>{<i>F</i>(<i>s</i>)}/<i>ds<sup>n</sup></i>.","T1-04"),
  ("1c","07",f"Given <i>L</i>{{sin&nbsp;{sq}<i>t</i>}}, show <i>L</i>{{cos&nbsp;{sq}<i>t</i>/{sq}<i>t</i>}}.","T1-13"),
  ("2a","06",f"(i) <i>L</i>{{<i>e</i><sup>&minus;2<i>t</i></sup>(2cos&nbsp;5<i>t</i> sin&nbsp;3<i>t</i>)}} &nbsp;(ii) <i>L</i>{{{INT}<sub>0</sub><sup><i>t</i></sup><i>te</i><sup>&minus;<i>t</i></sup>cos&nbsp;<i>t dt</i>}}","T2-10"),
  ("2b","07",f"Prove <i>L</i>{{<i>f</i>(<i>t</i>)/<i>t</i>}} = {INT}<sub>s</sub><sup>{inf}</sup><i>F</i>(<i>s</i>)<i>ds</i>; hence <i>L</i>{{sin&nbsp;4<i>t</i>/<i>t</i>}}.","T3-07"),
  ("2c","07","Triangular wave of period 2<i>a</i>.","T1-14"),
  ("3a","06",f"(i) {inv}{{<i>e</i><sup>&minus;<i>s</i></sup>(<i>s</i>+2)/(<i>s</i>+1)<sup>2</sup>}} &nbsp;(ii) {inv}{{tan<sup>&minus;1</sup>(2/<i>s</i>)}}","T2-08"),
  ("3b","07",f"{inv}{{<i>s</i><sup>2</sup>/((<i>s</i><sup>2</sup>+<i>a</i><sup>2</sup>)(<i>s</i><sup>2</sup>+<i>b</i><sup>2</sup>))}} by convolution.","T1-11"),
  ("3c","07","Solve <i>y</i>&Prime;+4<i>y</i>&prime;+3<i>y</i> = <i>e</i><sup>&minus;<i>t</i></sup>, <i>y</i>(0)=0, <i>y</i>&prime;(0)=0.","T2-05"),
  ("4a","06",f"{inv}{{(5<i>s</i>+3)/((<i>s</i>&minus;1)(<i>s</i><sup>2</sup>+2<i>s</i>+5))}}","T2-08"),
  ("4b","07",f"Heaviside form of cos&nbsp;<i>t</i> / cos&nbsp;2<i>t</i> / cos&nbsp;3<i>t</i> on (0,{pi}), ({pi},2{pi}), (2{pi},{inf}).","T1-08"),
  ("4c","07","Particle on a plane curve &rarr; 4<i>x</i><sup>2</sup>+4<i>xy</i>+5<i>y</i><sup>2</sup>=4.","T2-05"),
  ("5a","06","Is (1,&minus;2) a linear combination of (2,4) and (3,6)?","T2-12"),
  ("5b","07","<i>T</i>(<i>x</i>,<i>y</i>) = (2<i>x</i>, <i>x</i>+<i>y</i>): linear? Images of (1,2), (&minus;1,&minus;4).","T2-04"),
  ("5c","07",f"Transition matrix <i>B</i>={{(1,2),(3,&minus;1)}} {ARR} <i>B</i>&prime;={{(1,0),(0,1)}}; <i>U<sub>B</sub></i>={V(['3','4'])}.","T1-07"),
  ("6a","06","Define linear dependence/independence; test {(1,0,1),(2,1,3),(&minus;1,3,2)}.","T2-12"),
  ("6b","07",f"Define kernel and range; verify rank&ndash;nullity for {M([['1','2'],['3','0']])}.","T2-03"),
  ("6c","07",f"Reflection in <i>x</i>-axis, rotation {pi}/2, contraction 1/2. Image of {V(['4',sp+'1'])}.","T2-02"),
  ("7a","10",f"Basis for col(<i>A</i>) and nul(<i>A</i>) of <i>A</i>={A_SUB}.","T1-03"),
  ("7b","10","Complete solution of a 3&times;4 system, choosing an appropriate <i>B</i>.","T2-07"),
  ("8a","10",f"QR factorization of <i>A</i>={M([['1','0','0'],['1','1','0'],['1','1','1'],['1','1','1']])}.","T2-01"),
  ("8b","10",f"Least-squares: <i>A</i>={A_LS}, <i>b</i>={B_LS}.","T1-02"),
  ("9a","10",f"Orthogonally diagonalize <i>A</i>={A_ORTH}.","T1-01"),
  ("9b","10",f"(i) Is {M([['0','2+<i>i</i>','1'],['2&minus;<i>i</i>','<i>i</i>','0'],['1','0','1']])} Hermitian? &nbsp;(ii) Is {M([['8',sp+'6','2'],[sp+'6','7',sp+'4'],['2',sp+'4','3']])} positive definite?","T1-12 / T1-05"),
  ("10a","10",f"(i) Diagonalize {M([[sp+'1','4'],['0','3']])}, find <i>A</i><sup>5</sup> &nbsp;(ii) Is &frac12;{M([['1+<i>i</i>','1&minus;<i>i</i>'],['1&minus;<i>i</i>','1+<i>i</i>']])} unitary?","T2-11 / T2-13"),
  ("10b","10",f"SVD of <i>A</i>={A_SVD}.","T1-06"),
 ])

paper("Paper S &mdash; BACKLOG SUBJECT EXAMINATIONS, AUGUST / SEPTEMBER 2023",
 "Course: Linear Algebra and Laplace Transforms &middot; Code CS/IS/AI/AD31",
 [("1a","06",f"(i) <i>L</i>{{<i>te</i><sup>&minus;<i>t</i></sup>sin&nbsp;3<i>t</i>}} &nbsp;(ii) <i>L</i>{{(1&minus;<i>e<sup>t</sup></i>)/<i>t</i>}}","T2-10"),
  ("1b","07",f"Periodic function of period 2{pi}: <i>t</i> on (0,{pi}), {pi}&minus;<i>t</i> on ({pi},2{pi}).","T2-06"),
  ("1c","07",f"Evaluate {INT}<sub>0</sub><sup>{inf}</sup><i>te</i><sup>&minus;2<i>t</i></sup>cos&nbsp;3<i>t dt</i>.","T2-09"),
  ("2a","06",f"Show <i>L</i>{{sin&nbsp;{sq}<i>t</i>}} = ({sq}{pi}/2<i>s</i><sup>3/2</sup>)<i>e</i><sup>&minus;1/4<i>s</i></sup>.","T1-13"),
  ("2b","07","Prove <i>L</i>{(sinh&nbsp;<i>at</i>)<i>f</i>(<i>t</i>)} = &frac12;[<i>F</i>(<i>s</i>&minus;<i>a</i>)&minus;<i>F</i>(<i>s</i>+<i>a</i>)]; evaluate <i>L</i>[<i>t</i><sup>8</sup>sinh&nbsp;2<i>t</i>].","T3-07"),
  ("2c","07","Prove <i>L</i>{<i>t<sup>n</sup>f</i>(<i>t</i>)} = (&minus;1)<sup>n</sup><i>d<sup>n</sup></i>[<i>F</i>(<i>s</i>)]/<i>ds<sup>n</sup></i>.","T1-04"),
  ("3a","06","State and prove the convolution theorem.","T1-11 / T3-07"),
  ("3b","07",f"Heaviside form of 1 / <i>t</i> / <i>t</i><sup>2</sup> on (0,1], (1,2], (2,{inf}).","T1-08"),
  ("3c","07","Solve <i>dx/dt</i>&minus;<i>y</i>=<i>e</i><sup>&minus;<i>t</i></sup>, <i>dy/dt</i>+<i>x</i>=sin&nbsp;<i>t</i>, <i>x</i>(0)=1, <i>y</i>(0)=0.","T2-05"),
  ("4a","06",f"{inv}{{log((<i>s</i><sup>2</sup>+9)/(<i>s</i>(<i>s</i>+9)(<i>s</i>&minus;9)))}}","T1-09"),
  ("4b","07","Solve <i>y</i>&Prime;+4<i>y</i>&prime;+3<i>y</i>=<i>e</i><sup>&minus;<i>t</i></sup>, <i>y</i>(0)=<i>y</i>&prime;(0)=1.","T2-05"),
  ("4c","07",f"{inv}{{<i>s</i><sup>2</sup>/((<i>s</i><sup>2</sup>+1)(<i>s</i><sup>2</sup>+4))}} by convolution.","T1-11"),
  ("5a","06","Do {(1,2,3), (&minus;1,&minus;1,0), (2,5,4)} span <i>R</i><sup>3</sup>? Express (1,3,&minus;2).","T2-12"),
  ("5b","07","<i>T</i>(<i>x</i>,<i>y</i>)=(3<i>x</i>+<i>y</i>, 2<i>y</i>, <i>x</i>&minus;<i>y</i>): linear? Images of (1,2), (2,&minus;5).","T2-04"),
  ("5c","07",f"Kernel and range dimensions for {M([['1',sp+'2','3','5'],['1',sp+'1','8','7'],['2',sp+'4','6','10']])}.","T2-03"),
  ("6a","06",f"Reflection in <i>x</i>-axis, rotation {pi}/2, dilation 3. Image of {U21}.","T2-02"),
  ("6b","07","State and verify rank&ndash;nullity for <i>T</i>(<i>x</i>,<i>y</i>)=(3<i>x</i>, <i>x</i>&minus;<i>y</i>, <i>y</i>).","T2-03"),
  ("6c","07",f"<i>B</i>={{(1,2),(3,&minus;1)}} {ARR} <i>B</i>&prime;={{(3,1),(5,2)}}; <i>u<sub>B</sub></i>={U21}.","T1-07"),
  ("7a","10",f"QR factorization of <i>A</i>={M([['1','0','0'],['1','1','0'],['1','1','1']])}.","T2-01"),
  ("7b","10",f"Basis and dimension of nul(<i>A</i>) and col(<i>A</i>) for {M([[sp+'3','9',sp+'2',sp+'7'],['2',sp+'6','4','8'],['3',sp+'9',sp+'2','2']])}.","T1-03"),
  ("8a","10","Gram&ndash;Schmidt orthonormal basis for span{(1,1,1,1), (0,1,1,1), (0,0,1,1)}.","T3-03"),
  ("8b","10",f"Least-squares: <i>A</i>={M([['4','0'],['0','2'],['1','1']])}, <i>b</i>={V(['2','0','11'])}.","T1-02"),
  ("9a","10",f"Diagonalize <i>A</i>={M([['1',sp+'1'],['2','4']])}; find <i>A</i><sup>6</sup>.","T2-11"),
  ("9b","10",f"SVD of <i>A</i>={M([['4','11','14'],['8','7',sp+'2']])}.","T1-06"),
  ("10a","10",f"Orthogonally diagonalize <i>A</i>={M([['3','1'],['1','3']])}.","T1-01"),
  ("10b","10",f"(i) Is {A_HERM} Hermitian? &nbsp;(ii) Is 3<i>x</i><sup>2</sup>+5<i>y</i><sup>2</sup>+3<i>z</i><sup>2</sup>&minus;2<i>yz</i>+2<i>zx</i>&minus;2<i>xy</i> positive definite?","T1-12 / T2-14"),
 ])

w("""<div class="foot">
<b>24CS31 &mdash; SEE Prediction Sheet.</b> Built by transcribing four previous question papers question-by-question
from the page images, cross-tabulating all 40 questions by topic and question slot, and filtering the result against
the official 24CS31 syllabus. Frequencies, pairing laws and the back-test are computed from that table and are
reproducible from &sect;11. Predictions are inferences from four papers &mdash; a strong pattern, not a guarantee.
Study the syllabus, use this to prioritise.
</div>""")

# ============================== EMIT ==============================
doc = ("<!doctype html><html><head><meta charset='utf-8'>"
       "<title>24CS31 SEE Prediction Sheet</title><style>" + CSS + "</style></head><body>"
       + "".join(H) + "</body></html>")
import io, os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "24CS31_Prediction_Sheet.html")
io.open(out, "w", encoding="utf-8").write(doc)
print("wrote", out, len(doc), "bytes")

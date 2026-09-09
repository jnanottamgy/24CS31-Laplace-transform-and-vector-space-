# 24CS31 — Laplace Transforms & Vector Space

Reference notes extracted from the official curriculum PDF
(`syllabus/MSRIT_CSE_III-IV-Sem_Syllabus_2025-26_Batch2024.pdf`, pages 16–18).

---

## 1. Course Identity

| Field | Value |
|---|---|
| Course Title | Laplace Transforms & Vector Space |
| Course Code | **CS31** (full code `24CS31` — the `24` prefix is the batch year) |
| Semester | III Semester, B.E. Computer Science and Engineering |
| Batch / AY | Batch 2024 · Academic Year 2025–2026 |
| Institute | Ramaiah Institute of Technology (MSRIT), Bengaluru — Autonomous, affiliated to VTU |
| Teaching Department | **Mathematics** (not CSE) |
| Category | **BSC** — Basic Science Course |
| Credits (L:T:P) | **2 : 1 : 0** → **3 total credits** |
| Contact Hours | **30L + 30T + 30S** (L = Lecture, T = Tutorial, S = Self-learning) |
| Weekly Load | L = 2, T = 2, P = 0, S = 2 hours/week |
| Pre-requisites | Calculus and Basics of Linear Algebra |
| Course Coordinator | Dr. Govindaraju M V |

> Credit definition used by the scheme: 1 credit = 1 hr/week lecture, or 2 hrs/week tutorial,
> or 2 hrs/week practical, or 1 hr/week self-learning.

---

## 2. Course Content — Five Units

### Unit I — Laplace Transforms
Definition; transforms of elementary functions; properties of Laplace transforms; existence
conditions; transform of derivatives; transform of integrals; multiplication by `tⁿ`; division by
`t`; evaluation of integrals by Laplace transforms; transform of a periodic function.

### Unit II — Application of Laplace Transforms
Unit-step function; unit-impulse function; inverse transforms; convolution theorem; solution of
linear differential equations and simultaneous linear differential equations using Laplace
transforms; engineering applications.

### Unit III — Vector Space and Linear Transformation
Vector space; linear combination and span; linearly independent and dependent vectors; basis and
dimension; linear transformations; matrix of transformations; rotation about the origin; dilation,
contraction and reflection; composition of matrix transformations; kernel and range; change of basis.

### Unit IV — Orthogonal Projections
The null space of `A`; solving `Ax = 0` and `Rx = 0`; the complete solution to `Ax = b`; dimensions
of the four subspaces; orthogonality of the four subspaces; projections; orthonormal bases and the
Gram–Schmidt method; QR-factorization; least-squares approximations.

### Unit V — Applications of Eigenvalue Decomposition
Introduction to eigenvalues and eigenvectors; similarity and diagonalization; symmetric matrices;
complex matrices; Hermitian and unitary matrices; positive definite matrices; the singular value
decomposition (SVD); principal component analysis (PCA); applications to linear recurrence
relations; quadratic forms and conic sections.

**Shape of the course:** Units I–II are the *transform* half (integral transforms → ODE solving);
Units III–V are the *linear algebra* half, building Vector spaces → Orthogonality/least-squares →
Eigen/SVD/PCA.

---

## 3. Course Outcomes (COs)

At the end of the course, students will be able to:

| CO | Outcome | Mapping |
|---|---|---|
| CO1 | Evaluate Laplace Transforms of a given function and understand their properties | PO-1, 2 & PSO-2, 3 |
| CO2 | Obtain inverse Laplace transforms and use them to solve systems of ODEs | PO-1, 2 & PSO-2, 3 |
| CO3 | Obtain the matrix of a linear transformation | PO-1, 2 & PSO-2, 3 |
| CO4 | Solve systems of equations by the Least-Squares method | PO-1, 2 & PSO-2, 3 |
| CO5 | Obtain the eigenvalue decomposition of a matrix and use it to study SVD and PCA | PO-1, 2 & PSO-2, 3 |

**Referenced outcomes:**
- **PO1** Engineering Knowledge — apply mathematics, natural science, computing and engineering fundamentals.
- **PO2** Problem Analysis — identify, formulate, review literature and analyze complex engineering problems.
- **PSO2** Apply mathematical foundations, algorithmic principles and CS theory in modeling and design of computer-based systems.
- **PSO3** Apply software design and development practices in emerging areas — IoT, Data Analytics, Social Networks, Cloud and HPC.

---

## 4. Assessment and Evaluation

### Continuous Internal Evaluation (CIE) — 50 marks

| Assessment Tool | Marks | COs addressed |
|---|---|---|
| Internal Test-I | 30 | CO1, CO2, CO3 |
| Internal Test-II | 30 | CO3, CO4, CO5 |
| *Average of the two internal tests scaled to* | **30** | |
| Quiz | 10 | CO1, CO2, CO3 |
| Assignment | 10 | CO3, CO4, CO5 |
| **CIE Total** | **50** | |

### Semester End Examination (SEE) — 100 marks
Covers CO1 – CO5 (all units).

---

## 5. Books

**Text Books**
1. B. S. Grewal — *Higher Engineering Mathematics* — Khanna Publishers — 44th edition, 2017.
2. David C. Lay, Steven R. Lay, Judi J. McDonald — *Linear Algebra and its Applications* — Pearson — 5th edition, 2015.
3. Gilbert Strang — *Linear Algebra and its Applications* — 5th edition, 2016.

**Reference Books**
1. Peter V. O'Neil — *Advanced Engineering Mathematics* — Cengage Learning — 7th edition, 2011.
2. Gareth Williams — *Linear Algebra with Applications* — Jones and Bartlett Press — 9th edition, 2017.
3. Erwin Kreyszig — *Advanced Engineering Mathematics* — Wiley India — 10th edition, 2015.

---

## 6. Pedagogy and Resource Links

Delivery tools for all units: Chalk and talk, PowerPoint presentation, Videos.

**Units I & II (Laplace Transforms)**
- NPTEL: https://nptel.ac.in/courses/111/105/111105134/
- NPTEL: https://nptel.ac.in/courses/111/105/111105035/
- Impartus: https://a.impartus.com/ilc/#/course/119640/593
- Impartus: https://a.impartus.com/ilc/#/course/59742/295

**Units III, IV & V (Linear Algebra)**
- NPTEL: https://nptel.ac.in/courses/111/105/111105035/
- NPTEL: https://nptel.ac.in/courses/111/102/111102152/
- Impartus: https://a.impartus.com/ilc/#/course/621524/1030
- Impartus: https://a.impartus.com/ilc/#/course/619570/1030

---

## 7. Context — Full III Semester Scheme (CSE, Batch 2024)

| # | Code | Course | Dept | Category | L:T:P | Credits |
|---|---|---|---|---|---|---|
| 1 | **CS31** | **Laplace Transforms & Vector Space** | **Mathematics** | **BSC** | **2:1:0** | **3** |
| 2 | CS32 | Digital Design and Computer Organization | CSE | PCC (IC) | 3:0:1 | 4 |
| 3 | CS33 | Data Structures | CSE | PCC | 3:0:0 | 3 |
| 4 | CS34 | Object Oriented Programming | CSE | PCC | 3:0:0 | 3 |
| 5 | CS35 | Discrete Mathematical Structures | CSE | PCC | 2:1:0 | 3 |
| 6 | CSL36 | Data Structures Laboratory | CSE | PCC | 0:0:1 | 1 |
| 7 | CSL37 | Object Oriented Programming Laboratory | CSE | PCC | 0:0:1 | 1 |
| 8 | UHV38 | Universal Human Values | CSE | UHV | 2:0:0 | 2 |
| 9 | CSAEC39 | Ability Enhancement Course-III | CSE | AEC | 1:0:0 | 1 |
| | | **Total** | | | **16:2:3** | **21** |

Non-credit mandatory courses (NCMC): PE69 Physical Education / YO69 Yoga / NS69 NSS (register in
III sem, attend III–VI); AM31 Additional Mathematics-I (lateral entry students only).

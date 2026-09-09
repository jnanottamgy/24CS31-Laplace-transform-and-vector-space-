#!/usr/bin/env python3
"""Coverage audit: every part-slot of all 4 papers vs the cram sheet's topic rows."""
CRAM = {  # topic keys the cram sheet teaches
 'tn_proof','sqrt_t','mult_div_t','improper_int','periodic','sqrt_cube','defn1',
 'heaviside','ode','convolution','log_inv','short_inv','defn2',
 'composition','transition','kernel_range','prove_linear','span_basis','rotation_proof',
 'qr','least_sq','four_sub','complete_sol','projection','gram_schmidt',
 'orth_diag','pos_def','unitary_herm','svd','quad_form','markov','diag_an'}

# (paper, question, marks, unit, [topic keys in that part])
P = []
def add(paper,q,mk,unit,*keys): P.append((paper,q,mk,unit,list(keys)))

# ---- APRIL 2023 ----
add("APR23","1a",6,1,"sqrt_cube","transform_integral"); add("APR23","1b",7,1,"mult_div_t")
add("APR23","1c",7,1,"periodic")
add("APR23","2a",6,1,"sqrt_t"); add("APR23","2b",7,1,"tn_proof"); add("APR23","2c",7,1,"improper_int","mult_div_t")
add("APR23","3a",6,2,"short_inv"); add("APR23","3b",7,2,"convolution"); add("APR23","3c",7,2,"ode")
add("APR23","4a",6,2,"log_inv"); add("APR23","4b",7,2,"heaviside"); add("APR23","4c",7,2,"ode")
add("APR23","5a",6,3,"composition"); add("APR23","5b",7,3,"prove_linear"); add("APR23","5c",7,3,"transition")
add("APR23","6a",6,3,"span_basis"); add("APR23","6b",7,3,"rotation_proof"); add("APR23","6c",7,3,"kernel_range")
add("APR23","7a",10,4,"four_sub"); add("APR23","7b",10,4,"least_sq")
add("APR23","8a",10,4,"complete_sol"); add("APR23","8b",10,4,"qr")
add("APR23","9a",10,5,"diag_an"); add("APR23","9b",10,5,"unitary_herm","pos_def")
add("APR23","10a",10,5,"orth_diag"); add("APR23","10b",10,5,"svd")
# ---- JUNE 2023 MAKEUP ----
add("MAKEUP","1a",6,1,"defn1","mult_div_t"); add("MAKEUP","1b",7,1,"tn_proof"); add("MAKEUP","1c",7,1,"sqrt_t")
add("MAKEUP","2a",6,1,"mult_div_t","transform_integral"); add("MAKEUP","2b",7,1,"div_t_proof")
add("MAKEUP","2c",7,1,"periodic")
add("MAKEUP","3a",6,2,"short_inv"); add("MAKEUP","3b",7,2,"convolution"); add("MAKEUP","3c",7,2,"ode")
add("MAKEUP","4a",6,2,"short_inv"); add("MAKEUP","4b",7,2,"heaviside"); add("MAKEUP","4c",7,2,"ode")
add("MAKEUP","5a",6,3,"span_basis"); add("MAKEUP","5b",7,3,"prove_linear"); add("MAKEUP","5c",7,3,"transition")
add("MAKEUP","6a",6,3,"span_basis"); add("MAKEUP","6b",7,3,"kernel_range"); add("MAKEUP","6c",7,3,"composition")
add("MAKEUP","7a",10,4,"four_sub"); add("MAKEUP","7b",10,4,"complete_sol")
add("MAKEUP","8a",10,4,"qr"); add("MAKEUP","8b",10,4,"least_sq")
add("MAKEUP","9a",10,5,"orth_diag"); add("MAKEUP","9b",10,5,"unitary_herm","pos_def")
add("MAKEUP","10a",10,5,"diag_an","unitary_herm"); add("MAKEUP","10b",10,5,"svd")
# ---- AUG/SEP 2023 BACKLOG ----
add("SUPPLY","1a",6,1,"mult_div_t"); add("SUPPLY","1b",7,1,"periodic"); add("SUPPLY","1c",7,1,"improper_int")
add("SUPPLY","2a",6,1,"sqrt_t"); add("SUPPLY","2b",7,1,"sinh_proof"); add("SUPPLY","2c",7,1,"tn_proof")
add("SUPPLY","3a",6,2,"convolution_proof"); add("SUPPLY","3b",7,2,"heaviside"); add("SUPPLY","3c",7,2,"ode")
add("SUPPLY","4a",6,2,"log_inv"); add("SUPPLY","4b",7,2,"ode"); add("SUPPLY","4c",7,2,"convolution")
add("SUPPLY","5a",6,3,"span_basis"); add("SUPPLY","5b",7,3,"prove_linear"); add("SUPPLY","5c",7,3,"kernel_range")
add("SUPPLY","6a",6,3,"composition"); add("SUPPLY","6b",7,3,"kernel_range"); add("SUPPLY","6c",7,3,"transition")
add("SUPPLY","7a",10,4,"qr"); add("SUPPLY","7b",10,4,"four_sub")
add("SUPPLY","8a",10,4,"gram_schmidt"); add("SUPPLY","8b",10,4,"least_sq")
add("SUPPLY","9a",10,5,"diag_an"); add("SUPPLY","9b",10,5,"svd")
add("SUPPLY","10a",10,5,"orth_diag"); add("SUPPLY","10b",10,5,"unitary_herm","quad_form")
# ---- MARCH 2024 (current format) ----
add("MAR24","1a",2,1,"defn1"); add("MAR24","1b",4,1,"sqrt_t"); add("MAR24","1c",7,1,"tn_proof")
add("MAR24","1d",7,1,"improper_int","mult_div_t")
add("MAR24","2a",2,1,"defn1"); add("MAR24","2b",4,1,"sqrt_cube"); add("MAR24","2c",7,1,"mult_div_t")
add("MAR24","2d",7,1,"periodic")
add("MAR24","3a",2,2,"defn2"); add("MAR24","3b",4,2,"log_inv"); add("MAR24","3c",7,2,"heaviside")
add("MAR24","3d",7,2,"ode")
add("MAR24","4a",2,2,"defn2"); add("MAR24","4b",4,2,"short_inv"); add("MAR24","4c",7,2,"convolution")
add("MAR24","4d",7,2,"ode")
add("MAR24","5a",6,3,"span_basis"); add("MAR24","5b",7,3,"prove_linear"); add("MAR24","5c",7,3,"rotation_proof")
add("MAR24","6a",6,3,"composition"); add("MAR24","6b",7,3,"transition"); add("MAR24","6c",7,3,"kernel_range")
add("MAR24","7a",6,4,"complete_sol"); add("MAR24","7b",7,4,"projection"); add("MAR24","7c",7,4,"four_sub")
add("MAR24","8a",10,4,"qr"); add("MAR24","8b",10,4,"least_sq")
add("MAR24","9a",5,5,"quad_form"); add("MAR24","9b",5,5,"markov"); add("MAR24","9c",10,5,"svd")
add("MAR24","10a",5,5,"pos_def"); add("MAR24","10b",5,5,"unitary_herm"); add("MAR24","10c",10,5,"orth_diag")

def frac(keys):
    """fraction of the part the cram sheet covers"""
    hit = sum(1 for k in keys if k in CRAM)
    return hit/len(keys)

print(f"TOTAL PART-SLOTS: {len(P)}   TOTAL MARKS: {sum(x[2] for x in P)}")
gaps={}
for paper,q,mk,u,keys in P:
    f=frac(keys)
    if f<1.0:
        for k in keys:
            if k not in CRAM: gaps.setdefault(k,[]).append((paper,q,mk,round(mk*(1-f))))
print("\n--- UNCOVERED TOPICS ---")
for k,v in sorted(gaps.items(), key=lambda x:-sum(t[3] for t in x[1])):
    print(f"  {k:20s} appears in {len(v)} paper(s), ~{sum(t[3] for t in v)} marks total: "
          + ", ".join(f"{p} {qq} (~{m}m of {mk})" for p,qq,mk,m in v))
covered_marks = sum(mk*frac(keys) for _,_,mk,_,keys in P)
print(f"\nCOVERAGE: {covered_marks:.0f} / {sum(x[2] for x in P)} marks "
      f"= {100*covered_marks/sum(x[2] for x in P):.1f}%")

print("\n--- BEST-QUESTION SCORE PER UNIT PER PAPER (content coverage only) ---")
papers=["APR23","MAKEUP","SUPPLY","MAR24"]
grand={}
for pap in papers:
    tot=0; line=[]
    for u in (1,2,3,4,5):
        opts={}
        for paper,q,mk,uu,keys in P:
            if paper==pap and uu==u:
                qn=int(''.join(c for c in q if c.isdigit()))
                opts.setdefault(qn,0)
                opts[qn]+=mk*frac(keys)
        best=max(opts.values()); tot+=best
        line.append(f"U{u}: {best:.0f}/20 (Q{max(opts,key=opts.get)})")
    grand[pap]=tot
    print(f"  {pap:8s} " + "  ".join(line) + f"   -> TOTAL {tot:.0f}/100")
print(f"\nWORST PAPER (content floor): {min(grand.values()):.0f}/100")

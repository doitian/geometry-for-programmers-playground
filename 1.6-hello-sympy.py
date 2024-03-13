from sympy import symbols, solve, latex, rust_code

Va, Vp, Vpx, D, t = symbols("Va Vp Vpx D t")

r = solve([Vp - Va * Vpx, Va * t + Vp * t - D], (Va, Vp))
print(r)
print(latex(r))
print(rust_code(r))

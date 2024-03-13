from sympy import Matrix, solve, symbols, collect, simplify, rust_code

Px, Py, Pz = symbols("Px Py Pz")
dx, dy, dz = symbols("dx dy dz")
Ax, Ay, Az = symbols("Ax Ay Az")
ABx, ABy, ABz = symbols("ABx ABy ABz")
ACx, ACy, ACz = symbols("ACx ACy ACz")

P = Matrix([Px, Py, Pz])
d = Matrix([dx, dy, dz])
A = Matrix([Ax, Ay, Az])
AB = Matrix([ABx, ABy, ABz])
AC = Matrix([ACx, ACy, ACz])

t, u, v = symbols("t u v")

solution = solve(P + t * d - A - u * AB - v * AC, (t, u, v))

div = collect(
    ABx * ACy * dz
    - ABx * ACz * dy
    - ABy * ACx * dz
    + ABy * ACz * dx
    + ABz * ACx * dy
    - ABz * ACy * dx,
    (dx, dy, dz),
)
print(rust_code(div))
print(rust_code(collect(simplify(solution[t] * div), (ACx, ACy, ACz))))
print(rust_code(collect(simplify(solution[u] * div), (dx, dy, dz))))
print(rust_code(collect(simplify(solution[v] * div), (dx, dy, dz))))

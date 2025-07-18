def M(T, B, lambdas): # Magnetização
    def f(m_):
        Bef = Bef(m_,B,lambdas)
        arg = (g*mb*Bef) / (2*k*T)
        return (g*mb/2) * np.tanh(arg) - m_
    m0 = 1
    sol = fsolve(f, m0)
    return sol[0]
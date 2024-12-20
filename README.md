Point('P1', T=298.00, p=1.00, h=None, s=None, v=85526.00)
Point('P2', T=911.25, p=50.00, h=None, s=None, v=5230.56)

    # Test 1 - T and p
    p1 = Point('P1', T=298.00, p=1.00) #  v=85526.00
    p2 = Point('P2', p=50.00) # v=5230.56
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)

    p1 = Point('P1', p=1.00)
    p2 = Point('P2', T=911.25, p=50.00)
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)

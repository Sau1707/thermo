
class Turbine:
    """
    Properties:
    - Converts enthalpy (or energy) from the fluid into mechanical work
    - Isentropic expansion: s1 = s2 = s

    # Lecture 2 - Slide 8
    - p_in up to 300 bar
    - T_in up to 650°C
    - Expansion up to very low pressures into the wet steam area
    - Steady-state operation
    - No heat transfer to turbine and pump

    => P_12 = \dot{m} * (h_1 - h_2)

    Have an efficiency -> two points T_2 and T_2s

    where:
    μ = (h_2s - h_1) / (h_2 - h_1) = (T_2s - T_1) / (T_2 - T_1)
    if not given -> 1
    """

    def __init__(self):
        pass



    
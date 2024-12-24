import os
import pandas as pd
from dataclasses import dataclass


@dataclass
class RowSaturated:
    p: float # Pressure [bar]
    T: float # Temperature [°C]
    v_f: float # Specific volume - saturated liquid [m^3/kg] 
    v_g : float # Specific volume - saturated vapor [m^3/kg]
    u_f: float # Specific internal energy - saturated liquid [kJ/kg]
    u_g: float # Specific internal energy - saturated vapor [kJ/kg]
    h_f: float # Specific enthalpy - saturated liquid [kJ/kg]
    h_g: float # Specific enthalpy - saturated vapor [kJ/kg]
    s_f: float # Specific entropy - saturated liquid [kJ/kgK]
    s_g: float # Specific entropy - saturated vapor [kJ/kgK]


class TableSaturated(pd.DataFrame):
    def __init__(self):
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), "saturated.csv"))
        super().__init__(df)

    def get(self, **kwargs) -> RowSaturated:
        assert len(kwargs) == 1, "Only one argument is allowed"
        key, value = list(kwargs.items())[0]
        df = self.sort_values(by=key)

        # TODO: Check that the value is within the table

        # Find the two rows surrounding the target value
        below = df[df[key] <= value].iloc[-1]
        above = df[df[key] > value].iloc[0]

         # Perform linear interpolation for all columns
        interpolated_row = below + (value - below[key]) / (above[key] - below[key]) * (above - below)
        return RowSaturated(**interpolated_row)


@dataclass
class RowSuperheated:
    p: float # Pressure [bar]
    T: float # Temperature [°C]
    v: float # Specific volume [m^3/kg]
    u: float # Specific internal energy [kJ/kg]
    h: float # Specific enthalpy [kJ/kg]
    s: float # Specific entropy [kJ/kgK]

    def __init__(self):
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), "saturated.csv"))
        super().__init__(df)


class TableSuperheated:
    """"""


class Table:
    """Generic Table Class"""

    def __init__(self, pressure: float):
        self.pressure = pressure
        self.data = {}

    def add(self, T: float, *, v: float, u: float, h: float, s: float):
        self.data[T] = {
            "v": v,
            "u": u,
            "h": h,
            "s": s
        }

    def get(self, T: float) -> dict[str, float]:
        # If the temperature is in the table, return the values
        if T in self.data:
            return self.data[T]
        
        # Sort the table keys (temperatures)
        sorted_temps = sorted(self.data.keys())

        # Find the two closest temperatures for interpolation
        for i in range(len(sorted_temps) - 1):
            T1, T2 = sorted_temps[i], sorted_temps[i + 1]
            if not (T1 <= T <= T2):
                continue

            # Perform linear interpolation for each property
            interpolated_data = {}
            for key in self.data[T1]:
                value1 = self.data[T1][key]
                value2 = self.data[T2][key]
                interpolated_data[key] = value1 + (value2 - value1) * (T - T1) / (T2 - T1)

            return interpolated_data


class SteamTables:
    """
    Steam Tables
    -> Contains all the tables for steam
    """

    def __init__(self):
        self.tables: dict[float, Table] = {}

    def add_table(self, table: Table):
        self.tables[(table.pressure)] = table

    def get_values(self, p: float, T: float) -> dict[str, float]:
        # TODO: Interpolate the values
        return self.tables[(p)].get(T)
    

t80 = Table(80)
t80.add(T=295.06, v=0.02352, u=2569.8, h=2758.0, s=5.7432)
t80.add(T=320.00, v=0.02682, u=2662.7, h=2877.2, s=5.9489)
t80.add(T=360.00, v=0.03089, u=2772.7, h=3019.8, s=6.1819)
t80.add(T=400.00, v=0.03432, u=2863.8, h=3138.3, s=6.3634)
t80.add(T=440.00, v=0.03742, u=2946.7, h=3246.1, s=6.5190)
t80.add(T=480.00, v=0.04034, u=3025.7, h=3348.4, s=6.6586)
t80.add(T=520.00, v=0.04313, u=3102.7, h=3447.7, s=6.7871)
t80.add(T=560.00, v=0.04582, u=3178.7, h=3545.3, s=6.9072)
t80.add(T=600.00, v=0.04845, u=3254.4, h=3642.0, s=7.0206)
t80.add(T=640.00, v=0.05102, u=3330.1, h=3738.3, s=7.1283)
t80.add(T=700.00, v=0.05481, u=3443.9, h=3882.4, s=7.2812)
t80.add(T=740.00, v=0.05729, u=3520.4, h=3978.7, s=7.3782)


stream_tables = SteamTables()
stream_tables.add_table(t80)

TABLE_SATURATED = TableSaturated()

if __name__ == "__main__":
    row = TABLE_SATURATED.get(s_g=6.6586)
    assert round(row.p, 2) == 8.1, "Test failed"
    assert round(row.h_g, 2) == 2769.60, "Test failed"

    # Tutorial 2 - b) 1
    data = stream_tables.get_values(80, 480)
    print(data)
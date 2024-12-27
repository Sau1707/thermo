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
    def __init__(self, csv: str):
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), csv))
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



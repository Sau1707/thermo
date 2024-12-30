import os
import pandas as pd
from dataclasses import dataclass


@dataclass
class RowOverheated:
    p: float # Pressure [bar]
    T: float # Temperature [°C]
    v: float # Specific volume [m^3/kg]
    u: float # Specific internal energy [kJ/kg]
    h: float # Specific enthalpy [kJ/kg]
    s: float # Specific entropy [kJ/kgK]


class TableOverheated(pd.DataFrame):
    """"""
    def __init__(self, csv: str):
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), csv))
        super().__init__(df)

    def get(self, T: float, p: float) -> RowOverheated:
        # We can either interpolate using p or T
        df = pd.DataFrame()
        if len(df := self[self["p"] == p]) > 1:
            key, value = "T", T
        elif len(df := self[self["T"] == T]) > 1:
            key, value = "p", p

        assert not df.empty, "No data found"

        df = df.sort_values(by=key)

        # Find the two rows surrounding the target value
        below = df[df[key] <= value].iloc[-1]
        above = df[df[key] > value].iloc[0]

        # Perform linear interpolation for all columns
        interpolated_row = below + (value - below[key]) / (above[key] - below[key]) * (above - below)
        return RowOverheated(**interpolated_row)

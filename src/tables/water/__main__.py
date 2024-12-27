from ..saturated import TableSaturated
from ..overheated import TableOverheated

TABLE_SATURATED = TableSaturated("./water/saturated.csv")
TABLE_OVERHEATED = TableOverheated("./water/overheated.csv")

if __name__ == "__main__":
    row = TABLE_SATURATED.get(s_g=6.6586)
    
    # Tutorial 2 - b) 1
    assert round(row.p, 2) == 8.1, "Test failed"
    assert round(row.h_g, 2) == 2769.60, "Test failed"

    # NOTE: The values in the table might be wrong
    # The fist value is used as search key, and the second for interpolation
    row = TABLE_OVERHEATED.get(T=440, p=8.10)

    # Tutorial 2 - b) 3
    assert round(row.p, 2) == 8.1, "Test failed"
    assert round(row.h, 2) == 3351.83, "Test failed"
    assert round(row.s, 4) == 7.6952, "Test failed"
    
import polars as pl
from random import uniform
from datetime import date
df = pl.DataFrame({'dtm': [date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3)], 'num': [uniform(-500, 500), uniform(-500, 500), uniform(-500, 500)], 'val': [10000, 20000, 30000]})
df.write_excel(None,  None, column_widths=None, autofit=False, position='A1', conditional_formats=None, sparklines=None, column_totals=None, float_precision=3, row_heights=None, table_style=None, dtype_formats=None, autofilter=True, table_name=None, column_formats=None, has_header=True)
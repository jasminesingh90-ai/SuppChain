#! /usr/bin/env python3

import sys
import pandas

def year_total(orders):
    return pandas.DataFrame({
        "SKU": orders["SKU"],
        "SUM": orders.iloc[:, 1:].sum(axis=1)
    })

def sku_total(totals):
    return totals.groupby("SKU")["SUM"].sum().reset_index()

def main():
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
        orders = pandas.read_csv(file_name)

        print(sku_total(year_total(orders))) 
    else:
        print("Error: No data file provided.", file=sys.stderr)

if __name__ == '__main__':
    main()

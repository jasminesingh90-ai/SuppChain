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

def print_errors(messages):
    for message in messages:
        print("Error: " + message, file=sys.stderr)

def main():
    file_name = None
    orders = None
    errors = [];

    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    else:
        errors.append("No data file provided.")

    if file_name is not None:
        try:
            orders = pandas.read_csv(file_name)
        except FileNotFoundError:
            errors.append("File %s does not exist." % file_name)
    
    if len(errors) == 0:
        print(sku_total(year_total(orders))) 
    else:
        print_errors(errors)

if __name__ == '__main__':
    main()

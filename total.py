import pandas as pandas

def total(orders):
    return pandas.DataFrame({
        "SKU": orders["SKU"],
        "SUM": orders.iloc[:, 1:].sum(axis=1)
    })

def main():
    orders = pandas.read_csv("orders.csv")

    print(total(orders))

if __name__ == '__main__':
    main()

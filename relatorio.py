import pandas as pd

def gerar_relatorio(escolhidos):
    df = pd.DataFrame(escolhidos)
    df.columns = ["nome", "energia", "co2", "processamento", "custo"]

    print("\n=== RELATÓRIO FINAL ===\n")
    print(df)
    print("\nTotal energia:", df["energia"].sum())
    print("Total processamento:", df["processamento"].sum())
    print("Total CO2:", df["co2"].sum())
    print("Total custo:", df["custo"].sum())

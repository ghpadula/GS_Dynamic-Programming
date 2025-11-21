import pandas as pd

def gerar_datacenters():
    data = [
        ("SolarCloud_A1", 500, 50, 200, 100000),
        ("HydroEdge_01", 300, 20, 150, 80000),
        ("WindNode_X3", 450, 30, 170, 90000),
        ("GeoGreen_44", 600, 40, 220, 110000),
        ("FusionCore_1", 350, 10, 250, 150000),
        ("EcoByte_77", 280, 15, 120, 70000),
        ("SunFlow_9", 520, 52, 230, 95000),
        ("BlueHydra_5", 260, 18, 140, 76000),
        ("TerraGrid_02", 400, 25, 180, 90000),
        ("CarbonZero_A7", 320, 12, 160, 85000),
        ("QuantumEdge_8", 410, 33, 190, 100000),
        ("EcoCompute_S1", 305, 14, 125, 70000),
        ("CloudRiver_B2", 420, 28, 175, 87000),
        ("SunPeak_C3", 520, 50, 210, 92000),
        ("HydroTech_L4", 340, 17, 150, 88000),
        ("AirCool_92", 380, 22, 165, 89000),
        ("GeoPower_T3", 560, 45, 205, 100000),
        ("ZeroCO2_K9", 295, 11, 130, 72000),
        ("NanoCloud_55", 310, 16, 145, 76000),
        ("SunNeutral_Z0", 330, 13, 155, 81000)
    ]

    df = pd.DataFrame(data, columns=["nome", "energia", "co2", "processamento", "custo"])
    return df

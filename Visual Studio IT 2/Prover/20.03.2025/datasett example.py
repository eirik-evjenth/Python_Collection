# Bar plots for bool verdier
boolean_columns = ['Diabetes_binary', 'HighBP', 'HighChol', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk']
for col in boolean_columns:
    plt.figure(figsize=(8, 6))
    df[col].value_counts(normalize=True).plot(kind='bar', color=['lightcoral', 'lightgreen'])
    plt.title(f'Prosenter av {col}')
    plt.xlabel(f'{col} (0: Nei, 1: Ja)')
    plt.ylabel('Proporsjon')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()



import matplotlib.pyplot as plt
import pandas as pd
import csv


filnavn = "diabetes_binary_health_indicators_BRFSS2015.csv"


df = pd.read_csv(filnavn, delimiter=",", encoding="utf-8")

print(df.head())
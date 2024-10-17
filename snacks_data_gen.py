import pandas as pd
import numpy as np
from datetime import timedelta

np.random.seed(42)

num_students = 100
num_days = 7
snacks = ["Pizza", "Chips", "Fruit", "Chocolate", "Nuts"]

# Students dataset
students_data = []
for i in range(1, num_students + 1):
    age = np.random.randint(18, 25)
    major = np.random.choice(
        ["Engineering", "Arts", "Business", "Science", "Social Sciences"]
    )
    favorite_snack = np.random.choice(snacks)
    meme_quality = np.random.uniform(1, 10)  # Self-reported meme quality score
    students_data.append([f"S{i:03}", age, major, favorite_snack, meme_quality])

students_df = pd.DataFrame(
    students_data,
    columns=["student_id", "age", "major", "favorite_snack", "meme_quality"],
)

# Snack consumption dataset
dates = pd.date_range(end=pd.Timestamp.today(), periods=num_days).to_list()
snack_consumption_data = []
for student_id in students_df["student_id"]:
    for date in dates:
        snack_type = students_df.loc[
            students_df["student_id"] == student_id, "favorite_snack"
        ].values[0]
        quantity = np.random.randint(
            1, 6
        )  # Assume they eat between 1 to 5 units of their favorite snack
        snack_consumption_data.append([student_id, date, snack_type, quantity])

snack_consumption_df = pd.DataFrame(
    snack_consumption_data, columns=["student_id", "date", "snack_type", "quantity"]
)

# Productivity dataset (correlate snack types and quantities with productivity and energy levels)
productivity_data = []
for student_id in students_df["student_id"]:
    total_snacks_consumed = snack_consumption_df.loc[
        snack_consumption_df["student_id"] == student_id, "quantity"
    ].sum()
    snack_type = students_df.loc[
        students_df["student_id"] == student_id, "favorite_snack"
    ].values[0]

    # Correlation logic
    if snack_type in ["Fruit", "Nuts"]:
        energy_level = np.random.uniform(6, 10)  # Higher energy for healthy snacks
        hours_studied = np.random.uniform(5, 8)  # More hours of study
    else:
        energy_level = np.random.uniform(3, 7)  # Lower energy for indulgent snacks
        hours_studied = np.random.uniform(2, 5)  # Fewer hours of study

    memes_shared = np.random.poisson(2) + (
        total_snacks_consumed * 0.5
    )  # More snacks lead to more memes shared

    for date in dates:
        productivity_data.append(
            [student_id, date, hours_studied, energy_level, memes_shared]
        )

productivity_df = pd.DataFrame(
    productivity_data,
    columns=["student_id", "date", "hours_studied", "energy_level", "memes_shared"],
)

students_df.to_csv("data/students_snack.csv", index=False)
snack_consumption_df.to_csv("data/snack_consumption.csv", index=False)
productivity_df.to_csv("data/productivity.csv", index=False)

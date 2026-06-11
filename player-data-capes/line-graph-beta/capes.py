# --- Matplotlib CSV Plotting Script ---
# Made By: NeonWardonmc
# Date: 09/06/2024
# Description: This script imports data from the export.csv file which contains minecraft server info and turns it into a graph.
# Note: The export.csv file must be in the same directory as this script for it to work.
# Version: 1.0.2-beta
# License: MIT License
# LICENSE Found in the LICENSE file in the same directory as this script.



# --- Importing Libraries ---
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- Initialize Data Lists ---
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

x = []
y = []



# --- Data Import and Data Processing ---
with open('export.csv', newline='', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    next(reader, None)

    for i, row in enumerate(reader, start=2):
        if len(row) < 2:
            print(f"Skipping line {i}: not enough columns -> {row}")
            continue

        cape = row[0].strip()
        count_text = row[1].strip()

        try:
            count = int(count_text)
        except ValueError:
            print(f"Skipping line {i}: bad number -> {count_text!r}")
            continue

        x.append(cape)
        y.append(count)

# --- Debugging Output ---
print("Loaded rows:", len(x))
print("Max count:", max(y) if y else None)
print("Y:", y)

# --- Plotting ---
print("Loaded rows:", len(x))
print("Max count:", max(y) if y else None)
print("Y:", y)

if not x:
    print("No valid data found in export.csv")
else:
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o', color='blue')
    plt.title('Minecraft Capes by Player Count')
    plt.xlabel('Cape Name')
    plt.ylabel('Amount of players who have it')
    plt.xticks(rotation=45, ha='right')

    # Force y-axis to cover full range
    max_y = max(y)
    plt.ylim(0, max_y * 1.1)  # 10% headroom above tallest bar

    # Custom y-ticks so they’re not just 0–6
    step = max_y // 6  # 6 steps from 0 to max
    ticks = list(range(0, max_y + step, step))
    plt.yticks(ticks)

    plt.tight_layout()
    plt.show()
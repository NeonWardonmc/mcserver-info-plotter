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


# --- Initialize Data Lists ---
x = []
y = []


# --- Data Import and Data Processing ---
with open('export.csv', newline='', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # skip header
    for row in reader:
        x.append(row[11])       # Country of Server
        y.append(float(row[5])) # Amount of players online


# --- Filter to Top 10 by Player Count ---
# Combine country and player count into list of tuples
data = [(country, players) for country, players in zip(x, y)]

# Sort by player count (descending) and take top 10
data_sorted = sorted(data, key=lambda item: item[1], reverse=True)
top_10 = data_sorted[:10]

top_10_countries = [item[0] for item in top_10]
top_10_players = [item[1] for item in top_10]


# --- Plotting ---
plt.figure(figsize=(10, 6))
plt.bar(top_10_countries, top_10_players, color='blue')
plt.title('Top 10 Minecraft Servers by Country (Player Count)')
plt.xlabel('Country of Server')
plt.ylabel('Amount of players online')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

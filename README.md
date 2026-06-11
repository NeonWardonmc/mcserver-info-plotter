# Minecraft Server Info Plotter

A Python script that reads Minecraft server data from a CSV file and plots the top 10 servers by player count, grouped by country.

## What it does

- Imports server data from `export.csv`
- Extracts:
  - Country of server (column 11)
  - Player count (column 5)
- Sorts servers by player count
- Plots the **top 10** countries with the most players online using a bar chart or line graph.

## Requirements

- Python 3.8+
- `matplotlib`

Install dependencies:

```powershell
py -m pip install matplotlib
```

## How to use

1. Make sure `export.csv` is in the same folder as `mcserverinfo.py`.
2. Open PowerShell in that folder.
3. Run the script:

```powershell
py mcserverinfo.py
```

4. A bar chart will open showing the top 10 countries by player count.

## CSV format

The script expects `export.csv` with at least these columns:

- Column 5: **Amount of players online** (numeric)
- Column 11: **Country of Server** (text)

The CSV must:
- Have a header row (first line)
- Be readable as UTF-8 (or similar encoding)

## Output

A bar chart showing:

- X-axis: Country of server
- Y-axis: Number of players online
- Only the top 10 countries by player count

## License

MIT License – see the [LICENSE](LICENSE) file for details.

## Author

**NeonWardonmc**  
Year 8 student
Interested in IT, coding, Minecraft server management, and Roblox development.

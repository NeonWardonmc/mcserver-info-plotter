# Contributing to mcserver-info-plotter

Thanks for taking the time to contribute to **mcserver-info-plotter**!  
This project reads Minecraft server data (e.g. capes, player counts) from CSV files and visualizes it using Python and Matplotlib.

Contributions of all kinds are welcome: bug fixes, new features, documentation, and data/visual improvements.

---

## Getting Started

1. **Fork** the repository to your own GitHub account.
2. **Clone** your fork locally:

   ```bash
   git clone https://github.com/<your-username>/mcserver-info-plotter.git
   cd mcserver-info-plotter
   ```

3. Make sure you have **Python 3.10+** installed.
4. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # PowerShell
   .venv\Scripts\Activate.ps1
   # or cmd
   .venv\Scripts\activate.bat
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Project Layout

- `capes.py` – script that reads `export.csv` and plots cape usage as a bar chart.
- `export.csv` – sample input data for capes (cape name + player count).
- `LICENSE` – project license (MIT).
- `README.md` – project overview and usage instructions.
- `CONTRIBUTING.md` – this guide.

Additional scripts or data files may be added in future versions.

---

## CSV Data Requirements

The plotting scripts expect **real CSV files**, not Excel workbooks renamed as `.csv`.

For the cape plotter:

```csv
Cape Name,Count
Pan,6024829
Migrator,2747131
15th Anniversary,1513983
...
```

Rules:

- First row is a header with at least: `Cape Name,Count`.
- Each subsequent row:
  - Column 1: cape name (string).
  - Column 2: count (integer, no extra text or symbols).
- File must be UTF-8 encoded.
- Do **not** commit binary `.xlsx` files renamed as `.csv`.

If you add new data formats or files, document them in `README.md`.

---

## Ways To Contribute

You can help by:

- **Fixing bugs** in existing scripts (e.g. CSV parsing, plotting, error handling).
- **Improving graphs**:
  - Better labels, colors, fonts, tick formatting.
  - New views (log scale, filtered plots, etc.).
- **Adding new visualizations** for other server data (players, regions, uptime, etc.).
- **Improving DX**:
  - Command-line options (e.g. input file, output image).
  - Configurable themes or layouts.
- **Documentation**:
  - Clarifying README sections.
  - Commenting non-obvious code paths.
  - Adding examples and screenshots.

If unsure whether your idea fits, open an issue first.

---

## Workflow for Changes

1. **Create a branch**:

   ```bash
   git checkout -b feature/my-change
   ```

   Suggested naming:
   - Features: `feature/<short-description>`
   - Bug fixes: `fix/<short-description>`
   - Docs: `docs/<short-description>`

2. **Make your changes** and run the script(s):

   ```bash
   python capes.py
   ```

   If you add new scripts, include a short usage example in the README.

3. **Code style**:
   - Use 4 spaces for indentation.
   - Keep functions small and focused.
   - Prefer descriptive names (`cape_counts`, `load_csv()`) over single letters.
   - Handle obvious edge cases (missing file, bad CSV data) with clear error messages.

4. **Testing**:
   - At minimum, run your script(s) end-to-end with sample data.
   - If you change CSV parsing, test with:
     - Valid CSV.
     - CSV with bad rows (ensure they are skipped cleanly).
   - If you change visuals, take a screenshot for the PR.

5. **Commit** your changes:

   ```bash
   git add .
   git commit -m "Describe what you changed (e.g. 'Improve y-axis formatting for cape chart')"
   ```

6. **Push** your branch:

   ```bash
   git push origin feature/my-change
   ```

7. Open a **Pull Request** to:

   ```text
   https://github.com/NeonWardonmc/mcserver-info-plotter
   ```

   In your PR description:
   - Summarize the change.
   - Mention any related issues.
   - Include screenshots if the output graph changed.

---

## Versioning & Releases

- Tags follow a `vX.Y.Z[-label]` pattern, e.g. `v1.1.0`, `v1.1.0-beta`.
- When adding features or breaking changes:
  - Update the version in any relevant metadata or docs.
  - Optionally add an entry to `CHANGELOG.md` (if present) describing the change.

---

## Reporting Issues

When filing an issue:

- Provide your **Python version** and OS.
- Paste the **exact command** you ran.
- Include relevant **error messages / stack traces**.
- If it’s a plotting issue, add:
  - Description of what you expected.
  - Screenshot or description of what you actually saw.
  - A small sample of the CSV (with any sensitive data removed).

---

## Code of Conduct

- Be respectful and constructive.
- Assume good intentions; this project is also used for learning.
- Keep feedback technical and specific.

By contributing, you agree that your contributions will be licensed under the MIT License of this repository.

Happy plotting! 🎮📊
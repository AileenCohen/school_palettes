# School Palettes 🎨🐸🐟🌿

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**School Palettes** is a Python color palette library containing **166 curated, nature-inspired color palettes** across four distinct collections: Neotropical Poison Frogs, Marine & Freshwater Fish, LTC artistic palettes, and Nature landscapes. 

Designed specifically for data scientists and visualization enthusiasts, it integrates seamlessly with `matplotlib`, `seaborn`, and `plotly`, and features automatic HTML swatch rendering inside Jupyter Notebooks.

---

## 📦 Installation

Install the package directly from GitHub using `pip`:

```bash
pip install git+https://github.com/AileenCohen/school-palettes.git
```

---

## 🚀 Quick Start & Interactive Jupyter Previews

In Jupyter Notebooks, JupyterLab, or Google Colab, you don't even need to call a print function—just type the object, sub-library, or palette name at the end of a cell to render a visual HTML preview:

```python
from school_palettes import skl

# 1. View a scrollable table of ALL 166 palettes
skl

# 2. View a specific sub-library table ('frogs', 'fish', 'ltc', or 'nature')
skl.frogs
skl.nature

# 3. View a single palette's visual swatches and hex codes
skl.haureoguttatum
skl.frogs.ramaconica
```

You can also call `show_table()` explicitly at any time:

```python
skl.show_table()                  # Shows all palettes
skl.show_table('fish')            # Shows only the fish sub-library
skl.show_table('earthy_tones')    # Shows a single palette swatch
```

---

## 📊 Plotting Examples

Every palette in `school_palettes` inherits from Python's built-in `list`, meaning you can pass `skl.<palette_name>` directly into any plotting library that expects a list of hex strings, or use `.cmap` and `.continuous_cmap` for Matplotlib colormaps.

### 1. Seaborn Categorical Plots

```python
import seaborn as sns
import matplotlib.pyplot as plt
from school_palettes import skl

# Load example dataset
penguins = sns.load_dataset("penguins")

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    palette=skl.frogs.ramaconica[:3],  # Slice the first 3 colors
    s=90
)
plt.title("Penguin Bill Dimensions (Palette: ramaconica)")
plt.show()
```

### 2. Matplotlib Bar Charts

```python
import matplotlib.pyplot as plt
from school_palettes import skl

categories = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(7, 4))
plt.bar(categories, values, color=skl.nature.earthy_forest_hues, edgecolor='black')
plt.title("Category Breakdown (Palette: earthy_forest_hues)")
plt.ylabel("Score")
plt.show()
```

### 3. Heatmaps & Continuous Colormaps (`.continuous_cmap`)

Every palette automatically generates both a discrete colormap (`.cmap`) and a smooth interpolated gradient (`.continuous_cmap`):

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from school_palettes import skl

# Generate random 10x10 matrix
data = np.random.randn(10, 10)

plt.figure(figsize=(6, 5))
sns.heatmap(data, cmap=skl.ltc.heatmap0.continuous_cmap, annot=False)
plt.title("Smooth Heatmap using skl.ltc.heatmap0.continuous_cmap")
plt.show()
```

---

## 🗂️ Available Sub-Libraries

| Sub-Library | Accessor | Count | Description & Inspiration |
| :--- | :--- | :---: | :--- |
| **Poison Frogs** | `skl.frogs` | 41 | Inspired by the `poisonfrogs` R package by the Lauren O'Connell Lab, featuring vibrant aposematic coloration of Neotropical dart frogs. |
| **Fish** | `skl.fish` | 43 | Inspired by the `fishualize` project, capturing tropical reef and freshwater fish species. |
| **LTC** | `skl.ltc` | 32 | Curated artistic, categorical, and diverging palettes inspired by the `ltc` collection. |
| **Nature** | `skl.nature` | 50 | Earthy, oceanic, forest, and atmospheric landscape palettes curated from nature themes. |

### Listing Palette Names Programmatically

If you want to search or iterate through palette names in Python:

```python
# List all 166 palette names
all_names = skl.list_palettes()

# List only fish palettes
fish_names = skl.fish.list_palettes()
```

---

## 🙏 Acknowledgments & Credits

* **Frogs Collection:** Adapted from the R package [`poisonfrogs`](https://github.com/laurenoconnelllab/poisonfrogs) created by the Lauren O'Connell Lab.
* **Fish Collection:** Inspired by tropical and marine teleost species palettes and adapted from the R package fishualize.
* **LTC Collection:** Adapted from the R package LTC.
* **Nature Collection:** Curated from popular environmental and landscape color harmonies.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

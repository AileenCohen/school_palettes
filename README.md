# School Palettes 🎨🐸🐟🌿

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**School Palettes** is a Python color palette library containing **166 curated, nature-inspired color palettes** across four collections: Neotropical Poison Frogs, Marine & Freshwater Fish, LTC artistic palettes, and Nature landscapes.

**Every single palette works as both a discrete categorical list AND a smooth, continuous colormap**, essentially making it effortless to style everything from simple bar charts to high-density Pearson's $r$ correlation matrices and heatmaps.

---

## 📦 Installation

Install directly from GitHub using `pip`:

```bash
pip install git+[https://github.com/AileenCohen/school-palettes.git](https://github.com/AileenCohen/school-palettes.git)
```

---

## 🚀 Interactive Jupyter Previews

In Jupyter Notebooks, JupyterLab, or Google Colab, simply type the library, sub-library, or palette name at the end of a cell. It will automatically render an interactive HTML preview showing **both the discrete color swatches and the smooth continuous gradient**:

```python
from school_palettes import skl

# 1. View a scrollable table of ALL 166 palettes (Discrete + Continuous previews)
skl

# 2. View a specific sub-library table ('frogs', 'fish', 'ltc', or 'nature')
skl.frogs
skl.fish
skl.ltc
skl.nature

# 3. View a single palette's swatches, hex codes, and continuous gradient bar
skl.ramaconica
skl.frogs.dtazureus
skl.nature.glacial_lake
```

You can also call `show_table()` explicitly:

```python
skl.show_table()                  # Shows all 166 palettes
skl.show_table('fish')            # Shows only the fish sub-library
skl.show_table('earthy_tones')    # Shows a single palette swatch & gradient
```

---

## 🌈 All Palette Options & Features

Every palette in `school_palettes` is an enhanced `Palette` object that inherits from Python's `list` while adding powerful continuous and discrete capabilities:

| Feature / Syntax | What It Returns | Best Used For |
| :--- | :--- | :--- |
| `skl.ramaconica` | `['#3C6B78', ...]` (List of hex strings) | Categorical plots (`seaborn`, `matplotlib`, `plotly`) |
| `skl.ramaconica.cmap` | Smooth 256-bin `LinearSegmentedColormap` | Correlation matrices (Pearson's $r$), heatmaps, contours |
| `skl.ramaconica.continuous_cmap` | Alias for `.cmap` (Smooth continuous colormap) | Heatmaps, continuous colorbars, 2D density plots |
| `skl.ramaconica.discrete_cmap` | Stepped `ListedColormap` | Clustered heatmaps or binned colorbars |
| `cmap="ramaconica"` | Auto-registered Matplotlib continuous colormap | Passing directly as a string to `sns.heatmap` or `plt.imshow` |
| `cmap="ramaconica_r"` | Auto-registered reversed continuous colormap | Flipping gradient direction via string name |
| `skl.ramaconica.reversed` | Reversed `Palette` object | Reversing colors (`skl.ramaconica.reversed.cmap`) |
| `skl.ramaconica[:3]` | Sliced `Palette` object | Selecting a subset of colors while keeping HTML preview |
| `skl.ramaconica(50)` | `Palette` with 50 smoothly interpolated hex codes | Generating custom-length gradients from any palette |

---

## 📊 Plotting Examples

### 1. Continuous Palettes: Pearson's $r$ Correlation Matrices & Heatmaps

**All 166 palettes** are automatically interpolated into smooth, continuous colormaps and registered with Matplotlib when you import `school_palettes`. You can use `.cmap` or pass the palette name directly as a string (add `_r` to reverse any palette!):

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from school_palettes import skl

# Generate sample data and compute Pearson's r correlation matrix (-1 to +1)
np.random.seed(42)
df = pd.DataFrame(
    np.random.randn(100, 6),
    columns=['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E', 'Feature F']
)
corr = df.corr(method='pearson')

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Method 1: Using any palette's .cmap property (e.g., 'heatmap2' or 'ramaconica')
sns.heatmap(
    corr,
    cmap=skl.heatmap2.cmap,
    vmin=-1, vmax=1, center=0,
    annot=True, fmt=".2f", square=True,
    ax=axes[0]
)
axes[0].set_title("Pearson's r using skl.heatmap2.cmap")

# Method 2: Passing ANY frog/fish/nature palette string name directly!
sns.heatmap(
    corr,
    cmap="opescudo_r",  # Reversed 'opescudo' frog palette as a continuous gradient
    vmin=-1, vmax=1, center=0,
    annot=True, fmt=".2f", square=True,
    ax=axes[1]
)
axes[1].set_title("Pearson's r using cmap='opescudo_r'")

plt.tight_layout()
plt.show()
```

### 2. Continuous Scatter Plots & Surface Maps

Use any frog, fish, LTC, or nature palette to map continuous numerical variables:

```python
import numpy as np
import matplotlib.pyplot as plt
from school_palettes import skl

x = np.random.randn(500)
y = np.random.randn(500)
z = np.sqrt(x**2 + y**2)  # Continuous variable

plt.figure(figsize=(7, 5))
scatter = plt.scatter(x, y, c=z, cmap=skl.frogs.dtazureus.cmap, s=50, alpha=0.9)
plt.colorbar(scatter, label="Distance from Center")
plt.title("Continuous Scatter Plot (Palette: skl.frogs.dtazureus.cmap)")
plt.show()
```

### 3. Generating $N$ Smoothly Interpolated Hex Colors

Need 15 or 100 smoothly blended hex codes from a 5-color frog palette? Call the palette like a function:

```python
from school_palettes import skl

# Blend 'earthy_forest_hues' (5 colors) into 12 smooth hex steps:
twelve_greens = skl.nature.earthy_forest_hues(12)
print(twelve_greens)

# In Jupyter, typing `skl.frogs.oskoi(15)` displays all 15 interpolated swatches!
skl.frogs.oskoi(15)
```

### 4. Discrete Categorical Plots (Seaborn & Matplotlib)

Because every palette inherits from `list`, you can pass it directly to `palette=` in Seaborn or `color=` in Matplotlib:

```python
import seaborn as sns
import matplotlib.pyplot as plt
from school_palettes import skl

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
plt.title("Penguin Bill Dimensions (Palette: ramaconica[:3])")
plt.show()
```

---

## 🗂️ Available Sub-Libraries (166 Total Palettes)

| Sub-Library | Accessor | Count | Description & Inspiration |
| :--- | :--- | :---: | :--- |
| **Poison Frogs** | `skl.frogs` | 41 | Inspired by the `poisonfrogs` R package by the Lauren O'Connell Lab, featuring vibrant aposematic coloration of Neotropical dart frogs. |
| **Fish** | `skl.fish` | 43 | Adapted from the R `fishualize` project, capturing tropical reef and freshwater fish species. |
| **LTC** | `skl.ltc` | 32 | Curated artistic, categorical, and diverging heatmap palettes inspired by the `ltc` R collection. |
| **Nature** | `skl.nature` | 50 | Earthy, oceanic, forest, and atmospheric landscape palettes curated from nature themes. |

### Searching & Listing Palettes Programmatically

```python
# List all 166 palette names
all_names = skl.list_palettes()

# List only palettes within a specific sub-library
frog_names = skl.frogs.list_palettes()
fish_names = skl.fish.list_palettes()

# Fetch a colormap dynamically by string name (supports discrete=True/False and n bins)
my_cmap = skl.get_cmap("glacial_lake", n=256, discrete=False)
```

---

## 🙏 Acknowledgments & Credits

* **Frogs Collection:** Adapted from the R package [`poisonfrogs`](https://github.com/laurenoconnelllab/poisonfrogs) created by the Lauren O'Connell Lab.
* **Fish Collection:** Inspired by tropical and marine teleost species palettes (`fishualize`).
* **LTC & Nature Collections:** Curated from artistic and environmental color harmonies.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

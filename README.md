<div align="center">

# 〰️ Wave Divider Generator

Embed beautiful SVG wave separators between sections of any GitHub README — no API key required

[![Deploy to Vercel](https://img.shields.io/badge/Deploy%20to-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/new/clone?repository-url=https://github.com/readme-SVG/readme-SVG-wave-divider)
[![No API Key](https://img.shields.io/badge/No%20API%20Key-Required-22c55e?style=for-the-badge)](#how-it-works)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/Apache-2.0)
[![SVG Output](https://img.shields.io/badge/Output-Pure%20SVG-4f8cff?style=for-the-badge)](#)

</div>

---

## ✨ What is this?

**readme-SVG-wave-divider** turns a simple URL into a **customizable SVG wave** you can drop between sections of any GitHub README, Markdown file, or webpage.

```markdown
![Wave divider](https://your-app.vercel.app/wave?color_top=0d1117&color_bottom=161b22)
```

> The SVG is rendered inline — no external images, no blocked content, works everywhere GitHub renders Markdown.

---

## 🌊 Live Examples

<div align="center">

<!-- Smooth wave, GitHub Dark -->
![Wave](https://readme-svg-wave-divider.vercel.app/wave?type=smooth&color_top=0d1117&color_bottom=161b22&amplitude=20&frequency=1&height=80)

<!-- Ocean multi-layer -->
![Wave](https://readme-svg-wave-divider.vercel.app/wave?type=smooth&color_top=0a1628&color_bottom=0f3460&amplitude=30&frequency=1.5&layers=2&height=80)

<!-- Zigzag -->
![Wave](https://readme-svg-wave-divider.vercel.app/wave?type=zigzag&color_top=0f0f0f&color_bottom=222222&amplitude=22&frequency=3&height=60)

</div>

---

## ⚡ Quick Start

### Step 1 — Deploy your own instance

```bash
# Clone and enter the folder
git clone https://github.com/readme-SVG/readme-SVG-wave-divider.git
cd readme-SVG-wave-divider

# Install Vercel CLI and deploy (free)
npm install -g vercel
vercel
```

Done! Copy your Vercel URL — that becomes your `BASE_URL`.

### Step 2 — Add to your README

```markdown
![Wave divider](https://BASE_URL/wave?color_top=0d1117&color_bottom=161b22)
```

**That's it.** Replace `BASE_URL` with your Vercel domain and tweak colors to match your sections.

> **One-click deploy:**  
> [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/readme-SVG/readme-SVG-wave-divider)

---

## 🛠️ API Reference

```
GET /wave
```

### Parameters

<div align="center">

| Parameter | Default | Range | Description |
|:---|:---:|:---:|:---|
| `type` | `smooth` | smooth, sine, bump, zigzag, triangle | Wave shape |
| `width` | `1200` | `200 – 2400` | SVG width in pixels |
| `height` | `80` | `20 – 200` | SVG height in pixels |
| `color_top` | `0d1117` | hex, no `#` | Color of the section above |
| `color_bottom` | `161b22` | hex, no `#` | Color of the section below (wave fill) |
| `amplitude` | `20` | `1 – 100` | Wave height in pixels |
| `frequency` | `1` | `0.5 – 8` | How many wave peaks |
| `layers` | `1` | `1 – 3` | Number of stacked wave layers |
| `flip` | `false` | true/false | Flip wave vertically |
| `gradient` | `false` | true/false | Horizontal gradient fill |
| `mirror` | `false` | true/false | Add a ghosted mirror layer |
| `opacity` | `1` | `0.1 – 1` | Wave fill opacity |

</div>

### Example URLs

```bash
# GitHub Dark default
/wave?color_top=0d1117&color_bottom=161b22

# Ocean — multi-layer
/wave?type=smooth&color_top=0a1628&color_bottom=0f3460&amplitude=30&frequency=1.5&layers=2

# Sunset bump
/wave?type=bump&color_top=1a0a2e&color_bottom=f72585&amplitude=25&frequency=2

# Zigzag divider
/wave?type=zigzag&color_top=0f0f0f&color_bottom=222222&amplitude=22&frequency=3

# Flipped — wave points upward
/wave?color_top=161b22&color_bottom=0d1117&flip=true

# Triple layer neon
/wave?type=sine&color_top=020010&color_bottom=0d0030&amplitude=28&frequency=2&layers=3

# Minimal light
/wave?type=smooth&color_top=f0f0f0&color_bottom=ffffff&amplitude=10&frequency=0.5

# Gradient fill
/wave?color_top=0d1117&color_bottom=4f8cff&gradient=true&amplitude=24
```

---

## 🏗️ How It Works

```
Request: /wave?color_top=0d1117&color_bottom=161b22
              │
              ▼
   Parse parameters
   (type, size, colors, amplitude, frequency, …)
              │
              ▼
   Generate wave path using sine / bezier / zigzag math
   Support for multiple layers & effects
              │
              ▼
   Render inline SVG:
   ┌────────────────────────────────────┐  ← color_top
   │  ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿  │
   └────────────────────────────────────┘  ← color_bottom
   No external images, pure math → SVG path
              │
              ▼
   Response served with:
   Cache-Control: public, max-age=3600
```

### Why pure SVG paths?

| Approach | GitHub renders? | No external deps? | Infinitely scalable? |
|:---|:---:|:---:|:---:|
| PNG image | ✅ | ❌ | ❌ |
| SVG with external `<image>` | ❌ blocked | ❌ | ✅ |
| **SVG with math-generated paths** | **✅** | **✅** | **✅** |

GitHub renders inline `<path>` SVGs perfectly. No base64, no fetching external images — just clean vector math.

---

## 🎨 Style Recipes

Ready-made themes for your README:

```markdown
<!-- GitHub Dark (default) -->
![Wave](https://BASE_URL/wave?color_top=0d1117&color_bottom=161b22)

<!-- GitHub Dark → slightly lighter -->
![Wave](https://BASE_URL/wave?color_top=161b22&color_bottom=21262d)

<!-- Ocean -->
![Wave](https://BASE_URL/wave?type=smooth&color_top=0a1628&color_bottom=0f3460&amplitude=30&frequency=1.5&layers=2)

<!-- Sunset -->
![Wave](https://BASE_URL/wave?type=bump&color_top=1a0a2e&color_bottom=f72585&amplitude=25&frequency=2)

<!-- Forest Flip -->
![Wave](https://BASE_URL/wave?type=smooth&color_top=0a1a0d&color_bottom=1a4a22&amplitude=18&frequency=2&layers=2&flip=true)

<!-- Neon Triple Layer -->
![Wave](https://BASE_URL/wave?type=sine&color_top=020010&color_bottom=0d0030&amplitude=28&frequency=2&layers=3)

<!-- Minimal Light -->
![Wave](https://BASE_URL/wave?type=smooth&color_top=f0f0f0&color_bottom=ffffff&amplitude=10&frequency=0.5)

<!-- Gradient Fill -->
![Wave](https://BASE_URL/wave?color_top=0d1117&color_bottom=4f8cff&gradient=true)
```

---

## 🔄 Comparison

<div align="center">

| Feature | **readme-SVG-wave-divider** | Static PNG dividers |
|:---|:---:|:---:|
| No API key needed | ✅ | ✅ |
| Custom colors via URL params | ✅ | ❌ |
| Infinite shapes & styles | ✅ | ❌ |
| Renders inside GitHub README | ✅ | ✅ |
| GitHub Actions required | ❌ | ❌ |
| Setup time | ~30 sec | manual |
| Self-hosted on Vercel | ✅ | N/A |

</div>

---

## 🚀 Deploy Options

### Vercel _(recommended, free)_

```bash
npm install -g vercel
vercel
```

### Railway

```bash
railway login && railway up
```

### Self-hosted (Python / Flask)

```bash
pip install -r requirements.txt
gunicorn "api.index:app"
# Running on http://localhost:8000
```

---

## 🤝 Contributing

```bash
# Fork, then:
git clone https://github.com/YOUR_USERNAME/readme-SVG-wave-divider.git
cd readme-SVG-wave-divider
pip install -r requirements.txt
flask --app api.index run --debug
```

PRs welcome for:
- New wave shape types
- Additional URL parameters (noise, spikes, stepped)
- Bug fixes and edge case handling
- Translations and documentation

Check [open issues](https://github.com/readme-SVG/readme-SVG-wave-divider/issues) before starting.

---

<div align="center">

*Part of the [readme-SVG](https://github.com/readme-SVG) collection — beautiful SVG components for GitHub READMEs*

⭐ Star if it helped you

</div>

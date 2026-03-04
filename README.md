# SVG Wave Divider Generator

> Generate production-ready, customizable SVG wave dividers for GitHub READMEs and web UIs with a zero-friction HTTP API.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)](LICENSE)
[![Runtime: Python](https://img.shields.io/badge/Runtime-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](#technology-stack)
[![Platform: Vercel](https://img.shields.io/badge/Deploy-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](#deployment)
[![API: Stateless](https://img.shields.io/badge/API-Stateless-22c55e?style=for-the-badge)](#key-design-decisions)
[![Coverage: Not tracked](https://img.shields.io/badge/Coverage-Not%20tracked-lightgrey?style=for-the-badge)](#testing)

A lightweight service that renders mathematically generated SVG wave paths from URL query parameters. It is optimized for places where external assets are painful or blocked (like GitHub Markdown), and where you want crisp, scalable separators without shipping image files.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Technical Architecture](#technical-architecture)
  - [Project Structure](#project-structure)
  - [Key Design Decisions](#key-design-decisions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Contacts and Support](#contacts-and-support)

## Features

- Parameter-driven SVG generation via `GET /wave`.
- Multiple wave profiles: `smooth`, `sine`, `bump`, `zigzag`, `triangle`.
- Adjustable geometry: `width`, `height`, `amplitude`, `frequency`, `layers`.
- Visual controls: top and bottom colors, opacity, gradient mode, mirror layer.
- Orientation controls: `flip` and position options for divider direction.
- Frontend playground (`index.html` + `app.js`) for interactive tweaking.
- Output modes in UI: Markdown embed, raw HTML, and direct URL.
- Stateless backend suitable for serverless deployment.
- Zero database, zero background workers, low operational complexity.

## Technology Stack

- **Language**: Python 3.x.
- **Execution target**: Vercel Python serverless function.
- **Frontend playground**: Vanilla HTML, CSS, JavaScript.
- **API format**: HTTP GET with query string configuration.
- **Artifact format**: Inline SVG (`image/svg+xml`).

## Technical Architecture

### Project Structure

```text
.
├── api/
│   ├── __init__.py         # Package marker
│   ├── index.py            # HTTP entrypoint/router for Vercel
│   └── wavegen.py          # Core wave path generation and SVG assembly
├── index.html              # Local/UI playground shell
├── app.js                  # UI logic, controls, URL generation, preview sync
├── styles.css              # Playground styling
├── vercel.json             # Vercel routes/build configuration
├── requirements.txt        # Python dependencies for backend runtime
├── LICENSE                 # Apache 2.0
└── README.md               # Project documentation
```

### Key Design Decisions

- **Serverless-first contract**: The backend is tiny and stateless, which keeps cold-start overhead and operational burden low.
- **Pure SVG paths**: The service emits vector paths generated from math, not raster assets, so output scales cleanly and remains embeddable in Markdown contexts.
- **Query-driven rendering**: Every visual trait is encoded in the URL; this makes outputs reproducible, cache-friendly, and easy to version in docs.
- **No persistence layer**: There is no DB by design, because wave generation is deterministic and request-bound.
- **Separation of concerns**: `wavegen.py` handles geometry/rendering logic; `api/index.py` handles HTTP and routing concerns.

## Getting Started

### Prerequisites

Install the following tools locally:

- `Python 3.10+` (3.11 recommended).
- `pip` (bundled with Python).
- `Node.js 18+` (only needed if you want local static serving tooling; core backend is Python).
- `Vercel CLI` (for deploy flow):

```bash
npm install -g vercel
```

Optional but recommended:

- `git` for source control.
- `curl` for API smoke tests.

### Installation

```bash
# 1) Clone the repository
git clone https://github.com/readme-SVG/readme-SVG-wave-divider.git
cd readme-SVG-wave-divider

# 2) Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows PowerShell

# 3) Install Python dependencies
pip install -r requirements.txt

# 4) (Optional) run a quick syntax check
python -m py_compile api/index.py api/wavegen.py
```

## Testing

This repository currently has no formal test suite committed, so the practical validation strategy is smoke/integration checks against the API endpoint.

### Minimal local checks

```bash
# Python syntax sanity
python -m py_compile api/index.py api/wavegen.py

# Basic API behavior (replace URL with your deployed endpoint)
curl -i "https://<your-domain>/wave?type=smooth&color_top=0d1117&color_bottom=161b22"

# Validate response headers quickly
curl -sI "https://<your-domain>/wave?type=zigzag&amplitude=24&frequency=3"
```

### What to verify manually

- HTTP status is `200`.
- `Content-Type` is `image/svg+xml` (or equivalent SVG MIME).
- Output SVG renders in browser and markdown image embeds.
- Parameter boundaries are handled without crashes.

If you plan to contribute frequently, consider adding:

- unit tests for path builders in `api/wavegen.py`,
- route-level tests for `api/index.py`,
- and a lint stage in CI.

## Deployment

### Vercel (recommended)

```bash
# Authenticate once
vercel login

# Deploy preview
vercel

# Deploy production
vercel --prod
```

`vercel.json` already defines routing so `/wave` is served by `api/index.py`.

### CI/CD Notes

A robust pipeline should include:

1. Dependency install (`pip install -r requirements.txt`)
2. Syntax/lint checks
3. Optional tests
4. Preview deploy on PR
5. Production deploy on `main`

For GitHub-based workflows, wire Vercel Git integration and enforce checks before merge.

## Usage

Use the API directly or via the included browser UI.

### Direct API examples

```bash
# Default dark-mode style
a="https://<your-domain>/wave?color_top=0d1117&color_bottom=161b22"
echo "$a"

# Multi-layer ocean wave
b="https://<your-domain>/wave?type=smooth&color_top=0a1628&color_bottom=0f3460&amplitude=30&frequency=1.5&layers=2"
echo "$b"

# Sharp zigzag divider
c="https://<your-domain>/wave?type=zigzag&color_top=0f0f0f&color_bottom=222222&amplitude=22&frequency=3"
echo "$c"
```

### Markdown embed

```markdown
<!-- Put this between README sections -->
![Wave divider](https://<your-domain>/wave?type=smooth&color_top=0d1117&color_bottom=161b22&amplitude=20&frequency=1)
```

### HTML embed

```html
<!-- Responsive separator in web pages -->
<img
  src="https://<your-domain>/wave?type=sine&color_top=111827&color_bottom=1f2937&height=90&amplitude=24"
  alt="SVG wave divider"
  style="display:block;width:100%;height:auto;"
/>
```

## Configuration

There is no mandatory `.env` in the current implementation. Runtime behavior is controlled mainly by URL query parameters.

### API query parameters

- `type`: `smooth | sine | bump | zigzag | triangle`
- `width`: integer, typical range `200-2400`
- `height`: integer, typical range `20-200`
- `color_top`: hex color without `#` (e.g., `0d1117`)
- `color_bottom`: hex color without `#`
- `amplitude`: numeric wave amplitude
- `frequency`: numeric wave frequency
- `layers`: integer `1-3`
- `flip`: boolean (`true|false`)
- `gradient`: boolean (`true|false`)
- `mirror`: boolean (`true|false`)
- `opacity`: float `0.1-1`

### If you introduce `.env` later

Use `.env.example` and document keys in this section to keep contributor onboarding smooth and deterministic.

## License

This project is licensed under the Apache 2.0 License. See `LICENSE` for full legal text.

## Contacts and Support

## ❤️ Support the Project

If you find this tool useful, consider leaving a ⭐ on GitHub or supporting the author directly:

[![Patreon](https://img.shields.io/badge/Patreon-OstinFCT-f96854?style=flat-square&logo=patreon)](https://www.patreon.com/OstinFCT)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-fctostin-29abe0?style=flat-square&logo=ko-fi)](https://ko-fi.com/fctostin)
[![Boosty](https://img.shields.io/badge/Boosty-Support-f15f2c?style=flat-square)](https://boosty.to/ostinfct)
[![YouTube](https://img.shields.io/badge/YouTube-FCT--Ostin-red?style=flat-square&logo=youtube)](https://www.youtube.com/@FCT-Ostin)
[![Telegram](https://img.shields.io/badge/Telegram-FCTostin-2ca5e0?style=flat-square&logo=telegram)](https://t.me/FCTostin)

For technical issues, open a GitHub Issue with reproduction details. For contribution mechanics, see `CONTRIBUTING.md`.

# DS23 Guides

A collection of interactive Hebrew study guides for Data Science, Machine Learning and AI. 326 entries across four domains, with explanations, analogies, visualizations, code samples, and exercises.

## Live site

**[https://orarr2.github.io/ds23-guides-/](https://orarr2.github.io/ds23-guides-/)**

Mobile friendly. Works fully offline once loaded. The interface and all content are in Hebrew (RTL).

> All source files live in the [`docs/`](docs/) folder. GitHub Pages is served from that folder.

## Install on iPhone / iPad (Home Screen)

The site works as a standalone app once added to your iOS Home Screen.

1. Open the live URL in **Safari** on your iPhone or iPad. This must be Safari, not Chrome or another browser, because only Safari can install web apps to the iOS Home Screen.
2. Tap the **Share** button (the square with an arrow pointing up) in the bottom toolbar.
3. Scroll the share sheet and tap **Add to Home Screen**.
4. Confirm the name (default: "DS23") and tap **Add**.
5. You will now see a DS23 icon on your Home Screen. Tap it to launch the guides in full-screen mode, with no browser chrome.

A custom icon and theme color are bundled with the site, so the Home Screen tile looks like a native app rather than a screenshot.

## What is inside

| Guide | Entries | Main topics |
|------|---------|-------------|
| Math for ML ([docs/math guide DS23.html](docs/math%20guide%20DS23.html)) | 113 | Linear algebra, calculus, optimization, graph theory, information theory |
| Statistics glossary ([docs/stats guide DS23.html](docs/stats%20guide%20DS23.html)) | 59 | Distributions, hypothesis testing, regression, Bayesian inference |
| Machine Learning and AI ([docs/ai ml guide DS23.html](docs/ai%20ml%20guide%20DS23.html)) | 90 | Classical ML, neural networks, Deep Learning, NLP, Transformers, time series, evaluation |
| Python & Practical Tools ([docs/python tools guide DS23.html](docs/python%20tools%20guide%20DS23.html)) | 64 | DS lifecycle, Python basics, Pandas, SQL, sklearn, Plotly, PyTorch, Keras, Hugging Face, AI Agents, Storytelling |

## Entry structure

Every entry contains:

- **In short**: a tight definition of the concept
- **Visualization**: a diagram, chart, or illustration
- **Analogy**: an everyday mapping that helps build intuition
- **In ML**: practical context inside machine learning
- **Exercise and solution**: a self-check

## Features

- Built-in full-text search across every entry of a guide
- Cross-guide search from the home page (search a term once, jump into any of the three guides with the query pre-filled)
- Collapsible table of contents drawer with fast navigation between entries
- Home button on every page
- Long-press on the chapter number at the bottom of an entry to open a popup that lists every entry in that chapter
- Keyboard navigation (left and right arrows; Escape to close panels)
- Responsive design tuned for mobile
- Full RTL support
- Static files, no external dependencies, no build step
- Works offline after the first load

## Run locally

Everything you need is in the [`docs/`](docs/) folder:

```
docs/
├── index.html
├── icon.svg
├── favicon.png
├── favicon-32.png
├── apple-touch-icon.png
├── math guide DS23.html
├── stats guide DS23.html
├── ai ml guide DS23.html
└── python tools guide DS23.html
```

You can also grab the bundled archive: [docs/ds23-guides.zip](docs/ds23-guides.zip).

Open `docs/index.html` in any modern browser. No server needed.

On iOS, if you want to open the local HTML files (not the live site) with full JavaScript, use an app like Documents by Readdle. For day-to-day use, prefer the live URL above.

## License

Personal and educational use only.

---

Built by [@orarr2](https://github.com/orarr2). Updated June 2026.

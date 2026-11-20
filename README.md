# Mira Tenner — stories

The source for [miratenner.com](https://miratenner.com). Fiction by Mira Tenner.

A deliberately small static site: plain HTML and CSS generated with Python's
standard library. No JavaScript, analytics, external fonts, or dependencies.

## Build

```sh
python3 build.py
python3 test_site.py
python3 -m http.server --directory site 8000
```

Edit the curated Markdown files under `stories/`, then rebuild. Commit `site/`
alongside the source; GitHub Pages deploys that directory through Actions.
Private journals, correspondence, and working notes do not belong in this repository.

## Rights

Stories and other prose © 2026 Mira Tenner. All rights reserved.
The build script, test script, and CSS may be used under the MIT license (see LICENSE).

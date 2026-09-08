# Bellwether — landing site

The marketing site for [Bellwether](https://github.com/goker/bellwether-mobile), the
family health app for iOS and Android.

Three static pages, no build step, no dependencies. Open `index.html` in a browser
and it works.

| File | What it is |
|---|---|
| `index.html` | The landing page |
| `privacy.html` | Privacy Policy — converted from `docs/legal/PRIVACY_POLICY.md` in the app repo |
| `terms.html` | Terms of Service — converted from `docs/legal/TERMS_OF_SERVICE.md` |

## Design

The site uses the app's own design system rather than a separate web identity:
the Midnight and Ember palettes, the radial "low light from above" page glow, the
translucent glass borders, and the real metric hues from
`lib/core/theme/bw_palette.dart`. The appearance toggle in the top bar switches
the whole site between the two modes the app ships, and the choice is remembered
in `localStorage`.

Type is Fraunces for display, Karla for body, IBM Plex Mono for labels and data,
loaded from Google Fonts. The app icon is inlined as a data URI, so the pages
have no image requests of their own.

## Screenshots

The gallery loads screenshots by convention from `assets/screens/<mode>/<name>.png`
and swaps the whole set when the visitor changes mode. See
[`assets/screens/README.md`](assets/screens/README.md) for the file names and
capture notes. Missing files show a labelled placeholder naming the path they
expect, so the page never looks broken while the set is incomplete.

## Local preview

Any static server works. The screenshots need one — `file://` will not load them.

```bash
python -m http.server 4174
```

Then open http://localhost:4174.

## Before this goes live

- [ ] Fill the placeholders in `privacy.html` and `terms.html`: `[LEGAL ENTITY NAME]`,
      `[STATE]`, `[COUNTY/CITY]`, `[MAILING ADDRESS]`. They are highlighted in amber
      on the page so they are hard to miss.
- [ ] Have counsel review the arbitration agreement and class action waiver in
      Terms §17.
- [ ] Add the twelve screenshots (six screens × two modes).
- [ ] Point the App Store and Google Play buttons at the real listings — they are
      `#get` placeholders today.
- [ ] Add an Open Graph image and description for link previews.

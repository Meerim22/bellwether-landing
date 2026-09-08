# App screenshots

The gallery on the landing page loads screenshots by convention:

    assets/screens/<mode>/<name>.png

`<mode>` is `midnight` or `ember` — whichever the visitor picked in the top bar.
`<name>` is the `data-shot` value on the `<figure>` in `index.html`.

## Files the page looks for

| name          | screen                          |
|---------------|---------------------------------|
| `home`        | Home — the morning summary      |
| `circle`      | Circle                          |
| `sleep`       | Sleep                           |
| `win-streak`  | Win streak calendar             |
| `health`      | Health / activity trends        |
| `alerts`      | Alerts (nudges)                 |

That is 12 files in total — each screen captured twice, once per mode.

## Capturing them

- Shoot on one device so every frame has the same size. A 6.7" iPhone
  (1290 x 2796) or any 9:19.5 Android frame works; the page shows the top of each shot in a 9:15 frame and crops the rest.
- Switch the app's appearance (Profile -> Appearance) between Midnight and
  Ember and take the same six screens twice.
- Use the same account and the same day for both sets, so the two versions
  differ only in colour.
- Save as PNG. Keep them under ~400 KB each; the page loads six at a time.

## Missing files

Any file that is absent shows a labelled placeholder naming the exact path it
expects, so the page never looks broken while the set is incomplete.

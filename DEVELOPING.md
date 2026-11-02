# Developing

Edit the icons directly in `product-icons/osemoji-product-icons.json` and `file-icons/osemoji-file-icons.json`, then package:

```sh
vsce package --no-dependencies
```

`fonts/osemoji-base.ttf` is an empty font. VS Code requires interface icon themes to name a font, and its metrics set where the icons sit vertically. The emoji themselves come from the operating system. `scripts/make_base_font.py` rebuilds it and needs `fonttools`.

`lock` and `unlock` start with `U+E000`, an empty glyph in that font that moves the emoji after it 2px left at 16px. On 1× displays Apple's emoji are 20px wide at that size, not 16px, and VS Code's toolbars left-align them in a 16px box, so they sit 2px too far right. A theme can't tell 1× from Retina, so the nudge centres them on 1× displays and leaves them 2px left of centre on Retina. `make_base_font.py --nudge` sets the distance.

`docs/smaller-icons.css` shrinks the interface icons on machines that load custom CSS. It isn't part of the extension, and it lists icon IDs, so update it if you add any.

## Releasing

Pushing to `main` doesn't publish anything. To release, commit your changes, including a new entry in `CHANGELOG.md`, then run:

```sh
npm version patch
git push --follow-tags
```

`npm version` updates `package.json`, commits it and creates a tag such as `v1.0.1`. Pushing that tag runs `.github/workflows/publish.yml`, which publishes to the Marketplace through the publisher's Trusted Publishing policy. Use `minor` or `major` instead of `patch` for bigger changes.

The workflow stops if the tag doesn't match the version in `package.json`, and skips the upload if that version is already live.

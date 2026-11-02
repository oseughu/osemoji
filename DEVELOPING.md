# Developing

Edit the icons directly in `product-icons/osemoji-product-icons.json` and `file-icons/osemoji-file-icons.json`, then package:

```sh
vsce package --no-dependencies
```

`fonts/osemoji-base.ttf` is an empty font. VS Code requires interface icon themes to name a font, and its metrics set where the icons sit vertically. The emoji themselves come from the operating system. `scripts/make_base_font.py` rebuilds it and needs `fonttools`.

`docs/smaller-icons.css` shrinks the interface icons on machines that load custom CSS. It isn't part of the extension, and it lists icon IDs, so update it if you add any.

## Releasing

Pushing to `main` doesn't publish anything. To release, commit your changes, including a new entry in `CHANGELOG.md`, then run:

```sh
npm version patch
git push --follow-tags
```

`npm version` updates `package.json`, commits it and creates a tag such as `v1.0.1`. Pushing that tag runs `.github/workflows/publish.yml`, which publishes to the Marketplace through the publisher's Trusted Publishing policy. Use `minor` or `major` instead of `patch` for bigger changes.

The workflow stops if the tag doesn't match the version in `package.json`, and skips the upload if that version is already live.

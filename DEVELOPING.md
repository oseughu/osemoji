# Developing

Edit the icons directly in `product-icons/osemoji-product-icons.json` and `file-icons/osemoji-file-icons.json`, then package:

```sh
vsce package --no-dependencies
```

`fonts/osemoji-base.ttf` is an empty font. VS Code requires interface icon themes to name a font, and its metrics set where the icons sit vertically. The emoji themselves come from the operating system. `scripts/make_base_font.py` rebuilds it and needs `fonttools`.

`docs/smaller-icons.css` shrinks the interface icons on machines that load custom CSS. It isn't part of the extension, and it lists icon IDs, so update it if you add any.

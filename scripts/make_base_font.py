#!/usr/bin/env python3
import argparse
from pathlib import Path

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

UPEM = 1000
OUT = Path(__file__).resolve().parent.parent / "fonts/osemoji-base.ttf"


def main():
    parser = argparse.ArgumentParser(description="Build the empty font that sets the icons' vertical position.")
    parser.add_argument("--ascent", type=int, default=813)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    descent = args.ascent - UPEM

    empty = TTGlyphPen(None).glyph()
    font = FontBuilder(UPEM, isTTF=True)
    font.setupGlyphOrder([".notdef", "space"])
    font.setupCharacterMap({0x20: "space"})
    font.setupGlyf({".notdef": empty, "space": empty})
    font.setupHorizontalMetrics({".notdef": (UPEM, 0), "space": (UPEM, 0)})
    font.setupHorizontalHeader(ascent=args.ascent, descent=descent)
    font.setupNameTable({"familyName": "Osemoji Base", "styleName": "Regular"})
    font.setupOS2(sTypoAscender=args.ascent, sTypoDescender=descent, sTypoLineGap=0, usWinAscent=args.ascent, usWinDescent=-descent, fsType=0)
    font.setupPost()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    font.save(args.out)


if __name__ == "__main__":
    main()

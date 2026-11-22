#!/usr/bin/env python3
"""Adapt the upstream LOC chart PNG to the profile's transparent dark theme.

The upstream action does not expose Matplotlib's savefig(transparent=True)
setting. Its generated chart uses a white canvas and monochrome labels, so
this post-processing pass makes neutral pixels transparent and recolors the
labels without changing the chart's language-color palette.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

LABEL_COLOR = (201, 193, 217)
NEUTRAL_TOLERANCE = 4


def style_chart(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"Generated LOC chart not found: {path}")

    with Image.open(path) as source:
        image = source.convert("RGBA")

    styled_pixels: list[tuple[int, int, int, int]] = []
    for red, green, blue, alpha in image.getdata():
        if alpha == 0:
            styled_pixels.append((red, green, blue, 0))
            continue

        spread = max(red, green, blue) - min(red, green, blue)
        if spread <= NEUTRAL_TOLERANCE:
            # Matplotlib's text, axes and white canvas are neutral grayscale.
            # Convert grayscale intensity into alpha coverage so anti-aliased
            # edges remain smooth on the profile's dark background.
            intensity = (red + green + blue) // 3
            coverage = 255 - intensity
            styled_pixels.append((*LABEL_COLOR, (alpha * coverage) // 255))
        else:
            # Keep the upstream Linguist colors of the language bars intact.
            styled_pixels.append((red, green, blue, alpha))

    image.putdata(styled_pixels)
    image.save(path, format="PNG", optimize=True)

    with Image.open(path) as result:
        if result.mode != "RGBA" or result.getchannel("A").getextrema()[0] != 0:
            raise RuntimeError("LOC chart transparency check failed.")

    print(f"Styled transparent LOC chart: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Path to assets/bar_graph.png")
    args = parser.parse_args()
    style_chart(args.image)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

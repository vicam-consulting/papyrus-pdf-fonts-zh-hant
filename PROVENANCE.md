# Font provenance

- `fonts/NotoSansTC-Regular.ttf`: 7,149,124 bytes; SHA-256 `05df920c006ed7de22401b85df8f12a771f505ce3c57e56c2c9793434c47f6fd`.
- `fonts/NotoSerifTC-Regular.ttf`: 10,003,576 bytes; SHA-256 `4ddf703848ed8905f4f8ae46e8e71cbd3365278b8414a84b1b3f1a72a4c1e4c6`.
- `fonts/OFL-Serif.txt`: 4,350 bytes; SHA-256 `5e0da210fb04058a8c0087985d2d456b931c2579811a49655721d3cf0c36b6d6`.
- `fonts/OFL.txt`: 4,388 bytes; SHA-256 `1c05c68c34f9708415aada51f17e1b0092d2cea709bf4a94cd38114f9e73d7d9`.

Official Google Fonts commit `47d54ca1ebb14fd864695f1d39dc734f39017c33`, SIL OFL 1.1.

- `NotoSansTC-Regular.ttf`: version `Version 2.004-H2;hotconv 1.0.118;makeotfexe 2.5.65603`.
  Source: <https://raw.githubusercontent.com/google/fonts/47d54ca1ebb14fd864695f1d39dc734f39017c33/ofl/notosanstc/NotoSansTC%5Bwght%5D.ttf>; SHA-256 `864727d210d54f2537bbe23b3a839436c3992af72de9322af5270897246bd44f`.
  Licence: <https://raw.githubusercontent.com/google/fonts/47d54ca1ebb14fd864695f1d39dc734f39017c33/ofl/notosanstc/OFL.txt>; SHA-256 `1c05c68c34f9708415aada51f17e1b0092d2cea709bf4a94cd38114f9e73d7d9`.
- `NotoSerifTC-Regular.ttf`: version `Version 2.003-H1;hotconv 1.1.1;makeotfexe 2.6.0`.
  Source: <https://raw.githubusercontent.com/google/fonts/47d54ca1ebb14fd864695f1d39dc734f39017c33/ofl/notoseriftc/NotoSerifTC%5Bwght%5D.ttf>; SHA-256 `0077e18f57c6908f4a000969880940bdb0dad057c0e8d98b49dc364c3d1b09c6`.
  Licence: <https://raw.githubusercontent.com/google/fonts/47d54ca1ebb14fd864695f1d39dc734f39017c33/ofl/notoseriftc/OFL.txt>; SHA-256 `5e0da210fb04058a8c0087985d2d456b931c2579811a49655721d3cf0c36b6d6`.

Built with FontTools 4.66.1 (MIT), `TTFont(source, recalcTimestamp=False)` and
`instantiateVariableFont(font, {'wght': 400}, inplace=True, optimize=True,
updateFontNames=True)`, then `save()`. `tools/build-static.py` reproduces the exact
checksums above from pinned URLs and validates source hashes. Both are glyf
TrueType, no fvar, OS/2.fsType=0 (embedding and subsetting allowed). FontTools is
a development dependency, never required by PHP at runtime. No upstream code copied.

These static instances are Modified Versions under OFL. Sans is copyright
2014–2021 Adobe, Reserved Font Name “Source”; Serif is copyright 2017–2024 Adobe.
The Noto family names are not reserved. Licences are copied unmodified and must
travel with the fonts. TC follows Taiwan forms; it is not a separate HK font.

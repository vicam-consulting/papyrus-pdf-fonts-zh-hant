# Vicam PDF Traditional Chinese fonts

Optional static Noto Sans TC and Noto Serif TC Regular, distributed at no
charge. Fonts are SIL OFL 1.1; the existing PHP package licence remains unchanged.

```sh
composer require vicam/pdf-fonts-zh-hant
```

Requires PHP 8.3+ and Vicam PDF ^0.4.0. `PdfEngineFactory` discovers this pack
alongside any other installed language packs. Source and caller fonts retain
priority; regional and style hints choose these files only for missing glyphs.
Unknown shared Han is ambiguous; installing one pack does not assume a language.
Japanese requests never use Chinese glyph shapes. Regular only; no synthetic bold
or italic. TC has Taiwan regional forms; Hong Kong-specific glyph parity is not claimed.

Disable discovery with `new PdfEngineFactory(discoverFormFonts: false)` or supply
`formFallbacks: \Vicam\Pdf\FontsZhHant\NotoZhHant::formFallbacks()` explicitly.
For overlays, use `new OverlayFontFile(NotoZhHant::path(NotoZhHant::SANS))` from the
`Vicam\Pdf\Overlay` namespace and put it in your fallback list.

See [PROVENANCE.md](PROVENANCE.md), [font licence](fonts/OFL.txt) and
[Serif licence](fonts/OFL-Serif.txt). Run `composer test` after installing development
dependencies. The library parses fonts in PHP; building instances is development only.

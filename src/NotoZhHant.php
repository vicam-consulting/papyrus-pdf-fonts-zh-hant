<?php

declare(strict_types=1);

namespace Vicam\Pdf\FontsZhHant;

use Vicam\Pdf\Forms\{FormFontFallbacks, FormFontPackage};

/** Static Regular Traditional Chinese fonts; files are read lazily and subset-embedded. */
final class NotoZhHant implements FormFontPackage
{
    public const string SANS = 'NotoSansTC-Regular.ttf';
    public const string SERIF = 'NotoSerifTC-Regular.ttf';

    public static function path(string $file): string
    {
        if (!in_array($file, [self::SANS, self::SERIF], true)) {
            throw new \InvalidArgumentException('Unknown TC font file.');
        }

        return dirname(__DIR__).'/fonts/'.$file;
    }

    public static function formFallbacks(): FormFontFallbacks
    {
        return new FormFontFallbacks(
            traditionalChineseSans: self::path(self::SANS),
            traditionalChineseSerif: self::path(self::SERIF),
        );
    }
}

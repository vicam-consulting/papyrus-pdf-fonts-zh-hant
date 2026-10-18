import hashlib, json, urllib.request
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
import fontTools
root=Path(__file__).resolve().parent.parent/'build'
root.mkdir(exist_ok=True)
src=root/'sources';src.mkdir(exist_ok=True)
commit='47d54ca1ebb14fd864695f1d39dc734f39017c33'
records=[]
for style in ['Sans','Serif']:
    family=f'Noto{style}TC'
    url=f'https://raw.githubusercontent.com/google/fonts/{commit}/ofl/{family.lower()}/{family}%5Bwght%5D.ttf'
    source=src/(family+'[wght].ttf')
    urllib.request.urlretrieve(url, source)
    expected = {'https://raw.githubusercontent.com/google/fonts/47d54ca1ebb14fd864695f1d39dc734f39017c33/ofl/notosanstc/NotoSansTC%5Bwght%5D.ttf': '864727d210d54f2537bbe23b3a839436c3992af72de9322af5270897246bd44f', 'https://raw.githubusercontent.com/google/fonts/47d54ca1ebb14fd864695f1d39dc734f39017c33/ofl/notoseriftc/NotoSerifTC%5Bwght%5D.ttf': '0077e18f57c6908f4a000969880940bdb0dad057c0e8d98b49dc364c3d1b09c6'}
    assert hashlib.sha256(source.read_bytes()).hexdigest() == expected[url]
    font=TTFont(source,recalcTimestamp=False)
    version=font['name'].getDebugName(5)
    instance=instantiateVariableFont(font,{'wght':400},inplace=True,optimize=True,updateFontNames=True)
    output=src/(family+'-Regular.ttf');instance.save(output)
    expected_output = {'NotoSansTC-Regular.ttf': '05df920c006ed7de22401b85df8f12a771f505ce3c57e56c2c9793434c47f6fd', 'NotoSerifTC-Regular.ttf': '4ddf703848ed8905f4f8ae46e8e71cbd3365278b8414a84b1b3f1a72a4c1e4c6'}
    assert hashlib.sha256(output.read_bytes()).hexdigest() == expected_output[output.name]
    assert 'glyf' in instance and 'fvar' not in instance and instance['OS/2'].fsType==0
    license_url=f'https://raw.githubusercontent.com/google/fonts/{commit}/ofl/{family.lower()}/OFL.txt'
    license_path=src/('OFL-Serif.txt' if style=='Serif' else 'OFL.txt');urllib.request.urlretrieve(license_url,license_path)
    records.append(dict(file=output.name,bytes=output.stat().st_size,sha256=hashlib.sha256(output.read_bytes()).hexdigest(),url=url,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),version=version,license_url=license_url,license_sha256=hashlib.sha256(license_path.read_bytes()).hexdigest(),fonttools=fontTools.__version__))
(root/'tc-build.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))

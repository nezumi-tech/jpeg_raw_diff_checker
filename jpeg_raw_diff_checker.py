import pathlib
import shutil

#処理を行うフォルダを指定
p = pathlib.Path('H:/100OLYMP_M1mk2')

#.jpgと.orf(raw)のファイル名（拡張子付き）を取得する
jpg_filename = [x.name for x in p.glob('*.jpg')]
orf_filename = [x.name for x in p.glob('*.orf')]

#.jpgと.orf(raw)のファイル名から拡張子を取り除く
jpg_noext = [x.rstrip('.JPGjpg') for x in jpg_filename]
orf_noext = [x.rstrip('.ORForf') for x in orf_filename]

#jpgとorfのファイル名の集合(重複なし)をつくる
set_filename = set(jpg_noext + orf_noext)

#余分なファイルを探し、拡張子を付けて表示
extra_jpg = [x + '.JPG' for x in set_filename - set(orf_noext)]
print(extra_jpg)

extra_orf = [x + '.ORF' for x in set_filename - set(jpg_noext)]
print(extra_orf)

#余分なファイルが存在するとき
if (extra_jpg + extra_orf) != []:
    #余分なファイルを格納するフォルダを作成
    p_extra = p / 'Extra_Files'
    p_extra.mkdir(exist_ok=True)

    #余分なファイルを移動
    for x in extra_jpg + extra_orf:
        shutil.move(str(p / x), p_extra)

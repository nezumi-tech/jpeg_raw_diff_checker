import pathlib
import shutil

#処理を行うフォルダを指定
p = pathlib.Path('H:/100OLYMP_M1mk2')

#.jpgと.orf(raw)のファイル名（拡張子付き）を取得する
jpg_filename = list(map(lambda x: x.name, p.glob('*.jpg')))

orf_filename = list(map(lambda x: x.name, p.glob('*.orf')))

#.jpgと.orf(raw)のファイル名から拡張子を取り除く
jpg_noext = list(map(lambda x: x.rstrip('.JPGjpg'), jpg_filename))

orf_noext = list(map(lambda x: x.rstrip('.ORForf'), orf_filename))

#余分なファイルを探し、拡張子を付けて表示
extra_jpg = list(map(lambda x: x + '.JPG', [i for i in jpg_noext if i not in orf_noext]))
print(extra_jpg)

extra_orf = list(map(lambda x: x + '.ORF', [i for i in orf_noext if i not in jpg_noext]))
print(extra_orf)

#余分なファイルが存在するとき
if (extra_jpg + extra_orf) != []:
    #余分なファイルを格納するフォルダを作成
    p_extra = p / 'Extra_Files'
    p_extra.mkdir(exist_ok=True)

    #余分なファイルを移動
    for x in extra_jpg + extra_orf:
        shutil.move(str(p / x), p_extra)

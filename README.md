# myrlyn-lang
[![build result](https://build.opensuse.org/projects/home:slothsnow/packages/myrlyn-lang/badge.svg?type=default)](https://build.opensuse.org/package/show/home:slothsnow/myrlyn-lang)
[![translation](https://translate.codeberg.org/widget/myrlyn-lang/svg-badge.svg)](https://translate.codeberg.org/engage/myrlyn-lang/)\
This repository is for translations of [Myrlyn](https://github.com/shundhammer/myrlyn). For more information, you can also look into this [issue](https://github.com/shundhammer/myrlyn/issues/45).\
🌍 For translation work Weblate is used: https://translate.codeberg.org/projects/myrlyn-lang/ \
📦 It is built at Open Build Service:  https://build.opensuse.org/package/show/home:slothsnow/myrlyn-lang
## Add a language
If you want to add a language clone this repository and run this command with the desired locale instead of "nl" in the folder "po":
```
msginit --input=myrlyn.pot --locale=nl --output-file=nl.po
```
Then download the locale from https://github.com/yast/yast-translations/tree/master/po/qt-pkg and run this (edited) command:
```
msgmerge nl.po ~/Downloads/nl.po -o nl.po
```
Then open a pull request and after some time you should be able to translate using Weblate.

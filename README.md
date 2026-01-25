# Myrlyn Translations
[![Build Status](https://build.opensuse.org/projects/home:slothsnow/packages/myrlyn-lang/badge.svg?type=default)](https://build.opensuse.org/package/show/home:slothsnow/myrlyn-lang)
[![Translation Status](https://translate.codeberg.org/widget/myrlyn-lang/svg-badge.svg)](https://translate.codeberg.org/engage/myrlyn-lang/)

This repository hosts **translations for [Myrlyn](https://github.com/shundhammer/myrlyn)**. For more context, see this [GitHub issue](https://github.com/shundhammer/myrlyn/issues/45).

🌍 **Translations are managed via Weblate:** [translate.codeberg.org/projects/myrlyn-lang/](https://translate.codeberg.org/projects/myrlyn-lang/)    
📦 **Packages are built using Open Build Service (OBS):** [build.opensuse.org/package/show/home:slothsnow/myrlyn-lang](https://build.opensuse.org/package/show/home:slothsnow/myrlyn-lang)
## How You Can Contribute
Translation work happens directly in **Weblate** (see above). You use your GitHub account. If your language is already listed, you can start translating immediately.

If your language isn't available yet, follow the steps below.
## Adding a New Language
To add a new language, clone this repository and run the following command in the **`po`** folder, replacing `nl` with your desired locale:

```bash
msginit --input=myrlyn.pot --locale=nl --output-file=nl.po
```

Next, download the locale file from [yast-translations](https://github.com/yast/yast-translations/tree/master/po/qt-pkg) and run this command (adjust paths as needed):

```bash
msgmerge nl.po ~/Downloads/nl.po -o nl.po
```

Then, open a **Pull Request**. Once merged, your language will be available in Weblate, and you can start translating.

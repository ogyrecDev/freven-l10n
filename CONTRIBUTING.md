# Contributing Guide

Thanks for helping localize **Freven**!

## Files and format
- Translations live in `locales/<locale>.json`.
- Locale codes follow **BCP-47** (e.g. `en-US`, `ru-RU`, `pt-BR`).
- JSON is a **flat map**: `"namespace.key": "Text with {0} and {1}"`.
- **Do not change keys.** Translate **values only**.
- **Preserve placeholders** `{0}`, `{1}`, ... and their order/quantity.

## Add a new language
1. Copy `locales/en-US.json` → `locales/<your-locale>.json`.
2. Translate values.
3. Submit a Pull Request.

## Update an existing language
- Edit the corresponding `locales/<locale>.json`.
- Keep placeholders intact.

## Validation
- CI checks JSON syntax, **key set parity** with `en-US.json`, and **placeholder lists**.
- You can run the same checks locally (requires Python 3.11+):

```bash
python ci/validate.py
```

## Before opening a PR
- [ ] JSON is valid (no trailing commas, etc).
- [ ] Keys match `en-US.json` exactly.
- [ ] Placeholders `{0}`, `{1}`, … are preserved.
- [ ] CI (`python ci/validate.py`) passes locally.

## Style tips
- Keep strings concise and natural for your language.
- Use `\n` for intentional line breaks in longer messages.
- Avoid trailing spaces; preserve punctuation meaning.
- For game terminology, prefer the established terms in your language. (Optional glossary may appear later.)

## Credits
Translators are listed in the game credits. We appreciate every contribution! 🙌

## License confirmation
By opening a PR you confirm you have read and agree to the terms in
[LICENSE-TRANSLATIONS.md](LICENSE-TRANSLATIONS.md).
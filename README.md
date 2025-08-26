# freven-l10n — Community translations for Freven

This repository hosts **community-maintained translations** for the game **Freven**.
Contributions are welcome via Pull Requests (PRs).

- Base locale: `en-US`
- File format: flat JSON `key: "value"`
- Placeholders: positional `{0}`, `{1}`, ...
- Locale codes: [BCP-47](https://datatracker.ietf.org/doc/html/rfc5646) (e.g. `ru-RU`, `de-DE`)

## How to contribute (quick)
1. Fork this repo.
2. Copy `locales/en-US.json` to `locales/<your-locale>.json` (e.g. `locales/ru-RU.json`).
3. Translate **values only**. Keep keys and `{0}` placeholders intact.
4. Open a PR. CI will validate JSON, keys, and placeholders.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details and style guidelines.

## Using translations in the game
- Game bundles `en-US.json` and popular locales.
- Additional locales from this repo can be shipped or dropped into the game’s `translations/` folder.
- A CI artifact with all current locales is attached to each push to `main`.

## Legal
Translations are community-contributed and licensed under the terms in [LICENSE-TRANSLATIONS.md](LICENSE-TRANSLATIONS.md).  
The Freven game itself is closed-source and not covered by this repository.
See also our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

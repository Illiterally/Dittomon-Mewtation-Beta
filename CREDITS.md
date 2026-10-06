# Credits and asset provenance

Retain these credits with source and future patch releases. Existing notices, source comments and upstream documentation remain in the component repositories. This ledger is not a claim that every inherited asset has complete individual attribution.

## Dittomon beta testers

- **QingQing** — beta testing and an emailed bug report. This is the tester's
  requested public credit name and the only confirmed Dittomon beta tester
  so far. Upstream engine testers below belong to their respective projects.

## Development history and AI disclosure

**Dittomon is an Illiterally Custom: created and directed by Illy / Illiterally.**
Over two years, the project has grown through an ongoing collaboration with
OpenAI's ChatGPT and Codex. It began in RPG Maker XP with Pokémon Essentials
21.1, moved to a GBA beta built on Complete FireRed Upgrade (CFRU), and now
continues in the expanded CFRU Expansion / Gen 9 Dynamic Pokémon Expansion
rebuild. The opening carries forward work from that original RMXP project.

Along the way, Illy has worked with **o1, 4.0, 4.1, 5.0, 5.5, 6 Sol and
Astra ULTRA**, using the project-history labels supplied by Illy. AI has
assisted with research, planning, implementation, debugging, tests, porting,
and selected asset edits. This has been a sustained process of experiments,
revisions, and human review. Illy provides the concept, story, creative
direction, and final decisions. Community code and artwork retain their
original creators' credits.

**An ongoing cyborg partnership to bring Dittomon to the people.**

The opening credits draw from `data/opening-credits.json`, including the
confirmed beta-testers list and the named contributors in this ledger,
`SPRITE_RADRED_RESEARCH.md`, and `reports/essentials-source-audit.json`.
Inherited resource-pack credits are identified as such; listing them does
not assert that every optional asset or script is installed. Exact handles
remain in the ledger; underscores display as spaces in the GBA font.
Individual authors still unknown for some inherited art remain an open
attribution task, not an assertion of complete provenance.

## Engine and original expansion

**Complete FireRed Upgrade:** Skeli and Ghoulslash. The full original credit page is preserved in `engine/CFRU Documentation.pdf`, page 160, referenced by `engine/Credits.txt`.

That page credits:

- Code: Lixdel (attack animations); pret (pokeRuby, pokeFireRed, pokeEmerald); Sagiri (trainer-class Poké Balls, Pickup, Move Item, summary wrapping); DizzyEgg (Emerald battle-engine upgrades); FBI (save expansion, DexNav); Touched (Follow Me, Mega Evolution); Navenatox (dynamic overworld palettes); Doesntknowhowtoplay and Squeetz (Pokédex stats); Azurile13 (hidden abilities); Squeetz (footsteps and animations); JPAN (FireRed Hacked Engine); Diegoisawesome (triple-layer tiles); Jiangzhengwenjz (Linux support); Leon Dias (Gen 8 descriptions/data).
- Graphics: Golche (attack particles, battle backgrounds and other graphics); Criminon (Ultra Burst indicator); Bela (Poké Balls); Grey M (raid intro); Solo993 (backsprites); VentZX (type icons); canstockphoto.ca (battle backgrounds).
- Testers: Criminon, Dionen, Gail, Leon Dias, Recko Juice and Patrickz.

These are inherited project credits, not a guarantee that every listed optional asset is enabled in this build.

**CFRU Expansion / The Code Mining Hub:** Shiny hunter/Miner, ansh860, Zake, grilokapu and 1RWT16KU1D, as credited in the pinned [expansion README](https://github.com/Shiny-Miner/CFRU-expansion/blob/d1c9ee05c8183171faba69af07f708972f9a2d14/README.md). Preserve additional attribution in individual source files. The README permits use with credit to the respective code makers; no blanket root license was found for the entire combined repository.

## Species, forms and sprites

The RR/Essentials selection is documented in [ART_SOURCES.md](ART_SOURCES.md).
Exact RR 4.1 artist attributions and primary links are retained in
[SPRITE_RADRED_RESEARCH.md](SPRITE_RADRED_RESEARCH.md), including the credited
DS-style repository contributors and RR-specific art and shiny edits. The
owner's local donor ROM is identified by hash; it is not a source for importing
RR gameplay data. The official Pokédex source is an independent form-identity
reference. Local Essentials/Gen 9 contributor notices and source-file hashes are
recorded in `reports/essentials-source-audit.json`.

The mixed art policy and alternative sources are recorded in [ART_SOURCES.md](ART_SOURCES.md) and [SPRITE_OPTIONS.md](SPRITE_OPTIONS.md). The 386 original Pokémon and 27 Unown variants use their preserved beta / original FireRed battle artwork. The restoration reuses the original game's assets and does not create new artist credits. Later forms use the reviewed RR/Essentials layers or their retained DPE fallback. Researching an external resource does not mean its assets were imported.

**Dynamic Pokémon Expansion:** Skeli's original project and subsequent Gen 9 work. The [pinned Gen 9 fork](https://github.com/grilokapu/Dynamic-Pokemon-Expansion-Gen-9/tree/9048c7b70ab6623ecb46a636e44759409186e9a8) names Zake, Axel Loquendo and The Code Mining Hub; grilokapu maintains the selected update fork.

Species graphics source files are inventoried with SHA-256 hashes and immediate origins in `reports/asset-provenance.json`, including files superseded by restored classic art. Active selections and hashes are recorded in `species/dittomon-classic-art.json`, `species/dittomon-radred-art.json` and `species/dittomon-essentials-art.json`, with compiled-ROM audit reports. These identify immediate sources and versions; they do not substitute for the original artists' names. `species/LICENSE` is retained verbatim. That file must not be interpreted as proof that every third-party sprite has identical licensing terms.

**Open attribution work:** the pinned DPE does not include a complete artist-to-sprite roster for its Gen 9/ZA additions. The file named `Información.docx` is actually plain-text maintenance notes, not an attribution document. Its notes also predate later ZA commits. Do not assign sprite authorship to a commit uploader merely because they added the files. Known source-pack credits and notices are retained with this release; identifying the remaining individual contributors is ongoing.

**Dittomon eye edits:** the owner approved direct pixel editing and the 300-form
Anomaly batch. `art-review/anomaly-300/roster.json` records immediate sources,
original palettes and hashes, and every changed pixel. These are AI-assisted
coordinate edits following the owner's Ditto-eye style, not newly authored
whole sprites. Preserve all original artist credits above. The review ledger
and complete catalogue coverage ledger accompany the derived assets; unchanged
hidden-eye views are explicitly identified.

## Map and build tools

- **pret** and the contributors to [pokefirered](https://github.com/pret/pokefirered): source map reference.
- **huderlem** and Porymap contributors: [Porymap](https://github.com/huderlem/porymap), using the existing local installation. No claim that this executable is the newest release.
- **Alcaro** and Floating IPS contributors: [Flips](https://github.com/Alcaro/Flips), the existing patch utility.
- **devkitPro/devkitARM** and GNU toolchain contributors: ARM compilation.
- **Python** contributors: build and audit tooling.

## Video and research references

**CompuMaxx / GBA Video Studio** and its contributors: [project](https://github.com/CompuMaxx/GBA-Video-Studio), evaluated at commit `26e5606d6aabcd24338f198b1065e4392c1ba132`. Its GPL-3.0 license remains with the evaluation checkout. Its runtime decoder is not copied into this game; the sandbox indexed-frame/XOR encoder and movie player are new project code using the existing engine and GBA BIOS APIs. If that decoder is adopted later, review and preserve its applicable notices and source obligations.

**RHH**, its contributors, and **Project Pokémon**: researched as alternative engine/data references, not imported wholesale. Champions dumps are data evidence, not an asset pack with automatic redistribution permission.

The project owner supplied **Intro.mp4**, its replacement **IntroShortened.mp4**, and **Sunrise.mp4** for these two placements; original files are retained unchanged. Current input filenames and hashes are recorded in `reports/movie-assets.json`. This identifies the supplied source, not an inferred artist or music credit. Creator/music attribution from the supplied source project remains open in the provenance ledger. Conversion uses **FFmpeg** and its contributors, via the pinned **imageio-ffmpeg 0.6.0** binary distribution, plus **Pillow** and **NumPy**. Conversion tools are not ROM runtime components.

Additional opening artwork comes from the owner's earlier RMXP project. Individual attribution for those source-project images remains open in the internal provenance ledger.

## Dittomon

Dittomon's existing concept, story, authored encounters and beta content remain the project owner's work. The beta source history records prior implementation work; this pass preserves that history. New creative decisions remain with the user.

Pokémon and the original games/assets belong to their respective rights holders. Keep proprietary base/output ROMs and saves out of public source and patch packages.

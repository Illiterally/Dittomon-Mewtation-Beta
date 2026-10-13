# Sprite direction review — 2026-09-28

The initial foundation used the pinned DPE's bundled sprites. Selection prioritized catalogue compatibility; it did not include a visual comparison or owner approval of a replacement art style. The expanded species data does not require those particular pictures.

`python scripts/compare_sprite_art.py` renders the actual front/back tiles and normal palettes from the preserved beta, current output and clean FireRed into `output/sprite-comparison.png`. The initial expansion changed their poses and palettes; the current rebuilt output matches the beta and FireRed for all five samples. This comparison does not include emulator color correction, weather or battle palette effects.

## Adopted mixed selection

The user prefers the original beta artwork and explicitly selected RR 4.1 before Essentials/Gen 9 for later forms. The source retains exact beta front/back sprites, normal/shiny palettes and positioning for all 386 original Pokémon plus 27 original Unown variants. Later entries follow RR, compatible Essentials, then DPE fallback. Party icons are unchanged. [ART_SOURCES.md](ART_SOURCES.md) records the implemented selection and conversion limits; further individual choices can be made without changing species data.

The original compressed assets are still intact in the reserved vanilla region of the clean-ROM build. The protected entries in the seven art tables point to those bytes, retaining current species IDs, tags and size metadata. Castform keeps all four frames and palettes; Deoxys keeps its complete original stream. That initial classic restoration required no PNG changes; the subsequent RR and Essentials layers wrote 706 PNGs converted from existing donor artwork. Stats, abilities, moves and the 1,455-form catalogue are preserved.

Deoxys retains the expansion's separate form selection: its base row displays the original normal frame, while Attack/Defense/Speed use their separate expanded rows. The old beta's loader copied a different Deoxys frame into the base display. We preserve the source artwork without reinstating that old form-handling rule.

`species/dittomon-classic-art.json` records every selected row, original ROM hashes, compressed/decoded asset hashes and the pre-change source pointers. `scripts/restore_classic_art.py` checks the actual built ROM, including all 1,652 sprite/palette streams. Its optional `--compare-baseline` report is the historical classic-only preservation proof and does not apply after the RR/Essentials imports. The current combined proof is `reports/radred-art-import-audit.json`, covering the added layers, untouched art and compiled gameplay data.

## Available directions

| Direction | Benefit | Limitation |
| --- | --- | --- |
| Preserve beta/FireRed art for existing Pokémon, curate newer forms | Adopted for the current build; retains the established Dittomon appearance | Newer Pokémon have no original FireRed art and can still be curated individually |
| Curate a DS-style 64×64 collection | Established GBA-sized resources across generations | Some bundled DPE sprites already resemble this style; switching resource names alone does not guarantee an aesthetic change |
| Review a larger BW-style collection | More alternate poses and modern fan sprites to compare | Dimensions, palette limits, backs, shiny palettes and permissions require individual review before import |

The [Chaos Rush DS-style resource](https://www.pokecommunity.com/threads/the-ds-style-64x64-pok%C3%A9mon-sprite-resource-completed.267728/) and [MrDollSteak Gen VI resource](https://www.pokecommunity.com/threads/gen-vi-ds-style-64x64-pokemon-sprite-resource.314422/) are established source collections. MrDollSteak's thread provides contributor credits and permits use with credit.

The [Gen VII and Beyond 64×64 repository](https://www.pokecommunity.com/threads/ds-style-gen-vii-and-beyond-pok%C3%A9mon-sprite-repository-in-64x64.368703/) lists its download as updated June 18, 2026, publishes a contributor spreadsheet and permits credited use. Its current catalogue includes front/back entries for newer Megas such as Mega Glimmora. Listed entries do not establish that every one of our 1,455 forms has a complete matching set; check coverage before replacing anything.

[PokéAPI's sprite collection](https://github.com/PokeAPI/sprites) is another comparison source and credits kyledovey for newer backs and Z-A Mega sprites. It is an aggregator, not a guarantee of GBA-ready images or blanket asset permission. [Smogon's source repository](https://github.com/smogon/sprites#license) specifically asks users to discuss community-sprite reuse first; its code license does not license every sprite.

## Import boundary

Use a species-to-asset manifest with source URL, artist credit, usage terms and hashes. Replace matching front/back/normal/shiny sets together, preserve species IDs and data, check indexed palette ordering and 64×64 tile layout, and review in-game positions. Do not apply a separate old binary sprite patch over this expanded ROM. Choose the base art before producing the Ditto-eye variants so they follow the final poses.

The online resources above were researched as alternatives. The implemented replacements come from the owner's local RR 4.1 ROM and local Essentials/Gen 9 files, with per-entry manifests and the attribution records linked in [ART_SOURCES.md](ART_SOURCES.md).

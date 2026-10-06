# Radical Red 4.1 sprite provenance

Researched 2026-09-28. No ROM was downloaded, edited or launched, and nobody was contacted.

An exact local route is now available because the user already has Radical Red 4.1. Read-only extraction of that file can preserve its actual front/back pixel indices and normal/shiny palettes. Public community packs can supply related artwork, but I did not find a verified complete public RR 4.1 battle-art source pack with all four views/variants and matching custom shinies. This is a finding from the sources checked, not proof that no such pack exists.

Soupercell's [March 22, 2024 release announcement](https://www.pokecommunity.com/threads/pok%C3%A9mon-radical-red-version-4-1-released-gen-9-dlc-pokemon-character-customization-now-available.437688/page-120) links the [official 4.1 changelog](https://docs.google.com/document/d/1--HIABJp7iekqgFAYEN4To1EGdy8GkBMRT6HD1bTYeE/edit) and explicitly announces custom shinies. The changelog's public text export was read directly; its source URL, content hash and credit evidence are in `reports/radred-4.1-official-changelog-research.json`.

The relevant 4.1 artist attributions are below. They describe the credits' stated scope; they do not assign every individual extracted sprite to a single artist.

| Credited artist/project | Attributed work |
|---|---|
| Madgamermlg | Pecharunt sprites |
| Kingofthexroads | Gholdengo, Toedscruel, Roaring Moon, Ogerpon battle art |
| AxelLoquendo, Lykeron | Hydrapple and other Gen 9 battle art |
| Thedarkdragon11 and the DS-style repository contributors | Raging Bolt, Gouging Fire, Iron Crown, Iron Boulder, Armarouge, Ceruledge, Chi Yu, Basculegion M/F, Quaquaval, others |
| Ezart, Vent | Ursaluna Blood Moon, Archaludon, others; this credit also includes Poltchageist/Sinistcha icons |
| Togekissbunny1, ebaru | Terapagos |
| Kaixer | Custom shinies, Chesnaught, Cinderace, Gen 9 icons |
| Darkster, Plaininsane, Silva | Custom-shiny contributions and character-sprite formatting |
| Zoroark73 | An unnamed new Pokémon sprite |

The [official release thread's general credits](https://www.pokecommunity.com/threads/pok%C3%A9mon-radical-red-version-4-1-released-gen-9-dlc-pokemon-character-customization-now-available.437688/) additionally identify the DPE/CFRU base, leParagon and other DS-style repository contributors, kingofthe-x-roads, and the [Gen 8 Sprite Project](https://docs.google.com/spreadsheets/d/1acgzAjh0dnFRQnjZu8kSjS177rKCzpFfEHRLtwuuXRU/edit). That older general credit list is not a per-species RR 4.1 inventory.

The primary public resources resolve as follows:

| Source | What is established | What is not established |
|---|---|---|
| [DS-style Gen VII and Beyond 64×64 repository](https://www.pokecommunity.com/threads/ds-style-gen-vii-and-beyond-pok%C3%A9mon-sprite-repository-in-64x64.368703/) | Maintainer publishes battle sprites separately from icons, including Gen 9 and DLC species, and explicitly permits use with contributor credit. The opening post links its credits spreadsheet and [public Dropbox collection](https://www.dropbox.com/sh/qzcsjctxl8riqev/AADbTFTmn0zBtKT6WzkoEQmya?dl=0). | The current pack was updated June 18, 2026, so it is not a frozen RR 4.1 snapshot. Complete normal/shiny/front/back parity with RR was not verified. |
| [Chaos Rush's completed DS-style 64×64 resource](https://www.pokecommunity.com/threads/the-ds-style-64x64-pok%C3%A9mon-sprite-resource-completed.267728/) | Publisher describes sheets for the first 649 species and resized/cleaned DS-style backsprites. | Related source material, not an exact RR 4.1 export. It would also replace the beta style the user chose to preserve if applied indiscriminately. |
| [JonnyGoldApple/RR-Sprites](https://github.com/JonnyGoldApple/RR-Sprites) | Repository describes its files as Radical Red Showdown minisprites. | It does not establish a full GBA front/back battle-art and palette collection. Do not use it as a substitute for exact RR sprites. |

I found no RR-wide asset reuse license or RR-specific exclusivity statement in the official release material examined. The complete official 4.1 changelog contained no matches for license, permission, free-to-use, reuse, exclusive or redistribution terminology. That absence proves neither blanket permission nor a restriction. The DS-style repository's reuse-with-credit statement applies to its published contributions; it does not establish terms for all RR-specific edits, custom shinies or custom forms. Artist-level attribution remains incomplete where the release credits say “others” or mix battle art and icons.

The practical implementation route is to keep the approved beta Gen 1–3 layer intact, audit the user's local RR 4.1 file for exact optional newer-species art, and retain the proposed local Essentials 21.1/Gen 9 then DPE fallback where selected. Record source ROM hash, source species/form, destination species/form, both sprite hashes, both palette hashes, positioning and credited artist/project together. A source match should be called exact RR only after those bytes are checked; otherwise label it as an Essentials or community-source choice. Import matching front/back and palette sets together. Private local inspection and comparison need not wait on an inferred approval requirement; the provenance record should simply retain the unresolved attribution/reuse details honestly.

The later form-ID research found a stronger public source: [JwowSquared's Radical Red Pokédex repository](https://github.com/JwowSquared/Radical-Red-Pokedex). Its CNAME is `dex.radicalred.net`, and the [April 7, 2024 commit](https://github.com/JwowSquared/Radical-Red-Pokedex/commit/4de9a25d4dadfcb28b0f15442691ec40cf7a5042) explicitly updates the database to RR 4.1. The [pinned database](https://github.com/JwowSquared/Radical-Red-Pokedex/blob/a1d933de43a49394f41bc32da01daa0c8248c8ee/data.js) contains internal species IDs and full form keys. Its final data edit was April 15, 2024; later website commits did not replace the database. The repository also contains front/back and shiny graphics directories, but their complete four-image parity with the donor was not audited here, so they are not yet a verified exact replacement pack.

The identity audit compared all 1,343 database records with the user's local donor SHA-256 `679d112cdfe699c2793d82c7e7999ac9dfca9e222ad5a85d4f8f1e457cd0283f`: every record's six base-stat bytes matched its internal ID at ROM table `0x097B98EC`, stride 28. This is read-only identity evidence, not a request to import any gameplay data. The source data SHA-256 is `04c9dc94b6a7e3d33f5dcb5e804487466e7a249f4d340cf19853d70f37596df9`; its Git blob is `9bb59c6b2a45079b7aa6df0444a0978400d2ed65`.

`reports/rr41-authoritative-species-map.json` records 844 explicit DPE-symbol-to-RR-ID mappings from unique full form keys and reviewed equivalent naming aliases. It adds 89 mappings to the separate fingerprint audit, which had 796 proposals. A necessary rejection reduces their combined proposal count to 884 before catalogue/helper filtering: RR 1370 is **Terapagos-Terastal**, so DPE normal Terapagos must not use it. Only DPE `SPECIES_TERAPAGOS_TERASTAL` has the matching identity. Duplicate or absent source form keys remain unresolved; no inference from a truncated display name or donor Pokédex number was used to fill them. For example, some donor Hisui dex numbers differ from the Pokédex database even though the internal IDs and stats match exactly.

The map's recorded SHA-256 is `2c72aff8b99ab161d49aea02fa435ad75dd5f2ecf55d931b7d8137d1f3d14995`. Supporting metadata is under `reports/rr41-source-research/`; it retains species names, IDs, stats and source history, not extracted sprite images. The older `Darklord5437/Radical-Red` constants stop at Gen 8/Gigantamax and are unsuitable as a 4.1 ID authority. The community 4.1 save exporter's species list was inspected as a lead, but the explicit map relies on the versioned Pokédex source instead.

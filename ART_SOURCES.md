# Battle artwork sources

The owner's preferred look is the original beta for Gen 1–3 and Radical Red 4.1
for later Pokémon and additional forms. The source order is:

1. Preserved beta / FireRed artwork for the 386 original species and 27 original
   Unown variants.
2. Exact matching artwork from the owner's local Radical Red 4.1 ROM, identified
   by species and form rather than assuming the two games use the same IDs.
3. The owner's Essentials 21.1 and Generation 9 Pack v3.2.8 for compatible gaps.
4. The pinned expansion's current artwork for newer or otherwise uncovered forms.

Artwork selection does not change the Pokémon roster, stats, moves, abilities,
form mechanics or custom trainer encounters. Each layer must supply the front,
back, normal palette and shiny palette together. Original Gen 1–3 art stays
protected even when another pack supplies its own replacement.

The built ROM verifies 413 protected entries, 884 RR 4.1 matches, 21 compatible
Essentials/Gen 9 imports and 137 expansion fallbacks: all 1,455 usable forms.
Of the RR matches, 486 already matched completely, 370 needed artwork changes
and 28 needed positioning changes only. All 706 written PNGs round-trip through
the actual GBA graphics converter with the expected tiles and palettes.
`output/selected-art-preview.png` displays representative front/back and shiny
art extracted from this final ROM; it can be regenerated with
`scripts/preview_selected_art.py`.

## Local sources and comparison

`reports/essentials-source-audit.json` records the actual installation paths,
versions, source hashes and credit notices. The unmodified Essentials project is
21.1, and the separate Gen 9 pack is 3.2.8. The pack contains earlier generations
too; its files must not simply be copied over the whole catalogue.

`output/sprite-source-comparison.png` shows actual local artwork at a common pixel
scale. Some later-generation DPE pictures already match Radical Red. Other poses,
backs and shiny palettes differ. A resource's name alone is not an aesthetic
comparison.

The donor RR 4.1 file is pinned by SHA-256
`679d112cdfe699c2793d82c7e7999ac9dfca9e222ad5a85d4f8f1e457cd0283f`.
Its pointers are meaningful only inside that ROM. Importing artwork requires
copying the pixel/palette data and linking it into this game's tables; importing
the donor's addresses, species order or gameplay tables would be incorrect.

## Essentials compatibility

`scripts/audit_essentials_art.py` checks the actual four-image sets in the two
local packs. It removes only exact integer display magnification, then checks
opaque dimensions, alpha, normal/shiny pixel correspondence and shared palette
capacity. Its report is `reports/essentials-art-compatibility.json`.

Many Essentials images are genuine 80×80 or 96×96 art after removing display
magnification. The current GBA renderer uses 64×64 battle frames. A picture can
be cropped around transparent margins and repositioned without losing pixels;
a larger opaque figure cannot. There are also only 15 visible palette entries
plus transparency, shared between front and back, with corresponding normal and
shiny colors. Independently reducing four images can create mismatched colors.

The audit found 189 eligible file sets in stock Essentials and 764 in the Gen 9
pack without geometry or palette-count reduction. These are source-file counts,
including earlier generations and variants, not an import count or unique
Pokémon count. Many sets overlap the higher-priority layers. Mandatory GBA RGB555
color encoding still applies to imported RGB888 images.

Oversized or incompatible sets remain available for later manual curation. The
current pass does not silently shrink or recolor them. Radical Red's artwork is
already in the target hardware format, which avoids those compromises.

## Credits and verification

[SPRITE_RADRED_RESEARCH.md](SPRITE_RADRED_RESEARCH.md) records the official RR 4.1
artist credits, links and remaining attribution gaps. Local Essentials credit
files are recorded in the source audit. Keep donor provenance and artist credits
with future source/patch releases; a donor game's code license is not a blanket
asset license.

The Transform/form-change renderer previously derived its DMA transfer length
from sprite positioning metadata. The graphics review found both short copies
and copies beyond the allocated sprite frame. It now copies one 2,048-byte frame;
the existing animation system still selects Castform's additional frames from
its separate WRAM buffer. `scripts/test_transform_art.py` exercises the actual
handler with guarded memory and retains the old calculation as a negative test.
All 224 native cases pass, and the legacy calculation reproduces 144 expected
failures. The ROM check also confirms the complete compiled handler, entry hook,
frame-copy DMA constant and unchanged frame allocator are installed.

Source and ROM checks establish data preservation and memory boundaries. They do
not replace user-operated mGBA checks of Transform, form changes, shinies and
battle positioning.

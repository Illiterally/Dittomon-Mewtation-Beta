# Keep one clear player download

Game downloads belong in GitHub Releases. Keep the repository root limited to the README, credits, and supporting folders. Never add a second `PLAY-HERE`, upgrade ZIP, or loose patch to the file listing.

For each release:

1. Prepare and test the game patch. Preserve the existing release and its saves.
2. Update `.github/current-release.json` with the reviewed version, exact filenames, download URL, and hashes. Update the README's title, first download link, filename, and setup instructions together. Keep **Public Beta** prominent.
3. Check the actual ZIP: `python .github/scripts/check_downloads.py --package /path/to/package.zip`. This checks filenames inside instructions, packaged metadata, patch identity, and every included file's checksum.
4. Publish the release with a prominent direct ZIP link. Mark previous releases archived and point their notices at `/releases/latest`; preserve their tags and assets. Do not mark the whole repository archived.
5. Update the website's title, status, download URL, and expected filename together. Preserve the owner's saved copy. Keep the repository description version-neutral.
6. Run `python .github/scripts/check_downloads.py --live` after publication. This downloads the public assets and checks both website entry points. Check the GitHub Actions result and inspect the visible repository and release page before reporting completion.

The release check deliberately distinguishes historical version mentions from actual download filenames. It must reject stale ZIP/patch filenames, duplicate root downloads, broken moved-document links, mismatched patch metadata, and changed public file hashes.

A documentation-only package correction must preserve the patch and resulting ROM hashes. Record the correction in the release notes and regenerate both packaged and external checksums. Do not imply that an unchanged patch is a new game build.

# Model repository working instructions

- Read `HANDOFF.md` first, then the selected module/version README. The latest direct user request takes precedence.
- This repository contains C3 and BH1750 reference modules, L6 physical-prototype files, and the L7 enclosure. It is separate from the custom PCB repository.
- Preserve L6 as the tested prototype baseline. Save meaningful geometry revisions as a new version; do not silently overwrite a released baseline or reuse old tags.
- Use Autodesk Fusion for requested enclosure editing. Observe the actual app state before interacting; old screenshots/window IDs are not current state.
- Preserve optical alignment, four-corner supports, the USB-opposite lid hold-down, hidden glue joint, flush artwork, and one M3x30 direct-plastic hinge unless the user changes the requirement.
- Native F3D files retain hidden construction history. Export only intended active printable parts. Do not delete internal history merely because old component names appear.
- Keep geometry/source, exports, checks and user test feedback distinct. CAD checks do not establish successful printing or fit.
- Put temporary regeneration in ignored `generated/`. The consolidated L7 script has syntax checks but has not been rerun in Fusion after path consolidation.
- After changes update HANDOFF, the version README and relevant asset hashes. Check `git status` before committing. Do not force-push or move existing release tags.

# Progress meeting

21/03/2023

## Agenda

- Introductions (5 mins)
- Case study: Scythe (Logan Ward)
- Discussion
- Summary of progress on `api` in MaRDA Extractors WG (Matthew Evans)
- Open discussion

## Case study: Scythe: an extractor library you might like

Presented by [Logan Ward](https://github.com/WardLT). Unfortunately we forgot to record the talk. See [Scythe GH repo](https://github.com/materials-data-facility/scythe) as well as the [slides](scythe-overview.pdf).

- originally called MaterialsIO ➝ renamed to Scythe due to Google's material design SEO
- designed to introduce some standardisation into internal metadata extraction at Argonne
- group ➝ extract ➝ adapt pipeline
  - Group files that belong together, e.g. in/out files ➝ logic is extractor specific
  - Extract into a documentable format - currently JSON
  - Adapt for translating between known filetypes/formats
- Python interface
- Design principle: filesystem ➝ database should work in 1 line of code

1. Question (Matthew Evans): Self describing schema - how is this implemented?
   Answer: For now, in a JSONSchema as it is verifiable and human-readable.

2. Question (Matthew Evans): Handling groups of files - how does the user select the appropriate filetype?
   Answer: Better illustrated using an example:
    - 1) each file is treated separately
    - 2) each particular datatype has its own extractor
    - 3) supplemental files are pulled out by the extractor itself
   Filetype matching is done by prefixes or postfixes (e.g. for VASP).

- Manifesto: summaries of data, not necessarily lossless
- Well designed contributor guide
- Key feature: autodiscovery of Scythe-compatible Extractors on the current host via Stevedore

3. Question (Peter Kraus): Is the "losslessness" of the data described somewhere?
   Answer: If it's not in the documentation, then not.

4. Quetion (Ken Kroenlein): Universal datastructures might not work well. How about data dictionaries and standards or similar technologies to describe the structure of the data?
   Answer: This is currently an Extractor-level decision, to drive adoption.

## Summary of progress on `api` in MaRDA Extractors WG

Matthew gave a quick run-down of the current draft of `Extractor` execution api. Please see the PR [#5](https://github.com/marda-alliance/metadata_extractors_api/pull/5) for details, review and comments.


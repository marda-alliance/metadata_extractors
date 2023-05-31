# Progress meeting 5

30/05/2023

## Agenda

- Intro from Matthew Evans
- Overview of NOMAD Parsers Lauri Himanen
- Demo of API from Matthew Evans

## Minutes

### MaRDA WG status summary - Matthew Evans
- Quick summary of MaRDA Extractors WG
- Overview of the 3 repos, incl. [schema](https://github.com/marda-alliance/metadata_extractors_schema), [registry](https://github.com/marda-alliance/metadata_extractors_registry), and [api](https://github.com/marda-alliance/metadata_extractors_api)
- Overview of the current `Filetypes` and `Extractors` in the registry

**See also [Demo of API](#demo-of-api-videos) videos below!**

### NOMAD Parsers - Lauri Himanen

1. What is NOMAD:
    - RDM platform
    - covers simulations, experiments, workflows
    - funded by German NFDI
    - [nomad-lab.eu](nomad-lab.eu) is a freely available, open, central repository
    - NOMAD Oasis is a self-hosted instance
2. Getting started with NOMAD:
    - `upload` files
    - add / edit using ELN interface
    - publish to get a DOI
3. Parser infrastructure in NOMAD:
    - act on uploaded files and turn them into `entries`
    - `entries` can be searched, analysed, have a known structure -> implies a `schema`
    - each parser has to define its own `schema`
    - NOMAD has it's own Pydantic-like schema language called NOMAD metainfo
    - parsers are triggered on upload of a file, matching by using:
      - file extension
      - file mimetype
      - file contents (e.g. header)
    - one file is usually one `entry`, but sometimes one file is many `entries`
    - reading of auxilliary files in an upload is handled by the parser
4. Parser plugins
    - basic NOMAD has ~60 parsers pre-installed, mostly for electronic structure calculations
    - defining custom parsers is possible via a `plugin` mechanism
    - `plugins` may be integrated into the central service after a review
    - plugins have to have:
        - a schema definition in a specified location
        - the parsing code and file matching logic in a specified location
    - the general `schema` can be extended by the `parser`
    - the infrastructure is using a lot of regex to perform matching of quantities and filetypes
    - parsing is performed by passing the path of the file
    - `nomad.yaml`: a configuration file for the plugin

### Q/A:
- Peter: About auxiliary files - must be uploaded together, or can NOMAD ask for them?
- Lauri: They must be uploaded together. Their usage may be documented in the README. The parser can emit a debug/log message, but the user is responsible for uploading all files together.

---
- Nicolas: Use of regex on plaintext files does not sound efficient. Is this really the best way? Wouldn't it be better to fix QM codes upstream?
- Lauri: Some QM codes are moving away from text files, but progress is slow. There is also the important issue of legacy QM data, which has to be addressed somehow.

---
- Peter: Are you aware of QCSchema?
- Lauri: No, not yet.

---
- Matthew: Overlap with MaRDA WG. How would we go about validating plugins?
- Lauri: The plugin mechanism in NOMAD is very new. Registry and an authority marking/reviewing plugins would be useful.

---
- Matthew: How about sandboxing plugin code?
- Lauri: Sandboxing is tricky, as on an instance, it's a question for the Oasis (instance) admin


### Open Discussion:
- Matthew: Suggestion to skip next months (July) meeting in favour of writing & working.
- Peter: Agreed.

---
- Steffen: Multiple people have different goals. Focusing on a single extractor for a single filetype is perhaps too ambitious.
- Matthew: Yes, this is currently the goal of the WG.

---
- Steffen: Focus should be on getting more examples. This requires making the parser submission process to be simple and comfortable enough even for lazy people...
- Peter: A website frontend to avoid boilerplate is on the TODO list, however, manpower is a problem.

---
- Steffen: Review process of extractors should be currently very streamlined, as long as things don't overwrite other people's work, we should allow things in.
- Matthew: Sandboxing at some level might be necessary, as otherwise it's a big safety issue.

### Demo of API videos:
- [API Intro and `biologic-mpr` example](https://drive.google.com/file/d/10v6uE6By0bm3Z2Sfno1ULM6I8itX75uF/view?usp=drive_web)
- [Parsing `agilent-dx` using API](https://drive.google.com/file/d/1XeTYR14dJORUGIZnYzoc1FRM0eWUNSVu/view?usp=drive_web)
# Progress meeting 4

02/05/2023

## Agenda

Intro from Peter
ELN roundtable discussion of feature wishlist

## Minutes

Peter Kraus: Introduced the current state of the registry, API prototype and schema.

Suggestions from Kevin Jablonka:

- Reusability and validation as main focus: is the parser tested, how is it
  tested and how reliable is it?
- Able to use code without providing much boilerplate

Peter:
- possibility of MaRDA permanent infrastructure for running the registry
- output schema is still a target but perhaps not in current WG

Matthew: containerisation and construction of environments is important: how
about things outside Python: JS/WASM/docker?

Discussion about output formats: option to specify some useful common formats

Markus: wishlist -- must be open in the output format 100%

Nicolas: ELN developer's wishlist -- adding custom JSON to arbitrary files that
are added to a sample/experiment. Want to deploy a container that can scrape
arbitrary files.

Steffen: also ELN developer, in agreement with Nicolas but needs metadata instead of data -- i.e.,
should be a case switch, wish ability to see thumbnail of the data. Shouldn't
decide meaning of data, instead allow it to be mutable. Also something pip
installable for programmatic use.

Matthew: maybe having monolothic container baked with registry as a build engine

Markus: 
- Three execution pathways proposed: "external" service, local docker, local python package. 
- Very tricky to provide all three reliably, especially due to dependencies. 
- For Nomad, important to ensure scalability to ~million files -> single docker instance might not work

Steffen: how to deal with multiple parsers for a given file: some rating
process. Also all the different APIs for parsers are an issue, can we capture
that?

Peter: API and schema repository have some progress towards this

Nicolas: 
- common API is not feasible for all parsers, 
- ELN users should not be exposed to API related issues at all
- keep it simple by choosing/bundling one extractor per filetype

Markus: file type detection is crucial, NOMAD could contribute its own detection
system. Needs to be a combination of file extension, regex etc.

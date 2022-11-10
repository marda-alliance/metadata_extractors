# MaRDA Extractors WG

This repository contains organizational info for a [MaRDA](https://www.marda-alliance.org/) working group (WG) focused on connecting and advancing interoperability of efforts on automated extraction of metadata from materials files.

**Contacts**:

- *[Matthew Evans](https://ml-evs.science), UCLouvain*
  (`matthew.evans[at]uclouvain.be`)
- *Peter Kraus, TU Berlin*
- *David Elbert, Johns Hopkins University* 
  (`elbert[at]jhu.edu`)

## Organization & logistics

The working group will start with an initial meeting on [November 30th at 14:00 UTC/15:00 CET/09:00 EST](https://www.timeanddate.com/worldclock/fixedtime.html?iso=20221130T14).

- All meetings will be open and will take place on [Jitsi](https://meet.jit.si/)
  with the room code `marda-extractors`. Meeting dates will be arranged in the
  previous meeting, and will be announced on the mailing list.
- The [GitHub discussions on this
  repo](https://github.com/marda-alliance/metadata_extractors/discussions) will be used for asynchronous
  communications about the design, development and logistics of the overall
  working group - please introduce yourself in the [announcement
  thread](https://github.com/marda-alliance/metadata_extractors/discussions/1)!

## Proposal

The text below is taken from the initial working group proposal.

### Motivation

Enabling interoperability between experimental apparatus, software, scientists and informaticians requires a lot of plumbing.
This plumbing is often characterized as an **Extract-Transform-Load** (ETL) pipeline, whereby data is first extracted from some heterogeneous sources, transformed into a suitable format for the use case (querying, archival, further analysis) and then loaded onto a storage platform (a database, a filesystem, an archive repository, supplementary info for a publication).
Such pipelines are often opaque, not reproducible and not sufficiently modular to be reusable; these features penalize groups with fewer resources to devote to data management, leading to much duplicated effort on reimplementing parsers or extractors for different file types and transformed data models.

This working group aims to address these issues and promote FAIR practices by designing, creating and reusing software and infrastructure to streamline the process of describing ETL pipelines in such a way that they can be more broadly reused, and associated tooling for automated execution and discovery of said pipelines.
Following the name of the WG, it will primarily target the **Extraction** step, i.e., the literal parsing of unstructured data files, and the description of the output Transformed data model and encouragement of FAIR representations (c.f. the upcoming recommendations from MaRDA WG5).
This is a different approach from the typical target of creating a unifying output data schema; instead we will remain agnostic to the output format if it is sufficiently well-described in a machine-actionable manner.

### Work plan

This working group aims to investigate, design, and implement or re-use a hierarchy of open software tooling and open infrastructure to achieve the goals outlined above. The initial 6 months of meetings will primarily involve scoping the overall project, and the group members, to ensure that the WG is representative of existing efforts, thus maximizing the chances of adoption. The three main technical thrusts are expected to be:

1. **A lightweight metadata schema for parsers** and associated tooling for software libraries to self-report:
    - The file formats they support (e.g., output files from a particular experimental apparatus, or log files from a computational chemistry code)
    - The shape and semantics of the data models produced, via existing formats for data descriptionand tooling,  such as , for example self-contained formats (NeXus, CIF), schemas (JSONSchema, XSD) and, semantic data (RDF, JSON-LD & CSV-LD),  HDF5 and STAR (and their respective domain-specific derivatives NeXus and CIF). Depending on the output format, such metadata can be provided in-band or out-of-band in a well-defined location (e.g., a separate file, a persistent URL), following the upcoming recommendations of the MarDA Data Dictionaries WG5.
    - Any additional metadata required for re-use, such as code versions and environments, source and code archive URLs, and bibliographic data following, for example, Dublin Core.
1. **A common API specification for executing parser code**, and associated tooling.
    - Parsers could be run natively (in the language they were written in) on local files via the creation of a language-specific harness to which the parsers contribute plugins. This harness will execute the parser in such a way to maintain the link with its reported schema, as above.
    - Parsers could be packaged into containers (Docker or otherwise) that provide reproducible environments for their execution. Another harness for executing the containers from various languages, or via an HTTP API, will be investigated. Such containers can then be deployed as part of larger infrastructure, or used in a serverless fashion. This approach is well-suited for asynchronous message queues and streaming of data.
1. **A searchable registry of parsers**
    - Any parser code that implements the above functionality can be added (automatically or  otherwise) to a registry of parsers that can be filtered against the metadata schema from the I. This could allow for automated support of a new file type (i.e., filter for parsers that support such a file type, and that provide a container, automatically download and deploy the container and use the expected endpoints to parse the data file).
    - Such a registry would provide discoverability and automated validation of resources, accelerating the proliferation of shared or overlapping data models, schemas and semantics.
The registry can then be used to chain parsers together as composable blocks, for example, a custom semantic layer could be added to a data model as a converter from a JSON file with well-defined schema, into a JSON-LD file.

### Goals & expected impact

- Choose some “anointed” parsing libraries across underserved disciplines (primarily for experimental data), and use them as prototypical cases for the above tooling. There are already several options within the list of interested working group members that could be fruitful. The impact here should not only be a more reusable packaging of existing parsers, but also upstream improvements to the parsers themselves as schemas are formalized for the first time.
- Once a simple registry has been set up, WG members will trial its use within their own existing infrastructure projects across materials science and chemical data management. If the trial is successful, some of the maintenance burden for these steps could be shared amongst the interested parties, such that future development benefits all.

### Deliverables

Within 12 months of the commencement of the working group, we will deliver:

- A Working Group Note, published on the MaRDA Alliance website
- A proof-of-concept implementation of I, II and III: documented, open source and available under the MaRDA Alliance GitHub organization.

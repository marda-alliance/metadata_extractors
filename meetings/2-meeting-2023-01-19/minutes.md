# Progress meeting

19/01/2023

## Agenda

- Introductions (5 mins)
- Summary of main goals (Matthew Evans)
- Progress in WP1, WP2, WP3 (Matthew Evans)
- Case study: yadg (Peter Kraus)
- Open discussion

## Minutes from Discussion

1. David Elbert:
  - Suggestion: Please register for the [annual MaRDA meeting](https://www.marda-alliance.org/blog-2/marda2023/). Poster sessions for ECRs are scheduled, with prizes!

--

2. a) Casper Andresen:
  - Question: Will the transformation step in our pipeline be based on semantics, or only a pure syntax translation?

2. b) Matthew Evans:
  - Answer: LinkML allows linking to other schemas, such as Dublin Core or Schema.org. Therefore, capturing semantics should be possible. Contributions from experts are welcome!

--

3. a) Logan Ward:
  - Question: Interesting choice of going with a "dataschema" for yadg. What exactly is it? What are the limitations?

3. b) Peter Kraus:
  - Answer: It defines the "folder structure" of files related to a single experiment, as opposed to the layout within the individual files. User adoption is quite hard, and very often you just want the raw data, without bundling it.
 
3. c) Logan Ward:
  - Suggestion: Efforts such as this one (metadata extractors) could lead to a nice recursion, where your extractor taps into other linked tools.
  
 --
 
4. a) Steffen Brinkcmann:
  - Question: Is passing parameters into extractors (e.g. information about background etc.) condsidered for the schemas?

4. b) Peter Kraus:
  - Answer: From my point of view, not at the extractor level, which should not be post-processing the data values.

4. c) Matthew Evans:
  - Answer: This is a very application-dependent question. Parameters are likely to strongly depend on the extractors themselves. If we support it, it must be optional.
  
 --

5. a) Ken Kroenlein:
  - Suggestion: For extractor output, the data dictionaries WG of MaRDA can provide a controlled vocabulary.

5. b) Peter Kraus:
  - Answer: I will be in touch to figure out how I can implement this in my code!

 -- 

6. Closing remarks:
- MaRDA annual meeting on 25. - 27. Feb. 2023
    - have a first tagged schema by then (ME)
    - have an example implementation in yadg (PK)
- Office hours: 
    - fortnightly (approximately), informal
    - next one on 25. Jan 2023, 15:00 UTC
    - suggest a date/time if the dates planned don't suit!
    



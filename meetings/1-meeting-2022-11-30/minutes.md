# Kick-off meeting

30/11/2022

## Agenda

- Introductions (5 mins)
- Initial slides by Matthew Evans (15 mins)
- Q&A
- Open discussion

## Minutes from Q&A & Discussion

1. Matthew Evans: Introductory presentation. Recorded ([video](https://www.youtube.com/watch?v=6x5Ow-CLRWg), [slides](https://docs.google.com/presentation/d/1QTqDEO3H1s_wAtcE9DD6k1eCJ7GzvdV2spjHE94bEQw/edit?usp=sharing))

2. a) Markus Scheidgen:
- Question: Will slides be shared?
- Suggestion: A goal can be to establish a service registry with a searchable `filetype -> tools available` mapping.
- Comment: Skeptical about "chaining parsers" due to low chance of success.

2. b) Matthew Evans:
- Comment: A way of coordination might be to have a discussion for each WP.
- Answer: Slides will be published.

4. a) Steffen Brinckmann:
- Question: Transformation WP concerns not only data, but also filetype?
- Suggestion: CWL is used in chemistry field:
    - wrappable around Python
    - requires a server/service
- Question: What happens when the scientist wants to "add" processing (area under curve) as metadata?
- Question: Will it be possible to edit/customise extractors?

4. b) Matthew Evans:
- Answer: Are filetypes included, workflow & interoperability is well covered by the WPs.
- Answer: Optional features for extractors:
    - individual decision of parsers, implemented in parsers
    - good use-case for parser chaining (see 2a)
- Comment: Note the discussion "Prior Art" on GitHub.

5. a) Ken Kroenlein:
- Comment: Concerned that a parser that does `file -> JSON/XML` is already a full ETL pipeline.
- Suggestion: Reworking of schema (WP1) to be a lot tighter & low level, as the `file -> bytes in memory` step is where the "magic" and pipelining might happen. This would also allow to piece parsers together.

5. b) David Elbert:
- Answer: Important to check scope of WPs as we go.
- Answer: Boundary of data vs metadata, or what is defined as a derived value, is currently defined by the filetypes or parsers. Stick to that definition for now.

6. a) Ken Kroenlein & Jim Warren:
- Comment: Just achieving a schema (WP1) is a lot of work and would be a win.

6. b) Peter Kraus:
- Comment: Registry (WP3) is a "low hanging fruit" that can be done with little work.

6. c) Steffen Brinckmann:
- Question: Order of action: Should we start with schema (WP1) and then move to API (WP2), a "discussion based" approach, or should we start with WP2 and move to WP1, an "evolutionary approach"?

6. d) Markus Scheidgen:
- Comment: Schema (WP1) is key to be able to find the right parser.
- Comment: Registry (WP3) is not super valuable without WP1, as it's just a page with tools, it would need at least WP1, but ideally WP2 to be useful.
- Comment: We shouldn't worry about chaining tools at this moment, avoids specifying parser output schema.

6. e) Jim Warren:
- Comment: Figuring out schema (WP1) is key.
    - Examples are very important.
    - Need to identify what's broken in each parser.

7. a) Nicholas Carpi:
- Suggestion: Vision, as an ELN developer, is to be able to:
    - parse an user-supplied file using an "external service"
    - added value for the user, e.g. visualisation, post-processing
- Comment: Huge amount of prior art, but no common framework.
- Question: What's the difference between the goals of this WG and Clowder framework?

7. b) David Elbert:
- Answer: Unfortunate that Clowder folk are not present. Will try to get them involved.
 
7. c) Matthew Evans:
- Answer: Point taken about existing projects & Clowder. Risk of creating yet another standard.
- Question: What would an ELN developer like from this "external service"? Would we need to provide hardening?

7. d) Nicholas Carpi:
- Answer: "External" as in not within ELN, but not off-site. Everything should be done locally, via e.g. a HTTPS REST service: `post file -> get data`
- Answer: It would be great to have to use only one service, with reasonable and understandable errors.
- Suggestion: Maintenance of a single repo including all parsers can be tricky, so a plugin architecture might be the way to go.

7. e) Peter Kraus:
- Comment: There is a lot of prior art, some of it at various stages of bit rot. Added benefit of this WG would be testing of parsers via CI to detect broken/bitrotten parts of code.

7. f) Ken Kroenlein:
- Concern: Think about long term home for CI/CD. Relying on external services & running out of budget is a good recipe to fail.

7. g) David Elbert:
- Answer: While MaRDA itself cannot provide funding, we can try to arrange long-term funding as part of the work of this or future WG.

8. Closing remarks:
- Next meeting: January
    - should have some work done by then
    - a prototype for our own parsers (PK, ME)
- MaRDA annual meeting is also happening
- Suggestion: Weekly open hour on Jitsi - will be communicated in due course.




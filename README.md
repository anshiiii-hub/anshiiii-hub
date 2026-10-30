<div align="center">

**00 / SOMETHING IS GROWING**

# THE GLITCH GARDEN

*WHERE CURIOSITY GROWS INTO CODE*

<img src="assets/glitch-garden/hero-garden.png" width="100%" alt="NOVA, a tiny floating mint crystal, discovers a luminous seed among crystalline plants and branching data constellations.">

**Anshita Dawar** · Final-year B.Tech · Artificial Intelligence & Machine Learning

Python, data, practical applications — and the occasional beautifully uncooperative experiment.

[The human](#the-human) · [The ecosystem](#the-ecosystem) · **[Projects](#specimens)** · [Toolkit](#the-tool-garden) · [Next growth](#next-growth) · [Say hello](#say-hello)

</div>

> A small field guide to the things I build, the patterns I notice, and the questions that refuse to stay small.

<br>

<a id="the-human"></a>

## 01 / The human behind the experiments

<img src="assets/glitch-garden/nova-curious.svg" width="155" align="right" alt="NOVA examines three connected data points.">

Hi, I'm **Anshita**. I'm a final-year B.Tech student specializing in **Artificial Intelligence and Machine Learning**. I like turning messy information into something understandable, and turning “what if?” into software someone can actually use.

My projects span Python data stories, document tools, and backend systems. I'm still strengthening the fundamentals beneath them: how to design, test, explain, and reliably ship what I build. My ideas currently grow faster than my ability to name their folders.

**Already planted:** Python applications, data visualization, document comparison, and workflow orchestration prototypes.  
**Still growing:** ML foundations, resilient backend design, and better testing and deployment habits.

*NOVA is the fictional organism exploring this garden. I'm the human writing the code.*

<br clear="all">

<a id="the-ecosystem"></a>

## 02 / The ecosystem of ideas

<img src="assets/glitch-garden/idea-ecosystem.svg" width="100%" alt="Five connected habitats: a data marsh, neural tree, logic cavern, application canopy, and automation meadow.">

| Habitat | What grows here | Follow the path |
| :-- | :-- | :-- |
| **01 · The Data Marsh** | Raw information becomes patterns, charts, and questions worth asking. | [UPI analysis](https://github.com/anshiiii-hub/upi-analysis) |
| **02 · The Neural Forest** | ML foundations and intelligent applications, explored one experiment at a time. | [Learning directions](#next-growth) |
| **03 · The Logic Caverns** | Programming fundamentals, algorithms, and the patient art of reasoning. | [Next growth cycle](#next-growth) |
| **04 · The Application Canopy** | APIs and interfaces give an idea somewhere to live. | [DocDiff](https://github.com/anshiiii-hub/DocDiff) |
| **05 · The Automation Meadow** | Repeated steps become explicit, inspectable workflows. | [ORQESTRA](https://github.com/anshiiii-hub/ORQESTRA) |

*These habitats describe interests, not a checklist of completed achievements.*

<br>

<a id="specimens"></a>

## 03 / Specimens: things I've built

### Specimen 001 · ORQESTRA

**A task graph with a memory of what happened.**

[<img src="assets/glitch-garden/project-orqestra.svg" width="100%" alt="An illustrated task graph branches into parallel paths, converges at a review node, and reaches an output. NOVA watches.">](https://github.com/anshiiii-hub/ORQESTRA)

An orchestration prototype for running analysis through a persisted task graph, with validation, execution state, and recovery made visible. It explores how an AI-assisted workflow can remain inspectable when tasks fail or sensitive writes need review.

**Stack:** Python · FastAPI · PostgreSQL · SQLAlchemy · Pydantic · React · TypeScript · Docker

- **Durable scheduling:** a polling worker claims ready tasks with expiring leases and checks attempt ownership before publishing results.
- **Explicit execution boundaries:** validated dependencies and agent contracts; offline planning by default, with optional OpenAI planning.
- **Human review:** sensitive write tools pause for approval; the dashboard exposes workflow state, events, and outputs.

**Field note:** a prototype under development. Production readiness and hosted demos are not verified; a full autonomous coding product remains planned.

[Explore the source →](https://github.com/anshiiii-hub/ORQESTRA) · [Architecture](https://github.com/anshiiii-hub/ORQESTRA/blob/main/docs/architecture.md) · [Scheduler](https://github.com/anshiiii-hub/ORQESTRA/blob/main/docs/scheduler.md)

---

### Specimen 002 · DocDiff

**Find the change hiding between two versions.**

[<img src="assets/glitch-garden/project-docdiff.svg" width="560" alt="Two document specimens show highlighted lines connected by a comparison arrow.">](https://github.com/anshiiii-hub/DocDiff)

A Flask application that helps readers follow document revisions through paragraph-level changes and word-level highlights.

**Stack:** Python · Flask · difflib · python-docx · pdfplumber · HTML/Jinja

- Extracts text from TXT, Markdown, DOCX, and text-bearing PDFs.
- Uses `SequenceMatcher` and similarity-based pairing to classify additions, deletions, and modifications, then highlight word changes.
- Produces comparison reports with change counts; the documented summary flow supports optional Gemini assistance and a rule-based fallback.

**Field note:** reports are stored in memory. Scanned PDFs and complex layouts need additional processing.

[Explore the source →](https://github.com/anshiiii-hub/DocDiff) · [Comparison engine](https://github.com/anshiiii-hub/DocDiff/blob/main/diff_engine.py)

---

### Specimen 003 · UPI analysis

**A monthly payment dataset, made readable.**

[<img src="assets/glitch-garden/project-upi.svg" width="560" alt="Two abstract chart lines illustrate the data-story theme; these are decorative, not actual UPI measurements.">](https://github.com/anshiiii-hub/upi-analysis)

A Flask data story exploring UPI payment volume, value, and average transaction size through interactive charts and a data table.

**Stack:** Python · Flask · pandas · Plotly · HTML

- Reads a precomputed monthly CSV and converts dates for charts and tabular display.
- Presents transaction volume versus value on separate axes, plus average transaction size and year-on-year value growth.
- Calculates month-on-month volume change with pandas `pct_change()`.

**Field note:** descriptive analysis, with no trained prediction model. The CSV must be present for analysis pages to work.

[Explore the source →](https://github.com/anshiiii-hub/upi-analysis) · [Application code](https://github.com/anshiiii-hub/upi-analysis/blob/main/app.py)

*Project descriptions are grounded in repository documentation and source inspected on 30 October 2026. No public live demo is linked here.*

<br>

<a id="the-tool-garden"></a>

## 04 / The tool garden

<img src="assets/glitch-garden/tool-garden.svg" width="100%" alt="Four pressed botanical specimens represent tools used in projects, ongoing learning, experiments, and future goals.">

| Field classification | Tools & concepts | Evidence or direction |
| :-- | :-- | :-- |
| **01 · CULTIVATED** · used in projects | Python, Flask, pandas, Plotly | [UPI application](https://github.com/anshiiii-hub/upi-analysis/blob/main/app.py) |
| **01 · CULTIVATED** · used in projects | FastAPI, PostgreSQL, SQLAlchemy, Pydantic, React, TypeScript, Docker | [ORQESTRA architecture](https://github.com/anshiiii-hub/ORQESTRA/blob/main/docs/architecture.md) and [source](https://github.com/anshiiii-hub/ORQESTRA) |
| **01 · CULTIVATED** · used in projects | difflib, python-docx, pdfplumber, HTML/Jinja | [DocDiff](https://github.com/anshiiii-hub/DocDiff) |
| **02 · GROWING** · actively learning | ML foundations, algorithms, backend design, Git/GitHub workflow | Practice, smaller experiments, clearer explanations |
| **03 · EXPERIMENTAL** · exploring | AI-assisted planning, document summaries, recovery strategies | Optional integrations and prototypes; still evaluating the trade-offs |
| **04 · SEEDS** · future direction | More complete data pipelines, deployment practice, collaborative ML work | Turn the next useful question into a well-documented application |

*“Cultivated” means used, not mastered. No proficiency percentages; the projects are the evidence.*

<br>

<a id="unexpected-mutations"></a>

## 05 / Unexpected mutations

<img src="assets/glitch-garden/nova-debugging.svg" width="165" align="right" alt="NOVA inspects a small coral bug with six legs.">

**Fictional field notes from a very familiar ecosystem.**

<details>
<summary><strong>Incident M-01 · The multiplying bug</strong></summary>

**Observation:** one fix produced three new symptoms.  
**Hypothesis:** the first bug had an extended family.  
**Experiment:** isolate the smallest failing example; change one thing.  
**Outcome:** less mystery, a useful regression case, and a smaller family reunion.

</details>

<details>
<summary><strong>Incident M-02 · The observer effect</strong></summary>

**Observation:** the demonstration behaved differently with an audience.  
**Hypothesis:** confidence was an undocumented dependency.  
**Experiment:** reproduce with the same inputs and capture the logs.  
**Outcome:** “works on my machine” became a question, not a conclusion.

</details>

<details>
<summary><strong>Incident M-03 · The unusually helpful error</strong></summary>

**Observation:** the error message contained the answer all along.  
**Hypothesis:** reading it slowly might be faster than rewriting everything.  
**Experiment:** read it slowly.  
**Outcome:** a typo became a lesson in experimental restraint.

</details>

<br clear="all">

<a id="next-growth"></a>

## 06 / The next growth cycle

<img src="assets/glitch-garden/growth-paths.svg" width="100%" alt="Three uncompleted paths branch outward from NOVA toward mint, periwinkle, and lime seeds.">

| Path | What I'm working toward | A useful next experiment |
| :-- | :-- | :-- |
| **Roots · fundamentals** | Stronger problem-solving and software design | Solve a small problem, explain the trade-offs, test the awkward cases. |
| **Branches · applications** | Practical AI/ML and backend systems | Connect a bounded data workflow to an application with clear failure behavior. |
| **Canopy · delivery** | Better tests, documentation, and deployment | Make a project easier for someone else to run and understand. |
| **Cross-pollination · collaboration** | Shared learning through projects and hackathons | Build something useful with people who ask different questions. |

*Directions in progress. No invented deadlines, completion bars, or harvest guarantees.*

<br>

<a id="say-hello"></a>

### A little cross-pollination?

I'd love to collaborate on practical AI or data applications, small automation tools, and thoughtful hackathon projects.

[Find me on GitHub](https://github.com/anshiiii-hub) · [Wander through my repositories](https://github.com/anshiiii-hub?tab=repositories)

<br>

<a id="the-last-seed"></a>

## 07 / The last seed

<div align="center">

<img src="assets/glitch-garden/garden-footer.svg" width="100%" alt="NOVA floats quietly beside one tiny glowing seed beneath a constellation of pixels.">

**EVERY IDEA STARTS SMALL.**  
Every experiment changes something. Every project leaves a trace.

<details>
<summary>There's something inside the seed.</summary>

<br>

An unfinished idea isn't an empty one.

Sometimes the next step is a better question. Sometimes it's a smaller experiment. Sometimes it's finally reading the documentation.

Thanks for wandering through my little ecosystem.

**THE GARDEN IS NEVER FINISHED GROWING.**

</details>

<br>

*plant an idea · observe the unexpected · grow an experiment*

[Anshita Dawar](https://github.com/anshiiii-hub) · [Back to the roots](#the-human)

</div>

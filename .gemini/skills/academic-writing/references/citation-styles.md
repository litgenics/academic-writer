# Citation and Reference Style Reference

Use this reference when formatting in-text citations and reference lists. Never invent missing metadata. If a field is unavailable after verification, omit it if the style permits or mark `[metadata unavailable]` only in working notes, not polished references unless transparency is required.

## Supported styles

Support at least these styles when requested:

- APA 7
- MLA 9
- Chicago author-date
- Chicago notes-bibliography
- IEEE
- Harvard author-date
- Vancouver / numbered biomedical style
- BibTeX / LaTeX citation keys

If the user requests another style, adapt using verified style rules and state any uncertainty.

## Universal rules

- In-text citation must match a reference entry.
- Reference entry must match a cited source unless the user asks for a bibliography.
- Do not add DOI, URL, issue, volume, pages, publisher, or conference location unless verified.
- For direct quotations, include page number, paragraph number, section number, or clear locator when available.
- For paraphrases, page numbers are optional in some styles but useful when available.
- For sources with more than one version, cite the version actually read.
- For preprints, identify the preprint server when appropriate.

## APA 7 quick patterns

In text:

```text
Parenthetical: (Author & Author, 2024)
Narrative: Author and Author (2024) argue that...
Three or more authors: (Author et al., 2024)
Direct quote: (Author, 2024, p. 12)
```

Reference patterns:

```text
Journal article:
Author, A. A., & Author, B. B. (Year). Title of article. Title of Journal, volume(issue), page-page. https://doi.org/xxxxx

Conference paper:
Author, A. A. (Year). Title of paper. In Title of Conference Proceedings (pp. xx-xx). Publisher. https://doi.org/xxxxx

Preprint:
Author, A. A. (Year). Title of manuscript. Preprint Server. URL or DOI

Report:
Organization. (Year). Title of report. Publisher/Organization. URL
```

## MLA 9 quick patterns

In text:

```text
(Author page)
Author argues that ... (page).
```

Works Cited patterns:

```text
Author Last, First. "Title of Article." Journal Title, vol. x, no. x, Year, pp. xx-xx. DOI or URL.

Organization. Title of Report. Publisher, Year. URL.
```

## Chicago author-date quick patterns

In text:

```text
(Author Year, page)
Author (Year, page) argues that...
```

Reference patterns:

```text
Author Last, First. Year. "Title of Article." Journal Title volume (issue): pages. DOI/URL.

Organization. Year. Title of Report. Publisher. URL.
```

## Chicago notes-bibliography quick patterns

Footnote pattern:

```text
1. First Last, "Title of Article," Journal Title volume, no. issue (Year): page, DOI/URL.
```

Bibliography pattern:

```text
Last, First. "Title of Article." Journal Title volume, no. issue (Year): pages. DOI/URL.
```

## IEEE quick patterns

In text:

```text
Prior work has shown this pattern [1].
```

Reference patterns:

```text
[1] A. A. Author and B. B. Author, "Title of article," Journal Title, vol. x, no. x, pp. xx-xx, Year, doi: xxxxx.

[2] A. A. Author, "Title of paper," in Proc. Conference Name, Year, pp. xx-xx.
```

## Harvard quick patterns

In text:

```text
(Author and Author, 2024)
Author and Author (2024) suggest that...
```

Reference patterns:

```text
Author, A.A. and Author, B.B. (Year) 'Title of article', Journal Title, volume(issue), pp. xx-xx. doi: xxxxx.

Organization (Year) Title of report. Publisher. Available at: URL (Accessed: Day Month Year).
```

## Vancouver quick patterns

In text:

```text
Prior work has shown this pattern (1).
```

Reference patterns:

```text
1. Author AA, Author BB. Title of article. Journal Title. Year;volume(issue):pages. doi:xxxxx.
```

## BibTeX guidance

When the user wants LaTeX/BibTeX:

- create stable citation keys such as `smith2024misinformation`
- do not invent missing BibTeX fields
- include `url` or `doi` only when verified
- preserve existing citation keys if editing an existing manuscript

Example:

```bibtex
@article{smith2024shorttitle,
  author = {Smith, A. A. and Lee, B. B.},
  title = {Verified Title},
  journal = {Verified Journal},
  year = {2024},
  doi = {verified-doi}
}
```

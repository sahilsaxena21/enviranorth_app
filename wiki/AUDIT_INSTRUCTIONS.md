# Audit Workflow

When asked to **audit the wiki** or **lint the wiki**, execute all steps below in order, then produce a report.

## Step 1 — Structural lint checks

- [ ] All files have valid YAML frontmatter with `id`, `type`, and `last_verified`
- [ ] All frontmatter fields required for the file's `type` are present (check against `FRONTMATTER_TEMPLATES.md`)
- [ ] All `source_docs` values match actual filenames in `raw_text/`
- [ ] **Reverse coverage:** all files in `raw_text/` are referenced as a `source_doc` by at least one wiki page. Flag any raw_text file that no wiki page cites.
- [ ] All slugs in `controls_compatible`, `compares`, `recommended_products`, `works_with` resolve to real files in the wiki
- [ ] **Bidirectional relationships:** if product A lists control B in `controls_compatible`, then control B must list product A in `works_with` (and vice versa). Same for `compares` ↔ compared files, and `recommended_products` ↔ the product's `applications` list. Flag any one-way references.
- [ ] All inline markdown links (`[text](path)`) resolve to files that exist.
- [ ] `index.md` lists every product, control, comparison, guide, and application file that exists
- [ ] No orphaned files (files not referenced from `index.md` or another wiki page)
- [ ] All `Unverified` callouts are flagged for human review
- [ ] **Stale files:** flag any file where `last_verified` is more than 90 days old.
- [ ] **Glossary coverage:** scan wiki pages for technical terms and acronyms not defined in `glossary.md`. Flag missing terms.

## Step 2 — Hallucination check (claim verification)

For every wiki page, verify that each factual claim can be found verbatim or paraphrased directly from its cited `source_docs` file(s) in `raw_text/`.

For each claim that **cannot** be traced:
- Flag the claim with its wiki file, section heading, and the exact text
- Label it as: `UNVERIFIED` (no source file mentions it) or `CONTRADICTED` (source file says something different)
- Do **not** silently remove or correct it — report it for human review

## Step 3 — Cross-wiki consistency check

Compare wiki files against each other to detect contradictions. Focus on facts that appear in more than one file — specs, compatibility statements, part numbers, dimensions, and product relationships.

For each discrepancy found:
- Identify the two (or more) files that conflict
- Quote the exact text from each file
- Label each as: `CONFLICT` (files disagree with each other)
- Do **not** resolve it silently — report it for human review, then trace both claims back to `raw_text/` to determine which (if either) is correct

Common areas to check:
- The same spec stated differently across a product page, a comparison page, and an application guide
- Compatibility claims: product page says "works with SmartAIR" but the SmartAIR control page doesn't list that product in `works_with`
- A comparison page drawing a different conclusion than the individual product/control pages it summarises
- Application guides recommending a product that a product page marks as incompatible with that use case

## Step 4 — Produce the audit report

Write the audit report to `wiki_audits/audit-YYYY-MM-DD.md` (use today's date). Create the `wiki_audits/` folder if it doesn't exist. Use this structure:

```markdown
# Wiki Audit Report
**Date:** YYYY-MM-DD
**Files audited:** N
**Issues found:** N

---

## 1. Structural Issues
### 1a. Frontmatter problems (missing or invalid fields)
| File | Issue |
|---|---|

### 1b. Broken source_doc references
| File | source_doc listed | File exists in raw_text/? |
|---|---|---|

### 1c. Reverse coverage (raw_text files not used by any wiki page)
| raw_text file | Referenced by any wiki page? |
|---|---|

### 1d. Broken cross-references (frontmatter slugs)
| File | Broken slug | Field |
|---|---|---|

### 1e. Bidirectional relationship mismatches
| File A | Field (A) | File B | Field (B) | Issue |
|---|---|---|---|---|

### 1f. Broken inline markdown links
| File | Link text | Target path | Exists? |
|---|---|---|---|

### 1g. Missing from index.md
| File | Expected index entry |
|---|---|

### 1h. Orphaned files
| File | Reason |
|---|---|

### 1i. Unverified callouts requiring review
| File | Section | Callout text |
|---|---|---|

### 1j. Stale files (last_verified > 90 days)
| File | last_verified | Days stale |
|---|---|---|

### 1k. Missing glossary terms
| Term | Used in file(s) | Defined in glossary.md? |
|---|---|---|

---

## 2. Hallucination Check
### 2a. Unverified claims (not found in source_docs)
| Wiki File | Section | Claim | source_doc checked |
|---|---|---|---|

### 2b. Contradicted claims (conflicts with source_docs)
| Wiki File | Section | Wiki says | Source says | source_doc |
|---|---|---|---|---|

---

## 3. Cross-Wiki Conflicts
### 3a. Spec / fact conflicts between wiki files
| File A | File B | Section (A) | Section (B) | File A says | File B says |
|---|---|---|---|---|---|

### 3b. Compatibility conflicts
| File A | File B | Conflict description |
|---|---|---|

### 3c. Recommendation conflicts
| File A | File B | Conflict description |
|---|---|---|

---

## 4. Summary
- Structural issues: N
- Reverse coverage gaps: N
- Bidirectional mismatches: N
- Broken inline links: N
- Stale files (>90 days): N
- Missing glossary terms: N
- Unverified claims: N
- Contradicted claims (vs source): N
- Cross-wiki conflicts: N
- Recommended actions: [brief list]
```

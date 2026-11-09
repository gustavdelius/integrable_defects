---
name: github-markdown-math
description: >-
  Write, audit, and fix LaTeX math ($...$ and $$...$$) in Markdown files so that
  equations render properly on GitHub without vertical crushing, disallowed-macro
  errors, unrendered $$ blocks, or CommonMark backslash corruption. Activate this
  skill whenever drafting or editing mathematical Markdown documents intended for
  GitHub, or when fixing broken equation rendering on GitHub.
---

# GitHub Markdown Math Rendering Guidelines & Workarounds

GitHub renders Markdown math using a two-stage pipeline:
1. **Server-side (`cmark-gfm` + math sanitizer):** Parses `$ ... $` and `$$ ... $$` boundaries, applies CommonMark backslash-unescaping to ASCII punctuation, and filters disallowed LaTeX macros before emitting `<math-renderer>` tags.
2. **Client-side (`<math-renderer>` + `MathJax.tex2mml`):** Converts TeX into MathML and injects it directly into the DOM for native browser **MathML Core** layout.

Both stages have bugs that break standard LaTeX constructs. Follow the rules below whenever writing or fixing math in Markdown files.

---

## 1. Never use `\tag{...}` (Prevents 1-Character Vertical Crushing)

- **Bug:** `MathJax.tex2mml` serializes any equation with `\tag{2.1}` inside `<mtable displaystyle="true"><mlabeledtr><mtd>...`. Because the browser **MathML Core** specification removed `<mlabeledtr>`, Chromium/Blink and Firefox do not recognize `<mlabeledtr>` as a table row and crush the equation cell into a 1-character-wide vertical column.
- **Workaround:** Use `\qquad\text{(2.1)}` at the end of the display equation instead of `\tag{2.1}` (and Unicode prime `′` inside `\text{(3.3′)}` rather than nested `$\tag{3.3$'$}$`).

```markdown
<!-- Broken on GitHub (crushed into a vertical column) -->
$$
\partial_t \mathcal{Q} + \partial_x \mathcal{J} = 0 \tag{2.1}
$$

<!-- Works on GitHub -->
$$
\partial_t \mathcal{Q} + \partial_x \mathcal{J} = 0 \qquad\text{(2.1)}
$$
```

---

## 2. Never use `\operatorname{...}`, `\hbox{...}`, or `{\rm ...}` (Prevents Disallowed-Macro Errors)

- **Bug:** GitHub's server-side math sanitizer blocks `\operatorname` and `\operatorname*` with the banner:
  `The following macros are not allowed: operatorname`
- **Workaround:**
  - Replace `\operatorname{Foo}` with `\mathrm{Foo}`. When followed directly by a letter or backslash macro (e.g., `\operatorname{Im} D_t` or `\operatorname{pr} v`), add `\thinspace ` (`\mathrm{Im}\thinspace D_t`) to preserve operator spacing.
  - Replace plain-TeX `\hbox{...}` with `\text{...}` and `{\rm ...}` with `{\mathrm{...}}`.

```markdown
<!-- Broken on GitHub ("The following macros are not allowed: operatorname") -->
$\operatorname{diag}(1, -1)$ and $\operatorname{Im} D_t$

<!-- Works on GitHub -->
$\mathrm{diag}(1, -1)$ and $\mathrm{Im}\thinspace D_t$
```

---

## 3. Escape-Proof Delimiters, Spacing, and Row Breaks Against CommonMark Unescaping

- **Bug:** Before passing math to `<math-renderer>`, GitHub's Markdown parser runs CommonMark ASCII punctuation unescaping inside `$ ... $` and `$$ ... $$`:
  - `\{` $\to$ `{` and `\}` $\to$ `}` (causes `Missing or unrecognized delimiter for \left` on `\left\{` and silently strips braces from Poisson brackets `\{F, G\}` $\to$ `{F, G}`).
  - `\\` (when not followed by a newline) $\to$ `\` (breaks single-line matrices/cases like `\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}` into `\-1`, producing red undefined-macro errors).
  - `,\,` $\to$ `,,` (renders a double comma) and `\,` $\to$ `,` (renders a literal comma before `dx`).
  - Paired `*` inside a math block (e.g., `U_+(z - 2q_*), \quad z = w + Dq_*`) can be parsed as Markdown `<em>` emphasis.
- **Workaround:**
  - Use `\lbrace` and `\rbrace` instead of `\{` and `\}` (add a space if followed by a letter: `\lbrace F, G\rbrace`).
  - Use `\cr` instead of `\\` for row breaks inside single-line matrices/environments, or put a newline immediately after `\\` inside multi-line `$$\n...\n$$` blocks.
  - Use `\thinspace` instead of `\,` (with a trailing space before letters: `dt\thinspace dx`), and replace `,\,` with `, `.
  - Use `\ast` (`q_\ast`) instead of `*` (`q_*`) when an equation contains multiple asterisks.

```markdown
<!-- Broken on GitHub -->
Inline Poisson bracket $\{F, G\} = 0$, set $\left\{ x : x > 0 \right\}$, integral $\int dx\,dy$, matrix $\bigl(\begin{smallmatrix} 0 & 1 \\ -1 & 0 \end{smallmatrix}\bigr)$.

<!-- Works on GitHub -->
Inline Poisson bracket $\lbrace F, G\rbrace = 0$, set $\left\lbrace x : x > 0 \right\rbrace$, integral $\int dx\thinspace dy$, matrix $\bigl(\begin{smallmatrix} 0 & 1 \cr -1 & 0 \end{smallmatrix}\bigr)$.
```

---

## 4. Format `$$ ... $$` Block Boundaries for `cmark-gfm`

- **Bug:** GitHub's `cmark-gfm` math parser fails to recognize `$$ ... $$` blocks in three situations when the equation contains multiple `_` or `*` characters, leaving raw `$$` text and italicizing between underscores:
  1. Top-level `$$ ... $$` blocks without blank lines before and after.
  2. Multi-line `$$\begin{aligned} ... \end{aligned}$$` blocks where `$$` is on the same line as `\begin{aligned}` instead of on its own line.
  3. Multi-line `$$\n...\n$$` blocks indented inside list items (`1. ...` or `- ...`) or blockquotes (`> ...`).
- **Workaround:**
  - **Top-level display math:** Always place opening `$$` and closing `$$` on their own lines at column 0, preceded and followed by a blank line:
    ```markdown

    $$
    \begin{aligned}
    a &= b + c, \\
    d &= e + f.
    \end{aligned} \qquad\text{(1.1)}
    $$

    ```
  - **Display math indented inside list items or blockquotes:** Keep the entire equation on a **single line** as `$$\displaystyle ...$$` (using `\cr` for any internal environment row breaks), surrounded by blank lines:
    ```markdown
    1. Inside a numbered list item:

       $$\displaystyle S_d = \int_{\mathbb{R}} dt\thinspace \mathcal{L}_d(\phi_t, \psi_t) \qquad\text{(1.2)}$$

    ```

---

## Automated Check and Fix Script

Use [scripts/fix_github_math.py](scripts/fix_github_math.py) to check or automatically fix Markdown files:

```bash
# Check files without modifying them (exits non-zero if issues are found)
python3 .claude/skills/github-markdown-math/scripts/fix_github_math.py --check path/to/file.md

# Fix files in place
python3 .claude/skills/github-markdown-math/scripts/fix_github_math.py path/to/file.md
```

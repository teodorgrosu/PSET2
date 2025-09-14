# SE-for-Sci -- Homework 2

This assignment will explore a toy use case of `git` as a version control tool for scientific computing. Each part will have at most one short-answer question, which should be written in a file called `responses.txt` in the root directory of the repository. You may commit this file as you go, or you may opt to commit all of your responses at the end -- grading will not be affected by this choice. There is no minimum on what you are expected to write.

A fictional group of students are writing a package for computing the quadrature rules for [Gaussian quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature) on the interval $[-1,1]$ up to any precision (or more specifically, Gauss-Legendre quadrature). In practice, this task is trivialized by the [`mpmath`](https://mpmath.org/) package, but you do not have the heart to tell them that.
Without it, these students require arbitrary precision arithmetic to compute roots of Legendre polynomials, the foundation of which can be built from the native [`decimal`](https://docs.python.org/3/library/decimal.html) module.

They were fortunate enough to have the foresight of using a `git` repository to organize and combine their code contributions. However, due to inexperience, they are struggling to recombine all of their work back on the `main` branch for the upcoming milestone. Your task is to walk them through it.

Outside any merge conflicts (or personal interest, if you so wish), you do not need to know any contents or formats of the files.

## Part 1 - Accidentally-Committed Notes

Examine the `rootfind` branch (`git checkout rootfind`). Carla explains to you that when she finished implementing a different root finding algorithm, she accidentally committed her notes `polynomial_zeros.ipynb` to the repository. Once she figures out how to undo that, she wants to merge the branch into `main`. Frank complains that he also uses python notebooks and has to manually choose which files to commit, instead of using `git add .`. The group agrees to exclude `.ipynb` files from the repository.

Make a commit on `rootfind` that

- adds *all* `.ipynb` files to `.gitignore` (including subdirectories)
- removes Carla's `polynomial_zeros.ipynb`

Then, combine this commit with the previous one labelled `"now using newton's method for rootfind"`.
You may name this new commit however you like, but tag it as `part1-squash` (`git tag part1-squash`).

> [!TIP]
> The commands `git merge --squash` and `git checkout [branch/HEAD]~[N]` may be helpful to you.
> For the latter, `[N]` is the number of commits prior to the given branch (or `HEAD` if that was specified). Alternatively, you can use `git checkout [HASH]`.

Finally, `merge` (or rebase) from that commit into `main`, tagging the commit as `part1-merge`. You may want to create a new branch at the combined commit or move `rootfind` to it beforehand. Your goal for this part is to have the repository resemble the following:

```none
If by merge:
┄ ─[A]┬───[C]──┰───[Z]─────┲[G] < main
      └─[B]┬───┺[E]───[F]──┚
           └[D]─ ┄ (gaussquad continues)

If by rebase:
┄ ─[A]┬───[C]──┰───[Z]──────[G] < main
      └─[B]┬───┺[E]───[F]
           └[D]─ ┄ (gaussquad continues)
```

| Commit | Description |
|--------|------------|
| A| message: `"Started report"`|
|B | message: `"added zero finding, moved precision to conftest"`|
|C| message: `"layout / delegation of report"`|
|D| message: `"gauss quadrature + tests to 5-point"`|
|E| message: `"Merge branch 'main' into rootfind"`|
|F| (combined commits) change `legroot.py` and `report.md` for Newton's method, add notebooks to `.gitignore`; should be tagged `part1-squash`. |
|G| merge (or rebase) from `[F]` into `main`. Should be tagged `part1-merge`. |
|Z| commit(s) involving these instructions (pretend they're not there) |

You may keep the two initial commits (before the `squash`) after `[E]` in `rootfind`, or you may delete them.

Both squashed commits involve the `polynomial_zeros.ipynb` file, however, `[F]` does not, which can be verified with `git show`. Explain why this is the case in `responses.txt`. For full credit on this part, you must have

- A commit tagged `part1-squash` with changes to `gauss/legroot.py`, `.gitignore`, and `report.md`. You will need to push the tag to `GitHub`, or set the tag there. Tags can be pushed in the same way as branches: `git push <remote> part1`. Alternatively, you can create an annotated tag `git tag -a <tagname>` and use `git push --follow-tags` to push all annotated and reachable tags at once.
- An explanation in `responses.txt` for why `polynomial_zeros.ipynb` does not appear in the above commit.
- A commit `[G]` as in the table, labeled `part1-merge`, incorporating the changes to `main` (make sure `part1-merge` is also pushed to GitHub).

## Part 2 - Duplicate Work

`checkout` the `rational-legendre` branch. Iris had realized that the Legendre polynomials could be written with exact arithmetic, using rational numbers in the [`fractions`](https://docs.python.org/3/library/fractions.html) module.
Frank added a new test to verify the orthogonality, branching from the previous commit before Iris fixed the tests from that change. He also made a fix. They get into a small argument over which fix to employ.

> Both tests are valid, and pass with the current code. You can verify this with `pytest`. Note that the `pyproject.toml` specifies `pytest` under the optional dependency table `[project.optional-dependencies]`. This is an older way of providing optional dependencies -- in class we discussed `[dependency-groups]`. If you are using `uv`, you will need to pass `--extra <name>` rather than `--group <name>`. In `pip`, extras are specified using `pip install <package>[<extra>]` rather than `pip install <package> --group <group>`. In this case, you would use `uv sync --extra dev` or `pip install .[dev]`.

You will need to resolve the conflict (both `merge`, and interpersonal). Merge (or rebase) `orthotest` into `rational-legendre` if your choice requires it. Provide your reasoning for your choice in `responses.txt`. There is no correct answer to which test is better -- either test has valid reasoning. You may decide to write a better test, incorporating both, but that is not required. Tag the end result with label `part2`.

You should have a layout similar to

```none
If by merge:
┄ ─[A]┬ ┄ 
      └─[B]┬─[C]────┲[E]
           └─[D]────┚ ^
              ^     rational-legendre
          orthotest

If by rebase:
┄ ─[A]┬ ┄ 
      └─[B]┬─[C]─────[E]
           └─[D]      ^
              ^     rational-legendre
          orthotest
```

| Commit | Description |
|--------|------------|
| A| message: `"added zero finding, moved precision to conftest"`|
|B| message: `"egendre polynomials to fractions, section in report"`|
|C| message: `"fixed tests"`|
|D| message: `"added orthogonality test, fixed legendre test"`|
|E| merge (or rebase) `[D]` onto `[C]`. If you believe commit `[C]` is best, `[E]` might be omitted, or used only to commit changes `responses.txt`, should you decide to include `responses.txt` in the history. This commit should be tagged `part2`.|

For full credit, you must have:

- A commit tagged `part2` with tests that pass. Remember to make sure `part2` is pushed to GitHub.
- An explanation in `responses.txt` that justifies your choice.

## Part 3 - A More Complicated Merge Conflict

With `orthotest` and `rational-legendre` combined, merge (or rebase) `rational-legendre` into the main branch. The result should have a `report.md` file with sections in the following order:

- Legendre Polynomials
- Finding the Roots of $P_n$
  - Exterior Newton's Method
  - Deflation
- Gaussian Quadrature

You do not need to know the material in the report -- we will only check the section headers, but you should give some effort in keeping to the spirit of a merge (i.e. don't replace the whole report with just the above headers).
Additionally, there should be 2 test files, with all tests passing.

By the end, you should have a layout similar to

```none
If by merge:
┄ ───[F]─────┲[G] < main
             ┃
      ┄ ─[E]─┚
          ^
  rational-legendre
If by rebase:
┄ ───[F]──────[G] < main
             
      ┄ ─[E]
          ^
  rational-legendre
```

| Commit | Description |
|--------|------------|
|E| merge (or rebase) `[D]` onto `[C]` (from part 2)|
|F| commit on `main` from part 1|
|G| merge `[E]` onto `main` (If you rebased, the line from `[E]` to `[G]` will be absent.) This commit should be tagged `part3`. |

Frank remarks that they should have used $\LaTeX$ for the report with the [`import`](https://www.overleaf.com/learn/latex/Management_in_a_large_project#Using_the_import_package) package to combine separate files into one report. "It would be so much easier if everything was in a separate file," he remarks. In `responses.txt`, explain Frank's reasoning.

For full credit, you must have:

- A commit tagged `part3` where:
  - All tests pass
  - `report.md` has the sections laid out in the order specified above.
- An explanation in `responses.txt` justifying Frank's comment.

Remember to make sure `part3` is pushed to GitHub, along with the tags from the prior parts.

## Part 4 - Managing Scope Creep

Frank wishes to push his changes to `main`, but he was working on implementing composite quadratures in between his main contributions on the `gaussquad` branch. Before merging into `main`, Frank mentions that he wants to make some more changes, since he is not happy with just printing out estimates for $\pi$. However, `gauss` and the tests should be good to go.

Iris remarks that the commits can be pretty easily sorted between features:

|Commit message | Gauss quadrature feature | `compute_pi` / composite quadrature |
|----|------------|------------------|
| "gauss quadrature + tests to 5-point" | ✅ | ❌ |
| "type hinting to legroot" | ✅ | ❌ |
| "added example code for computing pi" | ❌ | ✅ |
|"add explicit function integration function"| ✅ | ❌ |
|"change compute_pi example code"| ❌ | ✅ |
|"formatting, add degree of exactness test"| ✅ | ❌ |
|"add composite quadrature"| ❌ | ✅ |
|"rename my tests files so pytest actually sees them"| ✅ | ❌ |

She then asks if it would be possible to merge just the base quadrature code, while keeping `compute_pi` and the composite quadrature code out of `main`.

Demonstrate how to do that by creating a new branch at `"type hinting to legroot"` or earlier, and `cherry-pick`ing or `rebase`ing commits into that new branch, selecting only those with a ✅ in the "Gauss quadrature feature" column. Tag the last commit `part4`. The tests should pass at this commit.

Then, create another branch called `composite` from `part4` with the remaining commits so that Frank may continue working on his code. While you may do it a different way, `rebase --interactive` can be used to handle both steps at the same time (minus the tagging and new branch creation). Additionally, specifying `[branch/HEAD]~[N]` may be helpful.

Merge (or rebase) `part4` into `main`. Note that the tests now fail. Explain why this is the case in `responses.txt`. You do not need to fix the issue, only explain what happened between `part4` and here. `git blame` may be useful to you.

Once you are done, `gaussquad`, `main`, and `composite` should look like

```none
            ┄ ───[I]───────┲[J] < main
┄ ─[A]──[B]──[D]──[F]──[H]┬┚
                          └─[C]──[E]──[G] < composite
           
```

Remember to push `main` and `composite` to your submission repo so that we can grade it.

| Commit | Description |
|--------|------------|
|A| `"gauss quadrature + tests to 5-point"` |
|B| `"type hinting to legroot"` |
|C| `"added example code for computing pi"` |
|D| `"add explicit function integration function"` |
|E| `"change compute_pi example code"` |
|F| `"formatting, add degree of exactness test"` |
|G| `"add composite quadrature"` |
|H| `"rename my tests files so pytest actually sees them"` -- there should be a tag `part4` here. |
|I| commit on `main` from part 3 |
|J| merge `H` into `main` (If you rebased, the line from `[H]` to `[J]` will be absent.) |

For full credit, you must have:

- A commit tagged `part4` where:
  - All tests pass
  - no history of `composite` is present. That is:
    - `compute_pi.py` is not present in the history at any point before this commit.
    - `compute_composite_integral()` is not defined yet in `gauss.py`.
- A `composite` branch with `compute_pi.py` and `compute_composite_integral()` defined in `gauss.py`.
- An explanation in `responses.txt` on why the tests went from passing to failing between `[H]` and `[J]`.

Please do not forget to push the `part4` tag and `composite` branch to your GitHub repository, along with all other tags from prior parts.

# Research Experiment — Minimal Profile

Use Minimal for a focused companion repository where one paper/study has one dominant environment and one canonical run path.

## Goal

A reader should be able to identify the study, prepare the required input, run one meaningful command, and understand where the result appears.

## Default structure

```text
Project / paper identity
One-line description
Paper link

Environment
Data
Run
Expected output / result
Citation
License
```

## Rules

- show one canonical environment setup;
- state the required dataset or input path explicitly;
- provide one primary run command;
- say where output is written;
- include a compact expected result or sanity check when possible;
- keep baseline grids, multi-seed protocol, ablations, and significance tests out of Minimal.

Novel or expensive research does not automatically require Full. Choose profile by reproducibility surface, not prestige or compute cost.

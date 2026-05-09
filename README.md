# Personal Codex Skills

This repository collects the Codex skills I use across machines. It is designed to be cloned into a normal Git workspace and then synced into the local Codex skills directory.

## Skills

| Skill | What it does |
| --- | --- |
| `arxiv2md` | Converts arXiv papers into clean Markdown through the online arxiv2md REST API, then runs a local cleanup pass for common conversion artifacts. |
| `global-stock-value-analysis` | Guides value-investing oriented stock research across US stocks, China A-shares, HK stocks, ADRs, and mixed portfolios. |

## Repository Layout

```text
.
├── arxiv2md/
│   ├── SKILL.md
│   ├── scripts/
│   └── ...
├── global-stock-value-analysis/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
└── scripts/
    └── sync-to-codex.ps1
```

Each skill folder is self-contained and can be copied into a Codex skills directory.

## Agent Conventions

This repository includes an `AGENTS.md` file for Codex/agent behavior. The main convention is:

- Use `uv` for Python installation, virtual environments, dependency resolution, script execution, and package management.

## Install Or Sync On Windows

Clone this repository, then run:

```powershell
.\scripts\sync-to-codex.ps1
```

By default the script syncs these skill folders to:

```text
$env:USERPROFILE\.codex\skills
```

To sync somewhere else:

```powershell
.\scripts\sync-to-codex.ps1 -Destination "D:\path\to\.codex\skills"
```

The sync replaces only the matching skill folders in the destination. Other skills in the destination are left untouched.

## Manual Install

Copy the desired folders into your Codex skills directory:

```text
%USERPROFILE%\.codex\skills\arxiv2md
%USERPROFILE%\.codex\skills\global-stock-value-analysis
```

Restart Codex or reload skills after copying.

## Notes

- `arxiv2md` is intentionally trimmed to the skill instructions, cleanup script, and license. It uses the public arxiv2md.org API rather than vendoring the upstream service project.
- `global-stock-value-analysis` is intentionally lightweight: the main workflow lives in `SKILL.md`, and detailed investing checklists live in `references/`.
- These skills are research and workflow helpers. The stock analysis skill is not personalized financial advice.

## License

Unless a skill folder contains its own license file, the contents are published under the repository license. The `arxiv2md` folder includes its own MIT license.

param(
    [string]$Destination = "$env:USERPROFILE\.codex\skills"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$skills = @(
    "arxiv2md",
    "global-stock-value-analysis"
)

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

foreach ($skill in $skills) {
    $source = Join-Path $repoRoot $skill
    $target = Join-Path $Destination $skill

    if (-not (Test-Path -LiteralPath $source)) {
        throw "Missing skill folder: $source"
    }

    if (Test-Path -LiteralPath $target) {
        Remove-Item -LiteralPath $target -Recurse -Force
    }

    Copy-Item -LiteralPath $source -Destination $target -Recurse
    Write-Host "Synced $skill -> $target"
}

Write-Host "Done."

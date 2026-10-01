# Regenerate agents/skills/bruin-expert/references from the upstream Bruin docs and templates.
#
# Needs: git, python (3.x). Does a shallow, sparse clone of docs/ and templates/ only.
# To use an existing local clone instead of fetching: $env:BRUIN_SRC = "C:\path\to\bruin"; .\tools\sync.ps1
$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Out  = Join-Path $Root "agents/skills/bruin-expert/references"
$Src  = $env:BRUIN_SRC

$Py = "python3"
if (-not (Get-Command $Py -ErrorAction SilentlyContinue)) { $Py = "python" }

$Tmp = $null
try {
    if (-not $Src) {
        $Tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("bruin-src-" + [guid]::NewGuid().ToString("N"))
        New-Item -ItemType Directory -Path $Tmp | Out-Null
        $Src = Join-Path $Tmp "bruin"
        git clone --depth 1 --filter=blob:none --sparse https://github.com/bruin-data/bruin.git $Src
        if ($LASTEXITCODE -ne 0) { throw "git clone failed" }
        git -C $Src sparse-checkout set docs templates
        if ($LASTEXITCODE -ne 0) { throw "git sparse-checkout failed" }
    }

    & $Py (Join-Path $Root "tools/build_references.py") --src $Src --out $Out
    if ($LASTEXITCODE -ne 0) { throw "build_references.py failed" }
    Write-Host "Done. See $Out/SOURCE.md for the upstream commit."
}
finally {
    if ($Tmp -and (Test-Path $Tmp)) { Remove-Item -Recurse -Force $Tmp }
}

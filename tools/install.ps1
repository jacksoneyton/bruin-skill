# Install this repo's skills into a project's .agents folder.
#
# Usage: .\tools\install.ps1 -Project <project-path>
#
# Safe to run whether or not <project-path>\.agents already exists. Existing files with the
# same path are overwritten by the copies in this repo, other files are left alone.
param(
    [Parameter(Mandatory = $true)]
    [string]$Project
)
$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
if (-not (Test-Path -LiteralPath $Project -PathType Container)) {
    throw "Project path '$Project' is not a directory"
}

$Dest = Join-Path (Resolve-Path $Project) ".agents"
New-Item -ItemType Directory -Force -Path $Dest | Out-Null
# Copy the contents of agents\ into .agents\ so agents\ is not nested inside it.
Copy-Item -Path (Join-Path $Root "agents\*") -Destination $Dest -Recurse -Force

Write-Host "Installed into $Dest"
Get-ChildItem (Join-Path $Dest "skills") | Select-Object -ExpandProperty Name

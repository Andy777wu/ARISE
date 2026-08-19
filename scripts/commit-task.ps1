param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^T-\d+(?:-TEST)?$')]
    [string]$Task,

    [Parameter(Mandatory = $true)]
    [string[]]$Paths,

    [string]$Message = ""
)

$ErrorActionPreference = 'Stop'

if (-not (git remote get-url origin)) {
    throw 'The origin remote is required to submit a task to GitHub.'
}

foreach ($path in $Paths) {
    if (-not (Test-Path -LiteralPath $path)) {
        throw "Task path does not exist: $path"
    }
}

git add -- $Paths
if (git diff --cached --quiet) {
    throw 'No staged changes were found for this task.'
}

if ([string]::IsNullOrWhiteSpace($Message)) {
    $Message = "feat($Task): complete task"
}

git commit -m $Message
git push origin HEAD:main

git add *
git commit -m "$(get-date)& Updated"
git fetch
$result = git merge
if ($result -like "Already up to date.") {
    Write-Output "Nothing to send"
}
git push
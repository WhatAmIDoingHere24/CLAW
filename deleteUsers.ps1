#$splat = @{
#    [string]$Users =@()
#}
Param   (
    $Users
)

#$Users = @splat
$message = "Done"
$userList = @()
for($counter= 0; $counter -lt $Users.Length; $counter++)
{

    If($Users[$counter] -eq ".")
    {
        $counter++
        $userList += $nextUser
        $nextUser = ''
    }
    $nextUser += $Users[$counter]
}


for ($counter= 0; $counter -lt $userList.Length; $counter++)
{
    $rmvUser = $userList[$counter]
    Remove-LocalUser -Name $rmvUser
    Write-Host $userList[$counter]
}
    
Write-Host "$message"
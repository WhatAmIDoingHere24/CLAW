Param   (
    $Users
)

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
}
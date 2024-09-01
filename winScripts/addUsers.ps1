Param   (
    $Users
)

$userList = @()
$password = ConvertTo-SecureString "ARea11yStr0ngpAssW0rd!?" -AsPlainText -Force
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
    $addUser = $userList[$counter]
    New-LocalUser -Name $addUser -Password $password
    Add-LocalGroupMember -Group "Users" -Member $addUser
}
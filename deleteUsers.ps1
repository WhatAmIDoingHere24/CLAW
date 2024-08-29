$splat = @{
    [string]$Users =@()
}

$message = "Done"
$length = $Users.Length
Write-Host "$length"
for ($counter= 0; $counter -lt $Users.Length; $counter++)
{
    #Remove-LocalUser -Name "$users[$counter]"
    Write-Host "$Users"
}
    
Write-Host "$message"
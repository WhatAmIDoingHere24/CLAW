Param   (
    $Path
)
if( -not (Test-Path -Path "$Path") )
{
    New-Item -Path "$Path"
}
Get-LocalUser | Out-File -FilePath "$Path"
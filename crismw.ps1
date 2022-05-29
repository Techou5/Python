
$password = ConvertTo-SecureString -String "PASSWORD" -AsPlainText -Force
$cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "Administrator", $password
$username = Read-Host "Enter username"
$userpassword= Read-Host "Enter user password" -assecurestring
$userfullname= Read-Host "Enter User full name"
#$cred = new-object -typename System.Management.Automation.PSCredential -argumentlist $username, $password

Invoke-Command -ComputerName COMPUTERNAME -Credential $cred -ScriptBlock{
                                                                        & { 
                                                                            New-LocalUser $using:username -Password $using:userpassword -FullName $using:userfullname
                                                                            Add-LocalGroupMember -Group "Users" -Member $using:username
                                                                            Add-LocalGroupMember -Group "Remote Desktop Users" -Member $using:username
                                                                          }
                                                                        }
Write-Output $username
Write-Output $userpassword

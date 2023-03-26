# Prompt user for input
$hostname = Read-Host 'Input Device Hostname:'
$domainlookup = Read-Host 'Do you want to enable DNS? If no, type #. If yes, hit ENTER:'
$dnsserverip = Read-Host 'Enter DNS Server IP address:'
$hostmanualaddingname = Read-Host 'Enter manual host name:'
$hostmanualaddingIP = Read-Host 'Enter manual host IP:'
$PassWord = Read-Host 'Enable Password:'
$secert = Read-Host 'Secret Password:'
$ContimeoutMinutes = Read-Host 'Console Timeout Minutes:'
$contimoutSeconds = Read-Host 'Console Timeout Seconds:'
$Conpassword = Read-Host 'Console Password:'
$Linevty04password = Read-Host 'VTY Password:'
$Aux0password = Read-Host 'Aux Password:'
$passwordEncyption = Read-Host 'Password Encryption? If no, type #. If yes, hit ENTER:'
$Bannertxt = Read-Host 'Enter Text for MOTD Banner:'
$interface = Read-Host 'Enter interface (ex. giga0/0):'
$interfaceip =  Read-Host 'Enter IP address:'
$interfacesubnet = Read-Host 'Enter subnet(255.255.255.0):'
$decriptionyn = Read-Host 'Do you want to describe interface? If no, type #. If yes, hit ENTER:'
$decriptiontext = Read-Host 'Interface description (if yes):'

# Print output with newlines and carriage returns
Write-Output "en `n`r" 
             "config t `n`r" +
             "hostname $hostname `n`r" +
             "$domainlookup `n`r" +
             "ip domain-lookup `n`r" +
             "ip name-server $dnsserverip `n`r" +
             "ip domain-name `n`r" +
             "ip host $hostmanualaddingname $hostmanualaddingIP `n`r" +
             "`n`r" +
             "enable password $PassWord `n`r" +
             "enable secret $secert `n`r" +
             "line con 0 `n`r" +
             "exec-timeout $ContimeoutMinutes $contimoutSeconds `n`r" +
             "login `n`r" +
             "password $Conpassword `n`r" +
             "line vty 0 4 `n`r" +
             "login `n`r" +
             "password $Linevty04password `n`r" +
             "line aux 0 `n`r" +
             "login `n`r" +
             "password $Aux0password `n`r" +
             "ex `n`r" +
             "$passwordEncyption service password-encryption `n`r" +
             "banner motd & `n`r" +
             "$Bannertxt `n`r" +
             "`n`r" +
             "interface $interface `n`r" +
             "ip address $interfaceip $interfacesubnet `n`r" +
             "no shutdown `n`r" +
             "$decriptionyn description $decriptiontext `n`r" +
             "ex `n`r" +
             "ex `n`r" +
             "copy run start"
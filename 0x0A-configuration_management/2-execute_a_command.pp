# kill a process named killmenow

exec {'/usr/bin/pkill -9 killmenow':
 path => '/usr/bin/',
}

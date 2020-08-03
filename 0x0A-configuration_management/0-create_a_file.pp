BBBBB# create a file in /tmp

file { '/tmp/holberton':
  content =>'I love Puppet',
  owner   =>'www-data',
  group   =>'www-data',
  mode    =>'0744',
}

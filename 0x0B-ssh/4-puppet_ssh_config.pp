# changing the ssh config file
exec { 'echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
  provider  => 'shell',
}
exec { 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config':
  provider  => 'shell',
}

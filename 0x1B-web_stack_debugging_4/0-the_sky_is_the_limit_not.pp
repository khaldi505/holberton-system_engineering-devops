# changing the ULIMIT value

exec{'ulimit_fix':
path    => [ '/usr/local/bin/', '/bin/' ],
command => 'sudo sed -i 's/-n 15/-n 2000/g' /etc/default/nginx; sudo service nginx restart',
}


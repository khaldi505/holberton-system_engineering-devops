# changing the ULIMIT value to accept 1000 request

exec {'ulimit_fix':
path    => [ '/usr/bin/', '/bin/' ],
command => "sudo sed -i 's/-n 15/-n 2000/g' /etc/default/nginx; sudo service nginx restart",
}

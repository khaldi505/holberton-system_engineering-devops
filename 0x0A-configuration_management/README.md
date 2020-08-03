# 0x0A-configuration_management

Configuration management is a process for maintaining computer systems,
servers, and software in a desired,
consistent state. Its a way to make sure that 
a system performs as its expectedto as changes are made over time

## working with puppet

puppet is a declarative language that saves you a lot of time later on
managing your servers it costs you a lot of time and energy at
the beginning but it'll save you from making small or
large changes that go undocumented.

## installation

to install [puppet-lint version 2.1.1]("https://puppet.com/") first install ruby.

'''bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
'''

## Genral requirements
A README.md file at the root of the folder of the project is mandatory
Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
Your Puppet manifests must run without error
Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
Your Puppet manifests files must end with the extension .pp


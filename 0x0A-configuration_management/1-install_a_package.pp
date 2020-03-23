# this script will install puppet version on a server
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
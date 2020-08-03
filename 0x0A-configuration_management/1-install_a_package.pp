# installing puppet using puppet \_(ツ)_/

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}

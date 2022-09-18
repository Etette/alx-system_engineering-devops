#!/usr/bin/pup
#installs the package FLASK
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

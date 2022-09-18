#!/usr/bin/pup
#Kills a process 'killmenow'
exec { 'pkill':
  command =>  'pkill killmenow',
  path    =>  '/usr/local/bin/:/bin',
}

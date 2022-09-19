# sets up SSH config file to connect to server without password
include stdlib
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '	identityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Turn off password auth':
  path_line => '/etc/ssh/ssh_config',
  line      => '	PasswordAuthentication no',
  replace   => true,
}

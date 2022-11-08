# change OS configuratioin so that its possible to login
# with the holbeerton user and open file without any error
# message.
exec { 'hard/soft':
  command => 'sed -i "s/5/50/" /etc/security/limits.conf; \
  sed -i "s/4/40/" /etc/security/limits.conf;',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

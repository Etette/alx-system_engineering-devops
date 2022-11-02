# Task 0
exec { 'phpp to php':
  command => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-setting.php",
  path    => '/bin',
}

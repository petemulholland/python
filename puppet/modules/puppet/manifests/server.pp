class puppet::server (
  $version = 'latest',
  $status  = 'running',
  $onboot  = true,
) {
  package { 'puppet-server':
    ensure => $version,
    notify => Service['puppetmaster'],
  }
  service { 'puppetmaster':
    ensure => $status,
    enable => $onboot,
  }
}

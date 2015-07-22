node default {
  class { 'puppet': }
  class { 'mygit': }
  package { 'apt-file': 		ensure => latest,  }
  package { 'ntfs-3g': 			ensure => latest,  }
  package { 'samba': 			ensure => latest,  }
  package { 'samba-common-bin': 	ensure => latest,  }
  package { 'tightvncserver':    	ensure => latest,  }
  class { 'myvim':  }
}

node pi-svr-puppet inherits default {
  class { 'puppet::server':
    version => 'latest',
  }
}

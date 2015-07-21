node default {
  class { 'puppet': }
  package { 'apt-file': 			ensure => latest,  }
  package { 'git': 					ensure => latest,  }
  package { 'ntfs-3g': 				ensure => latest,  }
  package { 'samba': 				ensure => latest,  }
  package { 'samba-common-bin': 	ensure => latest,  }
  package { 'tightvncserver':    	ensure => latest,  }
  package { 'vim':    				ensure => latest,  }
}

node pi-svr-puppet inherits default {
  class { 'puppet::server':
    version => 'latest',
  }
}

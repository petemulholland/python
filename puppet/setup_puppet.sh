#!/bin/sh
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-wheezy.deb
sudo dpkg –I puppetlabs-release-pc1-wheezy.deb
sudo apt-get update 
sudo apt-get puppet

# add to end of /etc/puppet/puppet.conf
#[agent]
#server = petes.puppet-server.net

# run:
# sudo puppet agent --test

# on server:
# sudo puppet cert list
# sudo puppet cert sign <hostname>

# on client rerun:
# sudo puppet agent --test



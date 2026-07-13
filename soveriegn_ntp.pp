# 🛡️ IRON LOGIC: SOVEREIGN NTP BLUEPRINT
# Goal: Manage the NTP service with strict dependency orchestration.

class sovereign_ntp {

  # 1. Ensure the base software is present
  package { 'ntp':
    ensure => installed,
  }

  # 2. Manage the configuration file
  # The 'require' ensures we don't place the config before the package exists.
  # The 'notify' ensures that if this file changes, the service restarts automatically.
  file { '/etc/ntp.conf':
    ensure  => file,
    source  => 'puppet:///modules/sovereign_ntp/ntp.conf',
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    require => Package['ntp'],
    notify  => Service['ntp'],
  }

  # 3. Ensure the service is active
  # The 'require' ensures the service only starts once the config file is placed.
  service { 'ntp':
    ensure  => running,
    enable  => true,
    require => File['/etc/ntp.conf'],
  }
}

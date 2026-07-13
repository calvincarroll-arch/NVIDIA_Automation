# 🛡️ IRON LOGIC PRACTICE BLUEPRINT 
# Goal: Ensure the VRAM Zombie Killer is installed and runs every 15 minutes.

class iron_logic_vram_manager {

  # 1. The 'File' Resource: Make sure the script is actually on the server
  file { '/usr/local/bin/vram_zombie_killer.py':
    ensure => file,                                      # We want a file, not a directory
    source => '/mnt/c/Users/carro/NVIDIA_Automation/production/vram_zombie_killer.py', # Grab it from your local path
    mode   => '0755',                                    # Make it executable (rwxr-xr-x)
    owner  => 'root',                                    # Only root should own security scripts
  }

  # 2. The 'Cron' Resource: Automate the execution (No more manual crontab)
  cron { 'run_vram_zombie_killer':
    command => '/usr/bin/python3 /usr/local/bin/vram_zombie_killer.py',
    user    => 'root',
    minute  => '*/15',                                   # Run every 15 minutes
    require => File['/usr/local/bin/vram_zombie_killer.py'], # DON'T run until the file is placed!
  }

}

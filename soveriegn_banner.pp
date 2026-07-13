# 🛡️ IRON LOGIC PRACTICE BLUEPRINT 
# Goal: Enforce dynamic, idempotent security banners based on hardware type.

class iron_logic_security_banner {

  # 1. The Conditional Logic (The Brain)
  # Puppet asks the node: "Are you a hologram?"
  if $facts['is_virtual'] {
    $banner_text = "WARNING: Iron Logic Virtualized Edge Node. All activity is monitored.\n"
  } else {
    $banner_text = "WARNING: Iron Logic Sovereign Bare-Metal Vault. Air-gapped environment.\n"
  }

  # 2. The Idempotent Resource (The Muscle)
  # Puppet enforces the state without running messy bash scripts.
  file { '/etc/issue':
    ensure  => file,
    content => $banner_text,
    mode    => '0644',
    owner   => 'root',
  }

}

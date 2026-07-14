terraform {
  required_providers {
    libvirt = {
      source  = "dmacvicar/libvirt"
      version = "0.7.6"
    }
  }
}

provider "libvirt" {
  uri = "qemu:///system"
}

resource "libvirt_pool" "iron_logic_pool" {
  name = "iron_logic_pool"
  type = "dir"
  path = "/var/lib/libvirt/images"
}

resource "libvirt_volume" "ubuntu_base" {
  name   = "ubuntu-jammy-base.qcow2"
  pool   = libvirt_pool.iron_logic_pool.name
  source = "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img"
  format = "qcow2"
}

# --- NEW: Cloud-Init Disk to inject the SSH key ---
resource "libvirt_cloudinit_disk" "commoninit" {
  name      = "commoninit.iso"
  pool      = libvirt_pool.iron_logic_pool.name
  user_data = <<EOF
#cloud-config
users:
  - name: ironadmin
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: users, admin
    home: /home/ironadmin
    shell: /bin/bash
    ssh_authorized_keys:
      - ${file("~/.ssh/id_rsa.pub")}
ssh_pwauth: false
disable_root: true
EOF
}

resource "libvirt_domain" "sovereign_node_01" {
  name   = "sovereign-node-01"
  memory = "2048"
  vcpu   = 2

  # --- NEW: Attach the Cloud-Init disk ---
  cloudinit = libvirt_cloudinit_disk.commoninit.id

  network_interface {
    network_name   = "default"
    # --- NEW: Tell Terraform to wait for the DHCP lease to grab the IP ---
    wait_for_lease = true
  }

  disk {
    volume_id = libvirt_volume.ubuntu_base.id
  }

  console {
    type        = "pty"
    target_port = "0"
    target_type = "serial"
  }
}

# --- NEW: Output the IP Address to the terminal ---
output "node_ip" {
  value = libvirt_domain.sovereign_node_01.network_interface[0].addresses[0]
}
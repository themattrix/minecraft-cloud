# "docker-machine" options
export PACKET_FACILITY_CODE=ewr1    # Parsippany, NJ
export PACKET_PLAN=baremetal_0      # 4 cores @ 2.4GHz (Atom C2550), 8GB DDR3 RAM, 80GB SSD, 1Gbps network
export PACKET_BILLING_CYCLE=hourly  # or "monthly"
export PACKET_OS=rancher            # default is "ubuntu_14_04"

# "cloud" options
export SWAP_SIZE=0               # don't enable swap since we have lots of RAM
export RAMDISK_SIZE=4g           # allow the minecraft world to be up to 4 GB

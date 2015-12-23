# Minecraft Cloud

Create a publically available Minecraft server for $0.03/hour (or less)!

Your world data is uploaded after the server is created, and downloaded
before the server is destroyed. It is incrementally archived with
[bup](https://github.com/bup/bup) after being downloaded so that you can always
access old versions of your world.

> Slow upload speed? Your world data can also be loaded from and saved to [Dropbox](#dropbox)!

Requirements:

- [docker](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [docker-machine](https://docs.docker.com/machine/install-machine/)
- [Vultr driver for machine](https://github.com/janeczku/docker-machine-vultr) (only if using [Vultr](https://www.vultr.com/))
- [OVH driver for machine](https://github.com/yadutaf/docker-machine-driver-ovh) (only if using [OVH](https://www.ovh.com/us/vps/vps-ssd.xml))
- [bup](https://github.com/bup/bup)

Get the code:

```bash
git clone git@github.com:themattrix/minecraft-cloud.git
cd minecraft-cloud
git submodule update --init
```

Configure your cloud provider with `<driver>.spec` and `<driver>.auth`.
Default spec files are provided for Digital Ocean, Vultr, and OVH, as well as
an example auth file for each.


## Usage Examples

```bash
# spin up a VM for $0.03/hour on DigitalOcean...
./cloud up digitalocean

# ...or spin up a slightly faster VM for $0.03/hour on Vultr...
./cloud up vultr

# ...or spin up a slightly slower but larger memory VM for $0.036/hour on OVH
./cloud up ovh

# monitor the logs from all running services
./cloud compose logs

# open the mark2 admin console
./cloud admin

# re-render the Google Maps-style world view (this is automatically run once)
./cloud map

# destroy the VM but save your world data locally (mincraft-fig/volumes/game/world*)...
./cloud rm

# ...or destroy the VM without saving your world data
./cloud rm --no-preserve
```

Updating to the latest version of this project:

```bash
git pull
git submodule update
```


## Dropbox

When the following config file is present, your world data will be loaded from
Dropbox after the server is created and saved to Dropbox before the server is
destoryed:

    minecraft-fig/volumes/dropbox/.dropbox_uploader

Your world data will *also* be downloaded locally for archival with bup.

See the [minecraft-fig README](https://github.com/themattrix/minecraft-fig/blob/master/README.md)
for details about setting up the config file.

# Minecraft Cloud

Create a publically available Minecraft server for $0.03/hour (or less)!

Your local world data is uploaded after the server is created, and downloaded
before the server is destroyed. It is archived with [bup](https://github.com/bup/bup)
after being downloaded so that you can always access old versions of your world.

Requirements:

- [docker](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [docker-machine](https://docs.docker.com/machine/install-machine/)
- [Vultr driver for machine](https://github.com/janeczku/docker-machine-vultr) (only if using [Vultr](https://www.vultr.com/))
- [bup](https://github.com/bup/bup)

Get the code:

```bash
git clone git@github.com:themattrix/minecraft-cloud.git
cd minecraft-cloud
git submodule update --init
```

Configure your cloud provider with `<driver>.spec` and `<driver>.auth`.
Default spec files are provided for Digital Ocean and Vultr, as well as
an example auth file for each.


## Usage Examples

```bash
# spin up a VM for $0.03/hour on DigitalOcean...
./cloud up digitalocean

# ...or spin up a slightly faster VM for $0.03/hour on Vultr
./cloud up vultr

# monitor the logs from all running services
./cloud logs

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

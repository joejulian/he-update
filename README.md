# HE Update

This utility updates the dynamic gateway address for IPv6 tunnel and the 
dyndns address if the address changes using Hurricane Electric's free 
service.

## Installation

```
pip install he-update
```

To manually install from the github source:

```
git clone https://github.com/joejulian/he-update.git

he-update/setup.py install
```

## Configuration

### Hurricane Electric

At https://dns.he.net edit the A record for the host you want to be 
able to update dynamically and check the box for 
```Enable entry for dynamic dns```.

At https://tunnelbroker.net get your ```Tunnel ID``` from your tunnel details. (12345 in the example)

Select the ```Advanced``` tab and configure ```HE Dynamic DNS Settings```. 
* Set the hostname to the fqdn of the A record you enabled above. (myhost.domain.dom in the example)
* Set the username to your username when logging in to tunnelbroker.net. (myuser in the example)
* Set the API key to an unguessable string. (mysupersecretpassword in the example)

### Create config file

```
cat > /etc/he-update/he-update.yaml
    12345:
        hostname: myhost.domain.dom
        username: myuser
        password: mysupersecretpassword
```

## Usage

```
$ he-update
myhost.domain.dom: nochg 192.168.0.1
```

# FANET-SDN-Mininet-WiFi

## Implementation of a FANET over SDN in Mininet-WiFi environment

In this case, on the advice of the developers of the emulation environment, we proceeded to download the .ova file from the following url:

https://drive.google.com/file/d/1R8n4thPwV2krFa6WNP0Eh05ZHZEdhw4W/view?usp=sharing

After this procedure, only the Ryu controller was installed in the system

```
#!/bin/sh
echo " Installazione Ryu"
sudo apt install python3-pip
git clone https://github.com/faucetsdn/ryu.git
sudo apt install gcc python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev zlib1g-dev
cd ryu
pip3 install -r tools/optional-requires
sudo pip3 install .
```

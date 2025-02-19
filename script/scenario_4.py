#!/usr/bin/python
"""
Scenario 4.
"""
from containernet.net import Containernet
from containernet.nodeimport DockerSta
from mn_wifi.linkimport wmediumd, adhoc
from containernet.cli import CLI
from containernet.termimport makeTerm
from mininet.log import info, setLogLevel
from mn_wifi.wmediumdConnectorimport interference


def topology():

    net = Containernet(link=wmediumd, wmediumd_mode=interference)

info('*** Adding docker containers\n')
sta1 = net.addStation('sta1', ip='11.0.0.11', mac='00:02:00:00:00:11',
cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='25,85,0')
    uav1 = net.addStation('uav1', ip='11.0.0.1', mac='00:01:00:00:00:01',
                          cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='50,100,0')
    uav2 = net.addStation('uav2', ip='11.0.0.2', mac='00:01:00:00:00:02',
                          cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='75,125,0')
    uav3 = net.addStation('uav3', ip='11.0.0.3', mac='00:01:00:00:00:03',
                          cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='100,140,0')
    uav4 = net.addStation('uav4', ip='11.0.0.4', mac='00:01:00:00:00:04',
                          cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='135,125,0')
uav5 = net.addStation('uav5', ip='11.0.0.5', mac='00:01:00:00:00:05',
                          cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='135,90,0')
    uav6 = net.addStation('uav6', ip='11.0.0.6', mac='00:01:00:00:00:06',
                          cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='100,75,0')
    uav7 = net.addStation('uav7', ip='11.0.0.7', mac='00:01:00:00:00:07',
                          cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='63,75,0')    
sta2 = net.addStation('sta2', ip='11.0.0.12', mac='00:02:00:00:00:12',
cls=DockerSta, dimage="openvswitch/ovs:2.11.2_debian", cpu_shares=20, position='165,120,0')

net.setPropagationModel(model="logDistance", exp=4.5)

info('*** Configuring WiFi nodes\n')

net.configureWifiNodes()

net.plotGraph(max_x=200, max_y=200)

info('*** Starting network\n')
net.start()

makeTerm(sta1, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br sta1 && ovs-vsctl set bridge sta1 protocols=OpenFlow13 && ovs-vsctl add-port sta1 vlan1 -- set interface vlan1 type=internal && ip addr add 10.0.0.11/8 dev vlan1 && ip link set vlan1 up && ip link set sta1 up && ovs-vsctl add-port sta1 vx1 -- set interface vx1 type=vxlan options:remote_ip=11.0.0.1 && ip link set dev vlan1 mtu 1400 && ovs-vsctl set bridge sta1 other_config:hwaddr=00:00:00:00:00:11;'")

    makeTerm(sta2, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br sta2 && ovs-vsctl set bridge sta2 protocols=OpenFlow13 && ovs-vsctl add-port sta2 vlan1 -- set interface vlan1 type=internal && ip addr add 10.0.0.12/8 dev vlan1 && ip link set vlan1 up && ip link set sta2 up && ovs-vsctl add-port sta2 vx5 -- set interface vx5 type=vxlan options:remote_ip=11.0.0.4 && ip link set dev vlan1 mtu 1400 && ovs-vsctl set bridge sta2 other_config:hwaddr=00:00:00:00:00:12;'")

    makeTerm(uav1, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br uav1 && ovs-vsctl set bridge uav1 protocols=OpenFlow13 && ovs-vsctl set-controller uav1 tcp:172.17.0.1:6653 && ovs-vsctl set-fail-mode uav1 secure && ip link set uav1 up && ovs-vsctl add-port uav1 vx1 -- set interface vx1 type=vxlan options:remote_ip=11.0.0.11 && ovs-vsctl add-port uav1 vx2 -- set interface vx2 type=vxlan options:remote_ip=11.0.0.2 && ovs-vsctl add-port uav1 vx9 -- set interface vx9 type=vxlan options:remote_ip=11.0.0.7 && ovs-vsctl set bridge uav1 other_config:hwaddr=00:00:00:00:00:01;'")

    makeTerm(uav2, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br uav2 && ovs-vsctl set bridge uav2 protocols=OpenFlow13 && ovs-vsctl set-controller uav2 tcp:172.17.0.1:6653 && ovs-vsctl set-fail-mode uav2 secure && ip link set uav2 up && ovs-vsctl add-port uav2 vx2 -- set interface vx2 type=vxlan options:remote_ip=11.0.0.1 && ovs-vsctl add-port uav2 vx3 -- set interface vx3 type=vxlan options:remote_ip=11.0.0.3 && ovs-vsctl set bridge uav2 other_config:hwaddr=00:00:00:00:00:02;'")

    makeTerm(uav3, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br uav3 && ovs-vsctl set bridge uav3 protocols=OpenFlow13 && ovs-vsctl set-controller uav3 tcp:172.17.0.1:6653 && ovs-vsctl set-fail-mode uav3 secure && ip link set uav3 up && ovs-vsctl add-port uav3 vx3 -- set interface vx3 type=vxlan options:remote_ip=11.0.0.2 && ovs-vsctl add-port uav3 vx4 -- set interface vx4 type=vxlan options:remote_ip=11.0.0.4 && ovs-vsctl set bridge uav3 other_config:hwaddr=00:00:00:00:00:03;'")

    makeTerm(uav4, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br uav4 && ovs-vsctl set bridge uav4 protocols=OpenFlow13 && ovs-vsctl set-controller uav4 tcp:172.17.0.1:6653 && ovs-vsctl set-fail-mode uav4 secure && ip link set uav4 up && ovs-vsctl add-port uav4 vx4 -- set interface vx4 type=vxlan options:remote_ip=11.0.0.3 && ovs-vsctl add-port uav4 vx5 -- set interface vx5 type=vxlan options:remote_ip=11.0.0.12 && ovs-vsctl add-port uav4 vx6 -- set interface vx6 type=vxlan options:remote_ip=11.0.0.5 && ovs-vsctl set bridge uav4 other_config:hwaddr=00:00:00:00:00:04;'")

    makeTerm(uav5, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br uav5 && ovs-vsctl set bridge uav5 protocols=OpenFlow13 && ovs-vsctl set-controller uav5 tcp:172.17.0.1:6653 && ovs-vsctl set-fail-mode uav5 secure && ip link set uav5 up && ovs-vsctl add-port uav5 vx6 -- set interface vx6 type=vxlan options:remote_ip=11.0.0.4 && ovs-vsctl add-port uav5 vx7 -- set interface vx7 type=vxlan options:remote_ip=11.0.0.6 && ovs-vsctl set bridge uav5 other_config:hwaddr=00:00:00:00:00:05;'")

    makeTerm(uav6, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br uav6 && ovs-vsctl set bridge uav6 protocols=OpenFlow13 && ovs-vsctl set-controller uav6 tcp:172.17.0.1:6653 && ovs-vsctl set-fail-mode uav6 secure && ip link set uav6 up && ovs-vsctl add-port uav6 vx7 -- set interface vx7 type=vxlan options:remote_ip=11.0.0.5 && ovs-vsctl add-port uav6 vx8 -- set interface vx8 type=vxlan options:remote_ip=11.0.0.7 && ovs-vsctl set bridge uav6 other_config:hwaddr=00:00:00:00:00:06;'")

    makeTerm(uav7, cmd="bash -c 'apt-get update && apt-get install iw -y && apt-get install iperf -y && /usr/share/openvswitch/scripts/ovs-ctl start && apt-get install iputils-ping -y && ovs-vsctl add-br uav7 && ovs-vsctl set bridge uav7 protocols=OpenFlow13 && ovs-vsctl set-controller uav7 tcp:172.17.0.1:6653 && ovs-vsctl set-fail-mode uav7 secure && ip link set uav7 up && ovs-vsctl add-port uav7 vx8 -- set interface vx8 type=vxlan options:remote_ip=11.0.0.6 && ovs-vsctl add-port uav7 vx9 -- set interface vx9 type=vxlan options:remote_ip=11.0.0.1 && ovs-vsctl set bridge uav7 other_config:hwaddr=00:00:00:00:00:07;'")

info("\n*** Colours...\n")

    sta1.set_circle_color("r")
    sta2.set_circle_color("r")

info('*** Running CLI\n')
CLI(net)

info('*** Stopping network\n')
net.stop()


if __name__ == '__main__':
    setLogLevel('info')
topology()

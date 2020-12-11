# Kubernetes-node-monitor

##To run
* Install python3 in your environment
* copy this repo over, adjust paths in sshalert.service
* copy monitor.service to /etc/systemd/system/ into whichever target directory you want (probably multi-user)
* systemctl daemon-reload
* systemctl start sshalert
* systemctl enable sshalert

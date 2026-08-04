FROM netboxcommunity/netbox:v4.6.7
USER root
RUN /opt/netbox/venv/bin/pip install netbox-topology-views
USER unit

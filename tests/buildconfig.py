#!/usr/bin/python3
from configparser import ConfigParser, NoOptionError

testconfig = ConfigParser()
testconfig.read('/root/tests/test.conf') # config deployed by docker/podman

himmelblau_config = ConfigParser()
himmelblau_config.add_section('global')
for setting in ['tenant_id', 'app_id']:
    try:
        himmelblau_config.set('global', setting, testconfig.get('global', setting))
    except NoOptionError:
        pass # Ignore when unset, and leave default

with open('/etc/himmelblau/himmelblau.conf', 'w') as w:
    himmelblau_config.write(w)

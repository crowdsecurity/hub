#!/usr/bin/env sh

set -e

# Setup the test environment.
cd /workspaces/crowdsec/
./test_env.sh
cd tests/

# Update config to point to correct paths for this devcontainer.
yq -iy '.config_paths.hub_dir = "/workspaces/hub/"' dev.yaml
yq -iy '.config_paths.index_path = "/workspaces/hub/.index"' dev.yaml

# As documented in https://github.com/crowdsecurity/crowdsec/issues/3183,
# running ./test_env.sh sets a bunch of relative paths with simply do not work
# as we need them to in a devcontainer.  The following lines set absolute paths
# that do work.
yq -iy '.api.client.credentials_path = "/workspaces/crowdsec/tests/config/local_api_credentials.yaml"' dev.yaml
yq -iy '.api.server.console_path = "/workspaces/crowdsec/tests/config/console.yaml"' dev.yaml
yq -iy '.api.server.online_client.credentials_path = "/workspaces/crowdsec/tests/config/online_api_credentials.yaml"' dev.yaml
yq -iy '.api.server.profiles_path = "/workspaces/crowdsec/tests/config/profiles.yaml"' dev.yaml
yq -iy '.config_paths.config_dir = "/workspaces/crowdsec/tests/config/"' dev.yaml
yq -iy '.config_paths.data_dir = "/workspaces/crowdsec/tests/data/"' dev.yaml
yq -iy '.config_paths.notification_dir = "/workspaces/crowdsec/tests/notifications/"' dev.yaml
yq -iy '.config_paths.plugin_dir = "/workspaces/crowdsec/tests/plugins/"' dev.yaml
yq -iy '.crowdsec_service.acquisition_path = "/workspaces/crowdsec/tests/config/acquis.yaml"' dev.yaml
yq -iy '.db_config.db_path = "/workspaces/crowdsec/tests/data/crowdsec.db"' dev.yaml

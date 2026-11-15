#!/usr/bin/env sh

set -e

# Setup the test environment.
cd /home/vscode/crowdsec/
./test_env.sh
cd tests/

# Update config to point to correct paths for this devcontainer.
yq -iy '.config_paths.hub_dir = "/workspaces/hub/"' dev.yaml
yq -iy '.config_paths.index_path = "/workspaces/hub/.index.json"' dev.yaml

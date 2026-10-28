# The `builder` fetches the latest crowdsec release and untars it so it can be
# used by the actual devcontainer.
FROM alpine:latest AS builder
WORKDIR /app
RUN wget -q https://github.com/crowdsecurity/crowdsec/releases/latest/download/crowdsec-release.tgz \
    && tar xvzf crowdsec-release.tgz \
    && mv $(find -name 'crowdsec-v*') /crowdsec

#
# The actual devcontainer.
#
FROM mcr.microsoft.com/devcontainers/base:debian

# Install Required Dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    yq \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install crowdsec
COPY --from=builder --chown=vscode:vscode /crowdsec /home/vscode/crowdsec

# Put crowdsec and cscli on the PATH.  Both are created by `test_env.sh` in
# postCreate.sh, and the default config path points at the config it generates,
# so neither command needs extra flags.
RUN ln -s /home/vscode/crowdsec/tests/crowdsec /usr/local/bin/crowdsec \
  && ln -s /home/vscode/crowdsec/tests/cscli /usr/local/bin/cscli \
  && mkdir -p /etc/crowdsec \
  && ln -s /home/vscode/crowdsec/tests/dev.yaml /etc/crowdsec/config.yaml

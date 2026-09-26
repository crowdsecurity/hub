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
COPY --from=builder /crowdsec /workspaces/crowdsec
RUN chown 1000:1000 -R /workspaces/crowdsec

# Install wrapper scripts.
COPY bin/crowdsec /usr/local/bin/crowdsec
COPY bin/cscli /usr/local/bin/cscli

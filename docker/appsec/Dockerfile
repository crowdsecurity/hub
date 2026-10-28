FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    make \
    software-properties-common \
    wget \
    gnupg \
    ca-certificates \
    gettext

RUN wget -O - https://openresty.org/package/pubkey.gpg | gpg --dearmor -o /usr/share/keyrings/openresty.gpg
ARG TARGETARCH
RUN if [ "$TARGETARCH" = "amd64" ]; then \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/openresty.gpg] http://openresty.org/package/ubuntu $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/openresty.list; \
    elif [ "$TARGETARCH" = "arm64" ]; then \
    echo "deb [arch=arm64 signed-by=/usr/share/keyrings/openresty.gpg] http://openresty.org/package/arm64/ubuntu $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/openresty.list; \
    fi
RUN apt-get update

RUN apt-get install -y openresty

# Install the bouncer
COPY build.sh /build.sh
COPY start.sh /start.sh

RUN chmod +x /build.sh && /build.sh
RUN chmod +x /start.sh

# Set the script as the entrypoint
ENTRYPOINT ["/start.sh"]
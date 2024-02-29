FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    make \
    software-properties-common \
    wget \
    gnupg \
    ca-certificates \
    gettext

RUN wget -O - https://openresty.org/package/pubkey.gpg | apt-key add -
RUN echo "deb http://openresty.org/package/ubuntu $(lsb_release -sc) main"| tee /etc/apt/sources.list.d/openresty.list

RUN apt-get update

RUN apt-get install -y openresty

# Install the bouncer
COPY build.sh /build.sh
COPY start.sh /start.sh

RUN chmod +x /build.sh && /build.sh
RUN chmod +x /start.sh

# Set the script as the entrypoint
ENTRYPOINT ["/start.sh"]
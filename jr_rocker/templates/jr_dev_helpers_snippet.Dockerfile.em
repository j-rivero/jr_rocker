# Development-related required and optional utils
RUN export DEBIAN_FRONTEND=noninteractive; \
    apt-get update \
    # Required packages
    && apt-get install -y \
        build-essential \
        clang \
        cmake \
        gdb \
        git \
        quilt \
        less \
        tree \
        ubuntu-dev-tools \
        vim \
        wget \
        xclip \
    # Clean
    && apt-get clean

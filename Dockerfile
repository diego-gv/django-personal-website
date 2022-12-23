FROM python:3.9
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
RUN mkdir /local
ADD . /local
RUN pip install --upgrade pip && \
    pip install -r /local/requirements.txt

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && chsh -s /bin/bash $USERNAME

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

EXPOSE 8888
CMD bash -c "gunicorn portfolio.wsgi --workers 3 --threads 100 --max-requests 1000 --max-requests-jitter 15 -b 0.0.0.0:8888"
WORKDIR /local

FROM node:10

# Create app directory
RUN mkdir -p /home/Service
WORKDIR /usr/src/app

# Bundle app source
COPY package*.json ./
RUN npm install
COPY . .

# Install MATLAB MCR
ENV MATLAB_VERSION R2018b
RUN mkdir /opt/mcr_install && \
    mkdir /opt/mcr && \
    wget --quiet -P /opt/mcr_install http://www.mathworks.com/supportfiles/downloads/${MATLAB_VERSION}/deployment_files/${MATLAB_VERSION}/installers/glnxa64/MCR_${MATLAB_VERSION}_glnxa64_installer.zip && \
    unzip -q /opt/mcr_install/MCR_${MATLAB_VERSION}_glnxa64_installer.zip -d /opt/mcr_install && \
    /opt/mcr_install/install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \
    rm -rf /opt/mcr_install /tmp/*

# Configure environment
ENV MCR_VERSION v95
# ENV LD_LIBRARY_PATH /usr/lib/fsl/5.0:/opt/mcr/${MCR_VERSION}/runtime/glnxa64:/opt/mcr/${MCR_VERSION}/bin/glnxa64:/opt/mcr/${MCR_VERSION}/sys/os/glnxa64:/opt/mcr/${MCR_VERSION}/sys/opengl/lib/glnxa64::${LD_LIBRARY_PATH}
ENV MCR_INHIBIT_CTF_LOCK 1
ENV MCRPath /opt/mcr/${MCR_VERSION}
RUN chmod +x run_y_Segment.sh
RUN chmod +x y_Segment
RUN chmod +x y_Segment.ctf

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 150
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install tensorflow
RUN pip install keras
RUN pip install nibabel
RUN pip install matplotlib

RUN apt-get -qq update && apt-get -qq install -y \
    x11vnc xvfb suckless-tools stterm connectome-workbench parallel wget unzip && \
    apt-get update

EXPOSE 8888
CMD [ "node", "index.js" ]


Install Bridge Client
=====================

Follow these steps to install the Phantom Bridge Client to your ROS2 machine. 
The Bridge Client is provided as a Docker container, ROS2 Humble to Rolling are supported.


.. rubric:: Prequisities

Make sure your Root SSL Certificates are up to date:

.. code-block:: bash

    sudo apt update
    sudo apt install ca-certificates curl

Install Docker, Docker Build & Docker Compose, e.g. on Debian/Ubuntu follow `these instructions <https://docs.docker.com/engine/install/debian>`_.
Then add the current user to the docker group:

.. code-block:: bash

    sudo usermod -aG docker ${USER}
    # reload session


.. rubric:: Register New Robot On The Bridge Server

This registers a new robot on the Bridge Server and returns a default config file you can edit further.
Unique ``ID_ROBOT`` and ``KEY`` pair are generated in this step.

.. code-block:: bash

    bash <(curl -s https://register.phntm.io/register.sh)

Follow the Registration Utility's instructions, a YAML configuration file will be generated and saved under the specified name, ``phntm_bridge.yaml`` is used by default (and in this documentation).
Note that the `register.phntm.io` service is geographically distributed and will return configuration with ``bridge_server_address`` set to the Bridge Server instance nearest to you.
You can always switch to a different Bridge Server, see our :doc:`Availability Zones <availability-zones>` for current options.


.. rubric:: Examine The Config File

Below is an example of the config file generated in the previous step, e.g. ``phntm_bridge.yaml``. \
Full list of configuration options can be found :doc:`here <configuration>`.

.. code-block:: yaml
    :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        id_robot: '%ID_ROBOT%'
        key: '%SECRET_KEY%'
        name: 'My Little Robot'
        maintainer_email: 'robot.master@example.com' # e-mail for service announcements

        bridge_server_address: https://us-ca.bridge.phntm.io

        ## Custom topic configs
        /battery:
          min_voltage: 19.2 # set empty voltage
          max_voltage: 25.2 # set set full voltage

        ui_battery_topic: /battery # battery to show in the UI, '' to disable

        net_interface: 'wlan0' # for cellular use the control iface (e.g. 'cdc-wdm0')
        enable_wifi_scan: True
        enable_wifi_roam: False

        enable_docker_control: True # Docker control via Agent

        ## User input config
        input_drivers: [ 'TwistInputDriver', 'JoyInputDriver' ] # enabled input drivers


.. rubric:: Add Bridge Service To Your Compose File

Add ``phntm_bridge`` service to your ``compose.yaml`` file with ``phntm_bridge.yaml`` mounted into the container as shown below.
See available pre-built Docker images `here <https://ghcr.io/phantomcybernetics/phntm_bridge_client>`_.

.. Note::

    We recommend using Cyclone DDS with Phantom Bridge as it offers a more predictable behavior,
    the default Fast DDS sometimes fails to receive messages for topics that were unsubscribed and subscribed to again.
    Cyclone DDS is installed with our Docker image, and selected with the ``RMW_IMPLEMENTATION`` environmental variable.

    All parts of your ROS2 system should be always using `the same ROS distro and the same RMW implementation! <https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Different-Middleware-Vendors.html>`_

.. code-block:: yaml
    :caption: compose.yaml

    services:
      phntm_bridge:

        # select a pre-built image according to your ROS distro
        image: ghcr.io/phantomcybernetics/phntm_bridge_client:main-humble
        # image: ghcr.io/phantomcybernetics/phntm_bridge_client:main-iron
        # image: ghcr.io/phantomcybernetics/phntm_bridge_client:main-jazzy
        # image: ghcr.io/phantomcybernetics/phntm_bridge_client:main-kilted
        # image: ghcr.io/phantomcybernetics/phntm_bridge_client:main-lyrical
        # image: ghcr.io/phantomcybernetics/phntm_bridge_client:main-rolling
        # or use phntm/bridge:$ROS_DISTRO if building from source (see below)

        container_name: phntm-bridge
        hostname: phntm-bridge.local
        restart: unless-stopped # restarts after first run
        privileged: true # bridge needs this
        network_mode: host # webrtc needs this
        ipc: host # bridge needs this to see other local containers
        # environment:
        #  - RMW_IMPLEMENTATION=rmw_cyclonedds_cpp # recommended, see the note above!
        #  - ROS_DOMAIN_ID=22 # if used, specify ROS domain ID here
        volumes:
          - ~/phntm_bridge.yaml:/ros2_ws/phntm_bridge_params.yaml # bridge config goes here
          - ~/phntm_bridge.yaml:/ros2_ws/phntm_agent_params.yaml # agent config goes here, can be shared with the bridge client config
          - /var/run:/host_run # docker file extractor and wifi/cellular control need this
          - /tmp:/tmp # wifi control needs this
        devices:
          - /dev:/dev # LED control needs this
        # logging:
        #   driver: local # (optional) persistent logs, read with `docker logs`
        command:
          ros2 launch phntm_bridge client_agent_launch.py # launches Bridge Client and Agent together


.. rubric:: Launch Bridge Client & Open Phantom Remote

.. code-block:: bash

    docker compose up phntm_bridge

Then navigate to ``https://remote.phntm.io/%YOUR_ID_ROBOT%`` in your web browser.
The exact URL will be printed out by the Registration Utility, also it can be found at the top of the generated Bridge config file.
It will be also e-mailed to maintainer's address for your reference.


.. rubric:: Building Docker Image From Source

In the above example we've used a pre-built Docker Image `provided by Phantom Cybernetics <https://ghcr.io/phantomcybernetics/phntm_bridge_client>`_.
You can also build your own from source:

.. code-block:: bash

    cd ~
    git clone git@github.com:PhantomCybernetics/phntm_bridge_client.git phntm_bridge_client
    cd phntm_bridge_client
    ROS_DISTRO=humble; docker build -f Dockerfile -t phntm/bridge:$ROS_DISTRO --build-arg ROS_DISTRO=$ROS_DISTRO .
    # then use "image: phntm/bridge:$ROS_DISTRO" in your ~/compose.yaml
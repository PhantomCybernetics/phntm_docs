Upgrading Phantom Bridge Client
===============================

.. Note:: You may want to follow our `Bluesky account <https://bsky.app/profile/phntm.io>`_ for updates and service announcements.
          Significant milestones and new features will be also occasionally announced by e-mail.

.. rubric:: Stop and remove the current Docker Container

.. code-block:: bash

    docker stop phntm-bridge && docker rm phntm-bridge

.. rubric:: If using pre-built Docker images:

.. code-block:: bash

    docker image rm ghcr.io/phantomcybernetics/phntm_bridge_client:main-humble
    docker compose pull phntm_bridge

.. rubric:: If building from source:

.. code-block:: bash

    docker image rm phntm/bridge:humble
    cd ~/phntm_bridge_client
    git pull
    ROS_DISTRO=humble; docker build -f Dockerfile -t phntm/bridge:$ROS_DISTRO --build-arg ROS_DISTRO=$ROS_DISTRO .

.. rubric:: All done, relaunch

.. code-block:: bash

    docker compose up phntm_bridge
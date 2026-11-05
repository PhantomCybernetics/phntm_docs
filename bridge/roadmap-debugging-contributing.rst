Logs & Debugging
================

If you're curious about the planned features and overall development roadmap, see the open issues on GitHub:

- `Phantom Remote <https://github.com/PhantomCybernetics/phntm_remote/issues>`_ for UI related improvements and new features
- `Bridge Client <https://github.com/PhantomCybernetics/phntm_bridge_client/issues>`_ for the Bridge Client node related features and capabilities
- `Bridge Server <https://github.com/PhantomCybernetics/phntm_bridge_server/issues>`_ for cloud related topics

If you'd like to contribute or get otherwise involved, get in touch via `GitHub <https://github.com/PhantomCybernetics>`_ or
:email:`e-mail <human@phntm.io>`, pull requests are highly appreciated.

Here are some quality-of-life tips for debugging and working with the Phantom Bridge Client node source code:

Logs
----
To enable persistent Bridge Client & Agent logging, we recommend adopting Docker's logging functionality over ROS. Using the configuration shown below,
you can read your logs using ``docker logs -t phntm-bridge``. See `Docker documentation <https://docs.docker.com/engine/logging/configure/>`_ for details.

.. code-block:: yaml
   :caption: compose.yaml

    services:
      phntm_bridge:

        container_name: phntm-bridge
        logging:
          driver: local
        # ...


Using GDB Server
----------------
For debugging Bridge Client crashes, GDB Server wrapper can be turned on for the node. Both `gdb` and `gdbserver` are installed in the container.
(The Agent is written in Python, so this does not apply).

.. code-block:: bash

    # launch your node like this inside the container:
    ros2 launch phntm_bridge client_agent_launch.py gdb_server:=true [gdb_server_port:=3000]

    # then on the host machine:
    sudo apt-get install gdb
    gdb
    (gdb) target remote localhost:3000
    (gdb) continue


Dev Mode
--------

To streamline development with frequently changing code, you can mount a live repository into the Docker container, overwriting the ``/ros2_ws/src/phntm_bridge`` directory.
This approach eliminates the need for constant image rebuilds, as illustrated in the example below.

You may also prefer to not launch the Bridge Client and Agent nodes automatically on the container start, but rather start it manually from
the container's interactive shell:

.. code-block:: yaml
   :caption: compose.yaml

    services:
      phntm_bridge:

        container_name: phntm-bridge
        volumes:
          - ~/phntm_bridge:/ros2_ws/src/phntm_bridge # override with live repo
          - ~/phntm_agent:/ros2_ws/src/phntm_agent
          - ~/phntm_interfaces:/ros2_ws/src/phntm_interfaces
        command:
          /bin/sh -c "while sleep 1000; do :; done" # don't launch on container start

Then you can launch the process manually like so:

.. code-block:: bash

    docker compose up phntm_bridge -d # launch the modified container (detached)
    docker exec -it phntm-bridge bash # get interactive shell inside the container
    colcon colcon build --symlink-install --packages-select phntm_bridge # build from live repo
    ros2 launch phntm_bridge bridge_agent_launch.py # launches Bridge & Agent nodes, Ctrl-C kills both

Note that when launched manually like this, on the first run inside the container the Bridge Client performs
:doc:`first run checks <custom-message-types>` and exists when some packages are installed. You may need to
``source /ros2_ws/install/setup.bash`` to make the new packages visible to ROS, then start Bridge Client again.

VS Code Setup
-------------
When editing the Bridge Client's or Agent's code, it is recommended to SSH into your ROS2 machine with VS Code, then to start its process
inside the Bridge's Docker container. Clangd server is pre-installed in our Images and the environment will have access to all C++ and Python header files.
In this setup, you will want to start and stop the ROS Nodes manually, as described above.
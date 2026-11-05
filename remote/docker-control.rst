Docker Control
==============

.. image:: https://d13exqa8fa735g.cloudfront.net/ui-docker-control.png
    :align: right
    :class: ui-docker-control

Phantom Bridge offers tools for remote Docker Container monitoring and control that allow to ``start``, ``stop`` or ``restart`` any discovered Container.
Your Containers are autodetected, but must be set up and configured beforehand on the machine. Using `Docker Compose <https://docs.docker.com/compose/>`_ for this is highly recommended.

This feature allows for various configurations of your ROS2 machine to co-exist and be selected at runtime, depending on the situation.
For instance, you can have a Container responsible for autonomous navigation and tele-operate your machine manually when it's stopped.

Docker control actions can be accessed from the menu, but also mapped to Keyboard, Gamepad or Touchscreen buttons by calling the ``docker_command`` Service of the Phantom Agent node.
See more about :doc:`configuring user input. <user-input-and-teleoperation>`

.. rubric:: Configuration Options

It is possible to enable monitoring (CPU, PID count, etc) while also disallowing Docker Container control.
Both parameters shown below are expected by both the Bridge Client as well as the Bridge Agent.

.. code-block:: yaml
   :caption: phntm_bridge.yaml or phntm_agent.yaml

    /**:
      ros__parameters:

        docker_monitor_topic: '/docker_info' # '' to disable monitoring
        enable_docker_control: True # allow start/stop/restart of a container

Phantom Bridge Configuration
============================

A YAML configuration file is generated in the registration step of the Bridge Client install process. In this documentation we refer to it as ``phntm_bridge.yaml``,
it needs to be mapped into the Bridge Client's Docker container as `/ros2_ws/phntm_bridge_params.yaml`.
The initial file comes with your secret credentials and a few common options pre-configured.


Bridge Connection
-----------------

.. include:: ../config-blocks/bridge-connection.rst


Remote UI Configuration
-----------------------
See :doc:`Phantom Remote Configuration </remote/configuration>` for UI-specific configuration options.


Introspection & Blacklisting
----------------------------
These settings affect how Topics, Nodes and Services are discovered.

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        discovery_period_sec: 3.0 # <0 introspection is disabled
        stop_discovery_after_sec: 10.0 # <0 run forever (default)

        blacklist_topics: [] # blacklist topics from discovery (msg types or full topic ids)
        blacklist_services: [] # blacklist services and actions from discovery (msg types or full service ids)
        blacklist_msg_types: [] # blacklist IDL definitions from discovery and upload (msg types)


Topic Subscription QoS
----------------------

.. include:: ../config-blocks/topic-subscription-qos.rst


Extra ROS Packages To Install
-----------------------------
Custom packages can be installed to enable support for any Topic or Service types, see :doc:`Custom message & Service types <custom-message-types>` for more details.

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        extra_packages:
         - /ros2_ws/src/vision_msgs # path to a custom package source directory (inside the container)
         - /ros2_ws/src/astra_camera_msgs
         - some-other-package # binary package name to be installed with apt-get (this will be translated ros-%DISTRO%-some-other-package)


Video Encoding & Streaming
--------------------------
See :doc:`Video & Image Topics </bridge/video-and-image-topics>` for complete explanation and complete list of configuration options.

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        encoder_default_hw_device: 'sw' # 'cuda' for Nvidia, 'vaapi' for AMD/Intel or 'sw' for CPU (default)
        encoder_default_thread_count: 2
        encoder_default_gop_size: 30 # key frame every N frames
        encoder_default_bit_rate: 5000000 # 610 KB/s

        /some_image_topic:
          create_node: True # create a dedicated ROS node for this topic
          debug_num_frames: 10 # will print debug for this many frames (incl. NAL units)
          encoder_thread_count: 2 
          encoder_gop_size: 30 # key frame every N frames
          encoder_bit_rate: 5000000 # 610 KB/s
          print_time_deltas: False # debug, prints the delay between received frames in ms

        /some_depth_image_topic:
            max_sensor_value: 4000.0 # depth max distance/sensor value for normalizing
            colormap: 13 # cv2.COLORMAP, e.g. 13 = cv2.COLORMAP_MAGMA
            print_time_deltas: False # debug, prints the delay between received frames in ms


Hardware LEDs
-------------
See :doc:`Connection State LEDs </bridge/connection-state-leds>` for more.

.. include:: ../config-blocks/leds.rst


Socket.io Configuration
-----------------------
.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        sio_path: /robot/socket.io/ # must end with /
        sio_port: 1337
        sio_ssl_verify: True
        sio_connection_retry_sec: 5.0
        sio_debug: False # verbose Socket.io debug logging
        sio_verbose: False # prints out received and sent messages, too


WebRTC Configuration
--------------------
This config is received from the Bridge Server but can be extended or overridden for use with custom ICE/TURN servers.

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        use_cloud_ice_config: True # server config ignored if False
        ice_servers: # custom ICE servers (will be added to server's list if use_cloud_ice_config==True)
         - 'turn:ca.turn.phntm.io:3478'
         - 'turn:ca.turn.phntm.io:3479'
        ice_username: 'robo' # STUN/TURN credentials, robot's ID is used if empty
        ice_secret: 'pass' # STUN/TURN password, robot's KEY is used if empty
        enable_ice_udp_mux: True # multiple WebRTC peer connections can be multiplexed over a single UDP port
        enable_ice_tcp: False # in addition to the default UDP candidates, the library will also attempt to establish peer-to-peer connections over TCP if UDP is unavailable or blocked by network restrictions
        disable_fingerprint_verification: False


ROS Parameter Services
----------------------
You can fine tune access to node runtime ROS parameters as shown below. See more in :doc:`Runtime ROS Parameters </remote/runtime-ros-parameters>`.

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        blacklist_parameter_services:
          - controller_manager # nodes with disabled parameter services
        enable_node_parameters_read: True
        enable_node_parameters_write: False # only reading allowed


File Extraction
---------------
See :doc:`File extraction </bridge/file-extraction>` for full explanation.

.. include:: ../config-blocks/file-extraction.rst


Logs & Debugging
----------------
.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        log_sdp: True # verbose WebRTC debug
        webrtc_debug: True # debug webrtc logging
        webrtc_verbose: False
        log_heartbeat: True # debug heartbeat
        log_message_every_sec: 10.0f
        service_calls_verbose: False


Agent Configuration
-------------------
The Bridge Agent is a lightweight node that performs system monitoring, Docker container control, file extraction, and various related tasks.
Typically, it runs in the same container as the Bridge Client and can share the same config file (mapped into the container's ``/ros2_ws/phntm_agent_params.yaml``).
In case of a distributed system, it can be also installed separately and run in multiple instances. The Agent only expects the following options in the 
config file:

.. code-block:: yaml
   :caption: phntm_bridge.yaml or phntm_agent.yaml

    /**
      ros__parameters:

        host_name: 'pi5' # lower case, must be a valid ROS id or ''
        agent_update_period_sec: 0.5

        docker_monitor_topic: '/docker_info' # '' to disable
        enable_docker_control: True # allow start/stop/restart of a container

        system_info_topic: '/system_info_pi5' # writes output here, '' to disable
        disk_volume_paths: [ '/', '/dev/shm' ] # volumes to monitor, must be accessible from the container, [ '/' ] default

        net_interface: 'wlan0' # for cellular use the control iface (e.g. 'cdc-wdm0'); wi-fi/cellular/wired interface to monitor, disabled if ''
        net_monitor_topic: '/net_status' # Agent writes output here, Client reads here
        enable_wifi_scan: True # enable wi-fi scanning (Agent and Client)
        enable_wifi_roam: False # enable wi-fi roaming (Agent and Client)

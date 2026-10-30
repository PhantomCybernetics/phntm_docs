Configuration
=============
A YAML configuration file is generated in the registration step of the Bridge Client install process. In this documentation we refer to it as ``phntm_bridge.yaml``,
it needs to be mapped into the Client's container as ``/ros2_ws/phntm_bridge_params.yaml``. The initial file comes with your secret credentials and a few common options pre-configured.
Here's the full reference of all the configurable options.


Basics
------
.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        battery_topic: /battery # battery to show in the UI, '' to disable

        net_monitor_topic: '/net_status' # connectivity monitor topic to show in the UI (produced by Agent)
        enable_wifi_scan: True # must be also enabled in Agent config
        enable_wifi_roam: False # must be also enabled in Agent config

        docker_monitor_topic: '/docker_info' # produced by the Agent
        enable_docker_control: True # Docker control via Agent

        low_fps_default: 25 # low fps warning default for all topics

        peer_limit: 10 # limits the numbers of users that can connect to the robot at the same time (DDOS protection)
        ui_background_disconnect_sec: 120.0 # the UI will disconnect after being this many seconds in the background

        about_dialog_header: "Popup dialog's header" # pop-up dialog shown on UI load (like the one in the Demos)
        about_dialog: "Popup dialog's body, <b>some HTML is ok.</b>" # you can customize this HTML with ui_custom_includes_css


Individual Widget Options
-------------------------
Many UI panel widgets define and expect custom configuration parameteres in the YAML file. 
See built-in widgets for full reference.


User Input
----------
See :doc:`User input & Teleoperation </remote/user-input-and-teleoperation>`.

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        input_drivers: [ 'TwistInputDriver', 'JoyInputDriver', 'CustomDriverClass' ] # enabled input driver classes, remove to disable user input entirely, custom driver classed must be loaded via ui_custom_includes_js
        input_defaults: /ros2_ws/phntm_input_config.json # path to input defaults JSON file (as mapped inside the container)
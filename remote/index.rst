.. meta::
   :description: Phantom Remote is universal ROS2 toolkit for teleoperation, human-robot interaction, and both local and remote robot monitoring
   :keywords: ros, ros2, remote, observability, teleoperation, debugging, monitoring, webrtc, data, visualization, video, streaming, rviz, mobile, tablet, mac
   :author: Phantom Cynernetics Inc.


Phantom Remote
==============

Phantom Remote is an open-source toolkit for ROS2 teleoperation, human-robot interaction, and both local and remote robot monitoring.
Under the hood, it uses :doc:`Phantom Bridge </bridge/index>` as its networking layer.

Remote comes with :doc:`Docker container <docker-control>` control for the teleoperated ROS2 machine, :doc:`system load <system-info>` display, 
Wi-Fi roaming capability, and Cellular signal strength monitoring.

The interface is web based, optimized for both Desktop, :doc:`Touchscreen <touchscreen-interface>` input and small screens.
It is highly :doc:`customizable <customizing>`, you can extend it with only JavaScript and CSS.
Various configuration options make Phantom Remote suitable both as a universal ROS2 development tool, and a customer-facing User Interface.

.. raw:: html

   <script src="https://cdn.jsdelivr.net/npm/@mux/mux-player" defer></script>
   <mux-player
      id="big-video-player"
      playback-id="x702nehU9WXT02rbXzIU7RmEr900EebihFPNdKZgQ6alKU" 
      metadata-video-title="Phantom Bridge Introduction" 
      video-title="Phantom Bridge Introduction" 
      default-hidden-captions="true" 
      thumbnail-time="3"
   ></mux-player>

To get started with Phantom Remote, you only need to install ``Phantom Bridge Client`` to your ROS2 machine.
The Bridge Client is provided as a Docker container, ROS2 Humble to Rolling are supported.

.. raw:: html

    <p class="center">
        <a href="/bridge/install" class="btn-install">
            <span>↓</span> Install Bridge Client To Your ROS2 Machine
        </a>
    </p>

.. rubric::  Features

- Connects P2P or via a TURN server when P2P link is not possible
- ~5-10ms RTT on local network, 50ms+ RTT remote teleoperation via a TURN server
- Fast streaming of binary ROS2 messages (both in a out)
- Fast H.264 Video streaming, ROS2 `Image` and `CompressedImage` topics streamed as H.264 video
- Docker container :doc:`discovery and control <docker-control>`
- Reliable :doc:`ROS2 Service & Action calls <ros-services-and-actions>`
- :doc:`Keyboard, Gamepad and Touch interfaces <user-input-and-teleoperation>` work out of the box
- Continuous ROS2 introspection and live ROS Graph
- ROS2 distro agnostic (Humble - Rolling), UI is also platform independent
- Robot's Wi-Fi/Cellular signal monitoring, :doc:`Wi-Fi network scanning & AP roaming </bridge/wifi-scanning-and-roaming>`
- :doc:`File retreival </bridge/file-extraction>` from any running Docker container and the host FS (such as URDF models)
- :doc:`System load, disk space <system-info>`, and :doc:`Docker stats <docker-control>` monitoring
- Support for custom ROS2 message and service types
- Multiple peers can connect to the same ROS2 machine remotely at a very low extra CPU cost
- Works with rosbags and headless sims such as MuJoCo, Gazebo, Isaac Sim, or Webots


.. toctree::
   :maxdepth: 5
   :hidden: 
   :caption: Contents:

   demos
   Configuration <configuration>
   
   nodes-and-topics
   networking

   world-model-3d
   battery-state
   imu
   laser-scan
   log
   range
   system-info
   video

   user-input-and-teleoperation
   ros-services-and-actions
   runtime-ros-parameters
   docker-control
   touchscreen-interface

   security-and-privacy
   Customizing & Extending <customizing>
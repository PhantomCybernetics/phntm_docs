.. meta::
   :description: Phantom Bridge is a fast WebRTC ROS2 Bridge and User Interface for real-time ROS2 data visualization and video streaming, teleoperation, human-robot interaction, and both local and remote robot monitoring
   :keywords: ros, ros2, bridge, observability, teleoperation, remote debugging, local debugging, monitoring, webrtc, data, video, streaming
   :author: Phantom Cynernetics Inc.


Phantom Remote
==============

Phantom Remote is an open-source toolkit for ROS2 teleoperation, human-robot interaction, and both local and remote robot monitoring.
Under the hood, it uses :doc:`Phantom Bridge </bridge/index>` as its networking layer.

Remote comes with :doc:`Docker container control <docker-control>` for the teleoperated ROS2 machine, :doc:`system load <system-info>`,
Wi-Fi/Cellular signal strength monitoring.

The interface is web based, optiomized for both for both desktop and touchscreen devices, and highly customizable.
The UI is :doc:`customizable with JavaScript & CSS plugins <customizing>`, various configuration options make it suitable
both as a universal development tool and a customer-facing products.

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

.. toctree::
   :maxdepth: 5
   :hidden: 
   :caption: Contents:

   demos
   getting-started
   configuration
   
   nodes-and-topics
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
   /bridge/wifi-scanning-and-roaming
   touchscreen-interface

   customizing

   security-and-privacy

.. rubric::  Features

- Connects P2P or via a TURN server when P2P link is not possible
- ~5-10ms RTT on local network, 50ms+ RTT remote teleoperation via a TURN server
- Fast streamimg of binary ROS messages (both in a out)
- Fast H.264 video streaming, ROS `Image` and `CompressedImage` topics streamed as H.264 video (hw or sw-encodeded frames)
- Docker container :doc:`discovery and control <docker-control>`
- Reliable :doc:`ROS service & action calls <ros-services-and-actions>`
- :doc:`Keyboard, gamepad and touch interface <user-input-and-teleoperation>` work out of the box
- Continuous ROS2 introspection and live ROSGraph
- ROS2 distro agnostic (HUmble-Rolling), UI platform independent
- Robot's Wi-Fi/Cellular signal monitoring, :doc:`Wi-Fi network scanning & AP roaming </bridge/wifi-scanning-and-roaming>`
- :doc:`File retreival </bridge/file-extraction>` from any running Docker container and host fs (such as URDF models)
- :doc:`System load, disk space <system-info>`, and :doc:`Docker stats <docker-control>` monitoring
- Support for custom ROS2 message / service types
- Multiple peers can connect to the same machine remotely at a very low extra CPU cost
- Works with `rosbag` and headless simulators such as `Gazebo`, `Isaac Sim` or `Webots`
   
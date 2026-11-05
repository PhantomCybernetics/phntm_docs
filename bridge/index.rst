.. meta::
   :description: Phantom Bridge is a fast WebRTC ROS2 Bridge and User Interface for real-time ROS2 data visualization and video streaming, teleoperation, human-robot interaction, and both local and remote robot monitoring
   :keywords: ros, ros2, bridge, observability, teleoperation, remote debugging, local debugging, monitoring, webrtc, data, video, streaming
   :author: Phantom Cynernetics Inc.


Phantom Bridge
==============

Phantom Bridge is a fast, open-source, WebRTC + WebSocket ROS2 networking stack written in C++, Python and Node.js.
It consists of two ROS2 Nodes (Bridge Client and Bridge Agent) and Server infrastructure that facilitates peer-to-peer handshake and fast low-latency connection.
This is the basic networking layer behind :doc:`Phantom Remote </remote/index>`, but can be also used independently.

The Bridge Client performs continuous introspection in the background and detects any running ROS2 Nodes, Topics, Services and Actions.
It also compresses and encodes Image & CompressedImage topics, Video, and Point Clouds for network transport using a GPU or other HW video encoder where available.

The Bridge Agent also implements :doc:`Docker container monitoring & control </remote/docker-control>`, :doc:`system load monitoring </remote/system-info>`,
Wi-Fi / Cellular signal strength monitoring, and :doc:`Wi-fi scanning & AP roaming <wifi-scanning-and-roaming>`.

.. toctree::
   :maxdepth: 5
   :hidden: 
   :caption: Contents:

   architecture
   install
   Configuration <configuration>
   Upgrading <upgrading>

   custom-message-types.rst
   video-and-image-topics
   file-extraction
   wifi-scanning-and-roaming
   connection-state-leds

   availability-zones
   self-hosted
   roadmap-debugging-contributing

.. rubric::  Features

- Connects P2P or via a TURN server when P2P link is not possible
- ~5-10ms RTT on local network, 50ms+ RTT remote teleoperation via a TURN server
- Fast streaming of binary ROS2 messages (both in a out)
- Reliable :doc:`ROS2 Service & Action calls </remote/ros-services-and-actions>`
- :doc:`ROS2 Parameneters </remote/runtime-ros-parameters>` discovery, read and write at runtime
- Extra ROS2 packages can be easily included for :doc:`custom message type support <custom-message-types>`
- :doc:`File retreival <file-extraction>` from any running Docker container and host FS (such as URDF models)
- Multiple peers can connect to the same machine at a very low extra CPU cost
- Works with rosbags and simulators such as MuJoCo, Gazebo, Isaac Sim or Webots
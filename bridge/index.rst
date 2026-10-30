:github_url: https://github.com/PhantomCybernetics/phntm_bridge_docs/edit/main/index.rst

.. meta::
   :description: Phantom Bridge is a fast WebRTC ROS2 Bridge and User Interface for real-time ROS2 data visualization and video streaming, teleoperation, human-robot interaction, and both local and remote robot monitoring
   :keywords: ros, ros2, bridge, observability, teleoperation, remote debugging, local debugging, monitoring, webrtc, data, video, streaming
   :author: Phantom Cynernetics Inc.


Phantom Bridge
==============

Phantom Bridge is a fast, open-source, WebRTC + WebSocket ROS2 networking stack written in C++, Python and Node.js.
It comes with server infrastructe that fascilitates peer-to-peer handshake and fast low-latency connection.
It's the basic networking layer behing :doc:`Phantom Remote </remote/index>` that can be also used separately from the UI.

It also encodes video and point clouds using a GPU or other HW video encoder and compresses data, when necessary.

The Bridge comes with :doc:`Docker container control </remote/docker-control>` for the host machine, :doc:`system load </remote/system-info>`,
Wi-Fi/Cellular signal strength monitoring, and highly customizable web UI called :doc:`Phantom Remote </remote/index>` for both desktop and mobile touchscreen devices.

.. toctree::
   :maxdepth: 5
   :hidden: 
   :caption: Contents:

   architecture
   install
   configuration
   upgrading

   custom-message-types.rst
   video-and-image-topics
   file-extraction
   wifi-scanning-and-roaming
   connection-state-leds

   /remote/security-and-privacy
   
   availability-zones
   self-hosted
   roadmap-debugging-contributing

.. rubric::  Features

- Connects P2P or via a TURN server when P2P link is not possible
- ~5-10ms RTT on local network, 50ms+ RTT remote teleoperation via a TURN server
- ROS topic and service discovery
- Fast streamimg of binary ROS messages (both in a out)
- Fast H.264 video streaming, ROS `Image` and `CompressedImage` topics streamed as H.264 video (hw or sw-encodeded frames)
- Docker container :doc:`discovery and control </remote/docker-control>`
- Reliable :doc:`ROS service & action calls </remote/ros-services-and-actions>`
- :doc:`ROS parameneters </remote/runtime-ros-parameters>` discovery, read and write at runtime
- Extra ROS packages can be easily included for :doc:`custom message type support <custom-message-types>`
- Robot's Wi-Fi/Cellular signal monitoring, :doc:`Wi-Fi network scanning & AP roaming<wifi-scanning-and-roaming>`
- :doc:`File retreival <file-extraction>` from any running Docker container and host fs (such as URDF models)
- :doc:`System load, disk space </remote/system-info>`, and :doc:`Docker stats </remote/docker-control>` monitoring
- Standalone lightweight Bridge Agent for monitoring and management of various parts of a distributed system
- Multiple peers can connect to the same machine at a very low extra CPU cost
- Works with `rosbag` and simulators such as `Gazebo`, `Isaac Sim` or `Webots`
   
Nodes and Topics
================

Phantom Bridge Client performs continuous introspection on the ROS2 machine and automatically detects
all available ROS Nodes and Topics. You can see these under the Nodes & Topics menu, which displays this as a live ROS graph.

.. image:: https://d13exqa8fa735g.cloudfront.net/ui-graph-view.png
    :align: center
    :class: ui-graph-view

Visual connections between Nodes and Topics signify publisher and subscriber relationships.
A warning is displayed when a QoS mismatch is detected.

The icon next to the Node's name opens a dialog allowing to examine and modify :doc:`Runtime Parameters <runtime-ros-parameters>` of the Node.
The checkbox next to a topic name opens a new panel for the Topic.

Message Type Inspector
----------------------

.. image:: https://d13exqa8fa735g.cloudfront.net/ui-message-definition.png
    :align: right
    :class: ui-message-definition

Wherever you see a ROS message or service type (such as `sensor_msgs/msg/CameraInfo`), you can click on it to reveal its full
definition transcribed into a pseudo-JSON, as shown here. This is particularly useful as you don't need to look up
IDL/MSG/SRV type definitions and their nested sub-structures when working with a ROS system.

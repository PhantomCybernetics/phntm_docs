Networking
==========

The networking layer behind Phantom Remote is called :doc:`Phantom Bridge </bridge/index>`.
It handles connection negotiation and establishes fast, low-latency P2P link between the Remote UI running on your computer or tablet and the ROS2 machine.
Alternatively, relay servers are provided for situations where direct P2P connection is not possible (such as teleoperating a machine behind aggressive NAT).

Phantom Bridge works well over Wi-Fi but also Cellular 4G/LTE connections. Several tools are provided to display quality of the connection in both cases.

.. image:: https://d13exqa8fa735g.cloudfront.net/ui-header.png
    :align: center
    :class: ui-header


Wi-Fi Scanning & Roaming
------------------------

When enabled on the Bridge Client, your ROS2 robot can scan Wi-Fi networks within reach and also
roam between Access Points using :doc:`the built-in functionality </bridge/wifi-scanning-and-roaming>`.
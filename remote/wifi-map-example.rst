Composite Widget Example: Wi-Fi Map
===================================

.. image:: https://d13exqa8fa735g.cloudfront.net/widget-wifi-map.gif
    :class: widget-wifi-map cover-graphic

.. raw:: html

  <p class="declared">Widget declared in <a href="https://github.com/PhantomCybernetics/phntm_remote_extras/tree/main/examples/custom-wifi-map-panel-widget">wifi-map-panel-widget.js</a></p>

This widget is an example of extending the :doc:`CompositePanelWidgetBase </remote-ui-api/CompositePanelWidgetBase>` class to create a composite panel.
It combines `nav_msgs/msg/Odometry` with `phntm_interfaces/msg/IWStatus` messages do draw a 2D map of Wi-Fi signal strength along the robot's path.
You can pan and zoom into the map. It utilizes the :doc:`MultiTopicSource </remote-ui-api/MultiTopicSource>` class to subscribe to both topics.

This widget also uses a custom CSS and loads external graphics. It demonstrates how to add items into the panel's
menu and how to store and load state variables from `panel vars`. These are stored in the
page's URL and preserved between reloads.

The widget reads its default topics to subscribe to from custom params defined in the robot's YAML config file.

You can see this widget in action in our :doc:`live demos <demos>`.

.. rubric:: Configuration Options

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        wifi_map_example:
          default_odometry_topic: /odom
          default_wifi_topic: /net_status

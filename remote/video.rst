Video
=====

.. raw:: html

   <video autoplay muted loop class="video-panel-widget cover-graphic">
      <source src="https://d13exqa8fa735g.cloudfront.net/video-widget.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/tree/main/static/widgets/video
   :file-name: video-base.js
   :caption: Widget declared in

This is the default widget for any video and image topics transmitted as H.264. This includes depth (or any other single-channel frames)
that can be colorized before encoding into video on the Bridge Client. See See :doc:`Video and image topics </bridge/video-and-image-topics>`
for configuration options related to video encoding.

.. rst-class:: overlay-section

Detection2DArray Overlay
------------------------

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/widgets/video/detections2d.js

The panel can also overlay video frames with custom data. Out of this box, these are ``vision_msgs/msg/Detection2DArray`` topics,
that are often used in computer vision. Below are configuration options for a Detection2DArray topic:

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        /detections/front/boxes_2d:
          input_width: 416 # detection input frame width
          input_height: 416 # detection input frame height
          label_map: [ 'person', 'woman', 'man', 'camera', 'TV' ] # class label map
          color_map: [ '#0000ff', 'red', NULL, 'yellow', '', '#ff00ff' ] # colors to use for each class


.. _implementing-custom-video-overlays:

Implementing Custom Overlays
----------------------------

.. raw:: html

   <video autoplay muted loop class="video-panel-widget-twist">
      <source src="https://d13exqa8fa735g.cloudfront.net/video-widget-twist.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

To display any data you need over your video streams, you can create a custom video overlays by extending the :doc:`VideoPluginBase </remote-ui-api/VideoPluginBase>` class.

There is one other very simple example available in :doc:`our demos <demos>` displaying `TwistStamped` messages as a visualization of input keys.
You will find the source code in the `Remote Extras <https://github.com/PhantomCybernetics/remote_extras/tree/main/examples/custom-video-cmd-vel-overlay>`_ repository.
It shows how to use custom graphics, CSS, and how to work with the UI API.
In case you'd like to extend the `Detection2DArray` overlay shown above, the source code `is here <https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/widgets/video/detections2d.js>`_.

See more details about creating, hosting and loading your own extensions
in :doc:`Customizing the User Interface <customizing>`.
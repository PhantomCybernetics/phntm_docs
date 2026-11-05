Subscription QoS can be configured individually for every topic.
When QoS is set to be ``RELIABLE``, extra effort is taken to make sure at least the latest message in the topic is always delivered.
``BEST_EFFORT`` + ``VOLATILE`` are the default and recommended options for most topics, however, ``/rosout``, ``/robot_description``
and ``/tf_static`` topics are strongly recommended to be configured as ``RELIABLE`` + ``TRANSIENT_LOCAL`` to ensure delivery of all their messages. 

Low FPS / Hz warning threshold can be also set individually for every topic, the default value is set by ``low_fps_default``.

Note that ``Image``, ``CompressedImage`` and ``Video`` topics have different QoS defaults, more about this in :doc:`Video Processing </bridge/video-and-image-topics>`.

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        /some_topic:
          reliability: BEST_EFFORT # SYSTEM_DEFAULT, RELIABLE, BEST_EFFORT (default)
          durability: VOLATILE # SYSTEM_DEFAULT, TRANSIENT_LOCAL, VOLATILE (default)
          history_depth: 10
          lifespan_sec: -1.0 # -1.0 = Infinity (default)
          low_fps: 10 # specify threshold for unhealthy FPS warning

        # QoS defaults for all Image/CompressedImage topics
        image_topics_default_reliability: BEST_EFFORT
        image_topics_default_durability: VOLATILE
        image_topics_default_depth: 1
        image_topics_default_lifespan_sec: -1.0

        # QoS defaults for all encoded Video topics
        video_topics_default_reliability: RELIABLIE
        video_topics_default_durability: VOLATILE
        video_topics_default_depth: 10
        video_topics_default_lifespan_sec: -1.0
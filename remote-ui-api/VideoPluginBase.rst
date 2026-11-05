VideoPluginBase
===============

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/widgets/video/video-plugin-base.js

.. container:: class-constructor

  .. js:autoclass:: VideoPluginBase

.. container:: class-attributes

  .. rubric:: Static Class Attributes
  .. js:autoattribute:: VideoPluginBase#SOURCE_DEFAULT_TOPIC
  .. js:autoattribute:: VideoPluginBase#SOURCE_DESCRIPTION
  .. js:autoattribute:: VideoPluginBase#SOURCE_MAX_NUM
  .. js:autoattribute:: VideoPluginBase#SOURCE_TOPIC_TYPE

.. container:: instance-attributes

  .. rubric:: Instance Attributes
  .. js:autoattribute:: VideoPluginBase#client
  .. js:autoattribute:: VideoPluginBase#overlays
  .. js:autoattribute:: VideoPluginBase#panel
  .. js:autoattribute:: VideoPluginBase#ui
  .. js:autoattribute:: VideoPluginBase#video

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: VideoPluginBase#addTopic
  .. js:autofunction:: VideoPluginBase#clearAllTopics
  .. js:autofunction:: VideoPluginBase#clearTopic
  .. js:autofunction:: VideoPluginBase#clearVisuals
  .. js:autofunction:: VideoPluginBase#onTopicData
  .. js:autofunction:: VideoPluginBase#onResize
  .. js:autofunction:: VideoPluginBase#setupMenu

.. rubric:: Code Example

.. code-block:: javascript
   :caption: custom-video-plugin.js

   import { VideoPluginBase } from "widgets/video-plugin-base";
    
   export class CustomVideoWidget_CmdVel extends VideoPluginBase {
        static SOURCE_TOPIC_TYPE = 'some_msgs/msg/TopicMsgType';
        static SOURCE_DESCRIPTION = 'Source description';   
        static SOURCE_DEFAULT_TOPIC = null;
        static SOURCE_MAX_NUM = 1;

        constructor(video) {
            super(video);
        }

        addTopic(topic) {
            super.addTopic(topic);
            // handle topic add
        }

        setupMenu(menu_els) {
            // add custom menu items to menu_els (jQuery List)
        }

        onResize() {
            // handle resize
        }

        onTopicData(topic, msg) {
             // process received topic data
        }

        clearVisuals(topic) {
            // clear all topic visuals
        }

        clearTopic(topic) {
            // handle your own topic cleanup
            super.clearTopic(topic);
        }
   }
WorldModel3DPluginBase
======================

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/widgets/world-model-3d/world-model-plugin-base.js

.. container:: class-constructor

  .. js:autoclass:: WorldModel3DPluginBase

.. container:: class-attributes

  .. rubric:: Static Class Attributes
  .. js:autoattribute:: WorldModel3DPluginBase#SOURCE_DEFAULT_TOPIC
  .. js:autoattribute:: WorldModel3DPluginBase#SOURCE_DESCRIPTION
  .. js:autoattribute:: WorldModel3DPluginBase#SOURCE_MAX_NUM
  .. js:autoattribute:: WorldModel3DPluginBase#SOURCE_TOPIC_TYPE

.. container:: instance-attributes

  .. rubric:: Instance Attributes
  .. js:autoattribute:: WorldModel3DPluginBase#client
  .. js:autoattribute:: WorldModel3DPluginBase#overlays
  .. js:autoattribute:: WorldModel3DPluginBase#panel
  .. js:autoattribute:: WorldModel3DPluginBase#ui
  .. js:autoattribute:: WorldModel3DPluginBase#world_model

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: WorldModel3DPluginBase#addTopic
  .. js:autofunction:: WorldModel3DPluginBase#clearAllTopics
  .. js:autofunction:: WorldModel3DPluginBase#clearTopic
  .. js:autofunction:: WorldModel3DPluginBase#clearVisuals
  .. js:autofunction:: WorldModel3DPluginBase#onModelRemoved
  .. js:autofunction:: WorldModel3DPluginBase#onTopicData
  .. js:autofunction:: WorldModel3DPluginBase#onRender
  .. js:autofunction:: WorldModel3DPluginBase#onResize
  .. js:autofunction:: WorldModel3DPluginBase#setupMenu

.. rubric:: Code Example

.. code-block:: javascript
   :caption: JavaScript
   
   import { WorldModel3DPluginBase } from 'widgets/world-model-plugin-base';

   export class CustomWorldModel3DPlugin extends WorldModel3DPluginBase {

        static SOURCE_TOPIC_TYPE = 'some_msgs/msg/TopicMsgType'; // set your message type
        static SOURCE_DESCRIPTION = 'Source description'; // show in the overlay selection
        static SOURCE_DEFAULT_TOPIC = null; // default topic id to select or null
        static SOURCE_MAX_NUM = -1; // number of allowed topics, -1=unlimited

        constructor(world_model) {
            super(world_model);
        }

        addTopic(topic) {
            super.addTopic(topic);
            // handle topic add
        }

        setupMenu(menu_els) {
            // add custom menu items to menu_els (jQuery List)
        }

        onTopicData(topic, msg) {
            // process received topic data
        }

        onRender() {
            // called from the widget's rendering loop
        }

        clearVisuals(topic) {
            // clear all topic visuals
        }

        clearTopic(topic) {
            // handle your own topic cleanup
            super.clearTopic(topic);
        }
    }
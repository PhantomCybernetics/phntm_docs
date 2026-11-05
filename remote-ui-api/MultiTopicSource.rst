MultiTopicSource
================

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/widgets/inc/multitopic.js

.. container:: class-constructor

  .. js:autoclass:: MultiTopicSource

.. container:: events

  .. rubric:: Triggers Events
  .. js:autoattribute:: MultiTopicSource#event:change

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: MultiTopicSource#add
  .. js:autofunction:: MultiTopicSource#getSources
  .. js:autofunction:: MultiTopicSource#hasType
  .. js:autofunction:: MultiTopicSource#hasSources
  .. js:autofunction:: MultiTopicSource#init
  .. js:autofunction:: MultiTopicSource#off
  .. js:autofunction:: MultiTopicSource#on
  .. js:autofunction:: MultiTopicSource#topicSubscribed

.. rubric:: Code Example

.. code-block:: javascript
   :caption: JavaScript
   
   import { CompositePanelWidgetBase } from 'widgets/composite-widget-base';

   export class SomeWidget extends CompositePanelWidgetBase {

        constructor (panel, widget_css_class) {

            // ...

            this.sources = new MultiTopicSource(this);

            this.sources.on("change", (topics) => this.onSourcesChange(topics));

            this.sources.add(
                "tf2_msgs/msg/TFMessage",
                "Static transforms source",
                "/tf_static", // default topic
                2, // max 2 of this type
                (topic, tf) => {
                    that.onTFData(topic, msg); // onData
                },
                 (topic) => {
                    // onSourceRemoved
                }
            );
            this.sources.add(
                "std_msgs/msg/BoolMessage",
                "Bool source",
                null, // no default topic
                -1, // no limit
                (topic, tf) => { 
                    that.onBoolData(topic, msg); // onData
                },
                (topic) => {
                    // onSourceRemoved
                }
            );
            
            this.sources.init();  // call when all sources are added

            this.onSourcesChange(this.sources.getSources());

            // ...
        }

        onSourcesChange(source_topics) {
            console.log('Panel sources changed: ', source_topics);
        }

        setupMenu(menu_els) { // CompositePanelWidgetBase does this in setupMenu()
            this.sources.setupMenu(menu_els); // adds its ui to the panel menu
        }

        onTFData(topic, msg) {
            console.log('Got TF data from ' + topic + ': ', msg);
        }

         onBoolData(topic, msg) {
            console.log('Got Bool data from ' + topic + ': ', msg);
        }
        
        onClose() { // CompositePanelWidgetBase does this in onClose()
            this.sources.close(); // cleanup
        }
   }
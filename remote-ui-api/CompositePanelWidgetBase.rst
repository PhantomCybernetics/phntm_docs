CompositePanelWidgetBase
========================

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/widgets/inc/composite-widget-base.js

.. container:: class-constructor

  .. js:autoclass:: CompositePanelWidgetBase

.. container:: class-attributes

  .. rubric:: Static Class Attributes
  .. js:autoattribute:: CompositePanelWidgetBase#DEFAULT_HEIGHT
  .. js:autoattribute:: CompositePanelWidgetBase#DEFAULT_WIDTH
  .. js:autoattribute:: CompositePanelWidgetBase#LABEL

.. container:: instance-attributes

  .. rubric:: Instance Attributes
  .. js:autoattribute:: CompositePanelWidgetBase#autoresize_renderer
  .. js:autoattribute:: CompositePanelWidgetBase#client
  .. js:autoattribute:: CompositePanelWidgetBase#panel
  .. js:autoattribute:: CompositePanelWidgetBase#sources
  .. js:autoattribute:: CompositePanelWidgetBase#ui
  .. js:autoattribute:: CompositePanelWidgetBase#widget_el

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: CompositePanelWidgetBase#getFpsString
  .. js:autofunction:: CompositePanelWidgetBase#onClose
  .. js:autofunction:: CompositePanelWidgetBase#onPaused
  .. js:autofunction:: CompositePanelWidgetBase#onResize
  .. js:autofunction:: CompositePanelWidgetBase#onUnpaused
  .. js:autofunction:: CompositePanelWidgetBase#setupMenu

.. rubric:: Code Example

.. code-block:: javascript
   :caption: JavaScript

   import { CompositePanelWidgetBase } from 'widgets/composite-widget-base';

   export class CustomSingleTypePanelWidget extends SingleTypePanelWidgetBase {

        static LABEL = 'Widget Label';
        
        constructor(panel) {
            super(panel, 'my-widget-class'); // gets added to the panel

            this.sources.add(
                "some_msgs/msg/SomeMsgType",	
                "Source description",
                null, // default topic
                1, // limit to 1
                (topic, msg) => this.onSomeData(topic, msg),
            );
            this.sources.add(
                "some_msgs/msg/SomeOtherMsgType",	
                "Source description",
                null, // default topic
                1, // limit to 1
                (topic, msg) => this.onSomeOtherData(topic, msg),
            );

            this.sources.init(); // init sources

            // set up DOM or Three.js Renderer+Scene here
        }

        setupMenu(menu_els) {
            this.sources.setupMenu(menu_els); // set up menu for the sources
            // add custom menu items to menu_els (jQuery List)
        }

        onSomeData (topic, msg) {
            // handle topic data
        }

        onSomeOtherData (topic, msg) {
            // handle other topic data
        }

        onResize() {
            // handle resize
        }

        onClose() {
            // clean up
             super.onClose();
        }
   }
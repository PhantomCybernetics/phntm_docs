SingleTypePanelWidgetBase
=========================

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/widgets/inc/single-type-widget-base.js

.. container:: class-constructor

  .. js:autoclass:: SingleTypePanelWidgetBase

.. container:: class-attributes

  .. rubric:: Static Class Attributes
  .. js:autoattribute:: SingleTypePanelWidgetBase#DEFAULT_HEIGHT
  .. js:autoattribute:: SingleTypePanelWidgetBase#DEFAULT_WIDTH
  .. js:autoattribute:: SingleTypePanelWidgetBase#HANDLED_MSG_TYPES

.. container:: instance-attributes

  .. rubric:: Instance Attributes
  .. js:autoattribute:: SingleTypePanelWidgetBase#autoresize_renderer
  .. js:autoattribute:: SingleTypePanelWidgetBase#client
  .. js:autoattribute:: SingleTypePanelWidgetBase#panel
  .. js:autoattribute:: SingleTypePanelWidgetBase#topic
  .. js:autoattribute:: SingleTypePanelWidgetBase#ui
  .. js:autoattribute:: SingleTypePanelWidgetBase#widget_el

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: SingleTypePanelWidgetBase#getFpsString
  .. js:autofunction:: SingleTypePanelWidgetBase#onClose
  .. js:autofunction:: SingleTypePanelWidgetBase#onData
  .. js:autofunction:: SingleTypePanelWidgetBase#onPaused
  .. js:autofunction:: SingleTypePanelWidgetBase#onResize
  .. js:autofunction:: SingleTypePanelWidgetBase#onUnpaused
  .. js:autofunction:: SingleTypePanelWidgetBase#setupMenu

.. rubric:: Code Example

.. code-block:: javascript
   :caption: JavaScript

   import { SingleTypePanelWidgetBase } from 'widgets/single-type-widget-base';

   export class CustomSingleTypePanelWidget extends SingleTypePanelWidgetBase {

        static HANDLED_MSG_TYPES = [ 'some_msgs/msg/TopicMsgType' ]; // associate with these types
        
        constructor(panel, topic) {
            super(panel, topic, 'my-widget-class'); // gets added to the panel
            // set up DOM or Three.js Renderer+Scene here
        }

        setupMenu(menu_els) {
            // add custom menu items to menu_els (jQuery List)
        }

        onData(msg) {
            // do something with the received data
        }

        onResize() {
            // handle resize
        }

        onClose() {
            // clean up
        }
   }

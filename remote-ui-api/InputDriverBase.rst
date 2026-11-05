InputDriverBase
===============

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/input/input-driver-base.js

.. container:: class-constructor

  .. js:autoclass:: InputDriverBase 

.. container:: class-attributes  

  .. rubric:: Static Class Attributes
  .. js:autoattribute:: InputDriverBase#LABEL

.. container:: instance-attributes

  .. rubric:: Instance Attributes
  .. js:autoattribute:: InputDriverBase#client
  .. js:autoattribute:: InputDriverBase#input_manager
  .. js:autoattribute:: InputDriverBase#output
  .. js:autoattribute:: InputDriverBase#output_topic

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: InputDriverBase#generate
  .. js:autofunction:: InputDriverBase#getAxes
  .. js:autofunction:: InputDriverBase#getButtons
  .. js:autofunction:: InputDriverBase#getConfig
  .. js:autofunction:: InputDriverBase#setConfig

.. rubric:: Code Example

.. code-block:: javascript
   :caption: JavaScript

   import { InputDriverBase } from 'input/input-driver-base';

   export class ExampleBoolInputDriver extends InputDriverBase {

        // human readable driver name
        static LABEL = "Example Bool Driver";

        // the message type to generate must be available to the Bridge node
        // (see https://docs.phntm.io/bridge/basics/custom-message-types.html)
        msg_type = 'std_msgs/msg/Bool';

        num_axes = 5; // number of mappable axes to create
        num_buttons = 5; // number of mappable buttons to create

        // create named axes to allow mapping input to
        getAxes() { 
            let axes = {};
            for (let i = 0; i < this.num_axes; i++) {
                axes[`axis.${i}`] = 'Test: Axis '+i
            }
            return axes;
        }

        // create named buttons to allow mapping input to
        getButtons() { 
            let buttons = {};
            for (let i = 0; i < this.num_buttons; i++) {
                buttons[`btn.${i}`] = 'Test: Button '+i
            }
            return buttons;
        }

        // generate output message from the current state of all axes and buttons
        // in this simple example, we only return True if something is pressed
        generate() {
            let something_pressed = false;

            for (let i = 0; i < this.num_axes; i++) {
                let id_axis = `axis.${i}`;
                if (this.axes_output[id_axis])
                    something_pressed = true;
            }

            for (let i = 0; i < this.num_buttons; i++) {
                let id_btn = `btn.${i}`;
                if (this.buttons_output[id_btn])
                    something_pressed = true;
            }

            // output message
            let msg = {
                data: something_pressed
            }

            return msg;
        }
   }
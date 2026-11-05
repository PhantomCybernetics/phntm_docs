ServiceInputBase
================

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/input/service-input-base.js

.. container:: class-constructor

  .. js:autoclass:: ServiceInputBase 

.. container:: instance-attributes

  .. rubric:: Instance Attributes
  .. js:autoattribute:: ServiceInputBase#client
  .. js:autoattribute:: ServiceInputBase#id_service

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: ServiceInputBase#getCurrentValue
  .. js:autofunction:: ServiceInputBase#makeElements
  .. js:autofunction:: ServiceInputBase#onValueChanged
  .. js:autofunction:: ServiceInputBase#updateDisplay

.. rubric:: Code Example

.. code-block:: javascript
   :caption: JavaScript

   import { ServiceInputBase } from 'input/service-input-base';

   export class ServiceInput_ExampleSlider extends ServiceInputBase {

        constructor(id_service, client) {
            super(id_service, client);

            this.config = this.client.getServiceConfig(id_service);  // read service config passed from YAML

            // do some init here
        }

        // get curren value via a getter service
        getCurrentValue(done_cb, err_cb) {
            if (!this.config.value_read_service) {
                err_cb("Getter service not provided for "+this.id_service + " widget");
                return;
            }
            let that = this;
            let timeout_sec = this.config.timeout_sec ? this.config.timeout_sec : 2.0; // timeout for the service call reply
            this.client.serviceCall(this.config.value_read_service, null, true, timeout_sec, (reply) => { // call w no payload & silent
                console.warn("Service widget for " + that.id_service + ' current value:', reply);
                if (reply.data !== undefined) {
                    done_cb(reply.data);
                } else {
                    err_cb("Getter service  "+this.config.value_read_service+" reply missing 'data' attribute");
                }
            });
        }

        makeElements(target_el) {
            // init your DOM here
        }

        updateDisplay(value, is_error=false) {
            // update DOM with value
        }

        onValueChanged(msg) {
            this.updateDisplay(msg.data); // update the UI
        }
   }
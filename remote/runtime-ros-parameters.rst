Runtime ROS Parameters
======================

.. image:: https://d13exqa8fa735g.cloudfront.net/ui-ros-params.png
    :align: right
    :class: ui-ros-params

In the graph view of :doc:`ROS Nodes and Topics <nodes-and-topics>`, the icon next to every ROS Node name opens the Parameter Inspector, as shown here.

This dialog allows to inspect and modify any ROS Parameters declared by the Node. Parameters marked as ``read_only`` can not be edited.
Input is validated according to parameter's type, ``description`` and ``additional_constraints`` are displayed as text hints.

The ROS Node needs to provide Services of type `rcl_interfaces/srv/ListParameters`, `rcl_interfaces/srv/DescribeParameters`, `rcl_interfaces/srv/GetParameters` and `rcl_interfaces/srv/SetParameters` for this functionality to work.
This is best achieved by instantiating the node class with `start_parameter_services=True`.
You also need to spin the Node to process these service requests.


.. rubric:: Configuration Options

You can adjust permissions for Parameter Services with the following configuration:

.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        blacklist_parameter_services: # nodes with disabled parameter services
          - controller_manager 
        enable_node_parameters_read: True
        enable_node_parameters_write: False # only reading allowed
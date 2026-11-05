.. code-block:: yaml
   :caption: phntm_bridge.yaml

    /**:
      ros__parameters:

        id_robot: '%ID_ROBOT%' # robot's ID generated during registration
        key: '%SECRET_KEY%' # robot's secret key generated during registration
        name: 'Unnamed Robot' # the name to show in the UI

        maintainer_email: 'robot.master@domain.com' # your e-mail for service announcements

        bridge_server_address: https://us-ca.bridge.phntm.io # the Bridge Server instance to connect to

The ``bridge_server_address`` parameter is initially set to the closest available Phantom Bridge Server from the robot's location.
It can be changed as needed, for instance when the robot moves, see :doc:`Availability Zones </bridge/availability-zones>` for current options.
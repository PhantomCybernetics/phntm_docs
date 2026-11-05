Security & Privacy
==================

All communication between the ROS2 machine and the Peers (such as Phantom Remote) takes place over encrypted channels.

The Bridge Server only stores basic metadata about the Robots for the purposes of improving the service.

No telemetry data, video or images are ever stored nor analyzed on any part of the infrastructure hosted by `Phantom Cybernetics <https://www.phantomcybernetics.com>`_.

The files :doc:`extracted </bridge/file-extraction>` from a ROS2 machine are cached on the Bridge Server until the cache is invalidated.

Access to your robot's basic Remote dashboard is secured by a unique URL. Don't share it on the internet!

Re-register your machine in case you need to invalidate the URL. `Phantom Remote Pro <https://remote.phntm.io>`_ offers the option to make access fully private and
precisely control who can do what with your robots. This is a feature of a commercial service.

The maintainer's email is only used for service and new feature announcements. We don't sell your personal data to anyone.

The source code is provided under the MIT license "as is" without any warranty or liability.
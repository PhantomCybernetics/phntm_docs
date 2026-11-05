BrowserClient
=============

.. declared-link:: https://github.com/PhantomCybernetics/phntm_remote/blob/main/static/browser-client.js

.. container:: class-constructor

  .. js:autoclass:: BrowserClient 

.. container:: instance-attributes

  .. rubric:: Instance Attributes (Read only)
  .. js:autoattribute:: BrowserClient#discovered_nodes
  .. js:autoattribute:: BrowserClient#discovered_services
  .. js:autoattribute:: BrowserClient#discovered_topics
  .. js:autoattribute:: BrowserClient#id_instance
  .. js:autoattribute:: BrowserClient#id_robot
  .. js:autoattribute:: BrowserClient#open_media_streams
  .. js:autoattribute:: BrowserClient#name
  .. js:autoattribute:: BrowserClient#pc
  .. js:autoattribute:: BrowserClient#socket
  .. js:autoattribute:: BrowserClient#supported_msg_types
  .. js:autoattribute:: BrowserClient#topic_streams
  .. js:autoattribute:: BrowserClient#ui

.. container:: events

  .. rubric:: Triggers Events
  .. js:autoattribute:: BrowserClient#event:defs_updated
  .. js:autoattribute:: BrowserClient#event:docker
  .. js:autoattribute:: BrowserClient#event:error
  .. js:autoattribute:: BrowserClient#event:media_stream
  .. js:autoattribute:: BrowserClient#event:nodes
  .. js:autoattribute:: BrowserClient#event:peer_connected
  .. js:autoattribute:: BrowserClient#event:peer_connection_changed
  .. js:autoattribute:: BrowserClient#event:peer_disconnected
  .. js:autoattribute:: BrowserClient#event:peer_service_call_broadcast
  .. js:autoattribute:: BrowserClient#event:peer_stats
  .. js:autoattribute:: BrowserClient#event:robot_peers
  .. js:autoattribute:: BrowserClient#event:services
  .. js:autoattribute:: BrowserClient#event:socket_connect
  .. js:autoattribute:: BrowserClient#event:socket_disconnect
  .. js:autoattribute:: BrowserClient#event:topics
  .. js:autoattribute:: BrowserClient#event:update

.. container:: instance-methods

  .. rubric:: Instance Methods
  .. js:autofunction:: BrowserClient#connect
  .. js:autofunction:: BrowserClient#disconnect
  .. js:autofunction:: BrowserClient#getConfigParam
  .. js:autofunction:: BrowserClient#getPeerConnectionInfo
  .. js:autofunction:: BrowserClient#getServiceConfig
  .. js:autofunction:: BrowserClient#getTopicConfig
  .. js:autofunction:: BrowserClient#off
  .. js:autofunction:: BrowserClient#offServiceConfig
  .. js:autofunction:: BrowserClient#offTopicConfig
  .. js:autofunction:: BrowserClient#offTopicData
  .. js:autofunction:: BrowserClient#offUIConfig
  .. js:autofunction:: BrowserClient#on
  .. js:autofunction:: BrowserClient#once
  .. js:autofunction:: BrowserClient#onServiceConfig
  .. js:autofunction:: BrowserClient#onTopicConfig
  .. js:autofunction:: BrowserClient#onTopicData
  .. js:autofunction:: BrowserClient#onUIConfig
  .. js:autofunction:: BrowserClient#openWriteChannel
  .. js:autofunction:: BrowserClient#requestRobotFileDownloadURL
  .. js:autofunction:: BrowserClient#serviceCall
  .. js:autofunction:: BrowserClient#writeTopicData
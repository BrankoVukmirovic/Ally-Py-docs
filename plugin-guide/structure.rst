Plugin structure
================

Each plugin is composed of two packages:

* ``_plugin_`` contains the configuration files that expose the plugin services. This package is automatically scanned by the application distribution loader and interpreted by the Inversion of Controls dependency injection container.
* ``<main package>`` contains the implementation of the plugin. The name of the main package must be lower case, with words separated by underscores. Plugins that share a main package name can have sub packages to separate functionality within the plugin group. 

Plugins also contain an ant build file called ``build-plugin.ant`` which packages the plugin to an egg file used by the application distribution.

The plugin package _plugin_
-----------------------------

The ``_plugin_`` package contains only the init module, which contains a description ``doc`` and a single package ``plugin.<unique package>``. 
The unique package is usually the plugin <main package> but if the main package is the same for multiple plugins we have to use a composition of this main package because the unique package within the plugin needs to be unique among all plugins, also this package name is used as the plugin id. 

For example the introspection functionality in Ally.py is provided by two plugins:

* ``plugin.introspection`` which provides the components and plugins that are active in the current distribution 
* ``plugin_.introspection_request`` the introspection for the possible requests that can be made

.. TODO:: Not sure about the difference here

The main package for both plugins is ``introspection``, which contains all the configuration modules. The Inversion of Control dependency injection container ignores any subpackages.

The ``plugin.<unique package>.init`` module contains the following global variables:

* NAME a short descriptive name for the plugin.
* GROUP used to define a collection of plugins that have a common purpose. 
* VERSION is a string of the form '1.2' where 1 is the major version of the plugin and 2 is the minor version. The minor version changes for every plugin release. The major version changes only when there are significant changes to the plugin.
* DESCRIPTION a short explanation of the functionality of the plugin.

The plugin package <main package>
------------------------------------
The ``<main package>`` contains two sub packages:

* ``<main package>.**.api`` contains only the modules that define the REST API models and services. Whenever another plugin uses only modules from this package it is considered to have a light dependency, which means that the two plugins can run on different servers using different databases communicating through the API.
* ``<main package>.**.meta`` contains modules that enhance the REST models, such as database mappings of the models. Whenever another plugin uses modules from this package it is considered to have a medium dependency, which means that the plugins can run on different servers but they have to use the same database.

Any other modules that are defined in the plugin and are not in this packages create a heavy dependency, which means that the plugins need to be part of the same application distribution.

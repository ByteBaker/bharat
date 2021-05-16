Bharat: Package For Data On The Largest Democracy
==================================================

A package for easily working with Bharat(India) and states' metadata.

-   All states and union territories of Bharat (India)
-   Capitals
-   GST Codes
-   Abbreviations (vehicle codes)
-   Websites
-   Postal Zones
-   Geographical Zones
-   Date of statehood
-   Is union territory
-   ISO3166-2:IN codes

Installation
------------

As usual:

    pip install bharat

Features
--------

Easy access to state information:

    >>> import bharat
    >>> bharat.states.UP
    <State:Uttar Pradesh>
    >>> bharat.states.UP.abbr
    'UP'
    >>> bharat.states.UP.name
    'Uttar Pradesh'
    >>> bharat.states.UP.post_zone
    2

Includes union territories too: 

    >>> bharat.states.DL.name
    'Delhi'
    >>> bharat.states.DL.is_UT
    True
    >>> bharat.states.UP.is_UT
    False

List of all states (or UTs):

    >>> bharat.states.STATES
    [<State:Andhra Pradesh>, <State:Arunachal Pradesh>, <State:Assam>, ...
    >>> bharat.states.UNION_TERRITORIES
    [<Union Territory:Andaman and Nicobar Island>, <Union Territory:Chandigarh>, ...

And the whole collection, if you want it:

    >>> bharat.states.ALL
    [<State:Andhra Pradesh>, <State:Arunachal Pradesh>, <State:Assam>, ...

For convenience, `STATES`, `UNION_TERRITORIES`, and `ALL`
can be accessed directly from the `bharat` module:

    >>> bharat.states.STATES
    [<State:Andhra Pradesh>, <State:Arunachal Pradesh>, <State:Assam>, ...
    >>> bharat.STATES
    [<State:Andhra Pradesh>, <State:Arunachal Pradesh>, <State:Assam>, ...

States' Attributes
--------
    >>> bharat.states.State.__annotations__.keys()
    dict_keys(['abbr', 'capital', 'code', 'iso31662in', 'is_UT', 'name', 'post_zone', 'statehood_date', 'website', 'zone'])
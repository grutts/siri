Siri
====

.. image:: https://img.shields.io/pypi/v/siri.svg
    :target: https://pypi.python.org/pypi/siri
    :alt: Latest PyPI version

---------------------

A library for dealing with `Service Interface for Real-time Information (SIRI) <http://siri.org.uk/index.htm>`_ data


Contains:

* Auto-generated python classes for dealing with SIRI 2.0 data. Generated from the SIRI 2.0 XSD using xsdata.
* A method to parse SIRI XML.
* A method to serialize objects into SIRI XML

This library leans heavily on the output and functions of `xsdata <https://github.com/tefra/xsdata>`_

No warranty is provided with this library. This library does not defend against XML attacks.

Installation
------------

.. code:: console

    $ pip install siri


Usage
-----

**Parse a file**

.. code:: python

    >>> from siri import parse
    >>> parse('my_siri_file.xml')

**Parse an XML string**

.. code:: python

    >>> from siri import parse
    >>> xml_string = """
        <?xml version="1.0" encoding="UTF-8"?>
            <ns0:Siri xmlns:ns0="http://www.siri.org.uk/siri" version="2.0">
                <ns0:SubscriptionResponse>
                    <ns0:ResponseTimestamp>2021-01-01T00:00:00</ns0:ResponseTimestamp>
                    <ns0:ResponderRef>Responder Ref</ns0:ResponderRef>
                    <ns0:ResponseStatus>
                        <ns0:ResponseTimestamp>2021-01-01T00:00:00</ns0:ResponseTimestamp>
                        <ns0:SubscriberRef>Subscriber Ref</ns0:SubscriberRef>
                        <ns0:SubscriptionRef>1</ns0:SubscriptionRef>
                        <ns0:Status>true</ns0:Status>
                    </ns0:ResponseStatus>
                </ns0:SubscriptionResponse>
            </ns0:Siri>
        """
    >>> siri_object = parse(xml_string)
    >> print(siri_object.subscription_response.response_status.subscription_ref)
    1




**Build and serialize a SIRI object**

.. code:: python

    >>> from siri import Siri, SubscriptionResponse, ResponseStatus
    >>>
    >>> obj = Siri(
    >>>     subscription_response=SubscriptionResponse(
    >>>      response_timestamp=datetime.datetime(2021, 1, 1).isoformat(),
    >>>      responder_ref="Responder Ref",
    >>>      response_status=ResponseStatus(
    >>>          response_timestamp=datetime.datetime(2021, 1, 1).isoformat(),
    >>>          subscriber_ref="Subscriber Ref",
    >>>          subscription_ref="1",
    >>>          status=True,
    >>>      )
    >>>  )
    >>>
    >>> serialize(obj)

    """<?xml version="1.0" encoding="UTF-8"?>
    <ns0:Siri xmlns:ns0="http://www.siri.org.uk/siri" version="2.0">
        <ns0:SubscriptionResponse>
            <ns0:ResponseTimestamp>2021-01-01T00:00:00</ns0:ResponseTimestamp>
            <ns0:ResponderRef>Responder Ref</ns0:ResponderRef>
            <ns0:ResponseStatus>
                <ns0:ResponseTimestamp>2021-01-01T00:00:00</ns0:ResponseTimestamp>
                <ns0:SubscriberRef>Subscriber Ref</ns0:SubscriberRef>
                <ns0:SubscriptionRef>1</ns0:SubscriptionRef>
                <ns0:Status>true</ns0:Status>
            </ns0:ResponseStatus>
        </ns0:SubscriptionResponse>
    </ns0:Siri>"""

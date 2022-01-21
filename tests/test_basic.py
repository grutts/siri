# For now, only basic tests looking for errors in the (de)serialization
from siri import parse, serialize


def test_with_file():
    obj = parse('tests/sample.xml')
    assert (
        obj.subscription_request.vehicle_monitoring_subscription_request[
            0
        ].vehicle_monitoring_request.vehicle_monitoring_ref
        == "12345"
    )
    assert parse(serialize(obj)) == obj


def test_with_string():
    siri_string = """
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
    obj = parse(siri_string)
    assert obj.subscription_response.response_status[0].status is True
    assert parse(serialize(obj)) == obj

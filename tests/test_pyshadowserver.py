import pytest

from pyshadowserver import InvalidConfiguration, ShadowServer


class TestPyShadowServer:
    def test_asn(self):
        ss = ShadowServer()
        res = ss.asn(origin="8.8.8.8")
        assert len(res) == 1
        assert res[0]["asn"] == "15169"

    def test_malware(self):
        ss = ShadowServer()
        res = ss.malware_query(samples=["dfe1832e02888422f48d6896dc8e8f73"])
        assert len(res) == 1
        assert (
            res[0]["sha256"]
            == "d8d395f8744335fba53b0a4308e7b380a0aca86bfc8939ded9f4c8c5cb1e838a"
        )

    def test_ping(self):
        ss = ShadowServer()
        try:
            ss.load_config()
        except InvalidConfiguration:
            pytest.skip("Please configure ShadowServer to test this library")
        res = ss.ping()
        assert "pong" in res

    def test_report_subscribed(self):
        ss = ShadowServer()
        try:
            ss.load_config()
        except InvalidConfiguration:
            pytest.skip("Please configure ShadowServer to test this library")
        res = ss.reports_subscribed()
        assert len(res) == 1
        assert isinstance(res[0], str)

    def test_reports_types(self):
        ss = ShadowServer()
        try:
            ss.load_config()
        except InvalidConfiguration:
            pytest.skip("Please configure ShadowServer to test this library")
        res = ss.reports_types(detail=True)
        assert len(res) > 0
        assert "description" in res[0].keys()
        assert "type" in res[0].keys()

    def test_reports_schema(self):
        ss = ShadowServer()
        try:
            ss.load_config()
        except InvalidConfiguration:
            pytest.skip("Please configure ShadowServer to test this library")
        res = ss.reports_schema("scan-snmp")
        assert len(res) == 28
        assert "asn" in res.keys()

    def test_trusted_program(self):
        ss = ShadowServer()
        res = ss.trusted_program("7fe2248de77813ce850053ed0ce8a474")
        assert isinstance(res, dict)
        assert "source" in res

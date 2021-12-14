import pytest

from rivalcfg import usbhid
from rivalcfg import mouse
from rivalcfg.devices import rival3_wireless
from rivalcfg import mouse_settings


class TestDevice(object):
    @pytest.fixture
    def mouse(self):
        settings = mouse_settings.FakeMouseSettings(
            0x1038,
            0xBAAD,
            rival3_wireless.profile,
        )
        return mouse.Mouse(
            usbhid.FakeDevice(),
            rival3_wireless.profile,
            settings,
        )

    @pytest.mark.parametrize(
        "value,expected_hid_report",
        [
            (100, b"\x02\x00\x20\x01\x01\x00\x00"),
            (200, b"\x02\x00\x20\x01\x01\x01\x00"),
            (300, b"\x02\x00\x20\x01\x01\x02\x00"),
            (18000, b"\x02\x00\x20\x01\x01\xD6\x00"),
            ("200,400", b"\x02\x00\x20\x02\x01\x01\x00\x03\x00"),
            (
                "200,400,800,1600",
                b"\x02\x00\x20\x04\x01\x01\x00\x03\x00\x08\x00\x11\x00",
            ),
        ],
    )
    def test_set_sensitivity(self, mouse, value, expected_hid_report):
        mouse.set_sensitivity(value)
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == expected_hid_report

    @pytest.mark.parametrize(
        "value,expected_hid_report",
        [
            (125, b"\x02\x00\x17\x03"),
            (250, b"\x02\x00\x17\x02"),
            (500, b"\x02\x00\x17\x01"),
            (1000, b"\x02\x00\x17\x00"),
        ],
    )
    def test_set_polling_rate(self, mouse, value, expected_hid_report):
        mouse.set_polling_rate(value)
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == expected_hid_report

    def test_save(self, mouse):
        mouse.save()
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == b"\x02\x00\x09"

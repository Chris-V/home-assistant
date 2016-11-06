"""the tests for the Wake on Lan switch platform."""
import unittest

from homeassistant.bootstrap import setup_component
import homeassistant.components.switch as switch
from homeassistant.const import (STATE_OFF, STATE_ON)
from homeassistant.core import callback

from tests.common import get_test_home_assistant, assert_setup_component


class TestWOLSwitch(unittest.TestCase):
    """Test the WOL switch."""

    def setUp(self):
        """Setup things to be run when tests are started."""
        self.hass = get_test_home_assistant()

    def tearDown(self):
        """Stop everything that was started."""
        self.hass.stop()

    def test_turn_off_with_off_action_none(self):
        """Test turn off with no actions"""
        assert setup_component(self.hass, switch.DOMAIN, {
            'switch': {
                'platform': 'wake_on_lan',
                'name': 'test_wol',
                'mac_address': '22:44:66:88:AA:CC',
                'host': '192.168.42.42'
            }
        })

        self.hass.states.set('switch.test_wol', STATE_ON)
        self.hass.block_till_done()

        self.hass.states.set('switch.test_wol', STATE_OFF)
        self.hass.block_till_done()

    def test_turn_off_action(self):
        """Test turn off with an action"""
        assert setup_component(self.hass, switch.DOMAIN, {
            switch.DOMAIN: {
                'platform': 'wake_on_lan',
                'name': 'test_wol',
                'mac_address': '22:44:66:88:AA:CC',
                'host': '192.168.42.42',
                'turn_off': {
                    'service': 'switch.test_turn_off'
                }
            }
        })

        self.hass.states.set('switch.test_wol', STATE_ON)
        self.hass.block_till_done()

        self.hass.states.set('switch.test_wol', STATE_OFF)
        self.hass.block_till_done()

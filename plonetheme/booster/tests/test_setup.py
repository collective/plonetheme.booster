# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.booster.testing import PLONETHEME_BOOSTER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.booster is properly installed."""

    layer = PLONETHEME_BOOSTER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.booster is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.booster'))

    def test_browserlayer(self):
        """Test that IPlonethemeBoosterLayer is registered."""
        from plonetheme.booster.interfaces import (
            IPlonethemeBoosterLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeBoosterLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_BOOSTER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.booster'])

    def test_product_uninstalled(self):
        """Test if plonetheme.booster is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.booster'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeBoosterLayer is removed."""
        from plonetheme.booster.interfaces import IPlonethemeBoosterLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeBoosterLayer, utils.registered_layers())

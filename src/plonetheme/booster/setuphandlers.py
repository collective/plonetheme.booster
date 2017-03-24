# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getUtility
from zope.interface import implementer
from plone import api
from plone.app.theming.interfaces import IThemeSettings
from plone.app.theming.utils import applyTheme
from plone.app.theming.utils import getAvailableThemes
from plone.app.theming.utils import getCurrentTheme
from plone.registry.interfaces import IRegistry
import os

DEFAULT_THEME = u'barceloneta'


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'plonetheme.booster:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    if hasattr(context, 'getSite'):
        if context.readDataFile('plonethemebooster_uninstall.txt') is None:
            return

    registry = getUtility(IRegistry)
    theme_settings = registry.forInterface(IThemeSettings, False)
    current_theme = getCurrentTheme()
    if not current_theme or current_theme == u'plonetheme.booster':
        themes = getAvailableThemes()
        for theme in themes:
            if theme.__name__ == DEFAULT_THEME:
                applyTheme(theme)
                theme_settings.enabled = True
                break

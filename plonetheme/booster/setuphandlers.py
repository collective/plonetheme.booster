# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
import os

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'plonetheme.booster:uninstall',
        ]


def post_install(context):
    """Post install script"""
    if context.readDataFile('plonethemetango_default.txt') is None:
        return
    # Do something during the installation of this package
    portal = api.portal.get()
    _create_content(portal)


def _create_content(portal):
    if not portal.get('slider-images', False):
        slider = api.content.create(
            type='Folder',
            container=portal,
            title=u'Slider',
            id='slider-images'
        )
        for slider_number in range(1, 4):
            slider_name = u'slider-{0}'.format(str(slider_number))
            slider_image = api.content.create(
                type='Image',
                container=slider,
                id=slider_name
            )
            slider_image.image = load_image(slider_number)
        # NOTE: if your plone site is not a vanilla plone
        # you can have different workflows on folders and images
        # or different transitions names so this could fail
        # and you'll need to publish the images as well
        # or do that manually TTW.
        api.content.transition(obj=slider, transition='publish')


def load_image(slider):
    from plone.namedfile.file import NamedBlobImage
    filename = os.path.join(os.path.dirname(__file__), 'theme', 'images',
                            'slide_{0}.jpg'.format(slider))
    return NamedBlobImage(
        data=open(filename, 'r').read(),
        filename=u'slide_{0}.jpg'.format(slider)
    )


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('plonethemetango_uninstall.txt') is None:
        return
        # Do something during the uninstallation of this package

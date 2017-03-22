from Products.Five import BrowserView
from ..interfaces import IPlonethemeBoosterLayer


class IsBoosterActiveView(BrowserView):
    """Checks request for marker interface to determine if this theme
    is active"""

    def __call__(self, *args, **kwargs):
        using_diazo = self.request.get('HTTP_X_THEME_ENABLED', False)
        if using_diazo:
            return IPlonethemeBoosterLayer.providedBy(self.request)
        return False

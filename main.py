from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class LaravelExtension(Extension):

    def __init__(self):
        super(LaravelExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        description = "Type in your query and press Enter..."

        url = "https://laravel.com/docs/"

        if event.get_argument() != None:
            description = url + event.get_argument()

        return RenderResultListAction([
            ExtensionResultItem(
                icon='icons/laravel.svg',
                name='Laravel Search',
                description=description,
                on_enter=OpenUrlAction(url + (event.get_argument() or ''))
            )
        ])

if __name__ == '__main__':
    LaravelExtension().run()
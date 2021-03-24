from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
import logging

# create an instance of logger at a module level
logger = logging.getLogger(__name__)

try:
    from algoliasearch.search_client import SearchClient
except ImportError:
    import subprocess
    import sys
    import os

    subprocess.call([sys.executable, '-m', 'pip', 'install', '--user', '-r',
                     os.path.join(os.path.dirname(__file__), 'requirements.txt')])

    from algoliasearch.search_client import SearchClient


def get_subtitle(hit):
    if hit["h4"] is not None:
        return hit["h4"]

    if hit["h3"] is not None:
        return hit["h3"]

    if hit["h2"] is not None:
        return hit["h2"]

    return ''


class LaravelExtension(Extension):

    def __init__(self):
        super(LaravelExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        agolia = SearchClient.create("8BB87I11DE", "8e1d446d61fce359f69cd7c8b86a50de")
        self.index = agolia.init_index("docs")


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        description = "Type in your query and press Enter..."

        url = "https://laravel.com/docs/"
        extension_results = []
        if event.get_argument() is not None:
            results = extension.index.search(
                event.get_argument(), {"tagFilters": "master", "hitsPerPage": 5}
            )

            for hit in results["hits"]:
                extension_results.append(ExtensionResultItem(
                    icon='icons/laravel.svg',
                    name=hit["h1"],
                    description=get_subtitle(hit),
                    on_enter=OpenUrlAction(url + hit["link"])
                ))
        if len(extension_results) == 0:
            extension_results.append(ExtensionResultItem(
                icon='icons/laravel.svg',
                name="Search Laravel docs",
                description=description,
                on_enter=OpenUrlAction(url)
            ))

        return RenderResultListAction(extension_results)


if __name__ == '__main__':
    LaravelExtension().run()

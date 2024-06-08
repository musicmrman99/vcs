from core.exceptions import VCSException

class Command:
    @staticmethod
    def context_type():
        return 'command'

    @staticmethod
    def can_be_root():
        return True

    def on_declare_item(self, contexts, item, *_, **__):
        item['tags'].add('command')

    def on_exit_manifest(self, items, item_sets, *_, **__):
        # Verify that required contexts were declared for all commands
        for item in items.values():
            if 'command' in item['tags'] and (
                'tool' not in item or
                'command' not in item
            ):
                raise VCSException(
                    "@tool context requires a command type to be declared for"
                    f" item '{item['ref']}'"
                )

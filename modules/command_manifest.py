from argparse import Namespace
from modules.manifest_modules import (
    # Generic
    tags,

    # Tools and Commands
    command,
    tool,
    query,
    subjects,
    primary_subject
)

class CommandManifestModule:

    # Lifecycle
    # --------------------

    def dependencies(self):
        return ['manifest']

    def configure(self, *, mod: Namespace, **_):
        mod.manifest.add_context_modules(
            tags.Tags,

            command.Command,
            tool.Tool,
            query.Query,
            subjects.Subjects,
            primary_subject.PrimarySubject
        )

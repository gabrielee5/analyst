"""Custom markdown extensions and helpers for report rendering."""

from markdown import Extension
from markdown.preprocessors import Preprocessor
import re


class CalloutPreprocessor(Preprocessor):
    """Convert !!! type "title" blocks into styled HTML admonitions."""

    PATTERN = re.compile(
        r'^!!! (\w+)(?: "([^"]*)")?\s*\n((?:    .+\n?)+)',
        re.MULTILINE,
    )

    ICONS = {}

    def run(self, lines):
        text = "\n".join(lines)
        while self.PATTERN.search(text):
            text = self.PATTERN.sub(self._replace, text)
        return text.split("\n")

    def _replace(self, match):
        admonition_type = match.group(1).lower()
        title = match.group(2) or admonition_type.title()
        body = "\n".join(line[4:] for line in match.group(3).split("\n") if line)
        return (
            f'<div class="admonition {admonition_type}">\n'
            f'<p class="admonition-title">{title}</p>\n'
            f"<p>{body}</p>\n"
            f"</div>\n"
        )


class CalloutExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(CalloutPreprocessor(md), "callout", 105)


def make_extensions():
    """Return the standard list of markdown extensions for report rendering."""
    return [
        "tables",
        "footnotes",
        "fenced_code",
        "codehilite",
        "toc",
        "meta",
        "admonition",
        "attr_list",
        "md_in_html",
        CalloutExtension(),
    ]


def extension_configs():
    """Return configuration for markdown extensions."""
    return {
        "codehilite": {
            "css_class": "highlight",
            "guess_lang": False,
        },
        "toc": {
            "permalink": False,
            "toc_depth": "2-3",
        },
        "footnotes": {
            "BACKLINK_TEXT": "&#8617;",
        },
    }

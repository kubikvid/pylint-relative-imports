# coding: utf-8
from astroid import ImportFrom
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

from pylint_relative_imports.utils import is_relative


class RelativeImportChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'relative-import-from-root'
    priority = -1
    msgs = {
        'C0001': (
            'Unacceptable relative import from another package',
            'relative-import-from-root',
            'Consider using absolute import',
        ),
    }

    def visit_importfrom(self, node: ImportFrom):
        if not is_relative(node):
            return
        self.add_message(
            'C0001',
            line=node.lineno,
            node=node,
            col_offset=node.col_offset,
        )


def register(linter):
    linter.register_checker(RelativeImportChecker(linter))

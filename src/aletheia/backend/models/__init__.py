"""Import all model modules so SQLAlchemy sees every mapped class once.

This is *the* canonical pattern for multi‑file declarative projects.
"""
from importlib import import_module
from pathlib import Path
from pkgutil import walk_packages

_pkg_path = Path(__file__).resolve().parent
_pkg_prefix = __name__ + "."

for _module in walk_packages([str(_pkg_path)], prefix=_pkg_prefix):
    import_module(_module.name)



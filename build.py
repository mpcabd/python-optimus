from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools.extension import Extension
from pathlib import Path

com_args = ["-std=c99", "-O3", "-fopenmp", "-W"]
link_args = ["-fopenmp"]

extensions = [
    Extension(
        "optimus_id.__init__",
        [str(Path("optimus_id") / "__init__.py")],
        extra_compile_args=com_args,
        extra_link_args=link_args,
    ),
    Extension(
        "optimus_id.optimus",
        [str(Path("optimus_id") / "optimus.pyx")],
        extra_compile_args=com_args,
        extra_link_args=link_args,
    ),
]


class BuildExt(build_ext):
    def build_extensions(self):
        try:
            super().build_extensions()
        except Exception:
            pass


def build(setup_kwargs):
    setup_kwargs.update(
        dict(
            cmdclass=dict(build_ext=BuildExt),
            ext_modules=cythonize(extensions, language_level=3),
            zip_safe=False,
        )
    )

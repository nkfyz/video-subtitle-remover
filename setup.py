from typing import List
from setuptools import find_packages, setup


def fetch_requirements(paths) -> List[str]:
    """
    This function reads the requirements file.

    Args:
        path (str): the path to the requirements file.

    Returns:
        The lines in the requirements file.
    """
    if not isinstance(paths, list):
        paths = [paths]
    requirements = []
    for path in paths:
        with open(path, "r") as fd:
            requirements += [r.strip() for r in fd.readlines()]
    return requirements


setup(
    name="watermark_remover",
    version="0.1.0",
    description="a watermark remover for videos generated from open-sora-serving.",
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=fetch_requirements("requirements.txt"),
    package_data={
        'watermark_remover.backend.lib': ['libstdc++.so.6'],  # 包含 .so.6 文件
    },
    include_package_data=True,  # 确保安装时包含包数据
)
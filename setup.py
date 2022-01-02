import os
from datetime import datetime
from setuptools import setup, find_namespace_packages
from setup_helpers import get_requirements

PATH_ROOT = os.path.dirname(__file__)
REQUIREMENTS = "requirements.txt"

# PACKAGE INFO - 아래 내용은 반드시 수정할 것!
NAME = "clutter"
AUTHOR = "Woojin cho"
AUTHOR_EMAIL = "woojin.cho@gsenc.com"
DESCRIPTION = ""
KEYWORDS = ["aws", "secrets"]

# REQUIRES - 수정하지 않아도 됨. Python 3.8 이상 권장!
# (NOTE)
#  - git tag와 package version을 일원화하기 위해 'setuptools-git-versioning' 패키지를 사용
#    https://pypi.org/project/setuptools-git-versioning/
VERSION_CONFIG = {
    "starting_version": f"{datetime.now().strftime('%Y.%m.0')}",  # tag가 하나도 없을 경우 사용하는 버전
    "template": "{tag}",  # 가장 최근의 tag를 기준으로 버저닝
}
SETUP_REQUIRES = ["setuptools-git-versioning"]
INSTALL_REQUIRES = get_requirements(REQUIREMENTS)
PACKAGES = find_namespace_packages()  #
ZIP_SAFE = False
PYTHON_REQUIRES = ">=3.8"
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]

# PYPI - PYPI 등록은 할 수 없습니다. 추후 사내 Registry가 생긴다면 그곳에 등록.
URL = ""
DOWNLOAD_URL = ""

# CLI - CLI 등록은 여기에
ENTRY_POINTS = {
    "console_scripts": [],
}

# SETUP
setup(
    name=NAME,
    version_config=VERSION_CONFIG,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
    entry_points=ENTRY_POINTS,
    keywords=KEYWORDS,
    python_requires=PYTHON_REQUIRES,
    zip_safe=ZIP_SAFE,
    classifiers=CLASSIFIERS,
)

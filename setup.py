import re
import ast
import glob
import os

import setuptools


_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("govuk_frontend_jinja/__init__.py", "rb") as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1)))

with open("README.md", "r") as fh:
    long_description = fh.read()


components = []
directories = glob.glob("govuk_frontend_jinja/**/**/*.html", recursive=True)
for directory in directories:
    components.append(os.path.relpath(os.path.dirname(directory), "govuk_frontend_jinja") + "/*.html")

setuptools.setup(
    name="ccs-govuk-frontend-jinja",
    version=version,
    author="CCS",
    description="GOV.UK Frontend Jinja Macros",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tim-s-ccs/govuk-frontend-jinja",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={"govuk_frontend_jinja": components},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.8",
    install_requires=["jinja2!=3.0.0,!=3.0.1"],
)

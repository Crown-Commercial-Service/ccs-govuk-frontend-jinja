# CCS GOV.UK Frontend Jinja Macros

[![PyPI version](https://badge.fury.io/py/ccs-govuk-frontend-jinja.svg)](https://pypi.org/project/ccs-govuk-frontend-jinja/)
![govuk-frontend 5.4.0](https://img.shields.io/badge/govuk--frontend%20version-5.4.0-005EA5?logo=gov.uk&style=flat)
[![Python package](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/actions/workflows/python-package.yml/badge.svg)](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/actions/workflows/python-package.yml)

**This is a fork of [GOV.UK Frontend Jinja Macros](https://github.com/LandRegistry/govuk-frontend-jinja) which has not been updated beyond GOV.UK Frontend v5.1. This is for use in the Digital Marketplace until it starts to get updated again.**

**GOV.UK Frontend Jinja is a [community tool](https://design-system.service.gov.uk/community/resources-and-tools/) of the [GOV.UK Design System](https://design-system.service.gov.uk/). The Design System team is not responsible for it and cannot support you with using it. Contact the [maintainers](#contributors) directly if you need [help](#support) or you want to request a feature.**

This repository provides a complete set of [Jinja](https://jinja.palletsprojects.com/) macros that are kept up-to-date and 100% compliant with the original [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) Nunjucks macros. Porting is intentionally manual rather than automated to make updates simpler than maintaining an automated conversion routine. A comprehensive test suite ensures compliance against the latest, and every subsequent, GOV.UK Frontend release.


## Compatibility

The following table shows the version of CCS GOV.UK Frontend Jinja that you should use for your targeted version of GOV.UK Frontend:

| CCS GOV.UK Frontend Jinja Version | Target GOV.UK Frontend Version |
| ----------------------------- | ------------------------------ |
| [1.7.0](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.7.0) | [5.11.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.11.0) |
| [1.6.0](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.6.0) | [5.10.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.10.0) |
| [1.5.0](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.5.0) | [5.9.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.9.0) |
| [1.3.0](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.3.0) | [5.7.1](https://github.com/alphagov/govuk-frontend/releases/tag/v5.7.1) |
| [1.2.2](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.2.2) | [5.5.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.5.0) |
| [1.2.1](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.2.1) | [5.4.1](https://github.com/alphagov/govuk-frontend/releases/tag/v5.4.1) |
| [1.2.0](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.2.0) | [5.4.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.4.0) |
| [1.1.0](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.1.0) | [5.4.0](https://github.com/alphagov/govuk-frontend/releases/tag/v5.4.0) |
| [1.0.0](https://github.com/Crown-Commercial-Service/ccs-govuk-frontend-jinja/releases/tag/1.0.0) | [5.3.1](https://github.com/alphagov/govuk-frontend/releases/tag/v5.3.1) |

Any other versions of GOV.UK Frontend not shown above _may_ still be compatible, but have not been specifically tested and verified.

Use [GOV.UK Frontend Jinja Macros](https://github.com/LandRegistry/govuk-frontend-jinja) for older versions of GOV.UK Frontend

## How to use

After running `pip install ccs-govuk-frontend-jinja`, ensure that you tell Jinja where to load the templates from using the `PackageLoader` as follows:

```python
from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)

app.jinja_loader = ChoiceLoader(
    [
        PackageLoader("app"),
        PrefixLoader({"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}),
    ]
)
```

### Calling a Macro in your template

To use a component in your project templates you must import and call the component macro and pass the relevant options, for example:

```html
{%- from 'govuk_frontend_jinja/components/button/macro.html' import govukButton -%}

{{ govukButton({
  'text': "Save and continue"
}) }}
```

The options available to each component macro can be found in the original [GOV.UK Design System Components](https://design-system.service.gov.uk/components/) documentation. Since this project is a like-for-like port, the only difference between the Nunjucks examples and their Jinja equivalents is having to quote key names, e.g. `'text'` instead of `text`.

## Running the tests

The tests are run in a GitHub actions pipeline and you can run them locally with `pytest`.

You will need to download the GOV.UK Frontend package via npm with:

```bash
npm i
```

You can install the requirements for your chosen version of Python with:

```bash
pip install -r requirements-test-<YOUR_PYTHON_VERSION>.txt
```

You can then run the tests with:

```bash
pytest
```

The tests compare the HTML for each component fixture, which are within the GOV.UK Frontend package, with HTML generated by the Jinja macros.

## Versioning

Releases of this project follow [semantic versioning](http://semver.org/), ie
> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> - MAJOR version when you make incompatible API changes,
> - MINOR version when you add functionality in a backwards-compatible manner, and
> - PATCH version when you make backwards-compatible bug fixes.

To make a new version:
- update the version in the `digitalmarketplace_frontend_jinja/__init__.py` file
- if you are making a major change, also update the change log;

When the pull request is merged a GitHub Action will tag the new version.

## Pre-commit hooks

This project has a [pre-commit hook][pre-commit hook] to do some general file checks and check the `pyproject.toml`.
Follow the [Quick start][pre-commit quick start] to see how to set this up in your local checkout of this project.

## Licence

Unless stated otherwise, the codebase is released under [the MIT License][mit].
This covers both the codebase and any sample code in the documentation.

The documentation is [&copy; Crown copyright][copyright] and available under the terms
of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

[pre-commit hook]: https://pre-commit.com/
[pre-commit quick start]: https://pre-commit.com/#quick-start

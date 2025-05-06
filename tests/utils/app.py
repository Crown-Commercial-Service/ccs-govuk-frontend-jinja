import os

from typing import Any

from flask import Flask, render_template_string, request, Blueprint
from jinja2 import ChoiceLoader, FileSystemLoader, PrefixLoader


def create_app():
    app = Flask(__name__)

    app.jinja_loader = ChoiceLoader(
        [
            PrefixLoader(
                {
                    "govuk_frontend_jinja": FileSystemLoader(
                        searchpath=os.path.join(
                            os.path.dirname(__file__),
                            "../../govuk_frontend_jinja/templates"
                        )
                    )
                }
            )
        ]
    )
    app.jinja_env.globals["govukRebrand"] = False

    main = Blueprint('main', __name__)

    app.register_blueprint(main)

    @app.post("/template")
    def template() -> Any:
        data: Any = request.json

        # Construct a page template which can override any of the blocks if they are specified
        # This doesn't need to be inline - it could be it's own file
        template = """
            {% extends "govuk_frontend_jinja/template.html" %}
            {% block pageTitle %}{% if pageTitle %}{{ pageTitle }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block headIcons %}{% if headIcons %}{{ headIcons }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block head %}{% if head %}{{ head }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block bodyStart %}{% if bodyStart %}{{ bodyStart }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block skipLink %}{% if skipLink %}{{ skipLink }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block header %}{% if header %}{{ header }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block main %}{% if main %}{{ main }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block beforeContent %}{% if beforeContent %}{{ beforeContent }}{% else %}{{ super() }}{% endif %}{% endblock %} # noqa: E501
            {% block content %}{% if content %}{{ content }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block footer %}{% if footer %}{{ footer }}{% else %}{{ super() }}{% endif %}{% endblock %}
            {% block bodyEnd %}{% if bodyEnd %}{{ bodyEnd }}{% else %}{{ super() }}{% endif %}{% endblock %}
        """

        # Render the full html template
        return render_template_string(template, **data)

    @app.post("/component/<string:component>")
    def component(component: str) -> Any:
        data: Any = request.get_json()
        # Render the component using the data provided
        # component is the hyphenated component name e.g. character-count
        # data['macro_name'] is the camelcased name e.g. CharacterCount
        # data['params] are the params that will be passed to the macro
        # Returns an html response that is just the template in question - no wrapping <html>, <body> elements etc
        return render_template_string(
            f"""
            {{% from "govuk_frontend_jinja/components/{component}/macro.html" import govuk{data['macro_name']} %}}
            {{{{ govuk{data['macro_name']}({data["params"]}) }}}}
            """
        )

    return app

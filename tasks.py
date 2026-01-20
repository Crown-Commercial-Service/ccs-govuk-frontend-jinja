from invoke import task

from dmdevtools.invoke_tasks import library_tasks as ns
from dmdevtools.invoke_tasks import npm_install


@task(ns['virtualenv'], ns['requirements_dev'])
def test_mypy(c):
    c.run('mypy tests/utils/')


ns.add_task(npm_install)
ns.add_task(test_mypy)
ns['test'].pre.insert(-2, npm_install)
ns['test'].pre.insert(-1, test_mypy)

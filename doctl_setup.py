from jinja2 import Environment, FileSystemLoader
import secrets
import argparse


arguments = argparse.ArgumentParser(
    description="Basic setup for the DigitalOcean's app.yaml"
)
arguments.add_argument(
    "-l", "--login", dest="DJANGO_ADMIN_LOGIN", help="Set the Django superuser login"
)
arguments.add_argument(
    "-p",
    "--password",
    dest="DJANGO_ADMIN_PASSWORD",
    help="Set the Django superuser password",
)
arguments.add_argument(
    "-e", "--email", dest="DJANGO_ADMIN_EMAIL", help="Set the Django superuser email"
)
parsed_args = arguments.parse_args()

app_vars = [
    {
        "DJANGO_ADMIN_LOGIN": parsed_args.DJANGO_ADMIN_LOGIN
        if parsed_args.DJANGO_ADMIN_LOGIN is not None
        else "admin",
        "DJANGO_ADMIN_PASSWORD": parsed_args.DJANGO_ADMIN_PASSWORD
        if parsed_args.DJANGO_ADMIN_PASSWORD is not None
        else "applepie94",
        "DJANGO_ADMIN_EMAIL": parsed_args.DJANGO_ADMIN_EMAIL
        if parsed_args.DJANGO_ADMIN_PASSWORD is not None
        else "admin@somebluelake.fr",
        "SECRET_KEY": f"{secrets.token_hex()}",
    }
]

environment = Environment(loader=FileSystemLoader(".do/"))
template = environment.get_template("app.j2")
output_filename = ".do/app.yaml"

content = template.render(app_vars[0])
with open(output_filename, "w") as fd:
    fd.write(content)

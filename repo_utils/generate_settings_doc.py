import os
from django.utils.translation import gettext_lazy
from django_twilio_2fa.app_settings import conf, Constant

os.environ["DJANGO_SETTINGS_MODULE"] = "test_app.settings"

filename = "docs/settings.md"

with open(filename, "w") as fh:
    fh.write("# Available Settings\n\n")

    settings = []

    for setting_name in dir(conf):
        if setting_name.startswith("__"):
            continue

        setting = getattr(conf, setting_name)

        if isinstance(setting, Constant):
            continue

        settings.append((
            setting.key, setting
        ))

    settings.sort(key=lambda n: n[0])

    for setting_name, setting in settings:
        fh.write(f"### `{setting.key}`\n")

        if setting.must_be_callable:
            fh.write("_This setting must be a callable._\n")

        fh.write(f"\n{setting.description}\n\n")

        if setting.cb_kwargs_required:
            fh.write("\nIf callable, the following kwargs are sent:\n")
            for kwarg in setting.cb_kwargs_required:
                fh.write(f" * `{kwarg}`\n")

        fh.write("\n\n")

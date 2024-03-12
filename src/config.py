import pathlib
import sys
import yaml


def root_path():
    """
    Path to configuration root path
    """
    root = pathlib.Path("/etc", "ireport")
    if sys.platform == "windows":
        root = pathlib.Path("C:\\ireport")

    return root


def conf_path():
    """
    Path to the configuration file
    """
    return root_path() / "conf.yml"


def template_path():
    """
    Path to the template file
    """
    return root_path() / "template.jinja"


def parse_conf():
    """
    Parse yaml config file
    """
    conf_file = conf_path()

    if not conf_file.is_file():
        print(f"Config file {conf_file} does not exist")
        sys.exit(1)

    data = {}
    with open(conf_file, "r") as yaml_conf:
        data = yaml.safe_load(yaml_conf)
    return data

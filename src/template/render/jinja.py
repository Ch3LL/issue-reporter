from jinja2 import Environment, FileSystemLoader
import config

class Render:
    def __init__(self, opts):
        self.template = config.template_path()

    def render(self, data=None):
        """
        Render jinja template file
        """
        environment = Environment(loader=FileSystemLoader(self.template.parent))
        template = environment.get_template(self.template.name)
        content = template.render(data)
        print(content)

import config
import importlib

def generate_report():
    opts = config.parse_conf()
    backend = opts.get("backend", "jira")
    render = opts.get("render", "jinja")
    backend_import = importlib.import_module(f"backend.{backend}.issues")
    issues = backend_import.Issues(opts).search_issues()
    render_import = importlib.import_module(f"template.render.{render}")
    template = render_import.Render(opts)
    template.render(data=issues)

if __name__ == "__main__":
    generate_report()

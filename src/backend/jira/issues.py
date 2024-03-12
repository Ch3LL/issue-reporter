import backend.jira.auth


class Issues(backend.jira.auth.Auth):
    def __init__(self, opts):
        super().__init__(opts)
        self.opts = opts
        self.fields = self.opts.get("fields")

    def search_issues(self):
        issues = {"issues": {}}
        report = ""
        _filter = self.opts["jira"]["filter"]
        get_filter = self.jira.search_issues(jql_str=_filter, fields="comment")
        for get_issue in get_filter:
            issue = self.jira.issue(get_issue.key)
            issue_key = get_issue.key
            issues["issues"][issue_key] = {}
            issues["issues"][issue_key]["title"] = issue.fields.summary
            issues["issues"][issue_key]["estimate"] = issue.fields.timeestimate
            comment = issue.raw['fields']['comment']["comments"]
            issues["issues"][issue_key]["url"] =  issue.raw['self']
            if comment:
                issues["issues"][issue_key]["comment"] = comment[0]['body']
        return issues

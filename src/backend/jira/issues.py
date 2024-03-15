import backend.jira.auth
import time
import utils.time_estimate


class Issues(backend.jira.auth.Auth):
    def __init__(self, opts):
        super().__init__(opts)
        self.opts = opts
        self.fields = self.opts.get("fields")

    def parse_comments(self, comments):
        """
        Function to parse all comments. If comment_filter is
        set only return that comment. If comment_filter is not
        set return latest comment
        """
        exists = False
        for comment in comments:
            body = comment["body"]
            comment_filter = self.opts["jira"]["comment_filter"]
            if comment_filter:
                exists = True
                if body.startswith(comment_filter):
                    body = body.replace(comment_filter, "")
                    return body
        if exists:
            # comment_filter is set but couldn't find it in
            # comments. Returning None.
            return None
        return body


    def search_issues(self):
        issues = {"issues": {}}
        report = ""
        _filter = self.opts["jira"]["filter"]
        get_filter = self.jira.search_issues(jql_str=_filter, fields="comment")
        for get_issue in get_filter:
            issue = self.jira.issue(get_issue.key)
            issue_key = get_issue.key
            issues["issues"][issue_key] = {}
            issues["issues"][issue_key]["key"] = issue_key
            issues["issues"][issue_key]["title"] = issue.fields.summary
            issues["issues"][issue_key]["status"] = issue.fields.status.name
            estimate = None
            time_estimate = issue.fields.timeestimate
            if time_estimate:
                estimate = utils.time_estimate.convert_estimate(time_estimate)

            issues["issues"][issue_key]["estimate"] = estimate

            issues["issues"][issue_key]["url"] =  issue.raw['self']

            # comments
            comments = issue.raw['fields']['comment']["comments"]
            if comments:
                issues["issues"][issue_key]["comment"] = self.parse_comments(comments)

            # custom fields
            custom_fields = self.opts["jira"].get("custom_fields")
            if custom_fields:
                for field in custom_fields:
                    issues["issues"][issue_key][field] = issue.raw["fields"][field]

        return issues

from jira import JIRA


class Auth():
    def __init__(self, opts):
        self.server = opts["jira"]["server"]
        self.user = opts["jira"]["auth"]["user"]
        self.passwd = opts["jira"]["auth"]["passwd"]
        self.jira = JIRA(server=self.server, basic_auth=(self.user, self.passwd))

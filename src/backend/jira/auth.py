from jira import JIRA


class Auth():
    def __init__(self, opts):
        default_auth = "token_auth"
        validate_auths = {"basic": "basic_auth", "token": default_auth}
        self.server = opts["jira"]["server"]
        self.user = opts["jira"]["auth"]["user"]
        self.passwd = opts["jira"]["auth"]["passwd"]
        self.auth_type = opts["jira"]["auth"].get("auth_type")
        auth_type = validate_auths.get(self.auth_type, default_auth)
        if auth_type == default_auth:
            kwargs = {auth_type: (self.passwd)}
        elif auth_type == "basic_auth":
            kwargs = {auth_type: (self.user, self.passwd)}
        self.jira = JIRA(server=self.server, **kwargs)

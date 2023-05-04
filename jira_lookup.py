import re
import webbrowser

import sublime_plugin

TICKET_REGEX = re.compile(r"\b[A-Z]+\-\d+\b")


class JiraLookup(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        line_region = self.view.line(region)
        line_content = self.view.substr(line_region)

        # Load JIRA URL from .sublime-project file
        jira_url = self.view.window().project_data().get("settings", {}).get("jira_url")

        if matches := TICKET_REGEX.findall(line_content):
            for match in matches:
                webbrowser.open_new_tab(jira_url.format(match))

import sublime
import sublime_plugin


class CopyGitlabLink(sublime_plugin.TextCommand):
    def run(self, edit):
        # Cursor position -> extract line
        cursor = self.view.sel()[0]
        row, _ = self.view.rowcol(cursor.begin())  # 0 based

        # Extract path relative to the project location to the current open file
        project_variables = self.view.window().extract_variables()
        full_path = self.view.file_name()
        folder = project_variables["folder"]
        project_path = full_path.replace(folder, "", 1).lstrip("/")

        # Find gitlab_url in settings.gitlab_url in project's .sublime-project file
        gitlab_url = (
            self.view.window().project_data().get("settings", {}).get("gitlab_url")
        )

        # Format link
        link = gitlab_url.format(project_path, row + 1)
        sublime.set_clipboard(link)

        print(link)

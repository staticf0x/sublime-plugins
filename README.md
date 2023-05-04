# sublime-plugins

This repo contains some helpful Sublime Text plugins and snippets
I use in my daily work.

## Installation

Copy the contents into `~/.config/sublime-text/Packages/User`.

## Configuration

These plugins use per-project config. The plugin config goes inside each
`your-project.sublime-project`, inside the `settings` key.

For example:

```json
{
    "settings": 
    {
        "rulers": 
        [
            80,
            100
        ],
        "gitlab_url": "https://gitlab.com/group/project/-/blob/master/{}#L{}",
        "jira_url": "https://your.jira.instance.com/browser/{}",
    }
}
```

## Jira Lookup

This plugin will find any JIRA ticket number and open the ticket in your web
browser.

### Config

`jira_url` -- `"https://your.jira.instance.com/browser/{}"`

The placeholder is for the ticket number.

## Copy GitLab Link

This plugin copies a sharable link to a GitLab instance to the open file
inside a project.

### Config

`gitlab_url` -- `"https://gitlab.com/group/project/-/blob/master/{}#L{}"`

First placeholder is for the file path, second for the line number.

## Snippets

For the `breakpoint` snippet it's good to set a shortcut like <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>b</kbd>, like this:

```json
{ "keys": ["ctrl+shift+b"], "command": "insert_snippet", "args": {"name": "Packages/User/breakpoint.sublime-snippet"}}
```

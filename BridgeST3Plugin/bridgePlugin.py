import sublime
import sublime_plugin
from . import bridgeRunCommand

class CopyBridgeGithubCommand(sublime_plugin.TextCommand):
	def run(self, edit):
			bridgeRunCommand.run_command(self.view, "copy-bridge-github")

class OpenBridgeGithubCommand(sublime_plugin.TextCommand):
	def run(self, edit):
			bridgeRunCommand.run_command(self.view, "open-bridge-github")

class SearchBridgeGithubCommand(sublime_plugin.TextCommand):
	def run(self, edit):
			bridgeRunCommand.run_command(self.view, "search-bridge-github")

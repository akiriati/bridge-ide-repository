# Bridge (IDE -> Online repository)
While viewing code in our IDE we often want to send a reference to the code, paste it on the specs/tasks, 
or just open it with an online repository. This document explains how we can do it easily using a small bridge snippet

### Open web browser from your IDE:
<p align="center">
  <img src="https://d2mxuefqeaa7sj.cloudfront.net/s_11F3C9DBC2699EB276FC6AB5BDFD86E99A8581A62445EEF6C31D93F93ED0C4A7_1491682386129_githubopen.gif"/>
</p>

### Copy a link to clipboard and share with your friends:
<p align="center">
  <img src="https://d2mxuefqeaa7sj.cloudfront.net/s_11F3C9DBC2699EB276FC6AB5BDFD86E99A8581A62445EEF6C31D93F93ED0C4A7_1491682055517_githubcopy.gif"/>
</p>

### Search with a web browser engine:
<p align="center">
  <img src="https://d2mxuefqeaa7sj.cloudfront.net/s_11F3C9DBC2699EB276FC6AB5BDFD86E99A8581A62445EEF6C31D93F93ED0C4A7_1491682389886_githubsearch.gif"/>
</p>

## Install

- Copy Bridge folder to your preferred location 
    for example: `/Applications/Bridge/` 
- Add execute permissions to your program
    for example: `sudo chmod +x /Applications/Bridge/bridge` 
- Configure the commands you want to use on configure.json:
```

{
  commands: 
  [ 
    {
        "name": a unique name to be used to call the commands,
        "operation": "open"/"copy"/"search",
        "with": "onlineRepositories", 
        "repository": use a name from the onlineRepositories list
    }
 ]
 
  onlineRepositories: 
  [
    {
        "name": a unique name for the repository,
        "one_line": link to the online repository when one line is selected 
                    (can include {file}, {line}),
        "multi_line": link to the online repository when multi line is selected 
                    (can include {file}, {fromline}, {toline})
        "search": link to the online repository's search with the selected text
                   (can include {file}, {text})
    } 
  ]
}
```
- Connect to your IDE:
  - [PyCharm](https://github.com/akiriati/Bridge-Project/#connect-to-pycharm)
  - [Sublime](https://github.com/akiriati/Bridge-Project/#connect-to-sublime)
  - [Command line](https://github.com/akiriati/Bridge-Project/#call-from-command-line)
  

## Connect to PyCharm
### Setup:
- [Install](https://github.com/akiriati/Bridge-Project/#install) Bridge
- Add as PyCharm external tool : on PyCharm go to top menu option Pycharm → Preferences… → Tools → External tools → + → Fill the new external tool:
```    
    Name: Open in Github
    Group: Web Viewers
    Program: /Applications/Bridge/bridge
    Parameters: open-bridge-github -f $FilePathRelativeToProjectRoot$ -l $LineNumber$ -a $SelectionStartLine$ -z $SelectionEndLine$ -t "$SelectedText$"
    Working Directory: You can leave it empty
```

<p align="center">
  <img src="https://d2mxuefqeaa7sj.cloudfront.net/s_98F321F8DFAFC39E8F08BA8ABB1A24A183DE38E5B37BED888C6C7EABAB07F8F0_1491340791745_Screen+Shot+2017-04-05+at+12.19.19+AM.png"/>
</p>


That’s it. You are ready to go! 
On the top menu go to Tools → Web viewers → Open in Github.

### Full configuration:
#### Launch other commands: 

In order to launch different command (e.g: copy to clipboard, open with Github, etc.), add/edit your require command on configure.json (see Install Bridge), and paste its name as the first params on the Parameters list of the external tool

Different ways to invoke bridge:

#### Execute from top menu / toolbar button / right click

a. Execute from top menu: Tools → < group name > → < tool name >
b. Add as toolbar button: Right click the toolbar you want to add the button to → Customize Menus and Toolbars → Browse to the place you want to add the button → Add after.. → External Tools → < group name > → < tool name >
c. Add to right click context menu: Right click the toolbar you want to add the button to → Customize Menus and Toolbars → Main Toolbar → Browse to the place you want to add the button → Add after.. → External Tools → < group name > → < tool name >

#### Add keyboard shortcut:

on the top menu go to PyCharm → Preferences.. → Keymap → External tools → < group name > → < tool name >. 


#### Add button icons

You can use any icons you want, or the ones I used in the icons folder.
Source: Open Externally icon, Link Icon, magnifier

## Connect to Sublime

### Setup:
- [Install](https://github.com/akiriati/Bridge-Project/#install)
- copy the BridgeST3Plugin folder to <Sublime application data path>/Packages (the default is ~/Library/Application Support/Sublime Text 3/Packages/ )
<p align="center">
  <img src="https://d2mxuefqeaa7sj.cloudfront.net/s_D5D266D4E3BBA65BBFF67EA1B1AC1DBB134D5E95090EAC9B94BAEBD4024DF8D8_1491672468895_Screen+Shot+2017-04-08+at+8.25.12+PM_2.png"/>
</p>


- That’s it. Right click on the row, or multiple rows to get the bridge options:

### Full Configuration
#### General properties:

edit configure.py:
working_dirs=["/path/to/working_dir"]
bin_file_path="/Applications/Bridge/bridge"

- working_dirs - as default, bridge takes the root path of your project, but if you open files independently (without project context) , you may want your roots to this list
- bin_file_path - full path to bridge executable

#### Change commands:
Add / edit commands on bridgePlugin.py - following to the bash command params
Call `bridgeRunCommand.run_command(self.view, "open-bridge-github")`  with the command name defined in configure.json (see Install Bridge for how to define commands).

#### Add / edit menu configuration
To create a menu entry you first need to decide where you want it to be viewed. You have three choices that have corresponding file names:

1. Main.sublime-menu
2. Side Bar.sublime-menu
3. Context.sublime-menu (the plugin is supplied with this as default)

Add json entry to your file with the following format*:
```
[
{
    "id" : "copytogithub",
    "caption" : "Copy to Github",
    "command" : "bridge_copy_bridge_github"
},
{
    "id" : "openingithub",
    "caption" : "Open in Github",
    "command" : "bridge_open_bridge_github"
},
{
    "id" : "searchingithub",
    "caption" : "Search in Github",
    "command" : "bridge_search_bridge_github"
},
]
```
### Add keyboard shortcut:
(OSX) “Sublime Text” ->  “Preferences” -> “Key Bindings – Default” *

*For the command you’ll need to strip the “command” string off of the end and take the beginning as the actual name in lower case. Multiple capitals will result in underscore separators between words. (ex: BridgeOpenGithubCommand = bridge_open_github)
See more details [here](https://cnpagency.com/blog/creating-sublime-text-3-plugins-part-1/) on Step 3 – Creating Menus and Key Bindings

## Call from command Line
- [Install Bridge](https://github.com/akiriati/Bridge-Project/#install)
- Call from command line:
`/path/to/bridge <your commande name> -l <LineNumber> -a <multi lines first line> -z <multi lines first line> -t "selected text">` 
for example:
`/Applications/Bridge/bridge open-bridge-github -a 10 -z 12` 


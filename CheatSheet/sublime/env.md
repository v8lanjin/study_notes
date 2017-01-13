### 快捷键设置

Preference -> Key Binding

```
[
	{ "keys": ["j", "j"], "command": "exit_insert_mode",
		"context":
		[
			{ "key": "setting.command_mode", "operand": false },
			{ "key": "setting.is_widget", "operand": false }
		]
	},
	{ "keys": ["enter"], "command": "move", "args": {"by": "characters", "forward": true}, "context":
		[
			{ "key": "following_text", "operator": "regex_contains", "operand": "^[)\\]\\>\\'\\\"]", "match_all": true }
		]
	},
	{ "keys": ["ctrl+shift+f"], "command": "reindent", "args": {"single_line": false}}
]
```

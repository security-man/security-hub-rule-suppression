# aws-security-hub-rule-disable.py
Automatically updates AWS security hub controls across all organizations accounts, using user-supplied list of security hub controls to suppress. Relies on .aws/config file configured with all account profiles necessary. For help in auto-populating .aws/config file with all organisation profiles, please see [auto-update-aws-config](https://github.com/security-man/auto-update-aws-config)

## Installation
Simply copy the python script to your local file system and execute! The 'control-suppression-list.csv' can be modified per your requirements. Simply add or remove any [security hub controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html) as needed to the 'control-suppression-list.csv' file.

To run the script, simply execute it via python:

```bash
python3 aws-security-hub-rule-disable.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3]
(https://choosealicense.com/licenses/gpl-3.0/)
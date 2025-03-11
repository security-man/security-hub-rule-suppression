## Installation
Simply copy the python script to your local file system and execute!  The 'get-controls.py' file will populate a list of configured standards, stored within benchmarks/ directory. The suppression/ directory contains a list of manually created controls files that are to be suppressed for each standard subscription. These can be modified per your requirements. Simply add or remove any [security hub controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html) as needed to the files within benchmarks/ directory.

# aws-security-hub-rule-disable.py
Automatically updates AWS security hub controls across all organizations accounts, using user-supplied list of security hub controls to suppress. Relies on .aws/config file configured with all account profiles necessary. For help in auto-populating .aws/config file with all organisation profiles, please see [auto-update-aws-config](https://github.com/security-man/auto-update-aws-config)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
# Overview

UserAudit is a CLI app which validates a user dataset and optionally validates and merges user input data with it.
_The validations performed are arbitrary and are used as a demonstration of the DataAudit module's generalized auditing capability._

`Usage: UserAudit.py [FILE] [OPTIONS]`

Audits the provided user dataset FILE and reports its validity.

Optionally, when the program is executed with the `-m` or `--merge` arguments (and the required file argument), audits are conducted on both files before an attempt is made to merge the provided user input data with the existing dataset. The net result of each file's audits and the merget attempt are then reported to the user.

The user may declare the following optional arguments:
```
--reserved [filename] | use provided username blacklist (JSON)
--titles [filename]   | use provided job title whitelist (JSON)
--merge [filename]    | attempt to merge provided JSON file with dataset
--purge               | remove invalid entries as they are encountered
-v                    | increase output verbosity
```

This application includes a set of configuration files, which are used by default:
- reserved_usernames.json: JSON array representing example blacklist
- valid_user_titles.json: JSON array representing example whitelist



### Module DataAudit

#### Classes

`DataAudit(*args, **kwargs)`
: 
##### Methods

   `blacklist_check(n, field, blacklist)`
   : 
Returns True if _n[field]_ is a member of _blacklist_

   `close_dataset(dataset_file_object, data=None)`
   : Closes an open dataset file

   `close_list(list_file_object)`
   : Closes an open list file

   `empty_check(n, field)`
   : Returns True if _n[field]_ is an empty string

   `maximum_length_check(n, field, max)`
   : Returns True if _n[field]_ is greater than or equal to _max_

   `minimum_length_check(n, field, min)`
   : Returns True if _n[field]_ is less than or equal to _min_

   `open_dataset(dataset_path, dataset_create_bit=0)`
   : Opens and imports a dataset file

   `open_list(list_path)`
   : Opens and imports a list file

   `precedence_check(n, bef_field, aft_field)`
   : Returns True if _bef_field_ is before _aft_field_

   `regex_check(n, field, reg)`
   : Returns True if _n[field]_ matches _regex pattern_

   `type_check(n, field, typename)`
   : Returns True if all characters in _n[field]_ are of _typename_

   `uniqueness_check(n, field, dataset)`
   : Returns True if _n[field]_ is not found within _dataset_

   `whitelist_check(n, field, whitelist)`
   : Returns true if _n[field]_ is a member of _whitelist_


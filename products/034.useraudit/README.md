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



Module DataAudit
================

Classes
-------

`DataAudit(*args, **kwargs)`
:   

    ### Methods

    `blacklist_check(n, field, blacklist)`
    :

    `close_dataset(dataset_file_object, data=None)`
    :

    `close_list(list_file_object)`
    :

    `empty_check(n, field)`
    :

    `maximum_length_check(n, field, max)`
    :

    `minimum_length_check(n, field, min)`
    :

    `open_dataset(dataset_path, dataset_create_bit=0)`
    :

    `open_list(list_path)`
    :

    `precedence_check(n, bef_field, aft_field)`
    :

    `regex_check(n, field, reg)`
    :

    `type_check(n, field, typename)`
    :

    `uniqueness_check(n, field, dataset)`
    :

    `whitelist_check(n, field, whitelist)`
    :



Module UserAudit
================

Classes
-------

`UserAudit(*args, **kwargs)`
:   

    ### Static methods

    `compile_audits(params, phase)`
    :

    `process_audit_result(failset)`
    :

    `report_audit_result()`
    :

    `run_audit(params, phase)`
    :

    ### Methods

    `authorized_date_must_be_earlier_than_last_authenticated_date(self)`
    :

    `authorized_date_must_be_earlier_than_released_date(self)`
    :

    `email_address_must_be_valid(self)`
    :

    `email_and_usernames_must_be_unique(self)`
    :

    `job_title_must_exist_in_whitelist(self)`
    :

    `last_authenticated_date_must_be_earlier_than_released_date(self)`
    :

    `name_and_email_fields_required(self)`
    :

    `phone_number_must_be_valid(self)`
    :

    `username_length_must_be_within_bounds(self)`
    :

    `username_must_not_contain_reserved_words(self)`
    :

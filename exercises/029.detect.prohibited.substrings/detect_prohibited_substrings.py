windows_reserved_filenames = ['com1', 'com2', 'com3', 'com4', 'com5', 'com6',
                              'com7', 'com8', 'com9', 'lpt1', 'lpt2', 'lpt3',
                              'lpt4', 'lpt5', 'lpt6', 'lpt7', 'lpt8', 'lpt9',
                              'con', 'nul', 'prn']
windows_filename_blacklist = ['/', '?', '<', '>', '\\', ':', '*', '|', '"']
osx_filename_blacklist = [':']
url_filename_blacklist = [':', '/', '#', '?', '&', '@', '%', '+', '~']


def substring_check(input_name, blacklist):
    invalid_list = []
    is_invalid = False
    for item in blacklist:
        if item in input_name:
            invalid_list.append(item)
            is_invalid = True
    return (is_invalid, invalid_list)


def reserved_name_check(input_name, blacklist, case_sensitive=False):
    if not case_sensitive:
        input_name = input_name.lower()
    for item in blacklist:
        if item == input_name:
            return True, item
    return False


input_str = str(input('Enter a string to check: '))
print(f'Input contains Windows-prohibited characters: '
      f'{substring_check(input_str, windows_filename_blacklist)}')
print(f'Input is a Windows-reserved name: '
      f'{reserved_name_check(input_str, windows_reserved_filenames)}')

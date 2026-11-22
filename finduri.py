import winreg

def search_url_protocol():
    # Open the HKEY_CLASSES_ROOT registry hive
    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, '') as root_key:
        try:
            i = 0
            while True:
                # Enumerate all subkeys under HKEY_CLASSES_ROOT
                subkey_name = winreg.EnumKey(root_key, i)
                subkey_path = f"{subkey_name}"

                try:
                    # Open the subkey
                    with winreg.OpenKey(root_key, subkey_path) as subkey:
                        try:
                            # Check if the subkey has a value named 'URL Protocol'
                            url_protocol_value, _ = winreg.QueryValueEx(subkey, 'URL Protocol')
                            if not url_protocol_value or '""' in url_protocol_value:
                                # Open the shell\open\command subkey
                                command_subkey_path = f"{subkey_path}\\shell\\open\\command"
                                with winreg.OpenKey(root_key, command_subkey_path) as command_subkey:
                                    # Get the default value of the command subkey
                                    default_value, _ = winreg.QueryValueEx(command_subkey, '')
                                    print(f"Key: {subkey_path}")
                                    print(f"URL Protocol Value: {url_protocol_value}")
                                    print(f"Default Value: {default_value}")
                                    print()
                        except FileNotFoundError:
                            pass  # The value 'URL Protocol' does not exist in this subkey
                except FileNotFoundError:
                    pass  # The subkey does not exist

                i += 1
        except OSError:
            pass  # No more subkeys to enumerate

if __name__ == "__main__":
    search_url_protocol()
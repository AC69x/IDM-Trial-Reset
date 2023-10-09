import ctypes, winreg, os, shutil

regkeys = [
    (winreg.HKEY_CURRENT_USER, r"Software\DownloadManager"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Internet Download Manager"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Wow6432Node\Internet Download Manager")
]
RK_Delete = [
    r"Software\Classes\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}",
    r"Software\Classes\Wow6432Node\CLSID\{7B8E9164-324D-4A2E-A46D-0165FB2000EC}",
    r"Software\Classes\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}",
    r"Software\Classes\Wow6432Node\CLSID\{6DDF00DB-1234-46EC-8356-27E7B2051192}",
    r"Software\Classes\CLSID\{D5B91409-A8CA-4973-9A0B-59F713D25671}",
    r"Software\Classes\Wow6432Node\CLSID\{D5B91409-A8CA-4973-9A0B-59F713D25671}",
    r"Software\Classes\CLSID\{5ED60779-4DE2-4E07-B862-974CA4FF2E9C}",
    r"Software\Classes\Wow6432Node\CLSID\{5ED60779-4DE2-4E07-B862-974CA4FF2E9C}",
    r"Software\Classes\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}",
    r"Software\Classes\Wow6432Node\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}"
]
licence_datasheet = {"FName": "-","LName": "-","Email": "-","Serial": "-"}

def main():
    if os.path.exists(f"{os.path.join(os.environ['APPDATA'])}\\DMCache"):
        shutil.rmtree(f"{os.path.join(os.environ['APPDATA'])}\\DMCache")
        
    for root_key, sub_key in regkeys:
        with winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_SET_VALUE) as reg_key:
            for licence_name, licence_data in licence_datasheet.items():
                winreg.SetValueEx(reg_key, licence_name, 0, winreg.REG_SZ, licence_data)

    for key_path in RK_Delete:
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
        except FileNotFoundError:
            pass

        try:
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        except FileNotFoundError:
            pass
    ctypes.windll.user32.MessageBoxW(0, "Successfully Patched!", "NoirBird IDM Reset", 0)

if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
        ctypes.windll.user32.MessageBoxW(0, "You need to run this file as administrator!", "NoirBird IDM Reset", 0)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
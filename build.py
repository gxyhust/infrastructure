import traceback

if __name__ == '__main__':
    import shutil
    try:
        shutil.rmtree("./dist/")
        shutil.rmtree("./build/")
    except Exception:
        traceback.print_exc()
    cmd = '''PyInstaller view/MainFrame.py --clean --paths "D:\\pack\\workspace\\Smoke\\Report\\RFCode_workflow\\view" --paths "D:\\pack\\workspace\\Smoke\\Report\\RFCode_workflow" --paths "C:\\Python3\\DLLs" --paths "C:\\Python3\\lib" --paths "C:\\Python3" --paths "C:\\Python3\\lib\\site-packages" --paths "C:\\Python3\\lib\\site-packages\\win32"  --paths "C:\\Python3\\lib\\site-packages\\win32\\lib" --paths "D:\\pack\\workspace\\Smoke\\Report\\RFCode_workflow\\controller\\test_runner\\../../lib"  --i D:\\pack\\workspace\\Smoke\\Report\\RFCode_workflow\\resources\\images\\RFCODE.ico  --hidden-import controller.system_plugin.edit.view --hidden-import  controller.system_plugin.edit.view.ProjectTreeItemEdit --hidden-import controller.system_plugin.edit.view.PyItemEdit --hidden-import controller.system_plugin.edit.view.ResourceItemEdit --hidden-import controller.system_plugin.edit.view.TestcaseItemEdit --hidden-import controller.system_plugin.edit.view.TreeItemEdit --hidden-import controller.system_plugin.edit.view.UserKeywordItemEdit --hidden-import controller.system_plugin.edit.view.SettingsItemEdit --hidden-import controller.system_plugin.edit.view.SuiteVariableItemEdit --hidden-import robot --hidden-import robot.libraries.BuiltIn --hidden-import robot.libraries.Collections --hidden-import robot.libraries.DateTime --hidden-import robot.libraries.Dialogs --hidden-import robot.libraries.Easter --hidden-import robot.libraries.OperatingSystem --hidden-import robot.libraries.Process --hidden-import robot.libraries.Remote --hidden-import robot.libraries.Reserved --hidden-import robot.libraries.Screenshot --hidden-import robot.libraries.String --hidden-import robot.libraries.Telnet --hidden-import robot.libraries.XML --hidden-import robot.run --hidden-import controller.system_plugin.edit.view.SuiteVariableItemEdit --hidden-import controller.system_plugin.edit.view.TestcaseItemEdit --hidden-import controller.system_plugin.edit.view.TreeItemEdit --hidden-import controller.system_plugin.edit.view.UserKeywordItemEdit --hidden-import controller.system_plugin.edit.view.SuiteItemEdit.py --hidden-import controller.system_plugin.edit.view.SettingsItemEdit.py --hidden-import controller.system_plugin.edit.view.ResourceVariableItemEdit --hidden-import controller.system_plugin.edit.view.ResourceItemEdit --hidden-import controller.system_plugin.edit.view.PyItemEdit --hidden-import controller.system_plugin.edit.view.ProjectTreeVariableItemEdit --hidden-import controller.system_plugin.edit.view.ProjectTreeItemEdit --hidden-import controller.system_plugin.edit.view.DirectoryEdit --hidden-import controller.system_plugin.edit.view.BlankEdit --hidden-import controller.system_plugin.edit.parser.ProjectTreeItemParser --hidden-import controller.system_plugin.edit.parser.SuiteItemParser --hidden-import controller.system_plugin.edit.parser.BlankParser --hidden-import controller.system_plugin.edit.parser.ItemParser --hidden-import controller.system_plugin.edit.parser.ItemParserFactory --hidden-import controller.system_plugin.edit.parser.ProjectTreeVariableItemParser --hidden-import controller.system_plugin.edit.parser.PyItemParser --hidden-import controller.system_plugin.edit.parser.ResourceItemParser --hidden-import controller.system_plugin.edit.parser.ResourceVariableItemParser --hidden-import controller.system_plugin.edit.parser.SuiteItemParser --hidden-import requests --hidden-import controller.system_plugin.edit.parser.SuiteVariableItemParser --hidden-import controller.system_plugin.edit.parser.TestcaseItemParser --hidden-import controller.system_plugin.edit.parser.UserKeywordItemParser --hidden-import utility.log.Logger
    '''
    import subprocess
    nowtime = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    build_log = nowtime.stdout.read()
    print(build_log)
    if "系统找不到指定的文件。: './dist/MainFrame/MainFrame.exe' -> './dist/MainFrame/RFCODE.exe'" in str(build_log):
        raise Exception("build error, MainFrame.exe not exist")
    shutil.copytree("./resources", "./dist/MainFrame/resources")
    shutil.copy("./config.ini", "./dist/MainFrame/config.ini")
    shutil.copytree("./pybot", "./dist/MainFrame/pybot")
    shutil.copytree("./plugins", "./dist/MainFrame/plugins")
    shutil.copy("./python-2.7.8.msi", "./dist/MainFrame/python-2.7.8.msi")
    shutil.copy("./robotframework-2.9.2.win32.exe", "./dist/MainFrame/robotframework-2.9.2.win32.exe")
    shutil.move('./dist/MainFrame/MainFrame.exe', "./dist/MainFrame/RFCODE.exe")
    shutil.copytree('./update/tools', "./dist/MainFrame/tools")

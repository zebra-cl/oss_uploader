#define MyAppName "������OSSͼ��"
#define MyAppVersion "1.0"
; ����������������޸�
#define PythonPath "C:\Program Files (x86)\Python37-32"
#define ProgramPath "F:\�ҵ�\����\oss_uploader"


[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{AFC0EBB6-DDDD-4150-98E6-17F3A44FFF6C}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
DisableDirPage=yes
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
; ������ļ���
OutputBaseFilename={#MyAppName}
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Icons]
Name: "{autodesktop}\������OSSͼ��"; Filename: "{app}\pythonw.exe"; Parameters: """{app}\main.py"""

[Files]
Source: "{#PythonPath}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "{#ProgramPath}\aliyun.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#ProgramPath}\*.py"; DestDir: "{app}"; Flags: ignoreversion
; Source: "{#ProgramPath}\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
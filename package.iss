#define MyAppName "阿里云OSS图床"
#define MyAppVersion "1.0"
; 下面两项，请根据情况修改
#define PythonPath "C:\Program Files (x86)\Python37-32"
#define ProgramPath "F:\我的\桌面\oss_uploader"


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
; 输出的文件名
OutputBaseFilename={#MyAppName}
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Icons]
Name: "{autodesktop}\阿里云OSS图床"; Filename: "{app}\pythonw.exe"; Parameters: """{app}\main.py"""

[Files]
Source: "{#PythonPath}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "{#ProgramPath}\aliyun.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#ProgramPath}\*.py"; DestDir: "{app}"; Flags: ignoreversion
; Source: "{#ProgramPath}\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
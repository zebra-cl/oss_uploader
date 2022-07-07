import os
from datetime import datetime
from io import BytesIO

import oss2
import pyperclip
import wx
from PIL import ImageGrab
from wx.adv import TaskBarIcon, TBI_DEFAULT_TYPE

from frames import MainFrame
from models import Config, UploadHistory

# OSS各地域Endpoint    https://help.aliyun.com/document_detail/31837.html
REGIONS = [
    {'region': '华东1（杭州）', 'regionId': 'oss-cn-hangzhou'},
    {'region': '华东2（上海）', 'regionId': 'oss-cn-shanghai'},
    {'region': '华东5（南京本地地域）', 'regionId': 'oss-cn-nanjing'},
    {'region': '华北1（青岛）', 'regionId': 'oss-cn-qingdao'},
    {'region': '华北2（北京）', 'regionId': 'oss-cn-beijing'},
    {'region': '华北 3（张家口）', 'regionId': 'oss-cn-zhangjiakou'},
    {'region': '华北5（呼和浩特）', 'regionId': 'oss-cn-huhehaote'},
    {'region': '华北6（乌兰察布）', 'regionId': 'oss-cn-wulanchabu'},
    {'region': '华南1（深圳）', 'regionId': 'oss-cn-shenzhen'},
    {'region': '华南2（河源）', 'regionId': 'oss-cn-heyuan'},
    {'region': '华南3（广州）', 'regionId': 'oss-cn-guangzhou'},
    {'region': '西南1（成都）', 'regionId': 'oss-cn-chengdu'},
    {'region': '中国（香港）', 'regionId': 'oss-cn-hongkong'},
    {'region': '美国（硅谷）', 'regionId': 'oss-us-west-1'},
    {'region': '美国（弗吉尼亚）', 'regionId': 'oss-us-east-1'},
    {'region': '日本（东京）', 'regionId': 'oss-ap-northeast-1'},
    {'region': '韩国（首尔）', 'regionId': 'oss-ap-northeast-2'},
    {'region': '新加坡', 'regionId': 'oss-ap-southeast-1'},
    {'region': '澳大利亚（悉尼）', 'regionId': 'oss-ap-southeast-2'},
    {'region': '马来西亚（吉隆坡）', 'regionId': 'oss-ap-southeast-3'},
    {'region': '印度尼西亚（雅加达）', 'regionId': 'oss-ap-southeast-5'},
    {'region': '菲律宾（马尼拉）', 'regionId': 'oss-ap-southeast-6'},
    {'region': '泰国（曼谷）', 'regionId': 'oss-ap-southeast-7'},
    {'region': '印度（孟买）', 'regionId': 'oss-ap-south-1'},
    {'region': '德国（法兰克福）', 'regionId': 'oss-eu-central-1'},
    {'region': '英国（伦敦）', 'regionId': 'oss-eu-west-1'},
    {'region': '阿联酋（迪拜）', 'regionId': 'oss-me-east-1'},
]


def get_remote_path(file):
    # 设置远程文件夹路径
    if Config.get_conf('fixpath') == 'False':
        remote_path = str(datetime.now().year) + '/' + str(datetime.now().month).rjust(2, '0') \
                      + '/' + os.path.basename(file)
    else:
        remote_path = Config.get_conf('path') + '/' + os.path.basename(file)
    return remote_path


class MyTaskBarIcon(TaskBarIcon):
    def __init__(self, frame, iconType=TBI_DEFAULT_TYPE):
        super().__init__(iconType)
        self.frame = frame
        self.SetIcon(wx.Icon('./aliyun.png'), tooltip='阿里云OSS图床')

    def CreatePopupMenu(self):
        m_menu_taskbarIcon = wx.Menu()

        # 添加菜单项
        m_menuItem_show_frame = wx.MenuItem(m_menu_taskbarIcon, wx.ID_ANY, u"显示主窗口", wx.EmptyString,
                                            wx.ITEM_NORMAL)
        m_menuItem_copy_last = wx.MenuItem(m_menu_taskbarIcon, wx.ID_ANY, u"复制最新的一条", wx.EmptyString,
                                           wx.ITEM_NORMAL)
        m_menuItem_upload_file = wx.MenuItem(m_menu_taskbarIcon, wx.ID_ANY, u"从文件上传", wx.EmptyString,
                                             wx.ITEM_NORMAL)
        m_menuItem_upload_paste = wx.MenuItem(m_menu_taskbarIcon, wx.ID_ANY, u"从粘贴板上传", wx.EmptyString,
                                              wx.ITEM_NORMAL)
        m_menuItem_quit = wx.MenuItem(m_menu_taskbarIcon, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL)

        m_menu_taskbarIcon.Append(m_menuItem_show_frame)
        m_menu_taskbarIcon.Append(m_menuItem_copy_last)
        m_menu_taskbarIcon.AppendSeparator()
        m_menu_taskbarIcon.Append(m_menuItem_upload_file)
        m_menu_taskbarIcon.Append(m_menuItem_upload_paste)
        m_menu_taskbarIcon.AppendSeparator()
        m_menu_taskbarIcon.Append(m_menuItem_quit)

        # 添加事件
        self.Bind(wx.EVT_MENU, self.evt_show_frame, id=m_menuItem_show_frame.GetId())
        self.Bind(wx.EVT_MENU, self.evt_copy_last, id=m_menuItem_copy_last.GetId())
        self.Bind(wx.EVT_MENU, self.evt_upload_file, id=m_menuItem_upload_file.GetId())
        self.Bind(wx.EVT_MENU, self.evt_upload_paste, id=m_menuItem_upload_paste.GetId())
        self.Bind(wx.EVT_MENU, self.evt_quit, id=m_menuItem_quit.GetId())

        return m_menu_taskbarIcon

    def evt_show_frame(self, event):
        self.frame.Show()

    def evt_copy_last(self, event):
        self.frame.copy_last_history()

    def evt_upload_file(self, event):
        self.frame.evt_m_button_upload_file_OnButtonClick(event)

    def evt_upload_paste(self, event):
        self.frame.evt_m_button_upload_paste_OnButtonClick(event)

    def evt_quit(self, event):
        self.frame.Destroy()
        self.Destroy()


class MyFrame(MainFrame):
    query = None

    def __init__(self, parent):
        super().__init__(parent)

        # 设置窗口图标
        self.SetIcon(wx.Icon('./aliyun.png'))

        # 设置 区域 下拉框
        self.m_comboBox_region.AppendItems([it['region'] for it in REGIONS])

        # 填充配置项
        self.m_radioBox_copyType.Select(int(Config.get_conf('copyType') or '0'))
        self.m_comboBox_region.Value = Config.get_conf('region')
        self.m_textCtrl_accessKeyId.Value = Config.get_conf('accessKeyId')
        self.m_textCtrl_accessKeySecret.Value = Config.get_conf('accessKeySecret')
        self.m_textCtrl_bucket.Value = Config.get_conf('bucket')
        self.m_checkBox_fixpath.Value = Config.get_conf('fixpath') == 'True'
        self.m_textCtrl_path.Value = Config.get_conf('path')

        # 创建托盘
        self.m_taskBarIcon = MyTaskBarIcon(self)

        # 设置表格字段
        self.m_grid_history.SetColLabelValue(0, '文件名')
        self.m_grid_history.SetColSize(0, 165)
        self.m_grid_history.SetColLabelValue(1, '上传日期')
        self.m_grid_history.SetColSize(1, 75)
        self.m_grid_history.SetColLabelValue(2, '删除')
        self.m_grid_history.SetColSize(2, 45)
        self.m_grid_history.SetColLabelValue(3, '复制')
        self.m_grid_history.SetColSize(3, 45)

        # 刷新表格数据
        self.refresh_history_table()

        # 设置 固定路径 的可见性
        self.m_textCtrl_path.Show(self.m_checkBox_fixpath.Value)
        self.m_staticText_path.Show(self.m_checkBox_fixpath.Value)
        self.m_panel_config.Layout()

    def refresh_history_table(self):
        # 刷新表格数据
        self.query = UploadHistory.select().order_by(UploadHistory.create_at.desc())
        if self.m_grid_history.GetNumberRows():
            self.m_grid_history.DeleteRows(numRows=self.m_grid_history.GetNumberRows())
        for index, it in enumerate(self.query):
            self.m_grid_history.AppendRows(1)
            self.m_grid_history.SetCellValue(index, 0, it.file)
            self.m_grid_history.SetCellValue(index, 1, it.create_at.strftime('%Y-%m-%d'))
            self.m_grid_history.SetCellValue(index, 2, '删除')
            self.m_grid_history.SetCellTextColour(index, 2, '#f73131')  # 字体颜色
            self.m_grid_history.SetCellAlignment(index, 2, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)  # 居中
            self.m_grid_history.SetCellValue(index, 3, '复制')
            self.m_grid_history.SetCellTextColour(index, 3, '#2440b3')  # 字体颜色
            self.m_grid_history.SetCellAlignment(index, 3, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)  # 居中

    def evt_OnClose(self, event):
        self.Hide()

    def evt_m_radioBox_copyType_OnRadioBox(self, event):
        # 更改 复制形式
        super().evt_m_radioBox_copyType_OnRadioBox(event)

        Config.set_conf('copyType', self.m_radioBox_copyType.Selection)

    def evt_m_checkBox_fixpath_OnCheckBox(self, event):
        # 点击 使用固定路径 复选框
        super().evt_m_checkBox_fixpath_OnCheckBox(event)

        self.m_textCtrl_path.Show(self.m_checkBox_fixpath.Value)
        self.m_staticText_path.Show(self.m_checkBox_fixpath.Value)
        self.m_panel_config.Layout()

    def evt_m_button_save_OnButtonClick(self, event):
        # 点击保存，储存配置项
        super().evt_m_button_save_OnButtonClick(event)

        for it in REGIONS:
            if self.m_comboBox_region.Value == it['region']:
                Config.set_conf('region', self.m_comboBox_region.Value)
                Config.set_conf('regionId', it['regionId'])
                break

        Config.set_conf('accessKeyId', self.m_textCtrl_accessKeyId.Value)
        Config.set_conf('accessKeySecret', self.m_textCtrl_accessKeySecret.Value)
        Config.set_conf('bucket', self.m_textCtrl_bucket.Value)
        Config.set_conf('fixpath', self.m_checkBox_fixpath.Value)
        if self.m_checkBox_fixpath.Value:
            Config.set_conf('path', self.m_textCtrl_path.Value)
        else:
            Config.set_conf('path', '')

        wx.MessageBox('保存成功', caption='提示')

    def evt_m_button_upload_file_OnButtonClick(self, event):
        # 点击 从文件上传
        super().evt_m_button_upload_file_OnButtonClick(event)

        dlg = wx.FileDialog(self, message="请选择文件", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file = dlg.GetPath()

            auth = oss2.Auth(Config.get_conf('accessKeyId'), Config.get_conf('accessKeySecret'))
            bucket = oss2.Bucket(auth, Config.get_conf('regionId') + '.aliyuncs.com', Config.get_conf('bucket'))

            try:
                resp = bucket.put_object_from_file(get_remote_path(file), file).resp
            except Exception as err:
                wx.MessageBox('上传错误，请检查配置信息。\n' + err.message, caption='提示')
            else:
                # 保存上传记录
                UploadHistory(file=os.path.basename(file), file_url=resp.response.url).save()
                self.m_taskBarIcon.ShowBalloon('提示', '上传成功')
                self.refresh_history_table()

    def evt_m_button_upload_paste_OnButtonClick(self, event):
        # 点击 从粘贴板上传
        super().evt_m_button_upload_paste_OnButtonClick(event)

        im = ImageGrab.grabclipboard()
        if im:
            auth = oss2.Auth(Config.get_conf('accessKeyId'), Config.get_conf('accessKeySecret'))
            bucket = oss2.Bucket(auth, Config.get_conf('regionId') + '.aliyuncs.com', Config.get_conf('bucket'))

            try:
                file = f"paste_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                buffer = BytesIO()
                buffer.name = file
                im.save(buffer)
                buffer.seek(0)
                resp = bucket.put_object(get_remote_path(file), buffer).resp
            except Exception as err:
                wx.MessageBox('上传错误，请检查配置信息。\n' + err.message, caption='提示')
            else:
                # 保存上传记录
                UploadHistory(file=file, file_url=resp.response.url).save()
                self.m_taskBarIcon.ShowBalloon('提示', '上传成功')
                self.refresh_history_table()
        else:
            wx.MessageBox('粘贴板中无图片', caption='提示')

    def evt_m_grid_history_OnGridCellLeftClick(self, event):
        # 右键表格的 删除 或 复制
        super().evt_m_grid_history_OnGridCellLeftClick(event)

        if event.Col == 2:
            # 删除
            self.query[event.Row].delete_instance()
            self.refresh_history_table()
            self.m_taskBarIcon.ShowBalloon('提示', '删除成功')
        elif event.Col == 3:
            # 复制
            if Config.get_conf('copyType') == '0':
                pyperclip.copy(self.query[event.Row].file_url)
            elif Config.get_conf('copyType') == '1':
                pyperclip.copy(f"[{self.query[event.Row].file}]({self.query[event.Row].file_url})")
            else:
                pyperclip.copy(self.query[event.Row].file_url)
            self.m_taskBarIcon.ShowBalloon('提示', '复制成功')

    def copy_last_history(self):
        # 复制最近的一条
        if Config.get_conf('copyType') == '0':
            pyperclip.copy(self.query[0].file_url)
        elif Config.get_conf('copyType') == '1':
            pyperclip.copy(f"[{self.query[0].file}]({self.query[0].file_url})")
        else:
            pyperclip.copy(self.query[0].file_url)
        self.m_taskBarIcon.ShowBalloon('提示', '复制成功')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()

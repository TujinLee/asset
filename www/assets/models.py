# coding=utf-8
# ----------------------------------
# @ 2017/4/6
# @ PC
# ----------------------------------

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import datetime

# Create your models here.


@python_2_unicode_compatible
class Vendor(models.Model):
    name = models.CharField(_('Name'), max_length=20, default='NULL')
    desc = models.CharField(_('Description'), max_length=100, default='Extra info.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Vendors')
        verbose_name_plural = _('Vendors')


@python_2_unicode_compatible
class DeviceType(models.Model):
    tag = models.CharField(_('Tag'), max_length=10, default='NULL')
    cpu = models.CharField(_('CPU'), max_length=20, default='NULL')
    memory = models.CharField(_('Memory'), max_length=20, default='NULL')
    disk_ssd = models.CharField(_('Disk SSD'), max_length=20, default='NULL')
    disk_sas = models.CharField(_('Disk SAS'), max_length=20, default='NULL')
    disk_sata = models.CharField(_('Disk SATA'), max_length=20, default='NULL')
    nic = models.CharField(_('NIC Card'), max_length=20, default='Onboard')
    psu = models.IntegerField(_('PSU'), default=1)
    raid_card = models.CharField(_('RAID Card'), max_length=20, default='NULL')
    desc = models.CharField(_('Description'), max_length=100, default='Extra info.')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _('Device Type')
        verbose_name_plural = _('Device Type')


@python_2_unicode_compatible
class InstanceType(models.Model):
    tag = models.CharField(_('Tag'), max_length=10, default='NULL')
    cpu = models.IntegerField(_('CPU(Core)'), default=1)
    memory = models.IntegerField(_('Memory(GB)'), default=1)
    desc = models.CharField(_('Description'), max_length=100, default='Extra info.')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _('Instance Type')
        verbose_name_plural = _('Instance Type')


@python_2_unicode_compatible
class IDCInfo(models.Model):
    tag = models.CharField(_('Tag'), max_length=10, default='NULL')
    name = models.CharField(_('Name'), max_length=20, default='NULL')
    location = models.CharField(_('Location'), max_length=100, default='Extra info.')
    desc = models.CharField(_('Description'), max_length=100, default='Extra info.')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _('IDC')
        verbose_name_plural = _('IDC')


@python_2_unicode_compatible
class OSType(models.Model):
    tag = models.CharField(_('Tag'), max_length=20, default='NULL')
    desc = models.CharField(_('Description'), max_length=40, default='Extra info.')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _('OS Type')
        verbose_name_plural = _('OS Type')


@python_2_unicode_compatible
class EndUser(models.Model):
    username = models.CharField(_('Username'), max_length=20, default='NULL')
    fullname = models.CharField(_('Fullname'), max_length=20, default='NULL')
    department = models.CharField(_('Department'), max_length=40, default='NULL')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('EndUser')
        verbose_name_plural = _('EndUser')


@python_2_unicode_compatible
class Cluster(models.Model):
    name = models.CharField(_('Name'), max_length=20, default='NULL')
    desc = models.CharField(_('Description'), max_length=40, default='Extra info.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Cluster')
        verbose_name_plural = _('Cluster')


@python_2_unicode_compatible
class BusinessUnit(models.Model):
    name = models.CharField(_('Name'), max_length=20, default='NULL')
    desc = models.CharField(_('Description'), max_length=100, default='Extra info.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('BizUnit')
        verbose_name_plural = _('BizUnit')


@python_2_unicode_compatible
class RuntimeEnvironment(models.Model):
    name = models.CharField(_('Name'), max_length=20, default='NULL')
    desc = models.CharField(_('Description'), max_length=100, default='Extra info.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('RunEnv')
        verbose_name_plural = _('RunEnv')


@python_2_unicode_compatible
class Machine(models.Model):
    hostname = models.CharField(_('Hostname'), max_length=100, unique=True)
    cluster = models.ForeignKey(Cluster, default='1', verbose_name=_('Cluster'))
    #
    os_ip_wan1 = models.GenericIPAddressField(_('IP_WAN1'), default='0.0.0.0')
    os_ip_wan2 = models.GenericIPAddressField(_('IP_WAN2'), default='0.0.0.0')
    os_ip_lan_mgmt = models.GenericIPAddressField(_('IP_LAN_MGMT'))
    os_ip_lan_stor = models.GenericIPAddressField(_('IP_LAN_STOR'), default='0.0.0.0')
    os_ip_lan_biz = models.GenericIPAddressField(_('IP_LAN_BIZ'), default='0.0.0.0')
    os_type = models.ForeignKey(OSType, default='1', verbose_name=_('OS Type'))
    os_user_root = models.CharField(_('Admin'), max_length=20, default='root')
    os_pass_root = models.CharField(_('Password of Admin'), max_length=40, default='NULL')
    os_user_guest = models.CharField(_('Guest'), max_length=20, default='root1')
    os_pass_guest = models.CharField(_('Password of Guest'), max_length=40, default='NULL')
    #
    app_desc = models.CharField(_('App Description'), max_length=40, default='NOT_IN_USE')
    biz_unit = models.ForeignKey(BusinessUnit, default='1', verbose_name=_('BizUnit'))
    run_env = models.ForeignKey(RuntimeEnvironment, default='1', verbose_name=_('RunEnv'))
    operator = models.ForeignKey(EndUser, default='1', verbose_name=_('EndUser'))
    #
    is_monited = models.BooleanField(_('Is Monited?'), default=False)
    is_online = models.BooleanField(_('Is Online?'), default=False)
    is_v_host = models.BooleanField(_('Is Virt Host?'), default=False)
    #
    device_sn = models.CharField(_('SN'), max_length=40, default='NULL')
    vendor = models.ForeignKey(Vendor, default='1', verbose_name=_('Vendor'))
    model = models.ForeignKey(DeviceType, default='1', verbose_name=_('Model'))
    device_ipmi_ip = models.GenericIPAddressField(_('IPMI IP'), default='192.168.0.120')
    device_ipmi_user = models.CharField(_('IPMI User'), max_length=20, default='root')
    device_ipmi_pass = models.CharField(_('IPMI Password'), max_length=40, default='calvin')
    device_raid_level = models.CharField(_('RAID'), max_length=10, default='5')
    desc = models.CharField(_('Description'), max_length=40, default='Extra info.')
    #
    idc = models.ForeignKey(IDCInfo, default='1', verbose_name=_('IDC'))
    idc_rack = models.CharField(_('IDC Rack No.'), max_length=10, default='A01')
    idc_rack_h = models.IntegerField(_('IDC Rack Height'), default=0)
    #
    asset_no = models.CharField(_('Asset No.'), max_length=100, default='NULL')
    dt_created = models.DateTimeField(_('When Created?'))
    dt_modified = models.DateTimeField(_('When Modified?'), auto_now=True)
    
    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = _('Machines')
        verbose_name_plural = _('Machines')

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.dt_created <= now

    was_added_recently.admin_order_field = 'dt_created'
    was_added_recently.boolean = True
    was_added_recently.short_description = _('Added recently?')


@python_2_unicode_compatible
class Vm(models.Model):
    hostname = models.CharField(_('Hostname'), max_length=100, unique=True)
    on_host = models.ForeignKey(Machine, default='1', verbose_name=_('On Host'))
    on_cluster = models.ForeignKey(Cluster, default='1', verbose_name=_('On Cluster'))
    on_idc = models.ForeignKey(IDCInfo, default='1', verbose_name=_('IDC'))
    #
    os_ip_wan = models.GenericIPAddressField(_('IP_WAN'), default='0.0.0.0')
    os_ip_lan = models.GenericIPAddressField(_('IP_LAN'))
    os_type = models.ForeignKey(OSType, default='1', verbose_name=_('OS Type'))
    os_user_root = models.CharField(_('Admin'), max_length=20, default='root')
    os_pass_root = models.CharField(_('Password of Admin'), max_length=40, default='NULL')
    os_user_guest = models.CharField(_('Guest'), max_length=20, default='root1')
    os_pass_guest = models.CharField(_('Password of Guest'), max_length=40, default='NULL')
    #
    is_monited = models.BooleanField(_('Is Monited?'), default=False)
    is_online = models.BooleanField(_('Is Online?'), default=False)
    #
    app_desc = models.CharField(_('App Description'), max_length=40, default='NOT_IN_USE')
    biz_unit = models.ForeignKey(BusinessUnit, default='1', verbose_name=_('BizUnit'))
    run_env = models.ForeignKey(RuntimeEnvironment, default='1', verbose_name=_('RunEnv'))
    operator = models.ForeignKey(EndUser, default='1', verbose_name=_('EndUser'))
    instance_type = models.ForeignKey(InstanceType, default='1', verbose_name=_('Instance Type'))
    mount_point = models.CharField(_('Mount Point'), max_length=40, default='NULL')
    desc = models.CharField(_('VM Description'), max_length=100, default='Extra info.')
    dt_created = models.DateTimeField(_('When Created?'))
    dt_modified = models.DateTimeField(_('When Modified?'), auto_now=True)

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = _('VMs')
        verbose_name_plural = _('VMs')

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.dt_created <= now
    was_added_recently.admin_order_field = 'dt_created'
    was_added_recently.boolean = True
    was_added_recently.short_description = _('Added recently?')

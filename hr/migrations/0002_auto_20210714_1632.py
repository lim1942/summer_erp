# Generated by Django 3.2 on 2021-07-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalaryitem',
            name='calculate_way',
            field=models.CharField(choices=[('10', '固定值'), ('20', '比例值'), ('30', '计算值')], default='10', max_length=2, verbose_name='calculate way'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.CharField(blank=True, choices=[('10', '经营者'), ('20', '中层管理人员'), ('21', '一般管理人员'), ('30', '专业技术人员'), ('40', '技能人员'), ('50', '服务人员'), ('90', '其他人员')], default='21', max_length=2, null=True, verbose_name='employ category'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='gender',
            field=models.CharField(choices=[('0', '未知的性别'), ('1', '男性'), ('2', '女性'), ('9', '未说明的性别')], default='1', max_length=2, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='probation_months',
            field=models.CharField(choices=[('0', '无试用期'), ('1', '1个月'), ('2', '2个月'), ('3', '3个月'), ('4', '4个月'), ('5', '5个月'), ('6', '6个月'), ('12', '1年')], default='3', max_length=2, verbose_name='probation months'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rank',
            field=models.CharField(choices=[('10', '领导班子'), ('11', '副总师（助理）'), ('12', '部门负责人（正职）'), ('13', '部门负责人（副职）'), ('14', '部门内设机构负责人（正职）'), ('15', '部门内设机构负责人（副职）'), ('20', '一级职员'), ('21', '二级职员'), ('22', '三级职员'), ('23', '四级职员'), ('24', '五级职员'), ('25', '六级职员'), ('26', '七级职员'), ('27', '八级职员')], default='00', max_length=2, verbose_name='employee rank'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='ygxs',
            field=models.CharField(blank=True, choices=[('1', '劳动合同制（长期）'), ('2', '劳动合同制（短期）'), ('3', '人事代理制'), ('4', '劳务派遣制'), ('5', '非全日制'), ('6', '业务外包'), ('9', '其他')], default='2', max_length=2, null=True, verbose_name='employ ygxs'),
        ),
        migrations.AlterField(
            model_name='salaryitem',
            name='classification',
            field=models.CharField(choices=[('10', '工资'), ('20', '社保'), ('30', '奖金'), ('40', '福利'), ('99', '其他')], default='10', max_length=2, verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='salaryitem',
            name='plus_or_minus',
            field=models.CharField(choices=[('+', '增加'), ('-', '扣款')], default='+', max_length=2, verbose_name='plus or minus'),
        ),
    ]

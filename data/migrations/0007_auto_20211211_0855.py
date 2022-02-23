# Generated by Django 3.2.10 on 2021-12-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_complaint_closed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='appt_block',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='APPT_BLOCK'),
        ),
        migrations.AlterField(
            model_name='property',
            name='appt_boro',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='APPT_BORO'),
        ),
        migrations.AlterField(
            model_name='property',
            name='appt_ease',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='APPT_EASE'),
        ),
        migrations.AlterField(
            model_name='property',
            name='appt_lot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='APPT_LOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='aptno',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='APTNO'),
        ),
        migrations.AlterField(
            model_name='property',
            name='attorney_group1',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='ATTORNEY_GROUP1'),
        ),
        migrations.AlterField(
            model_name='property',
            name='attorney_group2',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='ATTORNEY_GROUP2'),
        ),
        migrations.AlterField(
            model_name='property',
            name='attorney_group_old',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='ATTORNEY_GROUP_OLD'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bld_dep',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='BLD_DEP'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bld_ext',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='BLD_EXT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bld_frt',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='BLD_FRT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bld_story',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='BLD_STORY'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bldg_class',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='BLDG_CLASS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='block',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='BLOCK'),
        ),
        migrations.AlterField(
            model_name='property',
            name='boro',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='BORO'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbnactextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNACTEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbnactland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNACTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbnacttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNACTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbnmktland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNMKTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbnmkttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNMKTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbntaxclass',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNTAXCLASS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbntaxflag',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNTAXFLAG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbntrnextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNTRNEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbntrnland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNTRNLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbntrntot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNTRNTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbntxbextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNTXBEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cbntxbtot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CBNTXBTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='condo_number',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CONDO_Number'),
        ),
        migrations.AlterField(
            model_name='property',
            name='condo_sfx1',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CONDO_SFX1'),
        ),
        migrations.AlterField(
            model_name='property',
            name='condo_sfx2',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CONDO_SFX2'),
        ),
        migrations.AlterField(
            model_name='property',
            name='condo_sfx3',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CONDO_SFX3'),
        ),
        migrations.AlterField(
            model_name='property',
            name='coop_apts',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='COOP_APTS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='coop_num',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='COOP_NUM'),
        ),
        migrations.AlterField(
            model_name='property',
            name='corner',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CORNER'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cpb_boro',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CPB_BORO'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cpb_dist',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CPB_DIST'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curactextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURACTEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curactland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURACTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curacttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURACTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curmktland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURMKTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curmkttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURMKTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curtaxclass',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURTAXCLASS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curtaxflag',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURTAXFLAG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curtrnextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURTRNEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curtrnland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURTRNLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curtrntot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURTRNTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curtxbextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURTXBEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='curtxbtot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='CURTXBTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='easement',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='EASEMENT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='extracrdt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='EXTRACRDT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='factory_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FACTORY_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='finactextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINACTEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='finactland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINACTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='finacttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINACTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='finmktland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINMKTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='finmkttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINMKTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='fintaxclass',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINTAXCLASS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='fintaxflag',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINTAXFLAG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='fintrnextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINTRNEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='fintrnland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINTRNLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='fintrntot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINTRNTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='fintxbextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINTXBEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='fintxbtot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='FINTXBTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='garage_area',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='GARAGE_AREA'),
        ),
        migrations.AlterField(
            model_name='property',
            name='gepsupport_rc',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='GEPSUPPORT_RC'),
        ),
        migrations.AlterField(
            model_name='property',
            name='gross_sqft',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='GROSS_SQFT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='hotel_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='HOTEL_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='housenum_hi',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='HOUSENUM_HI'),
        ),
        migrations.AlterField(
            model_name='property',
            name='housenum_lo',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='HOUSENUM_LO'),
        ),
        migrations.AlterField(
            model_name='property',
            name='ident',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='IDENT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='land_area',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='LAND_AREA'),
        ),
        migrations.AlterField(
            model_name='property',
            name='loft_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='LOFT_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='LOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot_dep',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='LOT_DEP'),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot_frt',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='LOT_FRT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot_irreg',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='LOT_IRREG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='newdrop',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='NEWDROP'),
        ),
        migrations.AlterField(
            model_name='property',
            name='noav',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='NOAV'),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_bldgs',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='NUM_BLDGS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='office_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='OFFICE_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='other_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='OTHER_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='OWNER'),
        ),
        migrations.AlterField(
            model_name='property',
            name='parid',
            field=models.CharField(max_length=64, verbose_name='PARID'),
        ),
        migrations.AlterField(
            model_name='property',
            name='period',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PERIOD'),
        ),
        migrations.AlterField(
            model_name='property',
            name='protest_1',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PROTEST_1'),
        ),
        migrations.AlterField(
            model_name='property',
            name='protest_2',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PROTEST_2'),
        ),
        migrations.AlterField(
            model_name='property',
            name='protest_old',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PROTEST_OLD'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pyactextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYACTEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pyactland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYACTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pyacttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYACTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pymktland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYMKTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pymkttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYMKTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pytaxclass',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYTAXCLASS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pytaxflag',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYTAXFLAG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pytrnextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYTRNEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pytrnland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYTRNLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pytrntot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYTRNTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pytxbextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYTXBEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pytxbtot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='PYTXBTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='rectype',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='RECTYPE'),
        ),
        migrations.AlterField(
            model_name='property',
            name='residential_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='RESIDENTIAL_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='retail_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='RETAIL_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='reuc_ref',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='REUC_REF'),
        ),
        migrations.AlterField(
            model_name='property',
            name='roll_section',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='ROLL_SECTION'),
        ),
        migrations.AlterField(
            model_name='property',
            name='secvol',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='SECVOL'),
        ),
        migrations.AlterField(
            model_name='property',
            name='stcode',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='STCODE'),
        ),
        migrations.AlterField(
            model_name='property',
            name='storage_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='STORAGE_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='street_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='STREET_NAME'),
        ),
        migrations.AlterField(
            model_name='property',
            name='subident',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='SUBIDENT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='subident_reuc',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='SUBIDENT-REUC'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tenactextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENACTEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tenactland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENACTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tenacttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENACTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tenmktland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENMKTLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tenmkttot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENMKTTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tentaxclass',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENTAXCLASS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tentaxflag',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENTAXFLAG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tentrnextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENTRNEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tentrnland',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENTRNLAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tentrntot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENTRNTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tentxbextot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENTXBEXTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='tentxbtot',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='TENTXBTOT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='uaf_bldg',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='UAF_BLDG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='uaf_land',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='UAF_LAND'),
        ),
        migrations.AlterField(
            model_name='property',
            name='units',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='UNITS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='valref',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='VALREF'),
        ),
        migrations.AlterField(
            model_name='property',
            name='warehouse_area_gross',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='WAREHOUSE_AREA_GROSS'),
        ),
        migrations.AlterField(
            model_name='property',
            name='year',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YEAR'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yralt1',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YRALT1'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yralt1_range',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YRALT1_RANGE'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yralt2',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YRALT2'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yralt2_range',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YRALT2_RANGE'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yrbuilt',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YRBUILT'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yrbuilt_flag',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YRBUILT_FLAG'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yrbuilt_range',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='YRBUILT_RANGE'),
        ),
        migrations.AlterField(
            model_name='property',
            name='zip_code',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='ZIP_CODE'),
        ),
        migrations.AlterField(
            model_name='property',
            name='zoning',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='ZONING'),
        ),
    ]

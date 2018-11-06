# Generated by Django 2.1.3 on 2018-11-06 03:16

import django.core.validators
from django.db import migrations, models
import hknweb.alumni.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_auto_20181105_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumnus',
            old_name='location',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='alumnus',
            name='grad_semester',
        ),
        migrations.AddField(
            model_name='alumnus',
            name='country_state',
            field=models.CharField(choices=[('USA: AK', 'USA: AK'), ('USA: AL', 'USA: AL'), ('USA: AR', 'USA: AR'), ('USA: AZ', 'USA: AZ'), ('USA: CA', 'USA: CA'), ('USA: CO', 'USA: CO'), ('USA: CT', 'USA: CT'), ('USA: DE', 'USA: DE'), ('USA: DC', 'USA: DC'), ('USA: FL', 'USA: FL'), ('USA: GA', 'USA: GA'), ('USA: HI', 'USA: HI'), ('USA: IA', 'USA: IA'), ('USA: ID', 'USA: ID'), ('USA: IL', 'USA: IL'), ('USA: IN', 'USA: IN'), ('USA: KS', 'USA: KS'), ('USA: KY', 'USA: KY'), ('USA: LA', 'USA: LA'), ('USA: MA', 'USA: MA'), ('USA: MD', 'USA: MD'), ('USA: ME', 'USA: ME'), ('USA: MI', 'USA: MI'), ('USA: MN', 'USA: MN'), ('USA: MO', 'USA: MO'), ('USA: MS', 'USA: MS'), ('USA: MT', 'USA: MT'), ('USA: NC', 'USA: NC'), ('USA: ND', 'USA: ND'), ('USA: NE', 'USA: NE'), ('USA: NH', 'USA: NH'), ('USA: NJ', 'USA: NJ'), ('USA: NM', 'USA: NM'), ('USA: NV', 'USA: NV'), ('USA: NY', 'USA: NY'), ('USA: OH', 'USA: OH'), ('USA: OK', 'USA: OK'), ('USA: OR', 'USA: OR'), ('USA: PA', 'USA: PA'), ('USA: RI', 'USA: RI'), ('USA: SC', 'USA: SC'), ('USA: SD', 'USA: SD'), ('USA: TN', 'USA: TN'), ('USA: TX', 'USA: TX'), ('USA: UT', 'USA: UT'), ('USA: VA', 'USA: VA'), ('USA: VT', 'USA: VT'), ('USA: WA', 'USA: WA'), ('USA: WI', 'USA: WI'), ('USA: WV', 'USA: WV'), ('USA: WY', 'USA: WY'), ('USA: Puerto Rico', 'USA: Puerto Rico'), ('USA: Other Territory', 'USA: Other Territory'), ('', ''), ('', ''), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('', ''), ('', ''), ('The Bahamas', 'The Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('', ''), ('', ''), ('Cabo Verde', 'Cabo Verde'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo, Democratic Republic of the', 'Congo, Democratic Republic of the'), ('Congo, Republic of the', 'Congo, Republic of the'), ('Costa Rica', 'Costa Rica'), ('Côte d’Ivoire', 'Côte d’Ivoire'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('', ''), ('', ''), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('', ''), ('', ''), ('East Timor (Timor-Leste)', 'East Timor (Timor-Leste)'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Advertisement', 'Advertisement'), ('', ''), ('', ''), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('', ''), ('', ''), ('Gabon', 'Gabon'), ('The Gambia', 'The Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('', ''), ('', ''), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('', ''), ('', ''), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('', ''), ('', ''), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('', ''), ('', ''), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea, North', 'Korea, North'), ('Korea, South', 'Korea, South'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('', ''), ('', ''), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('', ''), ('', ''), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Micronesia, Federated States of', 'Micronesia, Federated States of'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar (Burma)', 'Myanmar (Burma)'), ('', ''), ('', ''), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Norway', 'Norway'), ('', ''), ('', ''), ('Oman', 'Oman'), ('', ''), ('', ''), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('', ''), ('', ''), ('Qatar', 'Qatar'), ('', ''), ('', ''), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('', ''), ('', ''), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Sudan, South', 'Sudan, South'), ('Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('', ''), ('', ''), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('', ''), ('', ''), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('', ''), ('', ''), ('Vanuatu', 'Vanuatu'), ('Vatican City', 'Vatican City'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('', ''), ('', ''), ('Yemen', 'Yemen'), ('', ''), ('', ''), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default='USA: CA', max_length=255),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='grad_season',
            field=models.CharField(choices=[('FA', 'Fall'), ('SP', 'Spring'), ('SU', 'Summer')], default='FA', max_length=2),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='grad_year',
            field=models.IntegerField(default=2018, validators=[django.core.validators.MinValueValidator(1915), hknweb.alumni.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

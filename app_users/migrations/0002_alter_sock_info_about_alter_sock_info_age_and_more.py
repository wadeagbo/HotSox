# Generated by Django 4.1.7 on 2023-02-26 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sock",
            name="info_about",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_age",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_brand",
            field=models.CharField(
                choices=[
                    ("1", "Adidas"),
                    ("2", "Puma"),
                    ("3", "Nike"),
                    ("4", "D&G"),
                    ("5", "Gucci"),
                    ("6", "Aldi"),
                    ("7", "From'ma'grandma"),
                    ("8", "Stolen"),
                    ("9", "Odd socks"),
                    ("10", "Hot socks"),
                    ("11", "Converse"),
                    ("12", "Pierre Cardin"),
                    ("13", "One Euro Shop"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_color",
            field=models.CharField(
                choices=[
                    ("1", "Black"),
                    ("2", "Grey"),
                    ("3", "White"),
                    ("4", "Red"),
                    ("5", "Green"),
                    ("6", "Yellow"),
                    ("7", "Blue"),
                    ("8", "Purple"),
                    ("9", "Orange"),
                    ("10", "Multicolor"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_condition",
            field=models.CharField(
                choices=[
                    ("1", "Brand new"),
                    ("2", "Fairly used"),
                    ("3", "Sunday best"),
                    ("4", "Well loved"),
                    ("5", "One of a kind"),
                    ("6", "Sporty"),
                    ("7", "Stained"),
                    ("8", "Overused"),
                    ("9", "Colorless but still going."),
                    ("10", "Involuntary Toesocks"),
                    ("11", "Lost and found"),
                    ("12", "Rescued from trash"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_fabric",
            field=models.CharField(
                choices=[
                    ("1", "Wool"),
                    ("2", "Cotton"),
                    ("3", "Polyester"),
                    ("4", "Bamboo"),
                    ("5", "Silk"),
                    ("6", "Nylon"),
                    ("7", "Unknown"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_fabric_thickness",
            field=models.CharField(
                choices=[
                    ("1", "Fishnets"),
                    ("2", "Nylon thin"),
                    ("3", "Fashion victim"),
                    ("4", "Summer type"),
                    ("5", "Winter type"),
                    ("6", "Cushioned Cozy one"),
                    ("7", "Double battery powered self warming one"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_holes",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_inoutdoor",
            field=models.CharField(
                choices=[
                    ("1", "Indoor Sock"),
                    ("2", "Outdoor Sock"),
                    ("3", "Love-live Sock"),
                    ("4", "Gym Sock"),
                    ("5", "Las Vegas Sock"),
                    ("6", "Sleeping Sock"),
                    ("7", "Japanese vendor maschine Sock"),
                    ("8", "Netflix'n'Chill Sock"),
                    ("9", "2-week Festival Sock"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_kilometers",
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_separation_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_size",
            field=models.CharField(
                choices=[
                    ("1", "25-31"),
                    ("2", "32-36"),
                    ("3", "37-40"),
                    ("4", "41-45"),
                    ("5", "46-47"),
                    ("6", "47+"),
                    ("7", "Big Foot"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_special",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_type",
            field=models.CharField(
                choices=[
                    ("1", "Toe Socks"),
                    ("2", "Invisible"),
                    ("3", "Ankle"),
                    ("4", "Crew"),
                    ("5", "Mid-Calf"),
                    ("6", "Calf"),
                    ("7", "Knee-High"),
                    ("8", "Toe less"),
                    ("9", "Ga'ma knitted socks"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="sock",
            name="info_washed",
            field=models.PositiveSmallIntegerField(),
        ),
    ]

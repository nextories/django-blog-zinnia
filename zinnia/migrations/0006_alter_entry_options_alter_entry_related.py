from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zinnia", "0005_category_mptt_update"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entry",
            options={
                "get_latest_by": "publication_date",
                "ordering": ["-publication_date"],
                "permissions": (("can_view_blog_entry", "Can view BlogEntry"),),
                "verbose_name": "entry",
                "verbose_name_plural": "entries",
            },
        ),
        migrations.AlterField(
            model_name="entry",
            name="related",
            field=models.ManyToManyField(
                blank=True, to="zinnia.entry", verbose_name="related entries"
            ),
        ),
    ]

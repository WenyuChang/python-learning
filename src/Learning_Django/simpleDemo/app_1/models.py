from django.db import models

# Create your models here.
class Table1(models.Model):
    field1_1 = models.CharField(max_length=30)
    field2_1 = models.URLField()
    
    def __unicode__(self):
        return 'Data from Table1: f1:%s,f2:%s' % (self.field1_1, self.field2_1)
    
class Table2(models.Model):
    field1_2 = models.CharField(max_length=40)
    field2_2 = models.EmailField()
    
    def __unicode__(self):
        return 'Data from Table2: f1:%s,f2:%s' % (self.field1_2, self.field2_2)
    
class Table3(models.Model):
    field1_3 = models.ManyToManyField(Table2)
    field2_3 = models.ForeignKey(Table1)
    field3_3 = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return 'Data from Table3: f1:%s,f2:%s,f3:%s' % (self.field1_3, self.field2_3, self.field3_3)
    

# In order to get the DB schema from this model
# please run the following command:
#     python manage.py sqlall app_1
#     or python manage.py syncdb
# following are the DB schema generated automatically by the command above
# BEGIN;
# CREATE TABLE "app_1_table1" (
#     "id" integer NOT NULL PRIMARY KEY,
#     "field1_1" varchar(30) NOT NULL,
#     "field2_1" varchar(200) NOT NULL
# );
#  
# CREATE TABLE "app_1_table2" (
#     "id" integer NOT NULL PRIMARY KEY,
#     "field1_2" varchar(40) NOT NULL,
#     "field2_2" varchar(75) NOT NULL
# );
# 
# CREATE TABLE "app_1_table3_field1_3" (
#     "id" integer NOT NULL PRIMARY KEY,
#     "table3_id" integer NOT NULL,
#     "table2_id" integer NOT NULL REFERENCES "app_1_table2" ("id"),
#     UNIQUE ("table3_id", "table2_id")
# );
#  
# CREATE TABLE "app_1_table3" (
#     "id" integer NOT NULL PRIMARY KEY,
#     "field2_3_id" integer NOT NULL REFERENCES "app_1_table1" ("id"),
#     "field3_3" date NOT NULL
# );
#  
# CREATE INDEX "app_1_table3_field1_3_207cb9ee" ON "app_1_table3_field1_3" ("table3_id");
# CREATE INDEX "app_1_table3_field1_3_bbb246cd" ON "app_1_table3_field1_3" ("table2_id");
# CREATE INDEX "app_1_table3_e6c43e51" ON "app_1_table3" ("field2_3_id");
#  
# COMMIT;

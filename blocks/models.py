# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

'''from taggit.managers import TaggableManager'''

college_choices = (
    ('M', u'كلية الطب'),
    ('A', u'كلية العلوم الطبية التطبيقية'),
    ('P', u'كلية الصيدلة'),
    ('D', u'كلية طب الأسنان'),
    ('B', u'كلية العلوم و المهن الصحية'),
    ('N', u'كلية التمريض'),
    ('I', u' كلية الصحة العامة والمعلوماتية الصحية'),
)

city_choices = (
    ('R', u'الرياض'),
    ('J', u'جدة'),
    ('A', u'الأحساء'),
)
gender_choices = (
    ('F', u'طالبات'),
    ('M', u'طلاب'),
)
university_choics = (
    ('KHS' , u'جامعة الملك سعود بن عبدالعزيز للعلوم الصحية'),
    ('KFU', u'جامعة الملك فيصل'),
    ('KSAU' ,u'جامعة الملك سعود'),
    ('PSU' ,u'جامعة الأمير سلطان'),
    ('KSU' , u'جامعة الملك سلمان الخرج'),
    )
blocks_choices= (
    ('FB',u'Foundation Block'),
    ('MSK',u'Musculoskeletal Block'),
    ('R',u'Respiratory Block'),
    ('HT',u'Hematology Block'),
    ('CV',u'Cardiovascular Block'),
    ('NS',u'Neurosciences Block'),
    ('EC',u'Endocrine Block'),
    ('UR',u'Urology and Renal Block'),
    ('GIT',u'Gastroenterology Block'),
    ('O',u'Oncology Block'),
    ('EBM',u'EBM Block'),
    ('FM',u'Family Medicine block'),
    ('M',u'Medicine Block'),
    ('P',u'Pediatric Block'),
    ('S',u'Surgery Block'),
    ('OBGN',u'Obstetrics and Gynecology Block'),
    ('SSMH',u'Special Sense & Mental Health Block Book'))
rating_choices=(
    ('5',u'5 Stars out of 5'),
    ('4',u'4 Stars out of 5'),
    ('3',u'3 Stars out of 5'),
    ('2',u'2 Stars out of 5'),
    ('1',u'1 Stars out of 5'),
)
clinical_choices=(
    ('Yes',u'It is clinical'),
    ('NO',u'It is not clinical')
)
class College(models.Model):
    name = models.CharField(max_length=1, choices=college_choices, verbose_name=u"الاسم")
    city = models.CharField(max_length=1, choices=city_choices, verbose_name=u"المدينة")
    gender = models.CharField(max_length=1, choices=gender_choices, verbose_name=u"الجنس")
class Profile(models.Model):

    is_student = models.BooleanField(default=True,
                                     verbose_name=u"طالب؟")
    ar_first_name = models.CharField(max_length=30,
                                     verbose_name=u'الاسم الأول')
    ar_last_name = models.CharField(max_length=30,
                                    verbose_name=u'الاسم الأخير')
    en_first_name = models.CharField(max_length=30,
                                     verbose_name=u'الاسم الأول')
    en_last_name = models.CharField(max_length=30,
                                    verbose_name=u'الاسم الأخير')
    city = models.CharField(max_length=1, choices=city_choices, verbose_name=u"المدينة")

    gender = models.CharField(max_length=1, choices=gender_choices,
                              verbose_name=u"الجنس", blank=True,
                              default="")

    email = models.EmailField(u"البريد الإلكتروني",
                                          blank=True)
    university = models.CharField (max_length=1, choices=university_choics, verbose_name=u"الجامعة")

    college = models.ForeignKey(College, null=True,
                                blank=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'الكلية')
    batch = models.IntegerField(max_length=2,
                                verbose_name=u'الدفعة')
    profile_picture = models.ImageField(width_field=60,height_field=60)
class Block (models.Model):
    title = models.CharField(max_length=120, verbose_name=u'اسم البلوك ')
    cover = models.FileField(upload_to='covers', blank=True, null=True)
    is_clinical = models.CharField(max_length=1,choices=clinical_choices)

class Book (models.Model):
    title = models.CharField(max_length=120,verbose_name=u'اسم الكتاب')

    description = models.CharField(verbose_name=u"وصف الكتاب", blank=True, help_text=u"اختياري")

    '''tags = TaggableManager(verbose_name=u"التصنيفات",
                           help_text=u"ما التصانيف الإنجليزية التي تراها ملائمة؟ (مطلوبة ومفصولة بفواصل، مثلا: \"Respiratory, Physiology\")")'''

    submitter = models.ForeignKey(User, null=True,
                                  on_delete=models.SET_NULL,
                                  related_name='book_contributions')

    cover = models.FileField(upload_to='covers', blank=True, null=True)

    download = models.CharField(max_length=250,verbose_name=u'رابط التحميل',blank=True, help_text=u"اختياري")

    submission_date = models.DateTimeField(u"تاريخ الرفع",
                                           auto_now_add=True)
    blocks = models.ManyToOneRel (max_length=2, choices=blocks_choices, verbose_name=u"البلوكات المستهدفة")


class Comment (models.Model):
    submitter = models.ForeignKey(User, null=True,
                                  on_delete=models.SET_NULL,)
    description = models.CharField(verbose_name=u"وصف التقييم", blank=True, help_text=u"اختياري")
    submission_date = models.DateTimeField(u"تاريخ الاضافة",
                                           auto_now_add=True)

    rating = models.CharField(max_length=1, choices=rating_choices)
class comment_rating (models.Model):
    submitter = models.ForeignKey(User, null=True,
                                  on_delete=models.SET_NULL, )

    '''comment_id=?? which one ?'''
    rating = models.CharField(max_length=1, choices=rating_choices)
''' tags ?? do we use tagit and how + we dont want to make it limited so if we use choices we need to add
a function that lets the user add new tags'''

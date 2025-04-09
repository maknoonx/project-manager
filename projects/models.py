# projects/models.py

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    name = models.CharField(_("اسم المشروع"), max_length=200)
    company = models.CharField(_("الشركة المنفذة"), max_length=200, blank=True, null=True )
    company_logo = models.ImageField(_("شعار الشركة"), upload_to="company_logos/", blank=True, null=True)
    start_date = models.DateField(_("تاريخ البدء"), blank=True, null=True)
    end_date = models.DateField(_("تاريخ الانتهاء"), blank=True, null=True)
    client = models.CharField(_("العميل"), max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = _("مشروع")
        verbose_name_plural = _("المشاريع")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:project_detail", kwargs={"pk": self.pk})
    
    def get_stages_count(self):
        return self.stages.count()


class Stage(models.Model):
    project = models.ForeignKey(Project, related_name="stages", on_delete=models.CASCADE, blank=True, null=True)
    number = models.PositiveIntegerField(_("رقم المرحلة"))
    name = models.CharField(_("اسم المرحلة"), max_length=200, blank=True, null=True)
    supervisor = models.CharField(_("المشرف"), max_length=200, blank=True, null=True)
    recipient = models.CharField(_("المستلم"), max_length=200, blank=True, null=True)
    start_date = models.DateField(_("تاريخ البدء"), blank=True, null=True)
    end_date = models.DateField(_("تاريخ الاستلام"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = _("مرحلة")
        verbose_name_plural = _("المراحل")
        ordering = ["number"]
        unique_together = ["project", "number"]

    def __str__(self):
        return f"{self.project.name} - {self.name}"


class Task(models.Model):
    stage = models.ForeignKey(Stage, related_name="tasks", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_("اسم المهمة"), max_length=200, blank=True, null=True)
    description = models.TextField(_("وصف المهمة"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("مهمة")
        verbose_name_plural = _("المهام")
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.stage} - {self.name}"
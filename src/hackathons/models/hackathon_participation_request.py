from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons
from projects.models.tools_in_project import Tool


class HackathonParticipationRequest(models.Model):
    class RequestStatus(models.TextChoices):
        PENDING = "Pending", _("Waiting for confirmation")
        ACCEPTED = "Accepted", _("Active")
        DECLINED = "Declined", _("Blocked")

    profile_id = models.ForeignKey(to=Tool, verbose_name=_("profile id"), on_delete=models.CASCADE)
    hackathon_id = models.ForeignKey(to=Hackathons, verbose_name=_("hackathon id"), on_delete=models.CASCADE)
    cover_letter = models.TextField(verbose_name=_("cover letter"), max_length=400, blank=True, null=True)
    resume_url = models.CharField(verbose_name=_("resume url"), blank=True, null=True)
    status = models.CharField(verbose_name=_("status"), max_length=25, choices=RequestStatus, blank=True, null=True)

    def __str__(self):
        return f'{self.profile_id} | {self.hackathon_id}'

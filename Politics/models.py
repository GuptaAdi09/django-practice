from django.db import models

# Create your models here.
class Parties(models.Model):
    party_name = models.CharField(max_length=50)
    current_leader = models.CharField(max_length=50)
    establish_in = models.DateField()
    total_vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.party_name


class Mumbai_Region(models.Model):
    assembly_constitution_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    distric = models.CharField(max_length=100,default="Mumbai")
    

    def __str__(self):
        return self.assembly_constitution_name

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=50)
    from_which_assembly = models.ForeignKey(Mumbai_Region,on_delete=models.CASCADE)
    candidate_age = models.IntegerField()
    party_name = models.ForeignKey(Parties,on_delete=models.CASCADE)
    total_vote = models.IntegerField(default=0)

    def __str__(self):
        return self.candidate_name


    
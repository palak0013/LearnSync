from enum import Enum  #will help by gnerating dropdowm

class ResourceType(str, Enum): #resource type will in dropdown list
    youtube = "YouTube"
    github = "GitHub"
    pdf = "PDF"
    website = "Website"


class ResourceStatus(str, Enum): # resource ststus will be in dropdown menu
    not_started = "Not Started"
    in_progress = "In Progress"
    completed = "Completed"
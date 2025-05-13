from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imágen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección Web", null=True,blank=True)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación") #se ejecuta la primera vez, al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") #se ejecuta cada que se actualiza la instancia
    
    #creo subclase para metadatos extendidos
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #de mas nuevo a mas antiguo ponemos el "-"

    def __str__(self):
        return self.title